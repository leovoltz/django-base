from django.shortcuts import render


def home(request):
    print('Home')

    context = {
        'text': 'Welcome Home'
    }

    return render(
        request,
        'home/index.html',
        context
        )
