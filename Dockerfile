FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c conda-forge rdkit=2020.03
RUN pip install mordred
RUN pip install flaml

WORKDIR /repo
COPY ./repo
