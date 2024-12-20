"""
URL configuration for test_project project.

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
from django.urls import path
from hello import views

# product_patterns = [
#     path("", views.products),
#     path("comments", views.comments),
#     path("questions", views.questions),
# ]

# 33
# urlpatterns = [
#     path("", views.index),
#     path("user/", views.user),
# ]

# 34
# urlpatterns = [
#     path("", views.index),
#     path("about/", views.about),
#     path("contact/", views.contact),
#     path("details/", views.details),
# ]

# 36
# urlpatterns = [
#     path("index/<int:id>", views.index),
#     path("access/<int:age>", views.access),
# ]

# 38
# urlpatterns = [
#     path('', views.index),
# ]

# 39
# urlpatterns = [
#     path('', views.index),
# ]

# 42
# urlpatterns = [
#     path("set", views.set),
# ]

# 43
# urlpatterns = [
#     path("set", views.set),
#     path("get", views.get),
# ]

# 46
# urlpatterns = [
#     path("", views.index),
# ]

# 47
# urlpatterns = [
#     path("", views.index),
#     path("about/", views.about),
#     path("contact/", views.contact),
# ]

# 49
# urlpatterns = [
#     path("", views.index),
# ]

# 51
urlpatterns = [
    path("", views.index),
]