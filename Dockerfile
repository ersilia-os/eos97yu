FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2020.03
RUN pip install mordred==1.2.0
RUN pip install flaml==0.6.5
RUN pip install scikit-learn==0.24.2

WORKDIR /repo
COPY ./repo
