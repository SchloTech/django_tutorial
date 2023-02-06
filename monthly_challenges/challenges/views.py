from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    "january": "This is the January Challenge!",
    "february": "This is the February Challenge!",
    "march": "This is the March Challenge!",
    "april": "This is the April Challenge!",
    "may": "This is the May Challenge!",
    "june": "This is the June Challenge!",
    "july": "This is the July Challenge!",
    "august": "This is the August Challenge!",
    "september": "This is the September Challenge!",
    "october": "This is the October Challenge!",
    "november": "This is the November Challenge!",
    "december": "This is the December Challenge!",
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months) or month <= 0:
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month-1]
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>No month by that name found, check spelling</h1>")
