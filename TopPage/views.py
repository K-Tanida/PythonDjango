from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'TopPage/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pagetitle'] = 'トップページ'
        
        return ctx
