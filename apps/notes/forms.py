from django import forms
from apps.notes.models import Note,Tag,Category
from django.contrib.auth.models import User

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = [
			'tag',
		]
		labels = {
			'tag': 'Tag',
		}
		widgets = {
			'tag': forms.TextInput(attrs={'class':'form-control'}),
		}

class NoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = [
			'title',
			'content',
			'visibility',
			'category',
			'tags',
		]
		labels = {
			'title': 'Title',
			'content': 'Content',
			'visibility': 'Visibility',
			'category': 'Categories',
			'tags': 'Tags',
		}
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'content': forms.Textarea(attrs={'class':'form-control','rows':'5'}),
			'visibility': forms.Select(attrs={'class':'form-control'}),
			'category': forms.Select(attrs={'class':'form-control'}),
			'tags': forms.CheckboxSelectMultiple(attrs={'class':''}),
		}

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = [
			'category',
		]
		labels = {
			'category': 'Category',
		}
		widgets = {
			'category': forms.TextInput(attrs={'class':'form-control'}),
		}

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
				'username',
				'password',
				'email',
			]
		labels = {
				'username': 'Username',
				'password': 'Password',
				'email': 'E-mail',
		}
		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'password': forms.PasswordInput(attrs={'class':'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
		}
