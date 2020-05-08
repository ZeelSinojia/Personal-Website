from django.shortcuts import render
from django.views.generic import ListView
from .models import (
	Project,
	Education,
	TechnicalSkill,
	PersonalWebsite,
	Activity,
)


def home(request):
	return render(request, 'Portfolio/base.html')

class PortFolioListView(ListView):
	context_object_name = 'project'
	template_name = 'Portfolio/base.html'
	query_set = Project.objects.all()

	def get_context_data(self, **kwargs):

		context = super(PortFolioListView, self).get_context_data(**kwargs)
		context['education'] = Education.objects.all()
		context['technicalskill'] = TechnicalSkill.objects.all()
		context['activity'] = Activity.objects.all()
		context['personalwebsite'] = PersonalWebsite.objects.all()
		
		return context

		