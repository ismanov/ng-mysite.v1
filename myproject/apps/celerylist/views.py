from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Celery


def index(request):
    latest_celery = Celery.objects.order_by('-pub_date')[:8]
    return render(request, 'celerylist/list.html', {'latest_celery': latest_celery})

def deteil(request, celery_id):
    try:
        a = Celery.objects.get(id = celery_id )
    except:
        raise Http404 ("Письма не найдены =(")

        letest_come = a.comment_set.order_by('-id')[:10]

    return render(request, 'celerylist/deteil.html', {'celery': a, 'letest_come': letest_come})


def leave_com(request, celery_id):
    try:
        a = Celery.objects.get(id = celery_id )
    except:
        raise Http404 ("Письма не найдены =(")

    a.comment_set.create(spes_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('celery:deteil.html', args= (a.id, )) )