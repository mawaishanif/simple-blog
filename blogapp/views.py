from django.http import HttpResponse


def homepage(request):
    # print(type(request))
    # dir(request)
    return HttpResponse('<h1>Welcome to the Home page of the website.</h1>')
