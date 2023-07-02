from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
def home(request):
  if request.method=='POST':
    name=request.POST.get('username')
    pas=request.POST.get('password')
    user=authenticate(username=name, password=pas)
    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      messages.warning(request, 'Wrong Username or password')
      return render(request, 'home.html')

  else: 
    if request.user.is_authenticated:
      return render(request,'home2.html') 
    return render(request, 'home.html')

def contact(request):
  if request.method=='POST':
    name=request.POST.get('username')
    pas=request.POST.get('password')
    user=authenticate(username=name, password=pas)
    if user is not None:
      login(request,user)
      return render(request,'home2.html')
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
      login(request,user)
      return render(request,'home2.html')
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
      login(request,user)
      return render(request,'home2.html')
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

def loggingout(request):
  logout(request)
  return redirect(home)