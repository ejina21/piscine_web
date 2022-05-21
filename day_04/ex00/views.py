from django.shortcuts import render

# Create your views here.
def my_view(request):
    template_name = 'admin/ex00/index.html'
    return render(request, template_name)