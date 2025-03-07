from django.shortcuts import render, redirect
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

def tasty_list(request):
  tasty_items = [
    {'foodname': 'Tea', 'price': 10, 'size': 'small', 'image': 'img/tea.png'},
    {'foodname': 'coffee', 'price': 20, 'size': 'medium', 'image': 'img/coffee-cup.png'},
    {'foodname': 'Juice', 'price': 40, 'size': 'large', 'image': 'img/juice.png'},
    {'foodname': 'Aaloo', 'price': 50, 'size': 'medium',  'image': 'img/potato.png'},
    {'foodname': 'Protien shake', 'price': 80, 'size': 'large',  'image': 'img/drink.png'},
  ]
  return render(request, 'tasty_list.html', {'tasty_items': tasty_items})


from django.middleware.csrf import get_token
def form(request):
  csrf_token = get_token(request)
  if request.method == "GET":
    html_form = f"""
    <form method="POST">
      <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
      <input type="text" name="textbox1">
      <input type="text" name="textbox2">
      <input type="submit" value="submit">
    </form>
    """
    return HttpResponse(html_form)
  elif request.method == "POST":
    textbox1 = request.POST.get('textbox1')
    textbox2 = request.POST.get('textbox2')
    return HttpResponse(f"The values are {textbox1} and {textbox2}")
  
from django.http import HttpResponse
from django.middleware.csrf import get_token

def taskForm(request):
    csrf_token = get_token(request)

    if request.method == "GET":
        html_form = f"""
        <form method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
            <input type="text" name="n1">
            <input type="text" name="n2">
            <input type="submit" value="add">
        </form>
        """
        return HttpResponse(html_form)

    elif request.method == "POST":
        n1 = request.POST.get('n1', '').strip()
        n2 = request.POST.get('n2', '').strip()

        try:
            n1 = int(n1)
            n2 = int(n2)
        except ValueError:
            return HttpResponse("Please enter valid integers")

        sum_result = n1 + n2
        return HttpResponse(f"The sum is {sum_result}")
      
def form1(request):
  csrf_token = get_token(request)
  if request.method == "GET":
    html_form = f"""
    <form method="POST">
      <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
      <input type="text" name="textbox1">
      <input type="text" name="textbox2">
      <input type="submit" value="submit">
    </form>
    """
    return HttpResponse(html_form)
  elif request.method == "POST":
    textbox1 = request.POST.get('textbox1')
    textbox2 = request.POST.get('textbox2')
    return redirect("success")

def success(request):
  return render(request, "success.html")

def htmlform(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    # return HttpResponse(f"The Values are {name}, {email} and {password}")
    if name and email and password:
      return render(request, "htmlform.html", {'name': name, 'email': email, 'password': password})
    else:
      return render(request, "htmlform.html")
  elif request.method == "GET":
    return render(request, "htmlform.html")
  
def validate(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    name_err = ""
    email_err = ""
    password_err = ""
    if not name:
      name_err = "name is required"
    if not email:
      email_err = "email is required"
    if not password:
      password_err = "password is required"
    if name_err or email_err or password_err:
      return render(request, 'validate.html', {'name_err': name_err, 'email_err': email_err, 'password_err': password_err})
    else:
      return render(request,'validate.html', {'name': name, 'email': email, 'password': password})
  elif request.method == "GET":
    return render(request, "validate.html")
  
  
def routes_details(request):
  routes = [
    {"name": "home"},
    {"name": "about"},
    {"name": "contact"}
  ]
  
  return render(request, "routes.html", {"routes": routes})

def home(request):
  return render(request, "home.html")

def about(request):
  return render(request, "about.html")

def contact(request):
  return render(request, "contact.html")