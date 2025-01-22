from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

app = Flask(__name__)

model = None

#upload
@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files.get("file")
    
    if not uploaded_file:
        return jsonify({"error": "No file provided"}), 400
    
    file_path = f"./{uploaded_file.filename}"
    uploaded_file.save(file_path)
    
    return jsonify({"message": "File successfully uploaded"}), 200

# train
@app.route("/train", methods=["POST"])
def train_model():
    uploaded_file = request.files.get("file")
    
    if not uploaded_file:
        return jsonify({"error": "No file uploaded for model training"}), 400
    
    dataset = pd.read_csv(uploaded_file)

    features = [
        "Air temperature [K]", "Process temperature [K]", "Rotational speed [rpm]", 
        "Torque [Nm]", "Tool wear [min]"
    ]
    
    data_prepared = dataset[features + ["Target"]]
    X = data_prepared[features]
    y = data_prepared["Target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    global model
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    metrics = {
        "Accuracy": round(accuracy, 2),
        "Precision": round(precision, 2),
        "Recall": round(recall, 2),
        "F1-score": round(f1, 2)
    }

    return jsonify(metrics), 200

# predictions
@app.route("/predict", methods=["POST"])
def make_prediction():
    if model is None:
        return jsonify({"error": "The model has not been trained yet"}), 400
    
    input_data = request.get_json()

    if not input_data:
        return jsonify({"error": "No data provided for prediction"}), 400

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)
    prediction_confidence = model.predict_proba(input_df).max()

    result = {
        "Downtime": "Yes" if prediction[0] == 1 else "No",
        "Confidence": round(prediction_confidence, 2)
    }

    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
