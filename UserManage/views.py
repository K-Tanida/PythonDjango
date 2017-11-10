from django.shortcuts import render
from django.views.generic import TemplateView
from .models import M_USER
from .forms import UserForm

class Index(TemplateView):
    template_name = 'TestPage/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = M_USER.objects.all()
        forms = UserForm()
        ctx['pagetitle'] = 'ユーザ一覧'
        ctx['forms'] = user
        return ctx
