from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import (
	Project,
	Education,
	TechnicalSkill,
	PersonalWebsite,
	Activity,
)


def home(request):
	return render(request, 'Portfolio/index.html')

class PortFolioListView(ListView):
	context_object_name = 'project'
	template_name = 'Portfolio/portfolio.html'

	def get_queryset(self):
		self.project = get_object_or_404

	def get_context_data(self, **kwargs):

		context = super(PortFolioListView, self).get_context_data(**kwargs)
		context['project'] = Project.objects.all()
		context['education'] = Education.objects.all()
		context['technicalskill'] = TechnicalSkill.objects.all()
		context['activity'] = Activity.objects.all()
		context['personalwebsite'] = PersonalWebsite.objects.all()
		
		return context

		