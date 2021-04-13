from django.http import HttpResponse #for sending http files 
from django.shortcuts import render

"""
def homepage(request): #anyone looking for url in website sends request object
    #return "Hello" will not work
    return HttpResponse('Hello')

def about(request):
    return HttpResponse('<h1>This is about Page</h1>') #Wrinting html code in this in not efficient so we will do in templates
"""
def homepage(request):
    return render(request, 'home.html',{'entertext':'Enter Text Below'}) #write python code in html file inside {{}} bracket

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] +=1
        else:
            #add to the dictionary
            worddictionary[word] =1

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist)})

def about(request):
    return render(request, 'about.html')