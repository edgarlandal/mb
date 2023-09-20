from django.shortcuts import render


def AboutMe(request):
    return render(request=request, template_name="me/about_me.html")
