# Machine Learning Model API

This repository contains a Flask-based RESTful API for uploading data, training a machine learning model, and making predictions. The model is trained using a logistic regression algorithm, and the API provides endpoints for training, making predictions, and uploading data.

## Features:
- **File Upload Endpoint**: Allows users to upload CSV files for training the model.
- **Model Training Endpoint**: Trains a logistic regression model using the uploaded data.
- **Prediction Endpoint**: Makes predictions on new data using the trained model.

## Setup and Installation

### Prerequisites
Ensure you have the following installed on your machine:
- Python 3.6+
- `pip` (Python package manager)

### Steps to Set Up the API

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   python app.py
   ```

   The Flask server will start running on `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Upload Endpoint (`/upload`)

**Method**: `POST`

**Description**: Upload a CSV file to be used for training the model. The file should contain the relevant features and a `Target` column.

**Request**:
- `file`: The CSV file to be uploaded.

**Example Request (using Postman or cURL)**:
```bash
curl -X POST -F "file=@your_file.csv" http://127.0.0.1:5000/upload
```

**Example Response**:
```json
{
  "message": "File successfully uploaded"
}
```

### 2. Train Endpoint (`/train`)

**Method**: `POST`

**Description**: Train the logistic regression model using the uploaded CSV file.

**Request**:
- `file`: The CSV file to train the model.

**Example Request (using Postman or cURL)**:
```bash
curl -X POST -F "file=@your_file.csv" http://127.0.0.1:5000/train
```

**Example Response**:
```json
{
  "Accuracy": 0.92,
  "Precision": 0.90,
  "Recall": 0.88,
  "F1-score": 0.89
}
```

### 3. Prediction Endpoint (`/predict`)

**Method**: `POST`

**Description**: Make a prediction using the trained model. The input should contain values for the features used for training.

**Request**:
- `data`: A JSON object containing the feature values for the prediction.

**Example Request (using Postman or cURL)**:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"Air temperature [K]": 300, "Process temperature [K]": 320, "Rotational speed [rpm]": 1500, "Torque [Nm]": 50, "Tool wear [min]": 40}' http://127.0.0.1:5000/predict
```

**Example Response**:
```json
{
  "Downtime": "Yes",
  "Confidence": 0.87
}
```

## Troubleshooting

- If you encounter any issues related to dependencies or libraries, make sure all the required Python packages are installed by running `pip install -r requirements.txt`.
- If the server is not starting, ensure that port 5000 is not already in use. You can change the port by modifying the `app.run()` call in the `app.py` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask for building the API.
- scikit-learn for providing machine learning algorithms and tools.
