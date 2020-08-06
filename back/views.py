from django.http import HttpResponse, JsonResponse

from back import dates


def get_date(request):
    return HttpResponse(dates.get_today())


