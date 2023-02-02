from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.views.generic import View

from main.forms import PenForm, StoreForm, StoresForm

# Create your views here.
class PenView(View):
    """Pen View."""

    form = PenForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(
            request=request,
            template_name='index.html',
            context={
                'ctx_form' : self.form()
            }
        )
    
    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        form = self.form(request.POST)
        if not form.is_valid():
            return HttpResponse('not ok')
        form.save()
        return HttpResponse('ok')


class StoreView(View):
    """Store View."""

    form = StoreForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(
            request=request,
            template_name='index.html',
            context={
                'ctx_form' : self.form()
            }
        )
    
    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        form = self.form(request.POST)
        if not form.is_valid():
            return HttpResponse('not ok')
        form.save()
        return HttpResponse('ok')


class StoresView(View):
    """Stores View."""

    form = StoresForm

    def get(self, request: HttpRequest, *args, **kwargs):
        return render(
            request=request,
            template_name='index.html',
            context={
                'ctx_form' : self.form()
            }
        )
    
    def post(
        self, 
        request: HttpRequest,
        *args: tuple, 
        **kwargs: dict
    ) -> HttpResponse:
        form = self.form(request.POST)
        if not form.is_valid():
            return HttpResponse('not ok')
        form.save()
        return HttpResponse('ok')
        