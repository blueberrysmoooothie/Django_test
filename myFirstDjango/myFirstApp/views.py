from django.shortcuts import render
from .models import MyModel

def my_view(request):
    queryset = MyModel.objects.all()
    context = {'queryset': queryset}
    return render(request, 'my_template.html', context)