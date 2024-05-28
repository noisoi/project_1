from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import TestDataSerializer
from .models import *
from django.http import HttpResponse, Http404
from .func import *

def home(request):
    keyword = request.GET.get('q')
    place_names = []
    keyword_list = []

    filter_keyword = text_filter(text_cleaning(str(keyword)))

    if filter_keyword:
        try:
            for kw in filter_keyword:
                keyword_objs = Keywords.objects.filter(test_name=kw)
                keyword_list.append(kw)
                if keyword_objs.exists():
                    keyword_obj = keyword_objs.first()
                    place_keywords = PlacesKeywords.objects.filter(test=keyword_obj)
                    place_names = [pk.place.place_name for pk in place_keywords]
                else:
                    raise Keywords.DoesNotExist
        except Keywords.DoesNotExist:
            raise Http404('Keyword does not exist')

    context = {
        'keyword': keyword_list,
        'place_names': place_names,
    }

    return render(request, 'home.html', context)