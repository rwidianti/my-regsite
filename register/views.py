from django.shortcuts import render, get_object_or_404
from .models import regdata
from .forms import RegDataForm
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
        regdatas = regdata.objects.all()
        return render(request, 'register/regdata_list.html', {'regdatas': regdatas})
def regdata_new(request):
    if request.method == "POST":
        form = RegDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('regdata_detail',pk=post.pk)
    else:
        form = RegDataForm()
    return render(request, 'register/regdata_edit.html', {'form': form})
def regdata_edit(request, pk):
    post = get_object_or_404(regdata, pk=pk)
    if request.method == "POST":
        form = RegDataForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('regdata_detail', pk=post.pk)
    else:
        form = RegDataForm(instance=post)
    return render(request, 'register/regdata_edit.html', {'form': form})
def regdata_detail(request, pk):
    post = get_object_or_404(regdata, pk=pk)
    return render(request, 'register/regdata_detail.html', {'post': post})
