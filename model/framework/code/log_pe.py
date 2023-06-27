import joblib
import os
import pathlib
import numpy as np
from mordred import Calculator, descriptors
import pathlib


PATH = pathlib.Path(__file__).resolve().parent

checkpoints_dir = PATH.parent.parent / "checkpoints"

    
def predict_log_pe(mols):
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
    return pred