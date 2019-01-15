# importing libraries
from keras.models import Sequential
from keras.layers import Dense, Activation, BatchNormalization, Flatten
from keras.utils import np_utils
from keras import losses
from keras import backend as K
from keras.utils.vis_utils import plot_model
import numpy as np
import pandas as pd
import tensorflow as tf
import random as rn
import os
from sklearn.model_selection import train_test_split
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Conv1D, MaxPooling1D
from keras.utils import to_categorical
from keras import optimizers
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
import h5py
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.utils import shuffle
from sklearn.model_selection import KFold 


os.environ['PYTHONHASHSEED'] = '0'
np.random.seed(123)
rn.seed(123)

session_conf = tf.ConfigProto(intra_op_parallelism_threads=0, inter_op_parallelism_threads=0)
#session_conf = tf.ConfigProto()
tf.set_random_seed(123)
sess = tf.Session(graph=tf.get_default_graph(), config=session_conf)
K.set_session(sess)

# reading the data. change of name for new data set.
train = pd.read_csv("6apr20_123.csv",delimiter=",",header=None)
train=shuffle(train)

# data seperated into attributes and classes.
x = train.values[:,0:train.shape[1]-1]
y = train.values[:,train.shape[1]-1:train.shape[1]]

kf = KFold(n_splits=10) 
kf.get_n_splits(x)

i=0
for train_index, test_index in kf.split(x):	

	file="model"+str(i) + ".hdf5"
	

	# test train split using kflod library indexes
	xTrain, xTest = x[train_index], x[test_index]
	yTrain, yTest = y[train_index], y[test_index]

	# spliting training data into training + validation.
	xTrain, xVal , yTrain, yVal = train_test_split(xTrain,yTrain,test_size=0.15)

	batchSize = len(xTrain)

	# reshaping for 2D convolution
	carrier = 180		#  = 30 * number of antennas. given all 30 subcarriers used and all antennas of both nodes
	numberWindows = int(xTrain.shape[1]/carrier)

	# reshaping the 1D input data into 2D for 2D CNN
	xTrain = xTrain.reshape(xTrain.shape[0] ,carrier,numberWindows, 1)
	xTest = xTest.reshape(xTest.shape[0],carrier,numberWindows,1)
	xVal = xVal.reshape(xVal.shape[0],carrier,numberWindows,1)
	
	# one hot encoding the data. To be used in case there more than binary classes.
	yTrainHot = to_categorical(yTrain, num_classes=2)		
	yTestHot = to_categorical(yTest, num_classes=2)
	yValHot = to_categorical(yVal, num_classes=2)


	# Defining the model
	model1 = Sequential([
	    Conv2D(filters=8, kernel_size=[2,2] , strides=1, activation='relu', input_shape=[carrier,numberWindows,1]),
	    MaxPooling2D(pool_size=[3,2]),
	    Flatten(),
	    Dense(200),				# Nodes in first hidden layer. To add a layers add dense,batchnormalization and acivation.
	    BatchNormalization(),
	    Activation('relu'),
	    Dense(100),				# second hidden layer with 100 nodes
	    BatchNormalization(),
	    Activation('relu'),
	    Dense(2),				# output layer. 2 nodes for binary and number of classes in case of multiclass.
	    BatchNormalization(),
	    Activation('softmax')
	])


	# Model checkpoints and stoppers. Save the best weights and stops the model when no increase in performance to save time.
	model1.compile(optimizer='nadam', loss='mean_squared_error', metrics=['accuracy'])
	esc = EarlyStopping(monitor='val_loss', min_delta=0, patience=100, verbose=0, mode='auto',)
	cp = ModelCheckpoint(filepath=file, verbose=1, save_best_only=True, save_weights_only=True)


	# fitting the model. 
	m1 = model1.fit(xTrain, yTrainHot , batch_size=batchSize, epochs=500, callbacks=[esc, cp],validation_data=(xVal,yValHot))


	# loading the best weights
	model1.load_weights(file)

	# computing training accuracy using best weights
	training = model1.evaluate(xTrain, yTrainHot)

	# predicting classes for testing cases.
	modelresults = model1.predict(xTest)
	

	# Coverting one-hot-encoded data back into single column for computing accuracy
	modelr=[]
	class_names = ['metal' , 'non-metal']

	for i2 in range(0,len(modelresults)):
		if modelresults[i2,0] >= modelresults[i2,1]:
			modelr.append(0)
		else:
			modelr.append(1)
 

	# Compute confusion matrix
	print(confusion_matrix(modelr, yTest))


	# saving the the results for each iteration in cross validation in the text file named below.
	# results for all 10 folds were averaged using the text file.
	f= open("results.txt","a")
	print('training data')
	print(model1.metrics_names[0], training[0])
	print(model1.metrics_names[1], training[1]*100)

	f.write('training data'+"\n")
	f.write(str(model1.metrics_names[0])+"\n")
	f.write(str(training[0])+"\n")
	f.write(str(model1.metrics_names[1])+"\n")
	f.write(str(training[1]*100)+"\n")
	testing = model1.evaluate(xTest,yTestHot)

	print('testing data')
	print(model1.metrics_names[0], testing[0])
	print(model1.metrics_names[1], testing[1]*100)
	f.write('testing data'+"\n")
	f.write(str(model1.metrics_names[0])+"\n")
	f.write(str(testing[0]))
	f.write(str(model1.metrics_names[1])+"\n")
	f.write(str(testing[1]*100)+"\n")
	f.write('confusion matrix'+"\n")
	f.write(str(confusion_matrix(modelr, yTest))+"\n")
	f.close()
	
	i=i+1
	
