from django.urls import path
from note_api.views import Notes, NoteDetial

urlpatterns = [
    path('', Notes.as_view()),
    path('<str:pk>', NoteDetial.as_view())
]
