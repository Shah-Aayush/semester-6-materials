# Deep Learning Questions-Answers

> Questions are taken from [`moodle`](https://sites.google.com/a/nirmauni.ac.in/2csde61---deep-learning/home/academic-docs/v-question-bank) and answers are prepared by me from the use of `google` 🥲

- ## What is unstable gradient problem? Discuss in details.
	- A fundamental problem that occurs to gradients in early layers of a neural network. The unstable gradient problem is a fundamental problem that occurs in a neural network, that entails that a gradient in a deep neural network tends to either explode or vanish in early layers.
	- The unstable gradient problem is not necessarily the vanishing gradient problem or the exploding gradient problem, but is rather due to the fact that gradient in early layers is the product of terms from all proceeding layers. More layers make the network an intrinsically unstable solution. Balancing all products of terms is the only way each layer in a neural network can close at the same speed and avoid vanishing or exploding gradients. Balanced product of terms occurring by chance becomes more and more unlikely with more layers. Neural networks therefor have layers that learn at different speeds, without being given any mechanisms or underlying reason for balancing learning speeds.
	- When magnitudes of gradients accumulate, unstable networks are more likely to occur, which is a cause of poor prediction results.
	
- ## Critically compare feed forward neural networks with convolutional neural networks.
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
		
- ## What is dropout? How is it useful?
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
		
- ## What are different architectures of CNN? Discuss its evaluation critically.
	- [in detail discussion can be found here](https://towardsdatascience.com/illustrated-10-cnn-architectures-95d78ace614d#:~:text=CNN%20Architectures%3A%20LeNet%2C%20AlexNet%2C,GoogLeNet%2C%20ResNet%20and%20more%20%E2%80%A6.)
	- LeNet-5
	- AlexNet
	- VGG-16
	- Inception-v1
	- Inception-v3
	- ResNet-50
	- Xception
	- Inception-v4
	- Inception-ResNets
	- ResNeXt-50
	
- ## What is transfer learning? In which scenarios, it is useful? Discuss different transfer learning scenarios.
	- In transfer learning, a machine exploits the knowledge gained from a previous task to improve generalization about another. For example, in training a classifier to predict whether an image contains food, you could use the knowledge it gained during training to recognize drinks.
	- Transfer learning is generally used: To save time and resources from having to train multiple machine learning models from scratch to complete similar tasks. As an efficiency saving in areas of machine learning that require high amounts of resources such as image categorisation or natural language processing.

- ## State the problem where transfer learning may be very useful. Justify your choice. Discuss how you will use transfer learning to solve this problem.
	- The main benefits of transfer learning include the saving of resources and improved efficiency when training new models. It can also help with training models when only unlabelled datasets are available, as the bulk of the model will be pre-trained.
	- Transfer learning reduces the efforts to build a model from scratch by using the fundamental logic or base algorithms within one domain and applying it to another. For instance, in the real-world, the balancing logic learned while riding a bicycle can be transferred to learn driving other two-wheeled vehicles.
	- More : 
		- Deep learning is definitely one of the specific categories of algorithms that has been utilized to reap the benefits of transfer learning very successfully. The following are a few examples:

		- Transfer learning for NLP: Textual data presents all sorts of challenges when it comes to ML and deep learning. These are usually transformed or vectorized using different techniques. Embeddings, such as Word2vec and FastText, have been prepared using different training datasets. These are utilized in different tasks, such as sentiment analysis and document classification, by transferring the knowledge from the source tasks. Besides this, newer models like the Universal Sentence Encoder and BERT definitely present a myriad of possibilities for the future.
		- Transfer learning for Audio/Speech: Similar to domains like NLP and Computer Vision, deep learning has been successfully used for tasks based on audio data. For instance, Automatic Speech Recognition (ASR) models developed for English have been successfully used to improve speech recognition performance for other languages, such as German. Also, automated-speaker identification is another example where transfer learning has greatly helped.
		- Transfer learning for Computer Vision: Deep learning has been quite successfully utilized for various computer vision tasks, such as object recognition and identification, using different CNN architectures. In their paper, How transferable are features in deep neural networks, Yosinski and their co-authors (https://arxiv.org/abs/1411.1792) present their findings on how the lower layers act as conventional computer-vision feature extractors, such as edge detectors, while the final layers work toward task-specific features.

- ## How can you use CNN for object detection? Propose possible modifications in the present state-of-the-art.
	- Object detection consists of two separate tasks that are classification and localization. R-CNN stands for Region-based Convolutional Neural Network. The key concept behind the R-CNN series is region proposals. Region proposals are used to localize objects within an image.
	- For each input image, we get a corresponding class as an output. Can we use this technique to detect various objects in an image? Yes, we can! Let’s look at how we can solve a general object detection problem using a CNN.
		1. First, we take an image as input
		2. Then we divide the image into various regions:
		3. We will then consider each region as a separate image.
		4. Pass all these regions (images) to the CNN and classify them into various classes.
		5. Once we have divided each region into its corresponding class, we can combine all these regions to get the original image with the detected objects
	- for **RCNN**
		Below is a succinct summary of the steps followed in RCNN to detect objects:

		- We first take a pre-trained convolutional neural network.
		- Then, this model is retrained. We train the last layer of the network based on the number of classes that need to be detected.
		- The third step is to get the Region of Interest for each image. We then reshape all these regions so that they can match the CNN input size.
		- After getting the regions, we train SVM to classify objects and background. For each class, we train one binary SVM.
		- Finally, we train a linear regression model to generate tighter bounding boxes for each identified object in the image.
	
- ## How can you use CNN for image classification? Propose possible modifications in the present state-of-the-art.
	- Convolutional neural networks (CNNs) are deep neural networks that have the capability to classify and segment images. CNNs can be trained using supervised or unsupervised machine learning methods, depending on what you want them to do.
		- Step 1: Choose a Dataset. ...
		- Step 2: Prepare Dataset for Training. ...
		- Step 3: Create Training Data. ...
		- Step 4: Shuffle the Dataset. ...
		- Step 5: Assigning Labels and Features. ...
		- Step 6: Normalising X and converting labels to categorical data. ...
		- Step 7: Split X and Y for use in CNN.
		- Step 8: Define, compile and train the CNN Model
		- Step 9: Accuracy and Score of model
	- disadvantages of current CNN
		- CNN do not encode the position and orientation of object.
		- Lack of ability to be spatially invariant to the input data.
		- Lots of training data is required.
- ## Can you use CNN for image super resolution? Propose possible solutions.
	- yes we can do this
	- what is image super resolution ?
		- Image super-resolution (SR) is the process of recovering high-resolution (HR) images from low-resolution (LR) images. It is an important class of image processing techniques in computer vision and image processing and enjoys a wide range of real-world applications, such as medical imaging, satellite imaging, surveillance and security, astronomical imaging, amongst others.
	- reconstructing a high-resolution version of an image given a low-resolution version. It leverages efficient "sub-pixel convolution" layers, which learns an array of image upscaling filters.
	- refer this paper for detail : [Fast and Accurate Image Super Resolution by Deep CNN with Skip Connection and Network in Network](https://arxiv.org/pdf/1707.05425.pdf)
	
- ## State different use cases of RNN and RBM. Identify novel applications of each.
	- Applications of Recurrent Neural Networks (RNNs)
		- RNN is great to recognize handwriting and speech, calculating each input (letter/word or a second of a audio file for example), to find the correct outputs. Basically, RNN was made to process information sequences.
			- Prediction problems.
			- Language Modelling and Generating Text.
			- Machine Translation.
			- Speech Recognition.
			- Generating Image Descriptions.
			- Video Tagging.
			- Text Summarization.
			- Call Center Analysis.
	- RBMs have found applications in dimensionality reduction, classification, collaborative filtering, feature learning, topic modelling and even many body quantum mechanics. They can be trained in either supervised or unsupervised ways, depending on the task.

- ## Ensemble method : Bagging Boosting Stacking
	- how to combine models in ensemble learning? : We can mention three major kinds of meta-algorithms that aims at combining weak learners:
	- **bagging**, that often considers homogeneous weak learners, learns them independently from each other in parallel and combines them following some kind of deterministic averaging process
	- **boosting**, that often considers homogeneous weak learners, learns them sequentially in a very adaptative way (a base model depends on the previous ones) and combines them following a deterministic strategy
	- **stacking**, that often considers heterogeneous weak learners, learns them in parallel and combines them by training a meta-model to output a prediction based on the different weak models predictions
	- Very roughly, we can say that bagging will mainly focus at getting an ensemble model with less variance than its components whereas boosting and stacking will mainly try to produce strong models less biased than their components (even if variance can also be reduced).

- ## Dead Neuron
	- The drawback of ReLU is that they cannot learn on examples for which their activation is zero. It usually happens if you initialize the entire neural network with zero and place ReLU on the hidden layers. Another cause is when a large gradient flows through, a ReLU neuron will update its weight and might be ended up with a big negative weight and bias. If this happens, this neuron will always produce 0 during the forward propagation, and then the gradient flowing through this neuron will forever be zero irrespective of the input.
	
	- In other words, the weights of this neuron will never be updated again. Such a neuron can be considered as a dead neuron, which is considered a kind of permanent “brain damage” in biological terms. A dead neuron can be thought of as a natural Dropout. But the problem is if every neuron in a specific hidden layer is dead, it cuts the gradient to the previous layer resulting in zero gradients to the layers behind it. It can be fixed by using smaller learning rates so that the big gradient doesn’t set a big negative weight and bias in a ReLU neuron. Another ﬁx is to use the Leaky ReLU, which allows the neurons outside the active interval to leak some gradient backward.




---

[Read more...](https://www.analyticsvidhya.com/blog/2017/01/must-know-questions-deep-learning/)

