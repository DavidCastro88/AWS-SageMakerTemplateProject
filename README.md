![SageMaker](https://github.com/aws/sagemaker-training-toolkit/raw/master/branding/icon/sagemaker-banner.png)


# **AWS SageMaker Template Project**

[![Latest Version](https://img.shields.io/pypi/v/sagemaker-training.svg)](https://pypi.python.org/pypi/sagemaker-training) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/sagemaker-training.svg)](https://pypi.python.org/pypi/sagemaker-training)

This repository serves as a template for organizing and running machine learning projects using AWS SageMaker. It provides a structured directory layout and example scripts for common tasks such as data preprocessing, model training, evaluation, and deployment.

```
AWS-SageMakerTemplateProject/
├── config/
│ ├── hyperparameters.json
│ ├── sage_maker_config.json
├── data/
│ ├── processed/
│ ├── raw/
├── notebooks/
│ ├── data_processing.ipynb
│ ├── exploratory_data_analysis.ipynb
│ ├── model_evaluation.ipynb
├── scripts/
│ ├── download_data_from_s3.py
│ ├── upload_data_to_s3.py
├── src/
│ ├── deploy.py
│ ├── evaluate.py
│ ├── preprocess.py
│ ├── train.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
```

## **Getting Started**
  **Prerequisites:**
  
    - Python 3.6 or higher
    - AWS account with SageMaker permissions
    - AWS CLI configured
    - SageMaker Python SDK installed (pip install sagemaker)

## **Setting Up**

1. Clone the repository:

    `https://github.com/DavidCastro88/AWS-SageMakerTemplateProject.git
    cd AWS-SageMakerTemplateProject`

2. Install dependencies:
   
     `pip install -r requirements.txt`

4. Configure AWS CLI:
   
     `aws configure`

## **Acknowledgements**:
  
  - [AWS SageMaker Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
    
  - [SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/)

## :handshake: Contributing

Feel free to contribute to this project by submitting issues or pull requests. Happy coding!
