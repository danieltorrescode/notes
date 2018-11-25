from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView, DeleteView
from django.views.generic import TemplateView,View,DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from apps.notes.forms import *
from .models import *
# Create your views here.

def index(request):
		try:
			public_notes = Note.objects.filter(visibility=1).order_by('-id')
		except Note.DoesNotExist:
			raise Http404("Note does not exist")
		return render(request, 'index.html', {'list_notes': public_notes})

class category_create(LoginRequiredMixin,CreateView):
	login_url = '/log_in/'
	model = Category
	form_class = CategoryForm
	template_name = 'notes/category_create.html'
	success_url = reverse_lazy('notes:category_list')
	'''
	# ,UserPassesTestMixin
	# determines if the user is part of the staff
	def test_func(self):
		if self.request.user.is_staff:
			return True
	'''


class category_list(LoginRequiredMixin,ListView):
	login_url = '/log_in/'
	model = Category

	def get_queryset(self):
		return Category.objects.order_by('id')

class category_update(LoginRequiredMixin,UpdateView):
	login_url = '/log_in/'
	model = Category
	fields = ['category']
	template_name_suffix = '_update'
	success_url = reverse_lazy('notes:category_list')

class category_delete(LoginRequiredMixin,DeleteView):
	login_url = '/log_in/'
	model = Category
	template_name_suffix = '_delete'
	success_url = reverse_lazy('notes:category_list')

@login_required(login_url='/log_in/')
def tag_create(request):
	if request.method == 'POST':
		form = TagForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('notes:tag_list')
	else:
		form = TagForm()
	return render(request, 'notes/tag_create.html', {'form':form})

@login_required(login_url='/log_in/')
def tag_list(request):
	tag = Tag.objects.all().order_by('id')
	tags = {'tags':tag}
	return render(request, 'notes/tag_list.html', tags)

@login_required(login_url='/log_in/')
def tag_update(request, pk):
	tag = Tag.objects.get(id=pk)
	if request.method == 'GET':
		form = TagForm(instance=tag)
	else:
		form = TagForm(request.POST, instance=tag)
		if form.is_valid():
			form.save()
		return redirect('notes:tag_list')
	return render(request, 'notes/tag_update.html', {'form':form})

@login_required(login_url='/log_in/')
def tag_delete(request, pk):
	tag = Tag.objects.get(id=pk)
	if request.method == 'POST':
		tag.delete()
		return redirect('notes:tag_list')
	return render(request, 'notes/tag_delete.html', {'tag':tag})

class note_create(LoginRequiredMixin,CreateView):
	login_url = '/log_in/'
	model = Note
	form_class = NoteForm
	template_name = 'notes/note_create.html'
	success_url = reverse_lazy('notes:note_list')

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			note = form.save()
			note.user = self.request.user
			note.save()
			return HttpResponseRedirect(self.get_success_url())
		#return render(request, 'notes/note_create.html', {'error':'Invalid data in form'})
		return self.render_to_response(self.get_context_data(form=form))

class note_list(LoginRequiredMixin,ListView):
	#redirect_field_name = 'redirect_to'
	login_url = '/log_in/'
	model = Note

	def get_queryset(self):
		return Note.objects.filter(user=self.request.user).order_by('-id')
	'''
	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(note_list, self).get_context_data(**kwargs)
		for note in context['note_list']:
			#note_tags is created in the object to place all related tags
			note.note_tags = note.tags.all()
		return context
	'''

class note_detail(LoginRequiredMixin,DetailView):
	login_url = '/log_in/'
	model = Note
	template_name = 'notes/note_detail.html'
	context_object_name = 'note'
	#queryset = Note.objects.all()

class note_update(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	login_url = '/log_in/'
	model = Note
	form_class = NoteForm
	template_name_suffix = '_update'
	success_url = reverse_lazy('notes:note_list')

	def test_func(self):
		note=Note.objects.get(id=self.get_object().pk)
		if note.user == self.request.user:
			return True
		else:
			return False

class note_delete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	login_url = '/log_in/'
	model = Note
	template_name_suffix = '_delete'
	success_url = reverse_lazy('notes:note_list')

	def test_func(self):
		note=Note.objects.get(id=self.get_object().pk)
		if note.user == self.request.user:
			return True
		else:
			return False

class register(CreateView):
	model = User
	template_name = 'register/sign_up.html'
	form_class = UserForm
	success_url = reverse_lazy('notes:note_list')

	def get_context_data(self, **kwargs):
		context = super(register, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(self.get_success_url())

		return self.render_to_response(self.get_context_data(form=form))

def log_in(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('notes:note_list') #render(request, 'notes/note_list.html')
			else:
				return render(request, 'register/log_in.html',
								{'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'register/log_in.html',
								{'error_message': 'Invalid login'})
	return render(request, 'register/log_in.html')

@login_required(login_url='/log_in/')
def log_out(request):
	logout(request)
	return redirect('notes:index')


def detail(request, id):
	return HttpResponse("Parametro recibido:  %s." % id)
