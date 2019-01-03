from django.http import HttpResponse

def homepage(request):
	return HttpResponse('Hello World')

def Repo(request):
	return HttpResponse('<h1>This is the Repo page!!!!</H1>')
	