import joblib
import csv
import os, sys
import numpy as np


PATH = os.path.dirname(os.path.abspath(__file__))

checkpoints_dir = os.path.join(PATH, "../checkpoints/")

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles = []
    for r in reader:
        smiles += [r[0]]

from rdkit import Chem
from mordred import Calculator, descriptors

idxs = []
mols = []
for i, smi in enumerate(smiles):
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        continue
    mols += [mol]
    idxs += [i]

calc = Calculator(descriptors, ignore_3D=True)

X = np.array(calc.pandas(mols), dtype=np.float32)

mask = np.logical_and(~np.isnan(X), X < -9e+12)
X[mask] = np.nan
mask = np.logical_and(~np.isnan(X), X > 9e+12)
X[mask] = np.nan

imputer = joblib.load(os.path.join(checkpoints_dir, "imputer.joblib"))
scaler = joblib.load(os.path.join(checkpoints_dir, "scaler.joblib"))
mdl = joblib.load(os.path.join(checkpoints_dir, "flaml.joblib"))

X = imputer.transform(X)
X = scaler.transform(X)
pred = mdl.predict(X)

y = [None]*len(smiles)

for i, p in zip(idxs, pred):
    y[i] = p

with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["LogPe"])
    for r in y:
        if r is None:
            writer.writerow(["None"])
        else:
            writer.writerow([r])
