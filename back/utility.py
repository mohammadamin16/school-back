import json
from accounts.models import User


def user2json(user: User):
    return {
        'username': user.username,
        'name': user.name,
    }

def get_data(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
    except:
        data = request.POST
    return data


def get_files(request):
    try:
        files = json.loads(request.body.decode('utf-8'))
    except:
        files = request.FILES
    return files


def get_response(msg, success=True, data=None):
    response = {'msg': msg,
                'success': success,
                'data': data}
    if not data:
        del response['data']

    return response
