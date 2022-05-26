from django.views.generic import FormView, ListView
from django.urls import reverse_lazy

from deploy.forms import ImageForm, Image


class HomeView(ListView, FormView):
    success_url = reverse_lazy('home')
    form_class = ImageForm
    template_name = 'base.html'
    model = Image
    context_object_name = 'images'
    object_list = Image.objects.all()

    def form_valid(self, form: ImageForm):
        form.save()
        return super().form_valid(form)

