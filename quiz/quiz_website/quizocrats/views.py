from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())
def aboutus(request):
  template = loader.get_template('aboutus.html')
  return HttpResponse(template.render())
def help(request):
  template = loader.get_template('help.html')
  return HttpResponse(template.render())
def samquiz(request):
  template = loader.get_template('quizpage.html')
  return HttpResponse(template.render())
