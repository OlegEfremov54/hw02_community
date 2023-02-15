# yatube/urls.py Версия от 3 февраля. Финиш
from django.contrib import admin
from django.contrib.auth import views
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='posts')),
    # path('group', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    # path('any-url/', ClassName.as_view()),
]
