from django.urls import path

from .views import index
from . import views #. はカレントパス　カレントパスのabout関数とか

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'), #127.0.0.1:800/myapp に対応（最後に）スラッシュなし
    path('about/', views.about, name='about'),
    path('info/', views.info, name='info'),
]