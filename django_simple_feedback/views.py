from django.views.generic.edit import FormView
from django.http import HttpResponse
from .forms import FeedBackForm
from .models import FeedBack

class ValidationView(FormView):
    template_name = "index.html"
    form_class = FeedBackForm
    success_url = '/feedback/success/'

    def form_valid(self, form): # Code below will be complete only if form is valid
        data = form.cleaned_data
        f = FeedBack(email=data['email'], message=data['message'])
        f.save()

        return super().form_valid(form)

def final(request):
    return HttpResponse('success')
