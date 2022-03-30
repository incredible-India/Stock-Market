from django.shortcuts import render
from django.shortcuts import HttpResponse
import pandas as pd 
from django.views import View
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pickle
# Create your views here.

# home page for the stock Market Page 
def index(request):
    return render(request, 'stockPrice/index.html')



#function for prediction data 

def marketPrediction(data):
     # extracting datasets we are getting the from data`s values in list`
   attr = list(data.values())#user form data bydefault it is in String and type list

 

   #default type of attr is string so convert into int or FLOat

   newAttrs = list(map(float, attr))
   

   with open('./stockPrice/model/market_model','rb') as f:

       model = pickle.load(f) #our saved model go to ./stockPrice/model/market_model this directory to see code market.py

       prediction = model.predict([newAttrs]) #Giveing the data to predict the values

        #prediction has a value ,but it is in list
       return [prediction,'98.60'] #second item is the accuracy of our model




       ######################################################################

class market(View):
    def get(self, request):
        return render(request, 'stockPrice/market.html')
    
    def post(self, request):

        #getting data from the form...
        open_price = request.POST.get('open')
        low_price = request.POST.get('low')
        close_price = request.POST.get('close')
        shares = request.POST.get('shares')
        
        Userdata ={
            'open' : open_price,
            'close' : close_price,
            'low' : low_price,
            'shares': shares
        }

        high_price = marketPrediction(Userdata) #return value and accuracy list type

        result = high_price[0] #value high price but it is in array of one item

        accuracy = high_price[1] #accuracy of model

        return render(request, 'stockPrice/market.html',{
            'result':True,  'data':result[0],'accuracy':accuracy , 'userdata' : Userdata
        })


