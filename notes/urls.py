from django.urls import path

from . import views


urlpatterns = [
    path('notes', views.NotesListView.as_view(), name='notes.list'),
    path('notes/<int:pk>', views.NoteDetailView.as_view(),name='notes.details'),
    path('notes/popular', views.PopularNotes.as_view()),
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),
    path('notes/<int:pk>/like', views.like_note, name='notes.like'),
    path('notes/<int:pk>/public', views.public_note, name='notes.public')
]