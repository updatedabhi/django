from django.shortcuts import render, redirect
from django.http import HttpResponse

def items_list(request):
  details = {"details": [
    {"name": "Abhishek", "age": 34, "gender": "male"},
    {"name": "Sonam", "age": 44, "gender": "female"},
    {"name": "Harsh", "age": 89, "gender": "male"},
  ]}
  return render(request, "ca.html", details)

def item_details(request, persondetail):
  details = [
    {"name": "Abhishek", "age": 34, "gender": "male"},
    {"name": "Sonam", "age": 44, "gender": "female"},
    {"name": "Harsh", "age": 89, "gender": "male"},
  ]
  return render(request, "cadetails.html", {"details": details, "persondetail": persondetail})