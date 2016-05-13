from django.shortcuts import render
from django.http import HttpResponse ,Http404 , HttpResponseRedirect
from django.views.generic import FormView, DetailView, ListView
from django.template import loader
from forms import ContactForm , UploadFileForm
from models import ModelFormWithFileField
from fileHandler import handle_uploaded_file
from os import remove
def upload_file(request):
    documents = ModelFormWithFileField.objects.all()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newDoc = ModelFormWithFileField(upload = request.FILES['file1'])
            newDoc.save()
            # form.save()
            # template = loader.get_template('geServer2/list.html')
            # return HttpResponse(template.render(request))
    else:
        form = UploadFileForm()
    # Load documents for the list page

    # return render(request, 'geServer2/contact.html', {'form': form })
    return render(request,'geServer2/list.html', {'form': form ,'documents': documents})

def index(request):
    template = loader.get_template('geServer2/index.html')

    return HttpResponse(template.render(request))
def delete(request):

    # ModelFormWithFileField.objects.all().delete()
    corfile = ModelFormWithFileField.objects.get(id=request.GET['fileID'])
    # remove(str(corfile.filename))
    corfile.delete()

    template = loader.get_template('geServer2/index.html')
    return upload_file(request)
class IndexFromView(FormView):
    template_name = 'geServer2/index.html'

class ContactView(FormView):
    template_name = 'geServer2/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
