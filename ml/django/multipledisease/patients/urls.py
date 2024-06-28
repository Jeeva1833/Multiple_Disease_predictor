from django.urls import path
from .import views

urlpatterns=[
    path('register',views.register,name='reg'),
    path('index',views.index,name='phome'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('multiple_disease',views.multipledisease,name='disease'),
    path('disease_pred',views.dispredict,name='dispred')




]