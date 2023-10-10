from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        'text': 'Welcome to the blog',
    }

    return render(
        request,
        'blog/index.html',
        context
        )


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Hello exemple',
        'title': 'Example page - '
    }

    return render(
        request,
        'blog/exemplo.html',
        context
        )
