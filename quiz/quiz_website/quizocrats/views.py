from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
  if request.method=='POST':
    name=request.POST.get('username')
    pas=request.POST.get('password')
    user=authenticate(username=name, password=pas)
    if user is not None:
      return HttpResponse('done')
  return render(request, 'home.html')
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
def quizanswers(request):
  template = loader.get_template('quizanswers.html')
  return HttpResponse(template.render())