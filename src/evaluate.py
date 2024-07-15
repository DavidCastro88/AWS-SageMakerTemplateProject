import boto3
import pandas as pd
from sagemaker.serializers import CSVSerializer
from sagemaker.deserializers import JSONDeserializer

def evaluate_model(endpoint_name, test_data_path):
    sm_runtime = boto3.client('sagemaker-runtime')

    # Load test data
    test_data = pd.read_csv(test_data_path)

    predictions = []
    for index, row in test_data.iterrows():
        # Prepare data for inference request (example using CSVSerializer)
        payload = ','.join(map(str, row.tolist()))
        response = sm_runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='text/csv',
            Accept='application/json',
            Body=payload
        )

        # Deserialize the response (example using JSONDeserializer)
        result = response['Body'].read().decode('utf-8')
        predictions.append(result)

        # Process inference results and perform evaluation
        # Here you could compare predictions with actual values, calculate metrics, etc.
        # For example, calculate accuracy, RMSE, etc.

        # Example of printing evaluation metrics
    print("Evaluación del modelo completada.")
    return predictions 

if __name__ == "__main__":
    endpoint_name = 'tu-endpoint-sagemaker'
    test_data_path = 'data/test_data.csv'  

    evaluate_model(endpoint_name, test_data_path)