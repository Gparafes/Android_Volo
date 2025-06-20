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
    path ('categories/', views.CategoryList.as_view(), name='category-list'),
    path ('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path ('sights/', views.SightList.as_view(), name='sight-list'),
    path ('sights/<int:pk>/', views.SightDetail.as_view(), name='sight-detail'),
    path ('categories/', views.CategoryListCreate.as_view(), name='category-list-create'),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)