from django.shortcuts import render
from django.views import View

from sklearn import linear_model,datasets
from sklearn.model_selection import train_test_split
# Create your views here.


# function for prediction of breast cancer
def predictionForCancer(data):
    # extracting datasets
    Cdata = datasets.load_breast_cancer()
    # Cdata contains all the attributes information
    #dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
    #spliting the test Training datasets for training in model
    xtrain,xtest,ytrain,ytest = train_test_split(Cdata.data,Cdata.target,test_size=0.01)

    model = linear_model.LinearRegression()
    #training our train datasets
    model.fit(xtrain,ytrain)

    #checking out model 
    finalData = model.predict(xtest)

    print(model.predict([[1,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,1,2]]))
  
    #aur model accuracy
    accuracy = model.score(xtest,ytest)

    print(accuracy)

   
    
    # print(model.score(xtest,ytest))




class cancerPrediction(View):
    def get(self,request):
        return render(request,'wineAndcancer/index.html')


predictionForCancer(1)