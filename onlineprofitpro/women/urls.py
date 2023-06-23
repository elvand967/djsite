
from django.urls import path, re_path

from .views import * # импортируем все текущие представления текущего приложения

urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/  # http://127.0.0.1:8000/women/
    path('cats/<int:catid>/', categories), # http://127.0.0.1:8000/cats/1/  # http://127.0.0.1:8000/women/cats/
    # path('cats/<slug:cat>/', categories), # http://127.0.0.1:8000/cats/test/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
