from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import ContactForm
from django.core.mail import send_mail
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


def contact(request):
    name = ''
    email = ''
    subject = ''
    message = ''

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        message = 'By:' + email + ' \n' + message

        send_mail(subject, message, 'sinojia.zeel2@gmail.com',
                  ['sinojia.zeel2@gmail.com'])
        form = ContactForm()
        context = {'form': form}

        return render(request, 'Portfolio/contact.html', context)

    else:
        context = {'form': form}
        return render(request, 'Portfolio/contact.html', context)
