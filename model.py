from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
import joblib

X, y = datasets.load_iris(return_X_y= True)

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, 'dt.joblib')
