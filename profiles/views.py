from django.shortcuts import render, redirect
from .models import Profile,Address
from .forms import AddressForm

def profile_detail(request, uid):
    profile = Profile.objects.get(user_id = uid)
    context = {
        'profile':profile,
    }
    print(profile.pk,1)
    return render(request, 'profile\profile_info.html', context)

def add_address(request, uid):
    if request.method != "POST":
        form = AddressForm()
    else:
        form = AddressForm(request.POST)
        if form.is_valid():
            address:Address = form.save(commit = False)
            ...
            address.save()
            return redirect('profile_detail', uid)
    context = {
        'form':form
    }
    return render(request, 'profile/add_address.html',context)