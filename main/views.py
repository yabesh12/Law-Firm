from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home/index.html')


def about(request):
	return render(request,'home/about.html')


def attorneys(request):
	return render(request,'home/attorneys.html')


def practice_areas(request):
	return render(request,'home/practice-areas.html')


def case(request):
	return render(request,'home/case.html')


def blog(request):
	return render(request,'home/blog.html')

def contact(request):
	return render(request,'home/contact.html')