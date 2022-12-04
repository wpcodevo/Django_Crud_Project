from django.urls import path
from note_api.views import Notes, NoteDetail

urlpatterns = [
    path('', Notes.as_view()),
    path('<str:pk>', NoteDetail.as_view())
]
