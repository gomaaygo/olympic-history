from django.shortcuts import render
from django.views.generic import TemplateView
from django.templatetags.static import static

# Create your views here.

class DocumentationView(TemplateView):
    def get(self, request):
        context = {
            'doc_path': static('docs/api_olympic.yaml')
        }
        return render(request, 'documentation.html', context=context)