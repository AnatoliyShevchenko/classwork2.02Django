from django.http import HttpResponse


class HttpResponseMixin:
    """Mixin from http handlers."""

    def check_form_send_response(self, request, form) -> HttpResponse:
        if not form.is_valid():
            return HttpResponse('not ok')
        form.save()
        return HttpResponse('ok')