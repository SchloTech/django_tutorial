from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    "january": "This is the January's Challenge!",
    "february": "This is the February's Challenge!",
    "march": "This is the March's Challenge!",
    "april": "This is the April's Challenge!",
    "may": "This is the May's Challenge!",
    "june": "This is the June's Challenge!",
    "july": "This is the July's Challenge!",
    "august": "This is the August's Challenge!",
    "september": "This is the September's Challenge!",
    "october": "This is the October's Challenge!",
    "november": "This is the November's Challenge!",
    "december": "This is the December's Challenge!",
}

# Create your views here.


def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months) or month <= 0:
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month-1]
    return HttpResponseRedirect(redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("<h1>No month by that name found, check spelling</h1>")
