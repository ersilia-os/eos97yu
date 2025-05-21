# PAMPA effective permeability

The authors provide a dataset of 200 small molecules and their experimentally measured permeability in a PAMPA assay. Using this data, we have trained a model that predicts the logarithm of the effective permeability coefficient.

This model was incorporated on 2021-11-10.

## Information
### Identifiers
- **Ersilia Identifier:** `eos97yu`
- **Slug:** `pampa-permeability`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Not Applicable`
- **Tags:** `Permeability`, `ADME`, `LogP`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Predicted Log of the Permeability Coefficient in PAMPA assay

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| log_pe | float | high | Log10 of permeability coefficient |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos97yu](https://hub.docker.com/r/ersiliaos/eos97yu)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos97yu.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos97yu.zip)

### Resource Consumption


### References
- **Source Code**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6651837/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6651837/)
- **Publication**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6651837/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6651837/)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2019`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos97yu
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos97yu
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
