import os
import pandas as pd

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Entry
from .forms import AddForm, SaveForm
from .dicts import fr_de, fr_ro, fr_ru
from django.conf import settings


def dashboard_view(request):
    entries = Entry.objects.all()
    form = AddForm()

    return render(request, "dashboard.html", {
        'entries': entries,
        'form': form
    })


def add_view(request):
    if request.method == "POST":
        form = AddForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']

            de = fr_de.translate(word)
            ru = fr_ru.translate(word)
            ro = fr_ro.translate(word)

            return render(request, "add.html", {
                "word": word,
                "de": de,
                "ru": ru,
                "ro": ro
            })
    else:
        return redirect("/")


def save_view(request):
    if request.method == "POST":
        form = SaveForm(request.POST)

        if form.is_valid():
            fr = form.cleaned_data['fr']
            de = form.cleaned_data['de']
            ru = form.cleaned_data['ru']
            ro = form.cleaned_data['ro']

            entry = Entry(fr=fr, de=de, ru=ru, ro=ro, confidence="Junk")
            entry.save()

    return redirect("/")


def export_view(request):
    entries = Entry.objects.all()

    dataset = {}

    for idx, entry in enumerate(entries):
        data = [entry.fr, entry.de, entry.ru, entry.ro, entry.confidence]
        dataset[idx] = data

    raw = pd.DataFrame(dataset)

    path = os.path.join(settings.MEDIA_ROOT, "exported_words.xlsx")

    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    raw.to_excel(writer, sheet_name='Sheet')
    writer.save()

    if os.path.exists(path):
        with open(path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
            return response
    raise Http404
