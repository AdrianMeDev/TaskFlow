from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def secret_view(request):
    """A simple secret view used to test LOGIN_REDIRECT_URL and redirects.

    Renders a template that displays a welcome and the current user's username.
    """
    return render(request, "api/secret.html", {"user": request.user})
