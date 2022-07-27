#----------------------------I have created this file - Khaled-----------------------------------
from django.http import HttpResponse
from django.shortcuts import render

def index(request) :
    dic = {'name':'Syed Khaled Hossain', 'place': 'Comilla'}
    return render(request, 'index.html', dic)

def analyze(request) :

    djtext = (request.POST.get('text', 'default'))
    removepunc = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    rmspc = request.POST.get('rmvexspc', 'off')
    charcnt = request.POST.get('charcnt', 'off')
    nlinerm = request.POST.get('newlinerm', 'off')

    params = {'purpose': 'Make Some Opperation', 'analyze_text': djtext}
    if (removepunc == 'on'):
        txt = ""
        pun = '''~`!@#$%^&*(){}[]_+,<.>/?;:'"\|'''

        for char in djtext:
            if (char not in pun):
                txt = txt + char
        params['analyze_text'] = txt
        djtext = txt;

    if (upper == "on"):
        txt = djtext
        txt = txt.upper()
        params['analyze_text'] = txt
        djtext = txt

    if (rmspc == 'on') :
        txt = ""
        i = 0
        while(djtext[i] == ' ') :
            i += 1
            continue;
        l = len(djtext)
        cnt = 0
        for char in range(i, l) :
            if(djtext[char] == ' ') :
                cnt += 1
            else :
               if(cnt >= 2):
                   txt += ' '
                   cnt = 0
               txt +=  djtext[char]
        params['analyze_text'] = txt
        djtext = txt

    if(nlinerm == 'on') :
        txt = ""
        for i in djtext :
            if i != '\n' and i != '\r' :
                txt += i
        djtext = txt

    params = {'purpose': 'Make Some Opperation', 'analyze_text': djtext}
    if(upper == 'on' or charcnt == 'on' or removepunc == 'on' or rmspc == 'on' or nlinerm == 'on') :
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("eRROR!")


def about(request) :
    return HttpResponse("Hello Khaled vai")
