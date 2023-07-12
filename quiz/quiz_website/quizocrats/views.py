from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import quizzes
# Create your views here.
def home(request):
  if request.method=='POST':
    if 'pass1' in request.POST:
      name=request.POST.get('username')
      pas1=request.POST.get('pass1')
      pas2=request.POST.get('pass2')
      email=request.POST.get('emailid')
      if len(name)>20:
        messages.warning(request, 'use shorter name')
        return render(request, 'home.html')
      
      if pas1!=pas2:
        messages.warning(request, 'password not same')
        return render(request, 'home.html')
      
      user=User.objects.create(username=name,email=email,password=make_password(pas1))
      user.save()
      user=authenticate(username=name, password=pas1)
      login(request,user)
      return redirect('home')
    else:
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
    if 'pass1' in request.POST:
      name=request.POST.get('username')
      pas1=request.POST.get('pass1')
      pas2=request.POST.get('pass2')
      email=request.POST.get('emailid')
      if len(name)>20:
        messages.warning(request, 'use shorter name')
        return render(request, 'home.html')
      
      if pas1!=pas2:
        messages.warning(request, 'password not same')
        return render(request, 'home.html')
      
      user=User.objects.create(username=name,email=email,password=make_password(pas1))
      user.save()
      user=authenticate(username=name, password=pas1)
      login(request,user)
      return redirect('home')
    else:
      name=request.POST.get('username')
      pas=request.POST.get('password')
      user=authenticate(username=name, password=pas)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.warning(request, 'Wrong Username or password')
        return render(request, 'contact.html')

  else:  
    return render(request, 'contact.html')

def aboutus(request):
  if request.method=='POST':
    if 'pass1' in request.POST:
      name=request.POST.get('username')
      pas1=request.POST.get('pass1')
      pas2=request.POST.get('pass2')
      email=request.POST.get('emailid')
      if len(name)>20:
        messages.warning(request, 'use shorter name')
        return render(request, 'home.html')
      
      if pas1!=pas2:
        messages.warning(request, 'password not same')
        return render(request, 'home.html')
      
      user=User.objects.create(username=name,email=email,password=make_password(pas1))
      user.save()
      user=authenticate(username=name, password=pas1)
      login(request,user)
      return redirect('home')
    else:
      name=request.POST.get('username')
      pas=request.POST.get('password')
      user=authenticate(username=name, password=pas)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.warning(request, 'Wrong Username or password')
        return render(request, 'aboutus.html')

  else:  
    return render(request, 'aboutus.html')

def help(request):
  if request.method=='POST':
    if 'pass1' in request.POST:
      name=request.POST.get('username')
      pas1=request.POST.get('pass1')
      pas2=request.POST.get('pass2')
      email=request.POST.get('emailid')
      if len(name)>20:
        messages.warning(request, 'use shorter name')
        return render(request, 'home.html')
      
      if pas1!=pas2:
        messages.warning(request, 'password not same')
        return render(request, 'home.html')
      
      user=User.objects.create(username=name,email=email,password=make_password(pas1))
      user.save()
      user=authenticate(username=name, password=pas1)
      login(request,user)
      return redirect('home')
    else:
      name=request.POST.get('username')
      pas=request.POST.get('password')
      user=authenticate(username=name, password=pas)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.warning(request, 'Wrong Username or password')
        return render(request, 'help.html')

  else:  
    return render(request, 'help.html')

def samquiz(request):
  template = loader.get_template('quizpage.html')
  return HttpResponse(template.render())
def cppquiz(request):
  template = loader.get_template('cppquiz.html')
  return HttpResponse(template.render())
def pythonquiz(request):
  template = loader.get_template('pythonquiz.html')
  return HttpResponse(template.render())
def adminquiz(request):
  admquiz=quizzes.objects.all()
  context={
    'admque':admquiz
  }
  return render(request,'adminquiz.html',context)
def quizanswers(request):
  template = loader.get_template('quizanswers.html')
  return HttpResponse(template.render())

def loggingout(request):
  logout(request)
  return redirect(home)

def quiz(request):
  active_quizzes=quizzes.objects.all()
  context={
    'actqui':active_quizzes
  }
  return render(request,'quizzesactive.html',context)

def create(request):
  if request.method=='POST':
    name=request.POST.get('quizname')
    topics=request.POST.get('topics')
    user=request.user.username
    questions=request.POST.get('que')
    time=request.POST.get('time')
    ques1=request.POST.get('Q1')
    ans1=request.POST.get('A1')
    op1_1=request.POST.get('Op1.1')
    op1_2=request.POST.get('Op1.2')
    op1_3=request.POST.get('Op1.3')
    op1_4=request.POST.get('Op1.4')
    ques2=request.POST.get('Q2')
    ans2=request.POST.get('A2')
    op2_1=request.POST.get('Op2.1')
    op2_2=request.POST.get('Op2.2')
    op2_3=request.POST.get('Op2.3')
    op2_4=request.POST.get('Op2.4')
    ques3=request.POST.get('Q3')
    ans3=request.POST.get('A3')
    op3_2=request.POST.get('Op3.1')
    op3_1=request.POST.get('Op3.2')
    op3_3=request.POST.get('Op3.3')
    op3_4=request.POST.get('Op3.4')
    ques4=request.POST.get('Q4')
    ans4=request.POST.get('A4')
    op4_1=request.POST.get('Op4.1')
    op4_2=request.POST.get('Op4.2')
    op4_3=request.POST.get('Op4.3')
    op4_4=request.POST.get('Op4.4')
    ques5=request.POST.get('Q5')
    ans5=request.POST.get('A5')
    op5_1=request.POST.get('Op5.1')
    op5_2=request.POST.get('Op5.2')
    op5_3=request.POST.get('Op5.3')
    op5_4=request.POST.get('Op5.4')
    quiz=quizzes(quiz_name=name,username=user,topics=topics,questions=questions,time=time,ques1=ques1,ques2=ques2,ques3=ques3,ques4=ques4,ques5=ques5,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4,ans5=ans5,op1_1=op1_1,op1_2=op1_2,op1_3=op1_3,op1_4=op1_4,op2_1=op2_1,op2_2=op2_2,op2_3=op2_3,op2_4=op2_4,op3_1=op3_1,op3_2=op3_2,op3_3=op3_3,op3_4=op3_4,op4_1=op4_1,op4_2=op4_2,op4_3=op4_3,op4_4=op4_4,op5_1=op5_1,op5_2=op5_2,op5_3=op5_3,op5_4=op5_4,)
    quiz.save()
    return redirect(home)
  return render(request,'createquiz.html')