from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  return render(request,'home.html')
def analyzed(request):
  djtext= request.GET.get('text','default')
  removepunc = request.GET.get('removepunc','off')
  fullcaps = request.GET.get('fullcaps','off')
  if removepunc == 'on':
    
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=""
    for chars in djtext:
      if chars not in punctuations:
        analyzed= analyzed + chars
    param={'analyzedtext':analyzed,'title':'Removed Punctuations', 'hed': 'Without Punctuations'}
    print(analyzed)
    return render(request,'ana.html',param)
  elif fullcaps=='on':
    analyzed=""
    for chars in djtext:
      analyzed=analyzed+chars.upper()
    param={'analyzedtext':analyzed,'title':'UpperCase', 'hed': ' Uppercase'}
    return render(request,'ana.html',param)
  else:
    return HttpResponse("Failed")