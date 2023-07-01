from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import NotesForms
from webapp.models import GuestBook


def notes(request):
    guestbook = GuestBook.objects.order_by("-created_at")
    search_query = request.GET.get('search', '')
    if search_query:
        note = guestbook.filter(title__icontains=search_query)
    else:
        note = guestbook.filter(status="Active")
    context = {'guestbook': note}
    return render(request, 'notes.html', context)


def note_create(request):
    if request.method == "GET":
        form = NotesForms()
        return render(request, "create.html", {'form': form})
    if request.method == 'POST':
        form = NotesForms(data=request.POST)
        if form.is_valid():
            note = GuestBook(title=form.cleaned_data.get('title'),
                             email=form.cleaned_data.get('email'),
                             text=form.cleaned_data.get('text'))
            note.save()
            return redirect('notes')
        else:
            return render(request, "create.html", {'form': form})


def note_update(request, pk):
    guestbook = get_object_or_404(GuestBook, id=pk)
    form = NotesForms(initial={
        "title": guestbook.title,
        "email": guestbook.email,
        "text": guestbook.text
    })
    if request.method == "GET":
        return render(request, "update.html", {'form': form})
    if request.method == 'POST':
        if form.is_valid():
            guestbook.title = request.POST.get('title')
            guestbook.email = request.POST.get('email')
            guestbook.text = request.POST.get('text')
            guestbook.updated_at = request.POST.get('updated_at')
            guestbook.save()
            return redirect('notes', pk=guestbook.pk)
        else:
            return render(request, "update.html", {'form': form})


def note_delete(request, pk):
    guestbook = get_object_or_404(GuestBook, id=pk)
    if request.method == "GET":
        return render(request, "delete.html", {'guestbook': guestbook})
    else:
        guestbook.delete()
        return redirect('notes')
