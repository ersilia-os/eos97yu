FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2023.3.1
RUN pip install mordredcommunity==2.0.6
RUN pip install flaml==0.6.5
RUN pip install scikit-learn==0.24.2

WORKDIR /repo
COPY . /repo
