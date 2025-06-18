from django.conf.urls.i18n import urlpatterns
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.conf.urls import include

urlpatterns = [
    path ('snippets/', views.SnippetList.as_view()),
    path ('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path ('users/', views.UserList.as_view()),
    path ('users/<int:pk>/', views.UserDetail.as_view()),
    path ('sights/', views.SightList.as_view(), name='sight-list'),
    path ('sights/<int:pk>/', views.SightDetail.as_view(), name='sight-detail'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)