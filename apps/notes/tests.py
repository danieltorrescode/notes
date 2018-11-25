from django.test import TestCase
from .models import *
# Create your tests here.


# class NoteModelTests(TestCase):
#
# 	def test_was_published_recently_with_future_question(self):
# 		"""
# 		was_published_recently() returns False for questions whose pub_date
# 		is in the future.
# 		"""
# 		time = timezone.now() + datetime.timedelta(days=30)
# 		future_question = Question(pub_date=time)
# 		self.assertIs(future_question.was_published_recently(), False)


# # ---------- /polls/urls.py ----------
#
# # 1 Generic views are normally used from the beginning
# # and they help you avoid having to write a lot
# # of custom code
#
# from django.conf.urls import url
#
# from . import views
#
# app_name = 'polls'
#
# # 1 We'll change the urlpatterns
#
# urlpatterns = [
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]
#
# # 1 Now remove our index, detail and results views in polls/views.py
#
# '''
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]
# '''
#
# # ---------- /polls/views.py ----------
#
# from django.http import HttpResponse
#
# from .models import Question, Choice
#
# from django.shortcuts import render
#
# from django.shortcuts import get_object_or_404
#
# from django.http import HttpResponseRedirect
#
# from django.urls import reverse
#
# # 2 Add the generic module
# from django.views import generic
#
# # 8 Import so we can get time information
# from django.utils import timezone
#
# # 2 The ListView displays your list of questions being
# # latest_question_list
# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#
#     # 2 This defines the question list we want to use
#     context_object_name = 'latest_question_list'
#
#     # 8 Replace get_queryset and don't return questions
#     #  published in the future
#     '''
#     def get_queryset(self):
#
#         # 2 Return the last 5 questions entered
#         return Question.objects.order_by('-pub_date')[:5]
#     '''
#
#     def get_queryset(self):
#
#         # 8 Return only questions with a pub_date less than
#         # or equal to now
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]
#
#         # 8 Add Choices to the Admin in admin.py
#
# # 2 The DetailView displays the details on your object
# # being the Question model
#
# # 2 The generic view expects the pk (Primary Key) value
# # from the URL to be called pk as we set in polls/urls.py
# class DetailView(generic.DetailView):
#     model = Question
#
#     # 2 Define the template to use with this data
#     template_name = 'polls/detail.html'
#
#     # 12 Exclude questions that are not published yet
#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now())
#
#     # 12 Add tests in polls/tests.py
#
# # 2
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
#
# # 2 Remove these functions
#
# '''
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#
#     question = get_object_or_404(Question, pk=question_id)
#
#     return render(request, 'polls/results.html', {'question': question})
# '''
#
# # 2 Vote stays the same
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#
#     except(KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice"
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#
# # 3 Now we will explore automated testing. You can either
# # check your code by entering values randomly (and miss
# # a bunch of errors), or you can automate the process.
#
# # 3 We'll now explore a bug in the was_published_recently() function
# # in polls/models.py in the shell : python3 manage.py shell
#
# # 3 Create a Question with a pub_date in the future
# '''
# import datetime
# from django.utils import timezone
# from polls.models import Question
# future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
# future_question.was_published_recently()
# Returns true even though that doesn't make sense
# '''
#
# # 3 Open the file called tests.py
#
#
# # ---------- /polls/tests.py ----------
#
# from django.test import TestCase
#
# # 4 Import your needed modules
# import datetime
# from django.utils import timezone
# from django.test import TestCase
#
# from .models import Question
#
# # 4 TestCase runs tests without effecting your data
# # by creating a temporary database for testing
# class QuestionMethodTests(TestCase):
#
#     # 4 Put the code used in the shell here
#     # Start the method name with test
#     def test_was_published_recently_with_future_question(self):
#
#         # 4 Create a time 30 days in the future
#         time = timezone.now() + datetime.timedelta(days=30)
#
#         # 4 Create a question using the future time
#         future_question = Question(pub_date=time)
#
#         # 4 Check to see if the output is False like we expect
#         self.assertIs(future_question.was_published_recently(), False)
#
#         # 4 Run the test in the terminal
#         # python3 manage.py test polls
#         # You'll see that the test failed
#
#         # 4 Fix the bug in models.py
#
#     # 6 Return false if pub_date is older then 1 day
#
#     def test_was_published_recently_with_old_question(self):
#         # Should return false if pub_date is older then 1 day
#         time = timezone.now() - datetime.timedelta(days=30)
#         old_question = Question(pub_date=time)
#         self.assertIs(old_question.was_published_recently(), False)
#
#     # 6 Return True if published within the last day
#
#     def test_was_published_recently_with_recent_question(self):
#         time = timezone.now() - datetime.timedelta(hours=1)
#         recent_question = Question(pub_date=time)
#         self.assertIs(recent_question.was_published_recently(), True)
#
#     # 6 Test with : python3 manage.py test polls
#
#     # 7 We can simulate user interaction at the view level in the shell
#     # python3 manage.py shell
#     '''
#     # This allows us access variable values in our templates
#     # We will be using our real database here
#     from django.test.utils import setup_test_environment
#     setup_test_environment()
#
#     # Create the client that we'll use to run our app
#     from django.test import Client
#     client = Client()
#
#     # Get the status code from localhost:8000/
#     response = client.get('/')
#     response.status_code
#
#     # Get the status code for localhost:8000/polls/
#     from django.urls import reverse
#     response = client.get(reverse('polls:index'))
#     response.status_code
#
#     # Get the HTML content
#     response.content
#
#     # Get the value of latest_question_list
#     response.context['latest_question_list']
#     '''
#
#     # 7 Let's update polls/views.py so it doesn't show
#     # questions published in the future
#
#     # 10 Create a function that creates questions at
#     # a specified date
#
#     def create_question(question_text, days):
#         time = timezone.now() + datetime.timedelta(days=days)
#         return Question.objects.create(question_text=question_text,
#                                        pub_date=time)
#
# # 10 Add more question tests
#
# class QuestionViewTests(TestCase):
#
#     # 10 Test to see what happens if there are no questions
#     def test_index_view_with_no_questions(self):
#
#         # Get the client
#         response = self.client.get(reverse('polls:index'))
#
#         # Check the status code
#         self.assertEqual(response.status_code, 200)
#
#         # Verify that response contains this string
#         self.assertContains(response, "No polls are available.")
#
#         # Check if latest_question_list is empty
#         self.assertQuerysetEqual(response.context['latest_question_list'], [])
#
#     # 10 Make sure questions with a pub_date in past are shown
#     def test_index_view_with_a_past_question(self):
#
#         # Create sample question
#         create_question(question_text="Past question.", days=-30)
#
#         # Get client
#         response = self.client.get(reverse('polls:index'))
#
#         # Verify that the question shows
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             ['<Question: Past question.>']
#         )
#
#     # 10 Make sure questions with future pub_date don't show
#     def test_index_view_with_a_future_question(self):
#
#         # Create question
#         create_question(question_text="Future question.", days=30)
#
#         # Get client
#         response = self.client.get(reverse('polls:index'))
#
#         # Verify response contains text
#         self.assertContains(response, "No polls are available.")
#
#         # Verify that latest_question_list is empty
#         self.assertQuerysetEqual(response.context['latest_question_list'], [])
#
#     # 10 Verify that if past and future questions exist that only
#     # past show
#     def test_index_view_with_future_question_and_past_question(self):
#
#         # Create questions
#         create_question(question_text="Past question.", days=-30)
#         create_question(question_text="Future question.", days=30)
#
#         # Get client
#         response = self.client.get(reverse('polls:index'))
#
#         # Verify that question list only contains past questions
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             ['<Question: Past question.>']
#         )
#
#     # 10 Make sure question list shows multiple questions
#     def test_index_view_with_two_past_questions(self):
#
#         # Create questions
#         create_question(question_text="Past question 1.", days=-30)
#         create_question(question_text="Past question 2.", days=-5)
#
#         # Create client
#         response = self.client.get(reverse('polls:index'))
#
#         # Verify that both questions show
#         self.assertQuerysetEqual(
#             response.context['latest_question_list'],
#             ['<Question: Past question 2.>', '<Question: Past question 1.>']
#         )
#
# # 11 Make sure future questions can't be accessed if the user
# # guess the URL in polls/views.py
#
# # 13 Add tests to make sure future posts aren't shown in detail
#
# class QuestionIndexDetailTests(TestCase):
#
#     # 13 Make sure future question detail pages show 404
#     def test_detail_view_with_a_future_question(self):
#
#         # Create question
#         future_question = create_question(question_text='Future question.', days=5)
#
#         # Open url using the future question in the url
#         url = reverse('polls:detail', args=(future_question.id,))
#
#         # Get client response
#         response = self.client.get(url)
#
#         # Verify that it returns 404
#         self.assertEqual(response.status_code, 404)
#
#     # 13 Verify that past questions show in detail
#     def test_detail_view_with_a_past_question(self):
#
#         # Create question
#         past_question = create_question(question_text='Past Question.', days=-5)
#
#         # Open url with past question
#         url = reverse('polls:detail', args=(past_question.id,))
#
#         # Get response
#         response = self.client.get(url)
#
#         # Verify the question shows
#         self.assertContains(response, past_question.question_text)
#
#
# # ---------- /polls/models.py ----------
#
# from django.db import models
#
# import datetime
# from django.utils import timezone
#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         # 5 return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#         # 5 Fix the code
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
#         # 5 Now the test will pass
#
#         # 5 Add further tests to polls/tests.py
#
# class Choice(models.Model):
#
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
#
#
# # ---------- /polls/admin.py ----------
#
# from django.contrib import admin
#
# # 9 Add choice to imports
#
# from .models import Question, Choice
#
# admin.site.register(Question)
#
# # 9 Add Choice to the Admin page
# admin.site.register(Choice)
#
# # 9 Create some future questions
#
# # 9 Add some tests in polls/tests.py
