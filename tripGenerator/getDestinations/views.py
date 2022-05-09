from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.views import generic
from django.contrib.auth import get_user_model

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

User = get_user_model()

def getThreePlaces():
    driver = webdriver.Chrome('/Users/jparke2/Desktop/tripGenerator/tripGenerator/chromedriver')
    driver.get('https://www.momondo.com')
    driver.close()

# Create your views here.
def index(request):
    getThreePlaces()
    destinations = ['Bali','Banff','Florida']
    context = {'recent': destinations}
    return render(request, 'getDestinations/index.html', context)