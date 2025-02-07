from django.http import HttpResponse

# if it won't work than alternate option HttpReponseNotFound
def handler404(request, exception):
  return HttpResponse(f"<h1 style=color:red>404 not found</h1>", status = 404)
