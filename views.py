from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.


def sum_double(request, a, b):
    if a == b:
        return HttpResponse((a + b) * 2)
    else:
        return HttpResponse(a + b)
  





def alarm_clock(request, vacation, day):
    if vacation == False:
        if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            return HttpResponse("7:00")
        else:
            return HttpResponse("10:00")
    else:
        if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            return HttpResponse("10:00")
        else:
            return HttpResponse("off")



def lucky_sum(request, a, b, c):
    if a == 13:
        return HttpResponse(0)
    elif b == 13:
        return HttpResponse(a)
    elif c == 13:
        return HttpResponse(a + b)
    else: 
        return HttpResponse(a + b + c)