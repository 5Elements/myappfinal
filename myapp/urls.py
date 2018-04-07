from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'analyze', views.analyzeData, name="Analyzer"),
    url(r'saved', views.savedData, name="Saved")
]
