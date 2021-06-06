from django.urls import path
from .views import index,herobanner,aboutme,facts,skilled,skilldes,resumedet
from django.conf.urls import url

urlpatterns = [
    path('',index,name="index" ),
    path('herobanner',herobanner,name='herobanner'),
    path('aboutme',aboutme,name='aboutme'),
    path('facts',facts,name='facts'),
    path('skilled',skilled,name='skilled'),
    path('skilldes',skilldes,name='skilldes'),
    path('resumedet',resumedet,name='resumedet'),

]