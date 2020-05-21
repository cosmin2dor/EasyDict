from django import forms


class AddForm(forms.Form):
    word = forms.CharField(label="French Word", max_length=200)


class SaveForm(forms.Form):
    fr = forms.CharField(label="fr", max_length=200)
    de = forms.CharField(label="de", max_length=200)
    ru = forms.CharField(label="ru", max_length=200)
    ro = forms.CharField(label="ro", max_length=200)
