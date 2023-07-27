from django.shortcuts import render

# Create your views here.
def one(request):
    return render(request, 'index_1.html')

def two(request):
    return render(request, 'index_2.html')