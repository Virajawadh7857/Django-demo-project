from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf

#PDF Generate using Class base and function base with static and media url with all External Stylesheet and image are working.


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("123355")
            content = "inline; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not Found")


'''
def GeneratePDF(request):
    template = get_template('invoice.html')
    context ={
        "invoice_id": 123,
    }
    html = template.render(context)
    pdf = render_to_pdf('invoice.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponse(html)
   '''