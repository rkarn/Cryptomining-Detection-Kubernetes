Syscalls_frame_Miner = pd.concat([ Syscalls_frame['bitcoin_syscalls.txt'], Syscalls_frame['dashcoin_syscalls.txt'], Syscalls_frame['vertcoin_syscalls.txt'], Syscalls_frame['litecoin_syscalls.txt'], Syscalls_frame['bytecoin_syscalls.txt'] ])

Syscalls_frame_App = pd.concat([ Syscalls_frame['cassandrastress_syscalls.txt'], Syscalls_frame['mysqlstress_syscalls.txt'], Syscalls_frame['dlearn_syscalls.txt'] ])        

import csv
import numpy as np
import os
import time
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import pylab
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.cluster import KMeans
pylab.rcParams['figure.figsize'] = (16.0, 5.0)
import sklearn
import re

#Confusion Matrix Function
from sklearn.metrics import confusion_matrix
import itertools
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):

    #print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    #Creating the sequence from the dataframe
def split_list (input_list, window_size):
    splitted_list = []
    for i in range(0, len(input_list), window_size):
        try:
            curr_list = input_list[i:i+window_size]
            splitted_list.append(curr_list)
        except:
            pass
    return splitted_list

def n_grams_split(input_list, len_ngram):
    n_gram_seq = []
    for i in range(len(input_list)-len_ngram+1):
        n_gram_seq.append(input_list[i:i+len_ngram])
    return(n_gram_seq)
#0 --> for syscalls sequence
sequence_type = 0

#Window size for sequence generation
window_size = 20

ML_TYPES = ['DECISION TREE']
CV_SCORES = []

Sequence_normal = Syscalls_frame_App[Syscalls_frame_App.columns[sequence_type]]
Sequence_normal = list(Sequence_normal)
#Sequence_normal = split_list(Sequence_normal,window_size)
Sequence_normal = n_grams_split(Sequence_normal,window_size)
print '# of normal application sequence:',len(Sequence_normal), '. Last seqeunce size:', len(Sequence_normal[-1])

Sequence_anomaly = Syscalls_frame_Miner[Syscalls_frame_Miner.columns[sequence_type]]
Sequence_anomaly = list(Sequence_anomaly)
#Sequence_anomaly = split_list(Sequence_anomaly,window_size)
Sequence_anomaly = n_grams_split(Sequence_anomaly,window_size)
print '# of anomaly sequence:',len(Sequence_anomaly), '. Last seqeunce size:', len(Sequence_anomaly[-1])

#Creating the new dataframe from the sequence
normal_seq_frame = pd.DataFrame(Sequence_normal)
normal_seq_frame['label'] = np.zeros(len(normal_seq_frame[0])) 
if len(Sequence_normal[-1]) < window_size:
    normal_seq_frame = normal_seq_frame.drop(normal_seq_frame.index[len(normal_seq_frame)-1])
    print 'Last deep_learning sequence deleted.'


anomaly_seq_frame = pd.DataFrame(Sequence_anomaly)
anomaly_seq_frame['label'] = np.ones(len(anomaly_seq_frame[0])) 
if len(Sequence_anomaly[-1]) < window_size:
    anomaly_seq_frame = anomaly_seq_frame.drop(anomaly_seq_frame.index[len(anomaly_seq_frame)-1])
    print 'Last anomaly sequence deleted.'

#combining normal and anomaly sequence together 
Complete_seq_frame = pd.concat([normal_seq_frame, anomaly_seq_frame], ignore_index=True)
print '# of normal application sequence:',len(normal_seq_frame), '. # of anomaly sequence:', len(anomaly_seq_frame), '. # of normal+anomaly sequence:', len(Complete_seq_frame)

X = Complete_seq_frame.values[:,:-1]
Y = Complete_seq_frame.values[:,-1]
Y=Y.astype('int')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42) 
print 'Trainset size is: {0}. Testset size is: {1}'.format(X_train.shape,X_test.shape)

#Decision Tree
import time
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion ='entropy', max_leaf_nodes=None); 
start = time.time()
print "Training: Decision Tree Modeling"; clf=clf.fit(X_train, Y_train);  
end = time.time()
print 'Training time:',(end - start)

start = time.time()
pred = clf.predict(X_test)
end = time.time()
print 'Prediction time:',(end - start)
scores = round(accuracy_score(Y_test, pred),3)*100
print 'Accuracy = {0}%'.format(scores)
# Compute confusion matrix
cnf_matrix = confusion_matrix(Y_test, pred)
np.set_printoptions(precision=2)
class_names=[0,1]
# Plot confusion matrix
plt.figure(figsize=(3,3))
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix')
plt.savefig('confusionmatrix_decisiontree25.pdf',bbox_inches='tight')
plt.show()
print "-----------*----------------"

#Tree Plotting
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  class_names=['1','0'],
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  

Image(graph.create_png())

graph.write_png('decisiontree_syscall.png')
