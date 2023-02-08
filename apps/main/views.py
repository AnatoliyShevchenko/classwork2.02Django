from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.views.generic import View

from main.forms import PenForm, StoreConfigForm, StoresForm, ColorForm
from abstracts.mixins import HttpResponseMixin
from main.utils import convert_to_int

# Create your views here.
class ColorView(HttpResponseMixin, View):
    """View for creating color."""

    form = ColorForm

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
        return self.check_form_send_response(
            request,
            form
        )


class PenView(HttpResponseMixin, View):
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
        # breakpoint()
        form = self.form(request.POST)
        ink_colors = request.POST.getlist('ink_color')
        request.POST['ink_color'] = convert_to_int(ink_colors)
        return self.check_form_send_response(
            request,
            form
        )


class StoreConfigView(HttpResponseMixin, View):
    """Store View."""

    form = StoreConfigForm

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
        return self.check_form_send_response(
            request,
            form
        )


class StoresView(HttpResponseMixin, View):
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
        return self.check_form_send_response(
            request,
            form
        )