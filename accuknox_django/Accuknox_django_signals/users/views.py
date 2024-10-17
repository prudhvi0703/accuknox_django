from django.shortcuts import HttpResponse
from django.contrib.auth.models import User

def create_user(request):
    try:
        User.objects.create(username='test_user')
    except Exception as e:
        return HttpResponse(f"Transaction rolled back: {e}")

    return HttpResponse("User created successfully")
