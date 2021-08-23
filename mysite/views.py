from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    dj=request.POST.get("text","default")

    # check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlinermv=request.POST.get('newlinermv','off')
    xtrspacermv=request.POST.get('xtrspacermv','off')
    #check which checkbox is on
    # remove Punctuation
    if removepunc == 'on':
        punctuations='''!()-[]`|{};:'"\,<>./?@#$%^&*~_+='''
        analyzed=""
        for char in dj:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        dj=analyzed
        # analyze the text
        # return render(request, 'analyze.html', params)

    # upper case
    if fullcaps=='on':
        analyzed=""
        for char in dj:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to UPPER CASE', 'analyzed_text':analyzed}
        dj=analyzed
        # return render(request, 'analyze.html', params)

    # new line remove
    if newlinermv=='on':
        analyzed=""
        for char in dj:
            if char !="\n" and char != "\r":
                analyzed=analyzed+char
        params={'purpose':'Removes New Line', 'analyzed_text':analyzed}
        dj=analyzed
        # return render(request, 'analyze.html', params)

    # extra space remover
    if (xtrspacermv=='on'):
        analyzed=""
        for index, char in enumerate (dj):
            if not(dj[index] == " " and dj[index+1] == " "):
                analyzed=analyzed+char
        params={'purpose':'Removes Extra Space', 'analyzed_text':analyzed}
        
        # return render(request, 'analyze.html', params)

    if (removepunc != 'on' and fullcaps != 'on' and  newlinermv != 'on' and xtrspacermv != 'on'):
        return HttpResponse("Error!!! Please write something in textbox or select any operations.")
    

    return render(request, 'analyze.html', params)


def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

    

