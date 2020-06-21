from django.urls import path

from . import views

app_name = 'celery'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('<int:celery_id>/', views.deteil, name = 'deteil'),
    path('<int:celery_id>/leave_com', views.leave_com, name = 'leave_com')
]