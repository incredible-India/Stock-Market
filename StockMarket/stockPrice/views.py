from django.shortcuts import render
from django.shortcuts import HttpResponse
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import linear_model
# Create your views here.

# home page for the stock Market Page 
def index(request):
    return render(request, 'stockPrice/index.html')
