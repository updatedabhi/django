from django.shortcuts import render

def details(request):
  name = request.GET.get("name")
  details = [
    {"name": name, "age": 34},
    {"name": name, "age": 93}
  ]
  return render(request, "abc.html", {"details": details})