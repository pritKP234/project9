from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request, 'index_3.html')

def two(request):
    return render(request, 'index_4.html')