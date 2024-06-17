from django.shortcuts import render, redirect
from .models import Notes
from .serializers import NoteSerializer
# from rest_framework.response import Response

def add(request):
    if request.method == 'POST':
        body = request.POST.get('body', '')
        if body:
            note = Notes.objects.create(body=body)
    return redirect('home', status=1)

def home(request, status):
    notes = Notes.objects.filter(status = status)
    serializer = NoteSerializer(notes, many=True)
    template_name = f"index{status}.html"
    return render(request, template_name, {'notes': serializer.data})

def update(request, pk):
    note = Notes.objects.get(id=pk)

    if request.method == 'POST':
        body = request.POST.get('body', '')
        if body:
            note.body = body
            note.save()
            return redirect('home', status=1)

    return redirect('home', status=1)

def delete(request, pk):
    notes = Notes.objects.get(id=pk)
    notes.delete()
    return redirect('home', status=1)

def done(request, pk):
    notes = Notes.objects.get(id=pk)
    notes.status = 2
    notes.save()
    return redirect('home', status=1)
