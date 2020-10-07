from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def click(request):
    words=request.GET['words']
    print(words)
    wordlist=words.split()
    a=len(wordlist)

    wordcount={}
    for word in wordlist:
        if word in wordcount:
            wordcount[word] +=1
        else:
            wordcount[word] =1
    return render(request,'click.html',{'words':words,'length':a,'wordcount':wordcount.items()})

def eggs(request):
    return HttpResponse('Hell')
def about(request):
    return render(request,'Info.html')
