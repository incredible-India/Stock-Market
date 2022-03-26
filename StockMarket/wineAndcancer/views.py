from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
from sklearn import linear_model,datasets
from sklearn.model_selection import train_test_split
import pickle
import os
# Create your views here.


# function for prediction of breast cancer
def predictionForCancer(data):
    # extracting datasets
   attr = list(data.values())

   #default type of attr is string so convert into int or FLOat

   newAttrs = list(map(float, attr))
   

   with open('./wineAndcancer/model/model_pickle','rb') as f:
       model = pickle.load(f)

       prediction = model.predict([newAttrs])

       return [prediction,0.9777559355496426] #second one is accuracy of our saved model

   
    
    # print(model.score(xtest,ytest))




class cancerPrediction(View):
    def get(self,request):
    
        return render(request,'wineAndcancer/index.html')


    def post(self,request):
        #storing data from the client side
        mean_radius = request.POST.get("mean_radius")
        mean_texture = request.POST.get("mean_texture")
        mean_perimeter = request.POST.get("mean_perimeter")
        mean_area = request.POST.get("mean_area")
        mean_smoothness = request.POST.get("mean_smoothness")
        mean_compactness = request.POST.get("mean_compactness")
        mean_concavity = request.POST.get("mean_concavity")
        mean_concave_points = request.POST.get("mean_concave_points")
        mean_symmetry = request.POST.get("mean_symmetry")
        mean_fractal_dimension = request.POST.get("mean_fractal_dimension")
        radius_error = request.POST.get("radius_error")
        texture_error = request.POST.get("texture_error")
        perimeter_error = request.POST.get("perimeter_error")
        area_error = request.POST.get("area_error")
        smoothness_error = request.POST.get("smoothness_error")
        compactness_error = request.POST.get("compactness_error")
        concavity_error = request.POST.get("concavity_error")
        concave_points_error = request.POST.get("concave_points_error")
        symmetry_error = request.POST.get("symmetry_error")
        fractal_dimension_error = request.POST.get("fractal_dimension_error")
        worst_radius = request.POST.get("worst_radius")
        worst_texture = request.POST.get("worst_texture")
        worst_perimeter = request.POST.get("worst_perimeter")
        worst_area = request.POST.get("worst_area")
        worst_smoothness = request.POST.get("worst_smoothness")
        worst_compactness = request.POST.get("worst_compactness")
        worst_concavity = request.POST.get("worst_concavity")
        worst_concave_points = request.POST.get("worst_concave_points")
        worst_symmetry = request.POST.get("worst_symmetry")
        worst_fractal_dimension = request.POST.get("worst_fractal_dimension")
        
        userData = {"mean_radius" : mean_radius,
                    "mean_texture" : mean_texture,
                    "mean_perimeter" : mean_perimeter,
                    "mean_area" : mean_area,
                    "mean_smoothness" : mean_smoothness,
                    "mean_compactness" : mean_compactness,
                    "mean_concavity" : mean_concavity,
                    "mean_concave_points" : mean_concave_points,
                    "mean_symmetry" : mean_symmetry,
                    "mean_fractal_dimension" : mean_fractal_dimension,
                    "radius_error" : radius_error,
                    "texture_error" : texture_error,
                    "perimeter_error" : perimeter_error,
                    "area_error" : area_error,
                    "smoothness_error" : smoothness_error,
                    "compactness_error" : compactness_error,
                    "concavity_error" : concavity_error,
                    "concave_points_error" : concave_points_error,
                    "symmetry_error" : symmetry_error,
                    "fractal_dimension_error" : fractal_dimension_error,
                    "worst_radius" : worst_radius,
                    "worst_texture" : worst_texture,
                    "worst_perimeter" : worst_perimeter,
                    "worst_area" : worst_area,
                    "worst_smoothness" : worst_smoothness,
                    "worst_compactness" : worst_compactness,
                    "worst_concavity" : worst_concavity,
                    "worst_concave_points" : worst_concave_points,
                    "worst_symmetry" : worst_symmetry,
                    "worst_fractal_dimension" : worst_fractal_dimension


                     }
        isCancer = predictionForCancer(userData)

        #accuracy in %
        accuracy = isCancer[1]*100
     

        accuracy = round(accuracy)

        status = isCancer[0]

     

        if status > 0.5 and status < 1:
            status = 'In Between malignant and benign'
        elif status >= 1:
            status = 'Malignant'
        else : 
            status = 'Benign'
        
        return render(request,'wineAndcancer/result.html',{
        'userData' : userData,'data':
        {
            'accuracy' : isCancer[1]*100,
            'roundOffAcc' :accuracy,
            'status' : status,
            'machineData' : isCancer[0]

        }})



#routing for the test of wine 

#Wine data testing function 

def testWineQuality(data):
    # extracting datasets
   attr = list(data.values())

   #default type of attr is string so convert into int or FLOat

   newAttrs = list(map(float, attr))

   with open('./wineAndcancer/model/wine_pickle','rb') as f:
       model = pickle.load(f)

       prediction = model.predict([newAttrs])

       return [prediction,0.9938476689573258] #second one is accuracy of our saved model




#routing for wineTest page 
class Wine(View):
    def get(self, request):
        return render(request,'wineAndcancer/wine.html')

    
    def post(self, request):
        alcohol = request.POST.get("alcohol")
        malic_acid = request.POST.get("malic_acid")
        ash = request.POST.get("ash")
        alcalinity_of_ash = request.POST.get("alcalinity_of_ash")
        magnesium = request.POST.get("magnesium")
        total_phenols = request.POST.get("total_phenols")
        flavanoids = request.POST.get("flavanoids")
        nonflavanoid_phenols = request.POST.get("nonflavanoid_phenols")
        proanthocyanins = request.POST.get("proanthocyanins")
        color_intensity = request.POST.get("color_intensity")
        hue = request.POST.get("hue")
        od280_od315_of_diluted_wines = request.POST.get("od280/od315_of_diluted_wines")
        proline = request.POST.get("proline")

        userdata ={'alcohol': alcohol, 'malic_acid': malic_acid, 'ash': ash, 'alcalinity_of_ash': alcalinity_of_ash, 'magnesium': magnesium, 'total_phenols': total_phenols, 'flavanoids': flavanoids, 'nonflavanoid_phenols': nonflavanoid_phenols, 'proanthocyanins': proanthocyanins, 'color_intensity': color_intensity, 'hue': hue, 'od280/od315_of_diluted_wines': od280_od315_of_diluted_wines, 'proline': proline}

        ModelPrediction = testWineQuality(userdata)

        accuracy = round(ModelPrediction[1]*100)
    
        Quality = round(ModelPrediction[0].tolist()[0])
        
        return render(request, 'wineAndcancer/wineResult.html',{'data':
        {
            'accuracy': accuracy,
            'quality': Quality,
            'exactAccuracy' : ModelPrediction[1]*100,
            'exactPrediction' : ModelPrediction[0]
            ,'userdata':userdata

        }})


