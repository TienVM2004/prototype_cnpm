from django.shortcuts import render
from django.http import Http404
from .models import Word 
from easygoogletranslate import EasyGoogleTranslate

# Create your views here.

def home_view(request):
    return render(request, 'dictionary/base.html')

def view_1(request):
    # try: 
    #     e_word = Word.objects.get(id = id)
    # except Word.DoesNotExist: 
    #     raise Http404("Not found.")
    # translator = EasyGoogleTranslate()
    # result = translator.translate(e_word, target_language='vi')

    return render(request, 'dictionary/view_1.html' )

def sub_view_2(request):
    # try: 
    #     e_word = Word.objects.get(e_word = e_word)
    # except Word.DoesNotExist: 
    #     raise Http404("Not found.")
    # translator = EasyGoogleTranslate()
    # result = translator.translate(e_word, target_language='fr')

    return render(request, 'dictionary/view_2.html')


def sub_view_3(request):
    # try: 
    #     e_word = Word.objects.get(e_word = e_word)
    # except Word.DoesNotExist: 
    #     raise Http404("Not found.")
    # translator = EasyGoogleTranslate()
    # result = translator.translate(e_word, target_language='tr')

    return render(request, 'dictionary/view_3.html')

