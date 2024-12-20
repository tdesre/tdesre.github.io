"""
URL configuration for site_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static

#lien a tester pour leguidevegetal:
# http://leguidevegetal:8000/catalogue/feuilles/
# Toujours ajt le port :8000, indispensable sur Django


urlpatterns = [
    path('', lambda request: redirect('accueil/')),  # Redirige vers l'accueil
    path("admin/", admin.site.urls),
    path('accueil/', include('accueil.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('description/', include('description.urls'))
]

# Ajouter les répertoires des images comme fichiers statiques
urlpatterns += static('/catalogue/', document_root=settings.BASE_DIR / 'catalogue')

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

