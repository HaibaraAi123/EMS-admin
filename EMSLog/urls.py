from django.urls import path,include,re_path
from EMSLog import views

urlpatterns = [
    path('',views.SyslogListView.as_view()),
]
