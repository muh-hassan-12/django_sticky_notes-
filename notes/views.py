from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Note, UserProfile
from .forms import NoteForm, RegisterForm

@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'note_list.html', {'notes': notes})

@login_required
def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.owner = request.user
        note.save()
        return redirect('note_list')
    return render(request, 'note_form.html', {'form': form, 'title': 'New Note'})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'note_form.html', {'form': form, 'title': 'Edit Note'})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, owner=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})

def register_view(request):
    form = RegisterForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save()
        profile_pic = form.cleaned_data.get('profile_picture')
        UserProfile.objects.create(user=user, profile_picture=profile_pic)
        login(request, user)
        return redirect('note_list')
    return render(request, 'register.html', {'form': form})