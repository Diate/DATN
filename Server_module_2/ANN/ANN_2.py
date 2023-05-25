from keras import models
import pandas as pd
import numpy as np
import pickle
X_test = pd.read_csv("X_train2.csv",sep=";")
model_Part1 = models.load_model("Part1.h5")
y_predict_test=model_Part1.predict(X_test, batch_size=1)
y_predict_test = np.concatenate(y_predict_test)
X_test['Predict'] = y_predict_test
model_Part2 = pickle.load(open('Part2.sav', 'rb'))
Y_result = model_Part2.predict(X_test)
A = np.mean(Y_result)
print(A)