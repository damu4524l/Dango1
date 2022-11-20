from django.http import HttpResponse
from django.shortcuts import render
import operator

def eggs(request):
    return HttpResponse ('<h1>EGGS</h1>')


def home(request):
    return render(request,"home.html",{'hithere':'this is me'})


def count(request):
    fulltext= request.GET['fulltext']
    wordlist=fulltext.split()
    wordd={}
    for word in wordlist:
        if word in wordd:
            wordd[word]+=word
        else:
            wordd[word]=1
    s_d=sorted(wordd.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,"count.html",{'fulltext':fulltext,"count":len(wordlist),'wordd':wordd.items(),'s_d':s_d})