
### * NEURAL NETWORKS
## * ARTIFICIAL NEURAL NETWORK
# a mathematical model for learning inspired by biological neural networks
'''
  models a mathematical function mappping inputs to outputss based on the network's structure and parameters

  ACTIVATION FUNCTION
  function calculating a node's output (refer to learning algorithms)
    e.g., 
      1. Step Function
        g(x) = 1 if x ≥ 0, else 0
        * can represent "OR" (with -1 bias) and "AND" (with -2 bias)

      2. Logistic Sigmoid
        g(x) = e^x / (e^x + 1)

      3. Rectified Linear Unit (ReLU)
        g(x) = max(0, x)
      
  used -> hw(x) = g(w • x)
  * weights are also called "biases"

  SIMPLE NEURAL NETWORK
  consists of single layer of:
    • input nodes
    • output nodes
    • activation function
'''


## * GRADIENT DESCENT
# algorithm for minimizing loss in training neural networks
'''
  OUTLINE
    1. initialize weights randomly
    2. repeat:
      • calculate gradient baseed on all data points that will lead to drop in loss
      • update weights according to gradient

  -> time complexity: O(n^2)

  STOCHASTIC GRADIENT DESCENT
  calculates gradient based on ONE data point (during iteration)
  -> time complexity: O(n) 
  -> less accurate than gradient descent

  MINI-BATCH GRADIENT DESCENT
  calculates gradient based on a subset of data points (during iteration)
  -> time complexity: O(n)
  -> more accurate than stochastic gradient descent but less accurate than gradient descent

  * activation functions can be used to output probabilities that can be used to classify data (i.e., supervised learning)
'''

## * PERCEPTRON
# a single layer neural network
# only capable of learning linearly separable decision boundaries

## * MULTI-LAYER PERCEPTRON
# aritificial neural network with:
'''
  • an input layer
  • one or more hidden layers
  • an output layer

  uses backpropagation 
    PSEUDOCODE:
      • start with random weights
      • repeat:
        • calculate error for output layer
        • for each layer, starting with output layer and moving inwards towards earliest hidden layer:
          • propagate error backwards
          • update weights

  allows for more complex decision boundaries
  risk of overfitting increases with number of hidden layers
'''
## ! 36:56