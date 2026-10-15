import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics  import(
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
#create and load dataset
data = {
    'rpm':[1000, 1200, 1400, 1600, 1800, 
           2000, 2200, 2400, 2600, 2800],

    "load":[30, 35, 40, 50, 55, 
            60,65, 70, 75, 80],

    'vibration':[1.2, 1.3,1.5,1.7,1.9,2.1,
                 2.3,2.5,2.8,3.2],

    "oprating hours":[2,3,4,5,6,
                      7,8,9,10,11],

    "ambient temp":[20, 20,21,21,22,
                    22,23,23,24,24],

    "machine_temp":[42,44,47,51,55,
                    59,63,68,74,81]
}
df = pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
  #define data and target 
X=df[["rpm", "load", "vibration", "oprating hours","ambient_temp"]]
y=df["machine_temp"]
#split data               into traning and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
#create and train the model
model = linearRegression()
model.fit(X_train, y_train)

y_predict=model.predict(X_test)
print( "predicted values",y_predict)
mae=mean_absolute_error(y_test,y_prdict)
msqe=mean_squared_error(y_test,y_prdict)
rmse=np.sqrt(mse)
r2=r2_score(y_test,y_prdict)
print("Mean Absolute Error:",mae)
print("Mean Squared  Error:", mse)
print('Root Mean Squared Error:',rmse)
print("R2 Score:",r2)

new_data =pd.DataFrame[(
    "rpm" : [2100], "load":[75],"vibration":[2.7], 
    "oprating_hours":[8], "ambient_temp":[24]
     predicted_temp = model.predict(new_data)
     print("predicted machine tempratute for new data:",  predicted_temp)

     plt.scatter(y_test, y_predict)
     plt.xlabel("Actual Machine Temprature")
     plt.ylabel("Predicted Machine Temprature")
     plt.title("Actual Vs predicted Machine")
     plt.show()
)]