from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import PythonInfo
from django.contrib.auth.models import User
from .forms import RegistrationForm

# List and Search
@login_required
def python_list(request):
    query = request.GET.get('q', '')
    if query:
        python_infos = PythonInfo.objects.filter(title__icontains=query) | PythonInfo.objects.filter(description__icontains=query)
    else:
        python_infos = PythonInfo.objects.all()
    return render(request, 'python/list.html', {'python_infos': python_infos, 'query': query})

# Create
@login_required
def python_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        PythonInfo.objects.create(title=title, description=description, created_by=request.user)
        messages.success(request, 'Python info created successfully!')
        return redirect('python_list')
    return render(request, 'python/create.html')

# Update
@login_required
def python_update(request, pk):
    python_info = get_object_or_404(PythonInfo, pk=pk)
    if request.user != python_info.created_by:
        messages.error(request, 'You can only edit your own entries!')
        return redirect('python_list')
    if request.method == 'POST':
        python_info.title = request.POST['title']
        python_info.description = request.POST['description']
        python_info.save()
        messages.success(request, 'Python info updated successfully!')
        return redirect('python_list')
    return render(request, 'python/update.html', {'python_info': python_info})

# Delete
@login_required
def python_delete(request, pk):
    python_info = get_object_or_404(PythonInfo, pk=pk)
    if request.user != python_info.created_by:
        messages.error(request, 'You can only delete your own entries!')
        return redirect('python_list')
    if request.method == 'POST':
        python_info.delete()
        messages.success(request, 'Python info deleted successfully!')
        return redirect('python_list')
    return render(request, 'python/delete.html', {'python_info': python_info})

# User Profile
@login_required
def profile_view(request):
    return render(request, 'python/profile.html', {'user': request.user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile_view')
    return render(request, 'python/edit_profile.html', {'user': request.user})



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'python/register.html', {'form': form})