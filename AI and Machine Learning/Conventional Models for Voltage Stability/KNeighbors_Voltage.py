# -*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
# import the necessary packages
import itertools
from sklearn.neighbors import KNeighborsClassifier
#%%
#In the future we can use the following command to reload data from the csv
imgPanel = pd.read_csv("C:/Users/Lenovo/CNN_KERAS_MNIST/voltage stability/gcv2.csv")
#The following codes use to retrive the 
#the trainig set and the label from the dataframe to use in the ML algorithm
Y= imgPanel['Bus voltage group'].as_matrix()
del imgPanel['Bus voltage group']
X = imgPanel.as_matrix()
#%%
X= (X - np.min(X, axis = 0)) / (np.max(X, axis = 0) + 0.001)
# STEP 1: split X and y into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=4)
print("Training and Testing data shapes:")
print("X_train.shape: {}".format(x_train.shape))
print("y_train.shape: {}".format(y_train.shape))
print("X_test.shape: {}".format(x_test.shape))
print("y_test.shape: {}".format(y_test.shape))
#%%
model = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
model.fit(x_train, y_train)
#%%
# Final evaluation of the model
y_pred = model.predict(x_test)
#p=model.predict_proba(x_test) # to predict probability
#print(p)
target_names = ['Acceptable', 'Near collapse']
print (classification_report(y_test, y_pred,target_names=target_names))
accuracy = accuracy_score(y_test, y_pred)
print("Random Forest Accuracy: %.2f%%" % (accuracy * 100.0))
#%%
# Final evaluation for each class and compute the confusion_matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
target_names1 = ['0', '1']
plt.imshow(cnf_matrix, interpolation='nearest', cmap= "YlOrBr_r")
plt.title('Confusion matrix')
plt.colorbar()
tick_marks = np.arange(len(target_names))
plt.xticks(tick_marks, target_names, rotation=45)
plt.yticks(tick_marks, target_names1, rotation=45)
thresh = cnf_matrix.max() / 2.
for i, j in itertools.product(range(cnf_matrix.shape[0]), range(cnf_matrix.shape[1])):
        plt.text(j, i, cnf_matrix[i, j],
                 horizontalalignment="center",
                 color="black" if cnf_matrix[i, j] > thresh else "white")
plt.tight_layout()
plt.title('Confusion Matrix', fontsize='12')
plt.ylabel('True label', fontsize='12')
plt.xlabel('Predicted label', fontsize='12')
plt.show()
#%%
