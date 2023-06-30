from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def home(request):
  if request.method=='POST':
    name=request.POST.get('username')
    pas=request.POST.get('password')
    user=authenticate(username=name, password=pas)
    if user is not None:
      
      return render(request,'home2.html')
    else:
      messages.warning(request, 'Wrong Username or password')
      return render(request, 'home.html')

  else:  
    return render(request, 'home.html')

def contact(request):
  if request.method=='POST':
    name=request.POST.get('username')
    pas=request.POST.get('password')
    user=authenticate(username=name, password=pas)
    if user is not None:
      return HttpResponse('done')
    else:
      messages.warning(request, 'Wrong Username or password')
      return render(request, 'contact.html')

  else:  
    return render(request, 'contact.html')

def aboutus(request):
  if request.method=='POST':
    name=request.POST.get('username')
    pas=request.POST.get('password')
    user=authenticate(username=name, password=pas)
    if user is not None:
      return HttpResponse('done')
    else:
      messages.warning(request, 'Wrong Username or password')
      return render(request, 'aboutus.html')

  else:  
    return render(request, 'aboutus.html')

def help(request):
  if request.method=='POST':
    name=request.POST.get('username')
    pas=request.POST.get('password')
    user=authenticate(username=name, password=pas)
    if user is not None:
      return HttpResponse('done')
    else:
      messages.warning(request, 'Wrong Username or password')
      return render(request, 'help.html')

  else:  
    return render(request, 'help.html')

def samquiz(request):
  template = loader.get_template('quizpage.html')
  return HttpResponse(template.render())

def quizanswers(request):
  template = loader.get_template('quizanswers.html')
  return HttpResponse(template.render())