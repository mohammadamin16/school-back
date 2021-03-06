import traceback

from django.db.utils import IntegrityError
from django.contrib.auth import authenticate
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

    except IntegrityError:
        traceback.print_exc()
        msg = "this username is taken. sorry:)"
        response = utility.get_response(msg, success=False)

    except Exception as e:
        traceback.print_exc()
        msg = "Something goes wrong!"
        response = utility.get_response(msg, success=False)

    return JsonResponse(response)


def login(request):
    post_data = utility.get_data(request)
    username = post_data.get('username')
    password = post_data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        user = utility.user2json(user)
        msg = f'welcome {user["name"]}'
        data = {'user': user}
        response = utility.get_response(msg, success=True, data=data)
    else:
        msg = 'username or password is wrong'
        response = utility.get_response(msg, success=False)

    return JsonResponse(response)

