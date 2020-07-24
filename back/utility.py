import json
from accounts.models import User
from study.models import Day, Item


def user2json(user: User):
    return {
        'username': user.username,
        'name': user.name,
    }


def item2json(item: Item):
    return {
        'course': item.course,
        'duration': item.duration,
        'tests_desc': item.tests_desc,
        'study_desc': item.study_desc
    }


def items2json(items: list):
    result = []
    for item in items:
        result.append(item2json(item))
    return result


def day2json(day: Day):
    return {
        'date': day.date.strftime('%y-%m-%d'),
        'items': items2json(day.items.all()),
        'total_time': day.total_time,
    }


def days2json(days: list):
    result = []
    for day in days:
        result.append(day2json(day))
    return result


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


def get_response(msg, success, data=None):
    response = {'msg': msg,
                'success': success,
                'data': data}
    if not data:
        del response['data']

    return response
