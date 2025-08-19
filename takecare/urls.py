from django.urls import path
from takecare.views import home
# from django.contrib import admin
# from django.urls import path,include
# from takecare.views import home
urlpatterns =[
    path('',home,name="home")
]