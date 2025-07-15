from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

# Create your views here.

from .models import Notes
from .forms import NotesForm

def like_note(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Notes, pk=pk)
        note.likes += 1
        note.save()

        return render(request, 'notes/notes_detail.html', {'note': note})
    raise Http404

def public_note(request, pk):
    if request.method == "POST":
        note = get_object_or_404(Notes, pk=pk)
        note.public = not note.public
        note.save()

        return render(request, 'notes/notes_detail.html' , {'note': note})
    raise Http404


class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smarts/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smarts/notes'
    form_class = NotesForm

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smarts/notes'
    template_name = 'notes/notes_delete.html'


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

class NoteDetailView(DetailView):
    model = Notes
    context_object_name = 'note'

class PopularNotes(ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    queryset = Notes.objects.filter(likes__gte=1)