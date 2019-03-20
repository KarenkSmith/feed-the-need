from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3
from .models import NeededItem, Profile, Photo
from django.views.generic.edit import CreateView, UpdateView, DeleteView 

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'feedtheneed2'

# Views
def signup(request):
	error_message = ''
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			profile = Profile(user=user)
			profile.save()
			# This is how we log a user in via code
			login(request, user)
			return redirect('profile', profile_id=profile_id)
	else:
		error_message = 'Invalid credentials - try again'
		# A bad POST or a GET request, so render signup.html with an empty form
		form = UserCreationForm()
		context = {'form': form, 'error_message': error_message}
	return render(request, 'registration/signup.html', context)

def add_photo(request, profile_id):
	# photo-file was the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
          s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
          url = f"{S3_BASE_URL}{BUCKET}/{key}"
          # we` can assign to cat_id or cat (if you have a cat object
          photo = Photo(url=url, profile_id=profile_id)
          photo.save()
        except:
          print('An error occurred uploading file to S3')
    return redirect('profile', profile_id=profile_id)

class ProfileUpdate(UpdateView):
  model = Profile
  fields = '__all__'

class ProfileDelete(DeleteView):
  model = Profile
  success_url = '/'

class ItemDelete(DeleteView):
	model = NeededItem
	success_url = 'user/<int:profile_id>/'

# class ProfileCreate(CreateView):
#   model = Profile
#   fields = '__all__'

#   def form_valid(self, form):
#     Assign the logged in user
#     form.instance.user = self.request.user
#     Let the CreateView do its job as usual
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

class AddItems(CreateView):
	model = NeededItem
	fields = '__all__'
	
