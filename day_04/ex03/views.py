from django.shortcuts import render


def my_table_color_view(request):
    sequence = [i / 50 for i in reversed(range(50))]
    return render(request, 'admin/ex03/index.html', context={'sequence': sequence})