from django.shortcuts import render
from .models import regdata

# Create your views here.
def post_list(request):
        regdatas = regdata.objects.all()
        return render(request, 'register/regdata_list.html', {'regdatas': regdatas})
