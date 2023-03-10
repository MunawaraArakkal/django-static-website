from django.shortcuts import render
from django.http import HttpResponse
from .models import place, people


def demo(request):
    obj = place.objects.all()
    sat = people.objects.all()
    return render(request, 'index.html', {'res': obj, 'out': sat})

# def mathoperations(request):
# a = int(request.GET['Number1'])
# b = int(request.GET['Number2'])
# add = a+b
# sub = a-b
# mul = a*b
# div = a/b
# return render(request, 'result.html', {'addition': add,  'subtraction' : sub,  'multiplication' : mul, 'division': div})
