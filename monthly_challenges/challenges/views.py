from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This Works!")

def monthly_challenges_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "January Challenge"
    elif month == "february":
        challenge_text = "February Challenge"
    elif month == "march":
        challenge_text = "March Challenge"
    elif month == "april":
        challenge_text = "April Challenge"
    elif month == "may":
        challenge_text = "May Challenge"
    elif month == "june":
        challenge_text = "June Challenge"
    elif month == "july":
        challenge_text = "July Challenge"
    elif month == "august":
        challenge_text = "August Challenge"
    elif month == "september":
        challenge_text = "September Challenge"
    elif month == "october":
        challenge_text = "October Challenge"
    elif month == "november":
        challenge_text = "November Challenge"
    elif month == "december":
        challenge_text = "December Challenge"
    else:
        return HttpResponse("This month is not supported")
    return HttpResponse(challenge_text)
