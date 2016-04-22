from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file1 = forms.FileField()
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
