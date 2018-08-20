from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from webapp.models import Shijing 
import logging
from django.core.paginator import Paginator 

# Create your views here.

logger = logging.getLogger('django')

def shijingtest(request):
    sjs = Shijing.objects.all()
    limit = 10
    paginator = Paginator(sjs, limit)
    page = request.GET.get('page', '1')
    logger.info("page=%s" % page)

    result = paginator.page(page)
    
    return render(request, 'shijing.html', {'sjs': result})

class ShijingView(View):
    def post(self, request, *args, **kwargs):
        # shijing = Shijing.objects.all()
        result = {
            "title": "桑中",
            "chapter": "国风",
            "section": "鄘风",
            "content": "爰采唐矣？沬之乡矣。云谁之思？美孟姜矣。期我乎桑中，要我乎上宫，送我乎淇之上矣。"
        }
        return HttpResponse(result)