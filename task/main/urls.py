from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

   # path('', views.post_list),
    path('admin/', admin.site.urls),
    path('', views.task_add),
    path('save/', views.save_list, name='task_new'),
]
