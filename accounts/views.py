from django.http import HttpResponse, JsonResponse

from accounts.models import User
from back import utility


def welcome(request):
    return HttpResponse("Welcome!")


def say_hi(request):
    name = utility.get_data(request).get('name')
    return HttpResponse(f'hello {name}')


def signup(request):
    data = utility.get_data(request)
    username = data.get('username')
    password = data.get('password')
    name     = data.get('name')
    user = User.objects.create_user(username, password, name)
    data = {'user': user}
    response = utility.get_response(f'user {username} created successfully!', data)
    return JsonResponse(response)

