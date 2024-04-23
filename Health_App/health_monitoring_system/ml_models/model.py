import tensorflow as tf

def create_model(input_shape):
    """Creates and compiles the LSTM model for ECG classification."""

    
    # Note that the model architecture should match the one used during training.So the function signature should include the input_shape parameter.
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(128, return_sequences=True, input_shape=input_shape),
        tf.keras.layers.LSTM(64),
        tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
    ])
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def load_model(model_path):
    """Loads a pre-trained model from the specified path."""
    return tf.keras.models.load_model(model_path)

def predict(model, data):
    """Makes predictions on the provided data using the loaded model."""
    predictions = model.predict(data)
    # Post-process predictions and generate recommendations according to your logic to convert predictions to recommendations.
    # Lemme give a sample prediction with simple logic here.
    if predictions[0][0] > 0.5:
        recommendation = "Normal ECG"
    else:
        recommendation = "Potential anomaly detected. Seek medical advice."
    return recommendation