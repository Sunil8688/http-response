from django.http import HttpResponse

def sheela(request):
    print("hello how are you all ")
    return HttpResponse('hello how are you all')


def apple(requst):
    print("apple keeps doctor away")
    return HttpResponse("apple keeps doctor away")


def banana(request):
    # print("I am Banana")
    return HttpResponse("<h1> I am a Banana </h1>")

def list(request):
    list_data=[1,2,3,"abc",True,{'key':'value'}]
    return HttpResponse(list_data)

def add(request):
    a=10
    b=20
    c=a+b
    return  HttpResponse(c)

