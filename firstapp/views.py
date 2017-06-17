from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	#context = {'data': 'Kumar'}
	return render(request,'firstapp/test.html',{'data': 'Kumar'})
