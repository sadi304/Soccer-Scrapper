from django.shortcuts import render

from .models import Post

def index(request):
  latest_posts = Post.objects.order_by('created_at')
  context = {'latest_question_list': latest_posts}
  return render(request, './index.html', context)

def detail(request, post_id):
  try:
    post = Post.objects.get(pk=post_id)
  except Question.DoesNotExist:
    raise Http404("Post does not exist")
  return render(request, './detail.html', {'post': post})