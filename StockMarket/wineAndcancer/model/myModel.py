from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split

data = datasets.load_breast_cancer()
print(data.keys())
import pickle
xtrain,xtest,ytarin,ytest = train_test_split(data.data,data.target,test_size=0.01)

model =linear_model.LinearRegression()

model.fit(xtrain,ytarin)

l= model.predict(xtest)
print(l.round(),ytest)

with open('model_pickle','wb') as f:
    pickle.dump(model,f)
print(model.score(xtest,ytest))

#0.9777559355496426 accuracy