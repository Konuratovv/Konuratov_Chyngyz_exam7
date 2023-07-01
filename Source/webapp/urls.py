from django.contrib import admin
from django.urls import path, include

from webapp.views import notes, note_create, note_update, note_delete

urlpatterns = [
    path('', notes, name="notes"),
    path('create/', note_create, name="create"),
    path('note/<int:pk>/update/', note_update, name="update"),
    path('note/<int:pk>/delete/', note_delete, name="delete")
]
