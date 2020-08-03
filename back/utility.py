import json
from accounts.models import User
from study.models import Day, Item, Comment


def user2json(user: User):
    return {
        'username': user.username,
        'name': user.name,
        'type': user.type,
    }


def users2json(users: list):
    result = []
    if len(users) == 0 : return[]
    for user in users:
        result.append(user2json(user))
    return result


def clean_items(_items: list):
    chosen_items = []
    for item in _items:
        if None not in item and item != {}:
            chosen_items.append(item)


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
    if len(items) == 0 : return []
    for item in items:
        result.append(item2json(item))
    return result


def json2item(j: dict):
    item = Item.objects.create(
        course=j[0],
        duration=int(j[3]),
        tests_desc=j[1],
        study_desc=j[2],
    )
    return item


def json2items(l: list):
    l = clean_items(l)
    print('edtied_items:')
    print(l)
    if len(l) == 0 : return []
    items = []
    for j in l:
        items.append(json2item(j))
    return items


def day2json(day: Day):
    try:
        return {
            'date': day.date.strftime('%y-%m-%d'),
            'items': items2json(day.items.all()),
            'total_time': day.total_time,
            'comments': comment2json(day.comment),
            'pk': day.pk,
        }
    except:
        return {
            'date': day.date.strftime('%y-%m-%d'),
            'items': items2json(day.items.all()),
            'total_time': day.total_time,
            'pk': day.pk,
        }


def days2json(days: list):
    result = []
    if len(days) == 0 : return []
    for day in days:
        result.append(day2json(day))
    return result


def comment2json(comment: Comment):
    return {
        'date': comment.date.strftime('%y-%m-%d'),
        'user': user2json(comment.user),
        'text': comment.text,
    }


def comments2json(comments: list):
    result = []
    for comment in comments:
        result.append(comment2json(comment))
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

