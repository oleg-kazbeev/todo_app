from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/todo_list/', include('todo_list.urls')),
    path('user/', include('users.urls'))
]
