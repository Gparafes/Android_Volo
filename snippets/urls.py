
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include
from .views import SensorDataAPI

urlpatterns = [
    path('api/sensor-data/', SensorDataAPI.as_view()),
]

urlpatterns = [
    path ('snippets/', views.SnippetList.as_view()),
    path ('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path ('users/', views.UserList.as_view()),
    path ('users/<int:pk>/', views.UserDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)