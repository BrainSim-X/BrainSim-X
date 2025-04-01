Lesson 2: Optimization of Activation Functions

2.1 Exploring Key Activation Functions

The Role of Activation Functions:

Activation functions introduce nonlinearity into neural network models, enabling them to capture complex patterns. Some key activation functions include:

ReLU (Rectified Linear Unit):

Formula: f(x) = max(0, x)

Advantages: Computationally efficient, reduces the vanishing gradient problem, and allows deeper networks to train effectively.

Disadvantages: Can cause "dying ReLU" issues, where neurons become inactive and stop learning.

ELU (Exponential Linear Unit):

Formula:

f(x) = x if x > 0

f(x) = α(e^x - 1) if x ≤ 0

Pros: Maintains negative outputs, which helps accelerate learning.

Cons: More computationally expensive due to the exponential function.

Swish:

Formula: f(x) = x · sigmoid(x) = x / (1 + e^(-x))

Pros: A self-gated activation function that can outperform ReLU in deep learning tasks by providing smoother gradients.

Cons: Higher computational cost due to the additional sigmoid operation.

Function   | Description                        | Advantages                        | Disadvantages
-----------|------------------------------------|----------------------------------|---------------------------
ReLU       | Linear for positive inputs        | Sparse representation            | Not zero-centered
ELU        | Smooth transition for negatives   | Robust against noise             | Higher computational cost
Swish      | Non-monotonic and smooth         | Improves model accuracy          | Computationally intensive


2.2 Performance Analysis
Empirical Evaluations:
Comparing activation functions based on performance metrics like accuracy and convergence speed:

Neural networks trained with ReLU often converge faster and perform better on complex tasks compared to sigmoid functions, especially in deeper architectures.

2.3 Hands-on Implementation: Activation Function Comparison

import tensorflow as tf  
from tensorflow.keras.models import Sequential  
from tensorflow.keras.layers import Dense  
from sklearn.datasets import load_iris  
from sklearn.model_selection import train_test_split  

# Load dataset  
data = load_iris()  
X = data.data  
y = tf.keras.utils.to_categorical(data.target)  

# Train-test split  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  

# Function to create models with different activation functions  
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

This code evaluates several activation functions on a simple dataset, helping uncover how 
architectural choices affect performance. 
