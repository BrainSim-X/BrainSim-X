import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load dataset
data = load_iris()
X = data.data
y = tf.keras.utils.to_categorical(data.target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

def create_model(activation_function):
    model = Sequential([
        Dense(10, activation=activation_function, input_shape=(X_train.shape[1],)),
        Dense(3, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Evaluate different activation functions
activations = ['relu', 'elu', 'sigmoid', 'swish']
results = {}
for act in activations:
    model = create_model(act)
    model.fit(X_train, y_train, epochs=50, verbose=0)
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
    results[act] = test_acc

print("Activation Function Accuracy Comparison:", results)
