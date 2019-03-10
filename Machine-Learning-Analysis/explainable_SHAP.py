import xgboost
import shap

# load JS visualization code to notebook
shap.initjs()

X_trainframe=pd.DataFrame(X_train, columns=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20']) 
X_testframe=pd.DataFrame(X_test, columns=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20']) 

# train XGBoost model
model = xgboost.train({"learning_rate": 0.01}, xgboost.DMatrix(X_train, label=Y_train), 100)

# explain the model's predictions using SHAP values
# (same syntax works for LightGBM, CatBoost, and scikit-learn models)
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_train)

# visualize the first prediction's explanation
shap.force_plot(explainer.expected_value, shap_values[1,:], X_testframe.iloc[1,:])

shap.force_plot(explainer.expected_value, shap_values[9,:], X_testframe.iloc[9,:])

shap.force_plot(explainer.expected_value, shap_values[0,:], X_testframe.iloc[0,:])

# visualize the training set predictions
shap.force_plot(explainer.expected_value, shap_values[0:1000,:], X_trainframe.iloc[0:1000,:])

#Plot for samples of vertcoin
vertcoin_syscalls = pd.DataFrame(n_grams_split(syscalldict['vertcoin_syscalls.txt'],window_size))
vertcoin_syscalls = vertcoin_syscalls.values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(vertcoin_syscalls)

shap.force_plot(explainer.expected_value, shap_values[0:5000,:], vertcoin_syscalls[0:5000,:])

#plot for samples of mysql application
mysqlstress_syscalls = pd.DataFrame(n_grams_split(syscalldict['mysqlstress_syscalls.txt'],window_size))
mysqlstress_syscalls = mysqlstress_syscalls.values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(mysqlstress_syscalls)

shap.force_plot(explainer.expected_value, shap_values[0:5000,:], mysqlstress_syscalls[0:5000,:])

#Artificial neural Network Visualizer
import keras
from keras.models import Sequential
from keras.layers import Dense
classifier = Sequential()
classifier.add(Dense(output_dim = 20, init = 'uniform', activation = 'relu', input_dim = 20))
classifier.add(Dense(output_dim = 20, init = 'uniform', activation = 'relu'))
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
classifier.fit(X_train, Y_train, batch_size = 100, nb_epoch = 10)
pred = classifier.predict(X_test)
pred = (pred > 0.5)
scores = round(accuracy_score(Y_test, pred),3)*100
print 'Accuracy = {0}%'.format(scores)
from ann_visualizer.visualize import ann_viz
import keras
from keras.models import Sequential
from keras.layers import Dense
classifier = Sequential()
classifier.add(Dense(output_dim = 20, init = 'uniform', activation = 'relu', input_dim = 20))
classifier.add(Dense(output_dim = 20, init = 'uniform', activation = 'relu'))
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
ann_viz(classifier, title="My first neural network", filename="network.gv", view = True)

