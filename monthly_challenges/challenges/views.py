from django.shortcuts import render
from django.http import HttpResponse

monthly_challenges_dict = {
    'january': 'January Challenge 1',
    'february': 'February Challenge 1',
    'march': 'March Challenge 1',
    'april': 'April Challenge 1',
    'may': 'May Challenge 1',
    'june': 'June Challenge 1',
    'july': 'July Challenge 1',
    'august': 'August Challenge 1',
    'september': 'September Challenge 1',
    'october': 'October Challenge 1',
    'november': 'November Challenge 1',
    'december': 'December Challenge 1'
}


def index(request):
    return HttpResponse("This Works!")


def monthly_challenges_by_number(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    try:
        return HttpResponse(monthly_challenges_dict[month])
    except KeyError:
        return HttpResponse("No challenges for " + month)
