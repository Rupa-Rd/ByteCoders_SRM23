import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

file = open('random_forest_model.pkl', 'rb')    
db = pickle.load(file)


test = np.array( [False,True,False,False,False,True,False,False,False,False,True,False,False,True,False,False,False,True,False,False,True,False,False,True,False,False,False,True,False,False,True,False,False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,True,False,False,6,12,3,12,0,0,0,4,55] )

def re_admission_prediction():

    df_train=pd.read_csv (r"df_naive.csv")

    rows_pos = df_train.readmitted == 1
    df_train_pos = df_train.loc[rows_pos]
    df_train_neg = df_train.loc[~rows_pos]

    # merge the balanced data
    df_train = pd.concat([df_train_pos, df_train_neg.sample(n = len(df_train_pos))],axis = 0)

    # shuffle the order of training samples 
    df_train = df_train.sample(n = len(df_train)).reset_index(drop = True)

    X_train = df_train.loc[:, df_train.columns != 'readmitted'].values
    y_train=df_train['readmitted'].values

    scaler  = StandardScaler()
    scaler.fit(test.reshape(1,-1))
    X_train_tf = scaler.transform(X_train)
    test_tf = scaler.transform(test.reshape(1,-1))

    classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    classifier.fit(X_train_tf, y_train)
    prediction_test =classifier.predict(test_tf.reshape(1,-1))
    return prediction_test[0]


print(re_admission_prediction())