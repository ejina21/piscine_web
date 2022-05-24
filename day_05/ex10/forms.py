from django import forms

GENDER = (
    ("n/a", "n/a"),
    ("male", "male"),
    ("female", "female"),
)


class SearchForm(forms.Form):
    min_date = forms.DateTimeField(label='Movies minimum release date')
    max_date = forms.DateTimeField(label='Movies maximum release date')
    diameter = forms.IntegerField(label='Planet diameter greater than')
    gender = forms.ChoiceField(label='Planet diameter greater than', choices=GENDER)

