from django import forms


class myForm(forms.Form):
    title = forms.ChoiceField(choices=[], required=True)
    opening_crawl = forms.CharField(required=True)

    def __init__(self, choices, *args, **kwargs):
        super(myForm, self).__init__(*args, **kwargs)
        self.fields['title'].choices = choices
