from django import forms


class UploadFileForm(forms.Form):
    file= forms.FileField(label='Select a file', help_text='max. 42 megabytes')
    # title = forms.CharField(max_length=50)
    # file = forms.FileField()
