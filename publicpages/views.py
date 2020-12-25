from django.shortcuts import render
from django.views.decorators.http import require_GET


@require_GET
def home_view(request):
    # Home page
    return render(request, 'publicpages/home.html')