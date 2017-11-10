from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import pyodbc
import pandas as pd
class Index(TemplateView):
    template_name = 'TestPage/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['pagetitle'] = 'テストページ'
        return ctx
