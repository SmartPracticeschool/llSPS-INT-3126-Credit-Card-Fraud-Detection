# Importing the libraries
import pandas as pd
import pickle

dataset = pd.read_csv('creditcard.csv')
FilteredData = dataset[['Time','V1','V7','V13','V27','Amount', 'Class']]

X =FilteredData .iloc[:, :6]
y = FilteredData .iloc[:, -1]

#Splitting the dataset into Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.25)

#Build Random Forest Calssifier
from sklearn.ensemble import RandomForestClassifier
rmf = RandomForestClassifier(max_depth=3, random_state=0)
rmf.fit(x_train, y_train)
  
# Saving model to disk
pickle.dump(rmf, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[0	,-1.359807,0.239599,-0.991390,0.133558	,149.62]]))