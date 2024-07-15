import os
import argparse
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # Arguments for data location
    parser.add_argument('--input-data', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--output-data', type=str, default=os.environ.get('SM_CHANNEL_OUTPUT'))

    args = parser.parse_args()

    # Load the data
    input_data_path = args.input_data
    df = pd.read_csv(input_data_path)

    # Separate data into features and labels
    X = df.drop(columns=['target_column'])
    y = df['target_column']

    # Data preprocessing (example: scale features)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Save preprocessed data
    output_data_path = args.output_data
    os.makedirs(output_data_path, exist_ok=True)

    # Save training and validation data
    train_data_path = os.path.join(output_data_path, 'train_data.csv')
    val_data_path = os.path.join(output_data_path, 'val_data.csv')

    pd.DataFrame(X_train).to_csv(train_data_path, header=False, index=False)
    pd.DataFrame(X_val).to_csv(val_data_path, header=False, index=False)

    # Save necessary objects for inference
    scaler_path = os.path.join(output_data_path, 'scaler.joblib')
    joblib.dump(scaler, scaler_path)

    print(f"Preprocessing complete. Training data saved to {train_data_path}")
    print(f"Validation data saved to {val_data_path}")
    print(f"Scaler saved to {scaler_path}")