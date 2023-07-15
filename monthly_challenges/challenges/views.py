from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
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
    'december': None
}


def index(request):
    months = list(monthly_challenges_dict.keys())

    return render(request, 'challenges/index.html', {
        'months' : months
        })
    ### Old way to do the thing, now we are using for in html template
    # months_li = ''
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     redirec_path = reverse("month-challenges", args=[month])
    #     months_li += f'<li><a href="{redirec_path}">{capitalized_month}</li>'
    # render_text = f'<ul>{months_li}</ul>'
    # return HttpResponse(render_text)


def monthly_challenges_by_number(request, month):
    month_keys = list(monthly_challenges_dict.keys())
    try:
        redirect_month = month_keys[month - 1]
        redirect_path = reverse('month-challenges', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except IndexError:
        return HttpResponseNotFound("Invalid Month")
    ### Bellow and other way but not using django structure
    # try:
    #     return HttpResponse(monthly_challenges_dict[month_keys[month-1]])
    # except IndexError:
    #     return HttpResponse("Invalid Month")


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_dict[month]
        return render(request, 'challenges/challenge.html', {
            # "month": month.capitalize(),
            "month": month, ### There is a built-in filter in django usefull to run the same that capitalize did (title) ###<title>{{ month|title }} Challenge</title>###
            "text" : challenge_text
        })
    except KeyError:
        raise Http404()
        #### STATIC WAY TO RENDER THE ERROR WITH from django.template.loader import render_to_string
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
