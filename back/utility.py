import json
from accounts.models import User
from study.models import Day, Item


def user2json(user: User):
    return {
        'username': user.username,
        'name': user.name,
    }


def clean_items(_items: list):
    chosen_items = []
    for item in _items:
        if None not in item:
            chosen_items.append(item)

    print('edited', chosen_items)
    return chosen_items


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


def json2item(j: list):
    item = Item.objects.create(
        course=j[0],
        duration=int(j[3]),
        tests_desc=j[1],
        study_desc=j[2],
    )
    print('item: ', item)
    return item


def json2items(l: list):
    l = clean_items(l)
    items = []
    for j in l:
        print('j', j)
        items.append(json2item(j))
    print('items: ', items)
    return items


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


def json2day(j: dict):
    return Day(
        date=j['date'],
        items=json2items(j['items'])
    )


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


def get_response(msg: str, success: bool, data: dict = None):
    response = {'msg': msg,
                'success': success,
                'data': data}
    if not data:
        del response['data']

    return response

