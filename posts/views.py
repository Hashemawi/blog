from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_home(request):

	context = {
	"title": "list",

	}
	return render(request, 'home.html', context)

def post_list(request):
	objects = Post.objects.all()
	context = {
	"post_items": objects,
	} 
	return render(request, "list.html", context)

def post_detail(request, post_id):
	#item = Post.objects.get(id=1)
	item = get_object_or_404(Post, id=post_id)
	context = {
	"item": item,
	} 
	return render(request, "detail.html", context)