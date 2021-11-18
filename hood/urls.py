from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
        path('', views.index, name = 'index'),
        path('home', views.home, name = 'home'),
        path('accounts/profile/', views.profile, name = 'profile'),
        path('services', views.services, name = 'services'),
        path('business', views.business, name = 'business'),
        path('about', views.about, name = 'about'),
        path('user_admin', views.user_admin, name = 'user_admin'),
        path('category', views.category, name = 'category'),
        path('newneighbourhood', views.newneighbourhood, name = 'newneighbourhood'),
        path('newservice', views.newservice, name = 'newservice'),
        path('newbusiness', views.newbusiness, name = 'newbusiness'),
        path('search', views.search, name = 'search'),
        path('change', views.change, name = 'change'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)