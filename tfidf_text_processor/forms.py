from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file and provide library ID')
    library_id = forms.CharField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['library_id'].widget.attrs.update({'placeholder': 'Library ID to assign to file'})


