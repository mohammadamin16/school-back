from django.http import JsonResponse

from back import utility
from accounts.models import User


def get_days(request):
    # data = utility.get_data(request)
    # username = data.get('username')
    username = 'amin'
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


