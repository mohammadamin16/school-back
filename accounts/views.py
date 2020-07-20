from django.http import HttpResponse, JsonResponse

from accounts.models import User
from back import utility


def welcome(request):
    return HttpResponse("Welcome!")


def say_hi(request):
    name = utility.get_data(request).get('name')
    return HttpResponse(f'hello {name}')


def signup(request):
    post_data = utility.get_data(request)
    username = post_data.get('username')
    password = post_data.get('password')
    name     = post_data.get('name')
    try:
        user = User.objects.create_user(username, password, name)
        user = utility.user2json(user)
        msg = f'user {username} created successfully!'
        data = {'user': user}
        response = utility.get_response(msg, data)
    except Exception as e:
        msg = e.args
        print(e)
        response = utility.get_response(msg, success=False)

    return JsonResponse(response)

