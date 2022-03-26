

from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split
import pickle
data = datasets.load_wine()

print(data.keys())

xtrain,xtest,ytrain,ytest = train_test_split(data.data,data.target,test_size=0.01)

model = linear_model.LinearRegression()

model.fit(xtrain,ytrain)

p= model.predict(xtest)
print(p,ytest)
print(model.score(xtest,ytest))

with open('wine_pickle','wb') as f:
    pickle.dump(model,f)
#0.9938476689573258 Accuracy
