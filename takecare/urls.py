from django.urls import path
from takecare.views import home,index
# from django.contrib import admin
# from django.urls import path,include
# from takecare.views import home
urlpatterns =[
    path('',index,name="index"),
    path('index/',home,name="home")

]
