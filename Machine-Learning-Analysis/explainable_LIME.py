import sklearn
import sklearn.datasets
from sklearn.neural_network import MLPClassifier
import numpy as np
import lime
import lime.lime_tabular
from __future__ import print_function
np.random.seed(1)
#X_train = X_train.astype(int); X_test = X_test.astype(int)
rf = MLPClassifier(solver='adam', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
rf.fit(X_train[:50000,:], Y_train[:50000])
explainer = lime.lime_tabular.LimeTabularExplainer(X_train[:50000,:], feature_names=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20'], class_names=['1','0'], discretize_continuous=True)

exp = explainer.explain_instance(X_test[2], rf.predict_proba, num_features=10)
exp.show_in_notebook(show_table=True, show_all=True)
exp.save_to_file('lime_explain0.html', predict_proba=True, show_predicted_value=True, show_table=True)

exp = explainer.explain_instance(X_test[119], rf.predict_proba, num_features=10)
exp.show_in_notebook(show_table=True, show_all=True)
exp.save_to_file('lime_explain1.html', predict_proba=True, show_predicted_value=True, show_table=True)

exp.as_pyplot_figure(label=1)

