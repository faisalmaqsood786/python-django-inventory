"""invent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings


from api.getCategories.category_api import CategoryData,CategoryDetail
from api.products.products import Products,ProductDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^apidoc/(?P<path>.*)$', serve,
        {'document_root': settings.API_DOC_ROOT}),
    url(r'v1/categories$', CategoryData.as_view()),
    url(r'v1/products$', Products.as_view()),
    url(r'v1/categories/(?P<category_id>[0-9]+)$', CategoryDetail.as_view()),
    url(r'v1/products/(?P<product_id>[0-9]+)$', ProductDetail.as_view()),
]
