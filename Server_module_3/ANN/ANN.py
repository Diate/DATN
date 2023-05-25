import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import keras


from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import mean_absolute_percentage_error


df = pd.read_csv("Datamerge.csv",sep=";")

X = df.drop(columns=['Mass'])
print(X)
# X = X.drop(X.columns[0],axis=1)
Y = df[['Mass']]
from sklearn.model_selection import train_test_split
X_train, X_val, Y_train, Y_val=train_test_split(X,Y,train_size=0.4, test_size=0.6, random_state=0)
X_train2, X_val, Y_train2, Y_val=train_test_split(X_val,Y_val,train_size=0.65, test_size=0.35, random_state=0)
X_val, X_test, Y_val, Y_test=train_test_split(X_val,Y_val,train_size=0.5, test_size=0.5, random_state=0)
print(X_train.shape,X_train2.shape, X_val.shape, X_test.shape, Y_train.shape,Y_train2.shape, Y_val.shape, Y_test.shape)

model = keras.models.Sequential()
model.add(keras.layers.Dense(128, activation='sigmoid', input_shape=(6,)))
model.add(keras.layers.Dense(64, activation='sigmoid'))
model.add(keras.layers.Dense(32, activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(128, activation='sigmoid'))
model.add(keras.layers.Dense(64, activation='sigmoid'))
model.add(keras.layers.Dense(32, activation='relu'))
model.add(keras.layers.Dense(16, activation='relu'))
model.add(keras.layers.Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
model.fit(X_train, Y_train,validation_split=0.2, epochs=80)

y_predict=model.predict(X_train2, batch_size=1)
y_predict = np.concatenate(y_predict)
X_train2['Predict'] = y_predict

y_predict_val=model.predict(X_val, batch_size=1)
y_predict_val = np.concatenate(y_predict_val)
X_val['Predict'] = y_predict_val

y_predict_test=model.predict(X_test, batch_size=1)
y_predict_test = np.concatenate(y_predict_test)
X_test['Predict'] = y_predict_test


model_RFR = RandomForestRegressor(n_estimators=10)
model_RFR.fit(X_train2, Y_train2)
Y_pred = model_RFR.predict(X_f)
mean_absolute_percentage_error(Y_val, Y_pred)

Y_fn=model_RFR.predict(X_val[200:220])
print("Predict:",Y_fn.T)
print("Real:",Y_val[200:220].to_numpy().T)
