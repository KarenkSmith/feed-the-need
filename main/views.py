from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import NeededItem, Profile
from django.views.generic.edit import CreateView,UpdateView, DeleteView

# Views
def signup(request):
	error_message = ''
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			# This is how we log a user in via code
			login(request, user)
			return redirect('home')
	else:
		error_message = 'Invalid credentials - try again'
		# A bad POST or a GET request, so render signup.html with an empty form
		form = UserCreationForm()
		context = {'form': form, 'error_message': error_message}
	return render(request, 'registration/signup.html', context)

class ProfileUpdate(UpdateView):
  model = Profile
  fields = '__all__'

class ProfileDelete(DeleteView):
  model = Profile
  success_url = '/'

# class ProfileCreate(CreateView):
#   model = Profile
#   fields = '__all__'

#   def form_valid(self, form):
#     # Assign the logged in user
#     form.instance.user = self.request.user
#     # Let the CreateView do its job as usual
#     return super().form_valid(form)

# Home
def home(request):
	needed_items = NeededItem.objects.all()
	return render(request, 'index.html', {'ni': needed_items})

# About
def about(request):
	return render(request, 'about.html')

def feeds(request):
	return render(request, 'feeds.html')

def profile(request, profile_id):
	profile = Profile.objects.get(id=profile_id)
	needed_items = NeededItem.objects.all()
	return render(request, 'user/profile.html', {
	'profile': profile, 'needed_items': needed_items,
})

