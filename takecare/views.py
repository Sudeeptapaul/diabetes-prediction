from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
import pickle
import sklearn
model_path= os.path.join(settings.BASE_DIR,"takecare","model.pkl")
with open(model_path,"rb") as file:
    model=pickle.load(file)
# Create your views here.
# def index(request):
#     return render(request, 'index.html')
def home(request):
    # return render(request,"index.html")
    pred=None
    if request.method=="POST":
        gender=int(request.POST['gender'])
        age=float(request.POST['age'])
        hypertension=float(request.POST['hypertension'])
        heart_disease=float(request.POST['heart_disease'])
        smoking_history=float(request.POST['smoking_history'])
        bmi=float(request.POST['bmi'])
        HbA1c_level=float(request.POST['HbA1c_level'])
        blood_glucose_level=float(request.POST['blood_glucose_level'])
        pred= model.predict([[gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level]])
    context={
        "prediction": pred
    }
    return render(request,"home.html",context)


