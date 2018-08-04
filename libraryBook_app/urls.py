from django.contrib import admin
from django.urls import path, include
from library_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library_list.urls'))
]
