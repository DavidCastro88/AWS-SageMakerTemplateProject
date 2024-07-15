import argparse
import os
import pandas as pd
import numpy as np
import joblib
import boto3
import sagemaker
import json
from sagemaker import get_execution_role
from sagemaker.estimator import Estimator
from sagemaker.inputs import TrainingInput

if __name__ == '__main__':
    BUCKET = "bucket_name"  # Replace with your actual S3 bucket name
    parser = argparse.ArgumentParser()
    
    # Arguments for data location (assuming they are passed as environment variables in SageMaker)
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))

    args = parser.parse_args()
    
    #Load hyperparameters
    with open('config/hyperparameters.json') as hyperparams_file:
        hyperparameters = json.load(hyperparams_file)
        
    # Initialize SageMaker session and get execution role
    session = boto3.Session()
    role = get_execution_role()

    # Define SageMaker estimator for XGBoost
    xgb_model = Estimator(image_uri='811284229777.dkr.ecr.us-east-1.amazonaws.com/xgboost:latest',
                          role=role,
                          instance_count=1,
                          instance_type='ml.m4.xlarge',
                          output_path=args.model_dir,
                          sagemaker_session=sagemaker.Session())

    # Set the hyperparameters from the JSON file
    xgb_model.set_hyperparameters(**hyperparameters)

    # Define TrainingInput for training data
    train_input = TrainingInput(
        f"s3://{BUCKET}/train/train.csv",  # S3 location of training data
        content_type="csv",  # Data format
        s3_data_type="S3Prefix"  # Type of S3 data
    )

    # Define TrainingInput for validation data
    validation_input = TrainingInput(
        f"s3://{BUCKET}/validation/validation.csv",  # S3 location of validation data
        content_type="csv",  # Data format
        s3_data_type="S3Prefix"  # Type of S3 data
    )

    # Train the model using both training and validation data
    xgb_model.fit({"train": train_input, "validation": validation_input}, wait=True)

    # Save the trained model
    model_path = os.path.join(args.model_dir, "model.tar.gz")
    xgb_model.save(model_path)

    # Print the path where the model is saved, required by SageMaker
    print(f"Model saved at: {model_path}")
