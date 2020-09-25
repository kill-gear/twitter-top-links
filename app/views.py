from django.shortcuts import render

# Create your views here.
def top_tweets_list(request):
    return render(request, 'app/top_tweets_list.html', {})

def user_tweets_list(request):
    return render(request, 'app/user_tweets_list.html', {})

def auth(request):
    pass

def callback(request):
    pass

def sign_out(request):
    pass