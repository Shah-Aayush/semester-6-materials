# Deep Learning Questions

1. **What is unstable gradient problem? Discuss in details.**
	- A fundamental problem that occurs to gradients in early layers of a neural network. The unstable gradient problem is a fundamental problem that occurs in a neural network, that entails that a gradient in a deep neural network tends to either explode or vanish in early layers.
	- The unstable gradient problem is not necessarily the vanishing gradient problem or the exploding gradient problem, but is rather due to the fact that gradient in early layers is the product of terms from all proceeding layers. More layers make the network an intrinsically unstable solution. Balancing all products of terms is the only way each layer in a neural network can close at the same speed and avoid vanishing or exploding gradients. Balanced product of terms occurring by chance becomes more and more unlikely with more layers. Neural networks therefor have layers that learn at different speeds, without being given any mechanisms or underlying reason for balancing learning speeds.
	- When magnitudes of gradients accumulate, unstable networks are more likely to occur, which is a cause of poor prediction results.
	
2. **Critically compare feed forward neural networks with convolutional neural networks.**
	- A feed-forward network connects every pixel with each node in the following layer, ignoring any spatial information present in the image. By contrast, a convolutional architecture looks at local regions of the image.
	- Convolutional neural network is better than a feed-forward network since CNN has features parameter sharing and dimensionality reduction. Because of parameter sharing in CNN, the number of parameters is reduced thus the computations also decreased. The main intuition is the learning from one part of the image is also useful in another part of the image. Because of the dimensionality reduction in CNN, the computational power needed is reduced. 
	- **Feed Forward Neural Network**
		> ![](https://i1.wp.com/cloudvane.net/wp-content/uploads/2019/11/fnn.png?w=1302&ssl=1)
		- Feedforward neural networks are the most general-purpose neural network. The entry point is the input layer and it consists of several hidden layers and an output layer. Each layer has a connection to the previous layer. This is one-way only, so that nodes can’t for a cycle. The information in a feedforward network only moves into one direction – from the input layer, through the hidden layers to the output layer. It is the easiest version of a Neural Network. The below image illustrates the Feedforward Neural Network.

		
	- **Convolutional Neural Networks (CNN)**
		> ![](https://editor.analyticsvidhya.com/uploads/90650dnn2.jpeg)
		- The Convolutional Neural Network is very effective in Image recognition and similar tasks. For that reason it is also good for Video processing. The difference to the Feedforward neural network is that the CNN contains 3 dimensions: width, height and depth. Not all neurons in one layer are fully connected to neurons in the next layer. There are three different type of layers in a Convolutional Neural Network, which are also different to feedforward neural networks:

		- Convolution Layer
			- Convolution puts the input image through several convolutional filters. Each filter activates certain features, such as: edges, colors or objects. Next, the feature map is created out of them. The deeper the network goes the more sophisticated those filters become. The convolutional layer automatically learns which features are most important to extract for a specific task.

		- Rectified linear units (ReLU)
			- The goal of this layer is to improve the training speed and impact. Negative values in the layers are removed.

		- Pooling/Subsampling
			- Pooling simplifies the output by performing nonlinear downsampling. The number of parameters that the network needs to learn about gets reduced. In convolutional neural networks, the operation is useful since the outgoing connections usually receive similar information.
		
3. **What is dropout? How is it useful?**
	- The term “dropout” refers to dropping out units (both hidden and visible) in a neural network.
	- Simply put, dropout refers to ignoring units (i.e. neurons) during the training phase of certain set of neurons which is chosen at random. By “ignoring”, I mean these units are not considered during a particular forward or backward pass.
	- More technically, At each training stage, individual nodes are either dropped out of the net with probability 1-p or kept with probability p, so that a reduced network is left; incoming and outgoing edges to a dropped-out node are also removed.
	- Observations : 
		- Dropout forces a neural network to learn more robust features that are useful in conjunction with many different random subsets of the other neurons. 
		- Dropout roughly doubles the number of iterations required to converge. However, training time for each epoch is less.
		- With H hidden units, each of which can be dropped, we have 2^H possible models. In testing phase, the entire network is considered and each activation is reduced by a factor p.
	- why do we need dropout?
		- “to prevent over-fitting”.
		- A fully connected layer occupies most of the parameters, and hence, neurons develop co-dependency amongst each other during training which curbs the individual power of each neuron leading to over-fitting of training data.
		
	- In machine learning, regularization is way to prevent over-fitting. Regularization reduces over-fitting by adding a penalty to the loss function. By adding this penalty, the model is trained such that it does not learn interdependent set of features weights. Those of you who know Logistic Regression might be familiar with L1 (Laplacian) and L2 (Gaussian) penalties.
	- Dropout is an approach to regularization in neural networks which helps reducing interdependent learning amongst the neurons.
		- Training Phase:
			- For each hidden layer, for each training sample, for each iteration, ignore (zero out) a random fraction, p, of nodes (and corresponding activations).
		- Testing Phase:
			- Use all activations, but reduce them by a factor p (to account for the missing activations during training).