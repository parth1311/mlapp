import os
import sys
import warnings

import mlflow
import logging

mlflow.set_tracking_uri("https://dagshub.com/parth1311/mlapp.mlflow")
tracking_uri = mlflow.get_tracking_uri()
print("Current tracking uri: {}".format(tracking_uri))

