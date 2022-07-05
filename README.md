mlapp
==============================

This README has details on the ML App created that has the template from Cookie-cutter. It has DVC pipelines implemented in the workflow.
The code is run on a remote server on Cloud9 platform in AWS.

Project Organization
------------
    LICENSE
    Makefile                        <- Makefile with commands to run for example installation of requirements
    README.md                       <- The top-level README for developers using this project.
    assets
       |-- .gitignore
       |-- metrics.json             <- Json file output. Actual assets are stored in https://dagshub.com/parth1311/mlapp. This file tracks the metrics (RMSE, MAE)
    data
       |-- .gitignore
       |-- raw.dvc                  <- Has information on the dataset used. Tracked in DVC. 
    docs
       |-- Makefile
       |-- commands.rst
       |-- conf.py
       |-- getting-started.rst
       |-- index.rst
       |-- make.bat
    dvc.lock                        <- Records the state of pipelines
    dvc.yaml                        <- YAML file to run all the stages on "dvc repro" command
    models
       |-- .gitkeep
    notebooks
       |-- .gitkeep
    params.yaml                     <- YAML file that has all the parameters required to train the model (Ex) type of regression, epochs, etc.
    references
       |-- .gitkeep
    reports
       |-- .gitkeep
       |-- figures
       |   |-- .gitkeep 
    requirements.txt                <- Sets up all the required libraries to execute this project
    setup.py
    src
       |-- __init__.py
       |-- data
       |   |-- .gitkeep
       |   |-- config.py            <- Has the config parameters required for the python script
       |   |-- create_dataset.py    <- Imports wine-quality.csv data set and creates train and test split
       |-- features
       |   |-- .gitkeep
       |   |-- config.py            <- Has the config parameters required for the python script
       |   |-- create_features.py   <- Extracts the feature (quality) set from train and test models
       |-- models
       |   |-- .gitkeep
       |   |-- config.py            <- Has the config parameters required for the python script
       |   |-- evaluate_model.py    <- Compares the Predicted output v/s Actual output, calculates RMSE, MAE, R2 parameters and outputs it to metrics.json
       |   |-- train_model.py       <- Trains the model with the parameters used in params.yaml
       |-- visualization
       |   |-- .gitkeep
       |   |-- __init__.py
       |   |-- visualize.py
    test_environment.py
    tox.ini


--------

GENERAL STEPS TO BE FOLLOWED :

Step 1:
 - Create GitHub Repo
 - Connect GitHub Repo to DagsHub

Step 2: (For DVC based tracking)
 - Install and Configure DVC (installation handled in requirements.txt)
 - dvc init
 - dvc remote add origin https://dagshub.com/parth1311/mlapp.dvc
 - dvc remote modify origin --local auth basic
 - dvc pull -r origin
 - dvc add <files> - Whenever new files have to be tracked on DVC
 - dvc push -r origin
 - git add <files> - Whenever files need to be committed and pushed to GitHub
 
Step 3 : 
 - Whenever a change to dataset/model is done, run a "dvc repro" in the project directory to run all the stages in DVC pipeline.
 - Add and commit the changes appropriately to DVC and GitHub and track the progress on DagsHub (https://dagshub.com/parth1311/mlapp)

Step : (For MLFlow based Tracking)
  - Install mlflow (Comes as part of requirement.txt)
  - mlflow.set_tracking_uri("https://dagshub.com/parth1311/mlapp.mlflow")
    tracking_uri = mlflow.get_tracking_uri()
    print("Current tracking uri: {}".format(tracking_uri))

SETTING UP DVC FOR THE FIRST TIME : 
  - Make sure you have all the required python files to create dataset, extract feature set, split the dataset into test and train, train the dataset, and evaluate the model based on some metrics
  - dvc run -f -n prepare -d src/data/create_dataset.py -o assets/data python src/data/create_dataset.py
  - dvc run -f -n featurize -d src/features/create_features.py -d assets/data -o assets/features python src/features/create_features.py
  - dvc run -f -n evaluate -d src/models/evaluate_model.py -d assets/features -d assets/models -p model_type -M assets/metrics.json python src/models/evaluate_model.py
  - On running these steps, the dvc.yaml file is updated with the stages in the pipeline/workflow.
  - Push all the files into the repo and run a "dvc repro" the next time you want to tune hyperparameters/ change the dataset

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
