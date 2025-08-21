from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, 'errors/500.html', status=500)

def about(request):
    """ About page view """
    return render(request, 'pages/about.html')

def privacy_policy(request):
    """ Privacy Policy page view """
    return render(request, 'pages/privacy_policy.html')

def terms(request):
    """ Terms and Conditions page view """
    return render(request, 'pages/terms.html')