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

def marketPrediction(data,companyName):
     # extracting datasets we are getting the from data`s values in list`
    attr = list(data.values())#user form data bydefault it is in String and type list

   
    #default type of attr is string so convert into int or FLOat

    newAttrs = list(map(float, attr))

    print(newAttrs)
    
    if int(companyName) == 500111 :  
        #Reliance Group
        with open('./stockPrice/model/market_model','rb') as f:

            model = pickle.load(f) #our saved model go to ./stockPrice/model/market_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
           
        #prediction has a value ,but it is in list
        
            return [prediction,'98.60',companyName,'RELIANCE CAPITAL LTD. 500111'] #second item is the accuracy of our model third one is comapny code



    elif int(companyName) == 512599: 
        #Adani group
        with open('./stockPrice/model/adani_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/adani_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
           
        #prediction has a value ,but it is in list
            return [prediction,'99.89',companyName,'ADANI ENTERPRISES LTD. 512599'] #second item is the accuracy of our model third one is comapny code


    
    elif int(companyName) == 500180: 
        #HDFC group
        with open('./stockPrice/model/hdfc_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/HDFC_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
           
        #prediction has a value ,but it is in list
            return [prediction,'99.93',companyName,'HDFC Bank Ltd 500180'] #second item is the accuracy of our model third one is comapny code
    
    elif int(companyName) == 542830: 
        #IRCTC Railway
        with open('./stockPrice/model/irctc_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/irctc_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
          
        #prediction has a value ,but it is in list
            return [prediction,'98.97',companyName,'Indian Railway Catering and Tourism Corporation Ltd 542830'] #second item is the accuracy of our model third one is comapny code

    

    elif int(companyName) == 500820: 
        #Asian paints Railway
        with open('./stockPrice/model/asianp_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/asianp_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
            
        #prediction has a value ,but it is in list
            return [prediction,'99.45',companyName,'ASIAN PAINTS LTD. 500820'] #second item is the accuracy of our model third one is comapny code

    
    elif int(companyName) == 532371: 
        #TATA TELESERVICE paints Railway
        with open('./stockPrice/model/ttm_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/asianp_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
            
        #prediction has a value ,but it is in list
            return [prediction,'98.45',companyName,'TATA TELESERVICES (MAHARASHTRA) LTD. 532371'] #second item is the accuracy of our model third one is comapny code

    
    elif int(companyName) == 540376: 
        #Dmart Avanue Super MArt
        with open('./stockPrice/model/dmart_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/asianp_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
          
        #prediction has a value ,but it is in list
            return [prediction,'99.05',companyName,'Avenue Supermarts Ltd 540376'] #second item is the accuracy of our model third one is comapny code
    

    elif int(companyName) == 500112: 
        #SBI
        with open('./stockPrice/model/sbi_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/asianp_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
          
        #prediction has a value ,but it is in list
            return [prediction,'95.13',companyName,'STATE BANK OF INDIA 500112'] #second item is the accuracy of our model third one is comapny code

    
    elif int(companyName) == 532343: 
        #TVS MOTORS
        with open('./stockPrice/model/tvs_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/asianp_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
         
        #prediction has a value ,but it is in list
            return [prediction,'99.04',companyName,'TVS MOTOR COMPANY LTD. 532343'] #second item is the accuracy of our model third one is comapny code

    
    elif int(companyName) == 543320: 
        #Zomato
        with open('./stockPrice/model/zomato_model','rb') as f:
            model = pickle.load(f) #our saved model go to ./stockPrice/model/asianp_model this directory to see code market.py

            prediction = model.predict([newAttrs]) #Giveing the data to predict the values
            
         
        #prediction has a value ,but it is in list
            return [prediction,'99.19',companyName,'Zomato Ltd 543320'] #second item is the accuracy of our model  third one is comapny code



    else:
        return ['Internal Server Error',00,500111,'Unknown']

  


       ######################################################################

class market(View):
    def get(self, request):
        return render(request, 'stockPrice/market.html')
    
    def post(self, request):

        #getting data from the form...
        CompName = request.POST.get('comp')
        open_price = request.POST.get('open')
        low_price = request.POST.get('low')
        close_price = request.POST.get('close')
        shares = request.POST.get('shares')

      
        Userdata ={
            'open' : open_price,
            'low' : low_price,
            'close' : close_price,
            'shares': shares
        }

        high_price = marketPrediction(Userdata,CompName) #return value and accuracy list type company code and company name

        
        result = high_price[0] #value high price but it is in array of one item

        accuracy = high_price[1] #accuracy of model

        companyCode = high_price[2] #company code

        cc = high_price[3] #company code

        return render(request, 'stockPrice/market.html',{
            'result':True,  'data':result[0],'accuracy':accuracy , 'userdata' : Userdata, 'companyCode':companyCode
            ,'cc' : cc
        })


