from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})



# this my view
#  Create your views here.
