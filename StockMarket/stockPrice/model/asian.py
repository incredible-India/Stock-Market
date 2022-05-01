import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('asianp.csv',parse_dates=['Date'])

x= df.drop(['Date','High Price'],axis = 'columns')

y = df[['High Price']]

print(x.shape)

print(x,y)

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.1)

model = LinearRegression()

model.fit(xtrain,ytrain)

predict = model.predict(xtest)
print(predict)
print('---',ytest)

print(model.score(xtest,ytest))

#saving the model
with open('asianp_model','wb') as f:
    pickle.dump(model,f)


#0.9945880889466807