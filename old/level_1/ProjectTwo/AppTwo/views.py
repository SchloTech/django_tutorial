from django.shortcuts import render


def index(request):
    return render('<em>My Second App</em>')


def help(request):
    views = {
        'help_tag': "Help Page!"
    }

    return render(request, 'projectTwo/help.html', context=views)
