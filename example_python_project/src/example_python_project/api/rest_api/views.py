from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def health_check(request):
    """Health check endpoint for the Django API."""
    return JsonResponse({"status": "OK"})