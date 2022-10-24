from django.urls import path,include
from csp.views import cspView

urlpatterns=[
    path('unicorn/',include("django_unicorn.urls")),
    path('',cspView.as_view()),
]