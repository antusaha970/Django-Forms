from django.urls import path
from . import views
urlpatterns = [
    path('', views.formApi, name="formApi"),
    path('model-form/', views.modelForm, name="modelForm"),
]
