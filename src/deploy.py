import boto3
import sagemaker
from sagemaker import get_execution_role

def deploy_model(model_path, model_name, endpoint_name):
    # Initialize the SageMaker client
    sm_client = boto3.client('sagemaker')

    # Define the S3 bucket and model data location
    bucket = "your-bucket-name"  # Replace with your S3 bucket name
    model_data = f"s3://{bucket}/{model_path}/{model_name}/model.tar.gz"

    # Define the role for SageMaker execution
    role = get_execution_role()

    # Create Model for SageMaker
    sm_model = sm_client.create_model(
        ModelName=model_name,
        PrimaryContainer={
            'Image': '811284229777.dkr.ecr.us-east-1.amazonaws.com/xgboost:latest',  # Replace with your Docker image URI
            'ModelDataUrl': model_data
        },
        ExecutionRoleArn=role
    )

    # Create endpoint configuration for SageMaker
    endpoint_config_name = f'{endpoint_name}-config'
    sm_endpoint_config = sm_client.create_endpoint_config(
        EndpointConfigName=endpoint_config_name,
        ProductionVariants=[
            {
                'InstanceType': 'ml.m4.xlarge',  # Replace with your desired instance type
                'InitialInstanceCount': 1,
                'ModelName': model_name,
                'VariantName': 'AllTraffic'
            }
        ]
    )

    # Create endpoint for SageMaker
    sm_endpoint = sm_client.create_endpoint(
        EndpointName=endpoint_name,
        EndpointConfigName=endpoint_config_name
    )

    print(f'SageMaker endpoint "{endpoint_name}" successfully deployed.')

if __name__ == '__main__':
    model_path = 'models'  # Replace with the path where your model is stored in S3
    model_name = 'my-model'  # Replace with the name you want to give to your SageMaker model
    endpoint_name = 'my-endpoint'  # Replace with the desired endpoint name
    deploy_model(model_path, model_name, endpoint_name)