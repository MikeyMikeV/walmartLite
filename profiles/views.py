from django.shortcuts import render, redirect
from .models import Profile,Address
from .forms import AddressForm

def profile_detail(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'profile':profile,
    }
    return render(request, 'profile\profile_info.html', context)

def add_address(request):
    profile = Profile.objects.get(user = request.user)
    if request.method != "POST":
        form = AddressForm()
    else:
        form = AddressForm(request.POST)
        if form.is_valid():
            address:Address = form.save(commit = False)
            address.current_address = False
            set_as_current = request.POST.getlist('set_as_current')
            if profile.address.exists():
                if set_as_current:
                    prev_addr = profile.address.get(current_address = True)
                    prev_addr.current_address = False
                    prev_addr.save()
                    address.current_address = True
            else:
                address.current_address = True
            address.save()
            profile.address.add(address)

            return redirect('profile_detail')
    context = {
        'form':form
    }
    return render(request, 'profile/add_address.html',context)