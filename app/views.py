from django.http import HttpResponse


def index(request):
    return HttpResponse('hello ' + str(dict(request.GET)))