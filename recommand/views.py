from operator import itemgetter
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

# contains algorithms and functions

def index(request):
  mov = Movie.objects.all()
  return render(request, 'index.html',{'mov':mov})

def home(request):
  mov = Movie.objects.all()
  return render(request, 'index.html',{'mov':mov})

def signup(request):
  return render(request, 'signup.html')

def register(request):
  if request.method == 'POST':
    First_name = request.POST['First_name']
    Last_name = request.POST['Last_name']
    User_name = request.POST['User_name']
    Email = request.POST['Email']
    Password = request.POST['Password']

    if User.objects.filter(username=User_name).exists():
      messages.info(request,'Username taken')
      return render(request, 'signup.html')
    elif User.objects.filter(email=Email).exists():
      messages.info(request,"Email taken")
      return render(request, 'signup.html')
    else:
      user = User.objects.create_user(first_name=First_name,last_name=Last_name,username=User_name,email=Email, password=Password)
      user.save()

    mov = Movie.objects.all()
    return render(request, 'index.html',{'mov':mov})

def signin(request):
  return render(request, 'signin.html')

def login(request):
  if request.method == 'POST':
    User_name = request.POST['User_name']
    Password = request.POST['Password']
    user = auth.authenticate(username=User_name,password=Password)
    mov = Movie.objects.all()
    if user is not None:
      auth.login(request, user)
      return render(request, 'index.html',{'mov':mov,'user':user})
    else: 
      messages.info(request,'Invalid Credentials')
      return render(request, 'signin.html')
   
def logout(request):
  auth.logout(request)
  return redirect("/")

class obj:
  def __init__(self, movie, count):
    self.movie = movie
    self.count = count

def returnobj(name):
  selected_movie = Movie.objects.filter(title__icontains=name)
  mov = Movie.objects.all()
  list_obj = []
  for i in selected_movie:
    gen1 = i.genre1
    gen2 = i.genre2
    gen3 = i.genre3

  o = obj(mov,3)
  list_obj.append(o)

  for m in mov:
      count = 0
      if m.genre1 == gen1 or m.genre1 == gen2 or m.genre1 == gen3:
        count+1
        if m.genre2 == gen1 or m.genre2 == gen2 or m.genre2 == gen3:
          count+1
          if m.genre3 == gen1 or m.genre3 == gen2 or m.genre3 == gen3:
            count+1
            o = obj(mov,count)
            list_obj.append(o)
          o = obj(mov,count)
          list_obj.append(o)
        o = obj(mov,count)
        list_obj.append(o)
      continue
  return list_obj
    
def quick_sort(s,key = 1):
  if len(s) == 1 or len(s) == 0:
    return s
  else:
    pivot = s[0][1]
    i = 0
    for j in range(len(s)-1):
      if s[j+1][1] < pivot:
        s[j+1][0],s[i+1][0] = s[i+1][0],s[j+1][0]
        s[j+1][1],s[i+1][1] = s[i+1][1],s[j+1][1]
        i += 1
    s[0][0],s[i][0] = s[i][0],s[0][0]
    s[0][1],s[i][1] = s[i][1],s[0][1]
    left_half = quick_sort(s[:i])
    right_half = quick_sort(s[i+1:])
    left_half.append(s[i])
    return left_half + right_half

def returnmovies(list_obj):
  list_mov = []
  for obj in list_obj:
    list_mov.append(obj.movie)
  return list_mov

def comp(list_obj):
  return list_obj.count

def searchbar(request):
  query = None
  if request.method == 'GET':
    query = request.GET.get('search')
    selected_movie = Movie.objects.filter(title__icontains=query)
    mov = Movie.objects.all()
    list_obj = returnobj(query)  
    list_obj.sort(key=comp, reverse=True)
    list_mov = returnmovies(list_obj)
    return render(request, 'searchbar.html', {'movies':mov, 'select':selected_movie, 'query': query, 'list_mov': list_mov})
