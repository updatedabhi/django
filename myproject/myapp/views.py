from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def message(request):
  return HttpResponse("""<h1>Hello message 1. This is this 
                      is django project</h1>""")

def message2(request):
  name = "Abhishek"
  return HttpResponse(f"<h1>Welcome {name}</h1>")


def greet(request, name):
  return HttpResponse(f"Welcome, {name}")

def add(request, n1, n2):
    try:
      result = int(n1) + int(n2)
      return HttpResponse(f"Addition: {n1 + n2}")
    except:
      return HttpResponse("Invalid input")
    
def add1(request):
  n1 = int(request.GET.get('n1'))
  n2 = int(request.GET.get('n2'))
  return HttpResponse(f"The result is {n1 + n2}")


def user(request, username):
  return HttpResponse(f"The Username is: {username}")

def user1(request, username):
  return HttpResponse(f"The Username is: {username}")

def user2(request, username):
  return HttpResponse(f"The Username is: {username}")

def user3(request, username):
  return HttpResponse(f"The Username is: {username}")

def user4(request, username):
  return HttpResponse(f"The Username is: {username}")

def user5(request, username):
  return HttpResponse(f"The Username is: {username}")

def user6(request, username):
  return HttpResponse(f"The Username is: {username}")

def user7(request, month, year):
  return HttpResponse(f"Username date is {month} and year is {year}")

def user8(request, username):
  return HttpResponse(f"The Username is: {username}")

def student(request, studentId, studentName):
  return HttpResponse(f"student id is {studentId} and name is {studentName}")

def employee(request, empname, empsalary):
  return HttpResponse(f"Employee name is {empname} and salary is {empsalary}")

def blog_details(request, post_slug=None):
  return HttpResponse(f"slug: {post_slug}")

def check(request):
  try:
    value = int(request.GET.get('value'))
    return HttpResponse(f"You entered: {value}")
  except:
    return HttpResponse(f"<h1 style=color:red>Please enter value</h1>", status=404)
  
  
def food_details(request, foodname, foodprice):
  if foodname and not foodprice:
    return HttpResponse("Food price is missing", status=404)
  elif not foodname and foodprice:
    return HttpResponse("Food name is missing", status=404)
  elif not foodname and not foodprice:
    return HttpResponse("Both foodname and foodprice are missing", status=404)
  elif foodname and foodprice:
    return HttpResponse(f"The food name is {foodname} and the food price is {foodprice}", status=200)
  

def test(request):
  return render(request, 'test.html')

def test1(request):
  details = {'name': 'Abhishek', 'gender': 'Male'}
  return render(request, 'details.html', details)

def test2(request):
  details = {'completDeatils':[
    {'Name': 'Abhishek', 'age': 34, 'marks': 82},
    {'Name': 'Rahul', 'age': 29, 'marks': 76},
    {'Name': 'Sneha', 'age': 22, 'marks': 88},
    {'Name': 'Priya', 'age': 25, 'marks': 90},
    {'Name': 'Vikram', 'age': 30, 'marks': 85}
  ]}
  return render(request, 'details.html', details)

def yummy_list(request):
  yummy_items = [
    {'foodname': 'Tea', 'price': 10, 'size': 'small'},
    {'foodname': 'coffee', 'price': 20, 'size': 'medium'},
    {'foodname': 'Juice', 'price': 40, 'size': 'large'},
    {'foodname': 'Aaloo', 'price': 50, 'size': 'medium'},
    {'foodname': 'Protien shake', 'price': 80, 'size': 'large'},
  ]
  return render(request, 'yummy_list.html', {'yummy_items': yummy_items})
    
    
  
def yummy_details(request, single_yummy_item):
  yummy_items = [
    {'foodname': 'Tea', 'price': 10, 'size': 'small'},
    {'foodname': 'coffee', 'price': 20, 'size': 'medium'},
    {'foodname': 'Juice', 'price': 40, 'size': 'large'},
    {'foodname': 'Aaloo', 'price': 50, 'size': 'medium'},
    {'foodname': 'Protien shake', 'price': 80, 'size': 'large'},
  ]
  return render(request, 'yummy_details.html', {'yummy_items': yummy_items, 'single_yummy_item' : single_yummy_item})

def test_css(request):
  return render(request, 'testcss.html')