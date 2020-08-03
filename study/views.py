import traceback

from django.http import JsonResponse, HttpResponse

from back import utility
from accounts.models import User
from study.models import Day, Comment


def get_days(request):
    data = utility.get_data(request)
    username = data.get('username')
    try:
        user = User.objects.get(username=username)
    except Exception as e:
        traceback.print_exc()
        response = utility.get_response('wrong user name', False)
        return JsonResponse(response)
    try:
        days = user.days.all()
        days = utility.days2json(days)
        response = utility.get_response(f"here is {username}'s days", True, days)
        return JsonResponse(response)
    except Exception as e:
        traceback.print_exc()

        response = utility.get_response('somethings wrong in retrieving data', False)
        return JsonResponse(response)


def add_day(request):
    data = utility.get_data(request)
    username = data.get('username')
    try:
        items = data.get('items')
        user = User.objects.get(username=username)
        day = Day.objects.create()
        print('items')
        print(items)
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


def get_student(request):
    try:
        data = utility.get_data(request)
        username = data.get('username')
        user = User.objects.get(username=username)
        students = user.students.all()
        json_students = utility.users2json(students)
        response = utility.get_response(f"here is {username}'s students", True, json_students)
    except:
        response = utility.get_response("something went wrong", False)
        traceback.print_exc()

    return JsonResponse(response)


def get_comment(request):
    try:
        data = utility.get_data(request)
        day_pk = int(data.get('day_pk'))
        print('day_pk', day_pk)

        day    = Day.objects.get(pk=day_pk)
        comment = day.comment
        response = utility.get_response("success msg!", True, utility.comment2json(comment))

    except AttributeError:
        response = utility.get_response("No Comment for this day!", False)

    except:
        response = utility.get_response("something went wrong", False)
        traceback.print_exc()

    return JsonResponse(response)


def add_comment(request):
    try:
        data = utility.get_data(request)
        teacher_username = data.get('teacher_username')
        day_pk           = int(data.get('day_pk'))
        text             = data.get('text')

        teacher    = User.objects.get(username=teacher_username)
        day        = Day.objects.get(pk=day_pk)

        comment = Comment.objects.create()
        comment.user = teacher
        comment.text = text
        comment.save()
        day.comment = comment
        day.save()

        response = utility.get_response(f"comment added!", True)

    except:
        response = utility.get_response("something went wrong", False)
        traceback.print_exc()

    return JsonResponse(response)


def edit_day(request):
    data = utility.get_data(request)
    username = data.get('username')
    try:
        day_pk = int(data.get('day_pk'))
        items = data.get('items')
        user = User.objects.get(username=username)
        day = user.days.get(pk=day_pk)
        day.items.clear()
        items = utility.json2items(items)
        for item in items:
            day.items.add(item)
        day.save()
        print(utility.day2json(day))
        user.save()
        response = utility.get_response(f'a day {day_pk} for {username} just edited!', True)

    except Exception as e:
        traceback.print_exc()
        response = utility.get_response('something goes wrong', False)
    return JsonResponse(response)


