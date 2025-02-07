from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
  n1 = int(request.GET.get('n1'))
  n2 = int(request.GET.get('n2'))
  operator = request.GET.get('operator')
  result = 0
  
  if (operator == "add"):
    result = n1 + n2
  elif (operator == 'sub'):
    result = n1 - n2
  elif (operator == 'mul'):
    result = n1 * n2
  elif (operator == 'divide'):
    if (n2 == 0): return HttpResponse("You can't divide by zero")
    result = n1 / n2;
  else:
    return HttpResponse("Invalid operator")
    
  return HttpResponse(f"Result: {result}")