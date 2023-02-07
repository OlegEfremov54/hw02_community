# yatube/urls.py Версия от 3 февраля. Финиш
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # импорт правил из приложения posts
    path('', include('posts.urls', namespace='posts')),
    # path('group', include('posts.urls')),
    path('admin/', admin.site.urls),
]
