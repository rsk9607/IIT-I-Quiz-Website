from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from datetime import datetime
from .models import quizzes,questionare,result
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

def htmlquiz(request):
  template = loader.get_template('htmlquiz.html')
  return HttpResponse(template.render())

def javascriptquiz(request):
  template = loader.get_template('javascriptquiz.html')
  return HttpResponse(template.render())

def cssquiz(request):
  template = loader.get_template('cssquiz.html')
  return HttpResponse(template.render())

def aiquiz(request):
  template = loader.get_template('aiquiz.html')
  return HttpResponse(template.render())

def mlquiz(request):
  template = loader.get_template('mlquiz.html')
  return HttpResponse(template.render())

def djangoquiz(request):
  template = loader.get_template('djangoquiz.html')
  return HttpResponse(template.render())

def adminquiz(request,name):
  admquiz=quizzes.objects.filter(quiz_name=name)[0]
  questions=questionare.objects.filter(quiz=admquiz)
  if request.method=='POST':
    score=0
    for i in range(admquiz.questions):
      givenans=request.POST.get('Q'+str(i+1))
      if givenans==questions[i].correct_opt:
        score=1+score
        print('done')
    res=result(quiz=admquiz,user=request.user,score=score,date=datetime.today())
    res.save()
    return redirect(quiz)          
  else:
    context={
      'admque':questions,
      'admquiz':admquiz
    }
    return render(request,'quizpage.html',context)

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

def quizans(request,name):
  admquiz=quizzes.objects.filter(quiz_name=name)[0]
  questions=questionare.objects.filter(quiz=admquiz)
  context={
    'admque':questions,
    'admquiz':admquiz
  }
  return render(request,'quizanswer.html',context)

def create(request):
  if request.method=='POST':
    if 'Q1' in request.POST:
      quizname=request.POST.get('quizname')
      quest=request.POST.get('que')
      admquiz=quizzes.objects.filter(quiz_name=quizname)[0]  
      for i in range(int(quest)):

        ques_question=request.POST.get('Q'+str(i+1))
        ques_correct_opt=request.POST.get('A'+str(i+1))
        ques_opt1=request.POST.get('Op.1'+str(i+1))
        ques_opt2=request.POST.get('Op.2'+str(i+1))
        ques_opt3=request.POST.get('Op.3'+str(i+1))
        ques_opt4=request.POST.get('Op.4'+str(i+1))
        ques=questionare(quiz=admquiz,question=ques_question,correct_opt=ques_correct_opt,opt1=ques_opt1,opt2=ques_opt2,opt3=ques_opt3,opt4=ques_opt4)
        ques.save()     
      return redirect(create)
    name=request.POST.get('quizname')
    topics=request.POST.get('topics')

    question=request.POST.get('que')
    time=request.POST.get('time')

    if quizzes.objects.filter(quiz_name=name).exists():
      messages.warning(request, 'The quiz name already exits. Use another one')
      return redirect(create)
    quiz=quizzes(quiz_name=name,topics=topics,questions=question,time=time)
    quiz.save()
    context={
      
      'quizname':name,
      'num':question,
      'range':range(1,int(question)+1)

    }
    return render(request,'createques.html',context)
  return render(request,'createquiz.html')

def quizexisting(request):
  active_quizzes=quizzes.objects.all()
  context={
    'actqui':active_quizzes
  }
  return render(request,'quizzesexisting.html',context)

def delete(request,name):
  quiz=quizzes.objects.filter(quiz_name=name)[0]
  quiz.delete()
  return redirect(quizexisting)

def progress(request):
  user=request.user
  results=result.objects.filter(user=user)
  context={
    'prog': results
  }
  return render(request,'progress.html',context)