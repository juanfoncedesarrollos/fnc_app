from django.urls import path

from .views import *

urlpatterns = [
    path('typedocument/', TypeDocumentView.as_view())
]