from django.urls import path, include

urlpatterns = [
    path('', include('gg_translation_api.urls')),
]
