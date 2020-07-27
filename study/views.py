import traceback

from django.http import JsonResponse, HttpResponse

from back import utility
from accounts.models import User
from study.models import Day


def get_days(request):
    data = utility.get_data(request)
    username = data.get('username')
    print('GET_DAYS')
    print(username)
    # username = 'amin'
    try:
        user = User.objects.get(username=username)
    except Exception as e:
        print(e)
        response = utility.get_response('wrong user name', False)
        return JsonResponse(response)
    try:
        days = user.days.all()
        days = utility.days2json(days)
        response = utility.get_response(f"here is {username}'s days", True, days)
        return JsonResponse(response)
    except Exception as e:
        print(e)
        response = utility.get_response('somethings wrong in retrieving data', False)
        return JsonResponse(response)


def view2(request):
    data = utility.get_data(request)
    username = data.get('username')
    try:
        items = data.get('items')
        user = User.objects.get(username=username)
        day = Day.objects.create()
        items = utility.json2items(items)
        for item in items:
            day.items.add(item)
        day.save()
        user.days.add(day)
        user.save()
        response = utility.get_response(f'a day added to {username}', True)

    except Exception as e:
        traceback.print_exc()
        response = utility.get_response('something goes wrong', False)
    return JsonResponse(response)
