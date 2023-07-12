from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

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
    months = list(monthly_challenges_dict.keys())
    months_li = ''
    for month in months:
        capitalized_month = month.capitalize()
        redirec_path = reverse("month-challenges", args=[month])
        months_li += f'<li><a href="{redirec_path}">{capitalized_month}</li>'
    render_text = f'<ul>{months_li}</ul>'
    return HttpResponse(render_text)


def monthly_challenges_by_number(request, month):
    month_keys = list(monthly_challenges_dict.keys())
    try:
        redirect_month = month_keys[month - 1]
        redirect_path = reverse('month-challenges', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except IndexError:
        return HttpResponseNotFound("Invalid Month")
    # Bellow and other way but not using django structure
    # try:
    #     return HttpResponse(monthly_challenges_dict[month_keys[month-1]])
    # except IndexError:
    #     return HttpResponse("Invalid Month")


def monthly_challenges(request, month):
    try:
        return render(request, 'challenges/challenge.html')
    except KeyError:
        return HttpResponseNotFound("No challenges for " + month)
