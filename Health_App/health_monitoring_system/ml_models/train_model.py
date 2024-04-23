import tensorflow as tf
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import AUC

# Function to parse a single TFRecord example
def parse_tfrecord(example_proto):
    feature_description = {
        # Define your feature descriptions here ...
        # e.g., 'ecg_data': tf.io.FixedLenFeature([sequence_length, n_features], tf.float32),
        #       'label': tf.io.FixedLenFeature([], tf.int64)
        # This depended on the data you stored in the TFRecord files,that's why I'm not able to provide the exact code since it's sensitive to the data you stored in the TFRecord files.
    }
    parsed_example = tf.io.parse_single_example(example_proto, feature_description)
    return parsed_example['ecg_data'], parsed_example['label']

# Create a dataset from TFRecord files in Cloud Storage
filenames = [
    # ... list of TFRecord file paths in Cloud Storage ...
]
dataset = tf.data.TFRecordDataset(filenames)

# Parse the TFRecord examples
dataset = dataset.map(parse_tfrecord)

# ... (optional additional preprocessing steps, e.g., normalization, feature scaling) ...

# Shuffle and batch the data
dataset = dataset.shuffle(buffer_size=10000).batch(batch_size=32)

# Split the data into training and validation sets
train_size = int(0.8 * len(dataset))
val_size = int(0.1 * len(dataset))
test_size = len(dataset) - train_size - val_size
train_dataset = dataset.take(train_size)
val_dataset = dataset.skip(train_size).take(val_size)
test_dataset = dataset.skip(train_size + val_size)

# Define the input shape based on your data
# (assuming your ECG data has 'sequence_length' and 'n_features' dimensions)
input_shape = (sequence_length, n_features)

# Create and compile the RNN model
model = Sequential([
    LSTM(128, return_sequences=True, input_shape=input_shape),
    LSTM(64),
    Dense(1, activation='sigmoid')  # Output layer for binary classification (normal/anomalous)
])
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=[AUC()])

# Train the model
model.fit(train_dataset, epochs=10, validation_data=val_dataset)

# Evaluate the model
loss, auc = model.evaluate(test_dataset)
print("Loss:", loss)
print("AUC:", auc)

# Save the trained model
model.save('ecg_model.h5')