"""
URL configuration for loyiha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from loyiha_app.views import home, batafsil, create_country, update_country, delete_country, contact, states_page, airline_detail,airlines_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_page"),
    path('contact/', contact, name="contact_page"),
    path('airlines/', airlines_list, name='airlines_list'),
    path('create_country/', create_country, name="create_country"),
    
    path('batafsil/<int:id>/', batafsil, name="batafsil_page"),
    path('update_country/<int:id>', update_country, name="update_country"),
    path('delete_country/<int:id>', delete_country, name="delete_country"),
    path('airline/<int:id>/', airline_detail, name='airline_page'),
    path('states/<int:id>/', states_page, name='states_page'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
