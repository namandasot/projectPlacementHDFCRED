'''
Created on 28-Jul-2016

@author: prateek
'''

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
# from models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from projectPlacement import projectPlacement


p = projectPlacement()

@api_view(['GET'])
def getProjectPlacement(request):
    
    a =  Response(p.getProjectScore())
    return a