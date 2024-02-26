from django.shortcuts import render, redirect
from .models import Profile,Address
from .forms import AddressForm

def profile_detail(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'profile':profile,
    }
    print(profile.pk,1)
    return render(request, 'profile\profile_info.html', context)

def add_address(request):
    if request.method != "POST":
        form = AddressForm()
    else:
        form = AddressForm(request.POST)
        if form.is_valid():
            address:Address = form.save(commit = False)
            ...
            address.save()
            return redirect('profile_detail', request.user.pk)
    context = {
        'form':form
    }
    return render(request, 'profile/add_address.html',context)