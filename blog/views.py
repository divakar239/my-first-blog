from django.shortcuts import render
from .models import Post      			# the . infront of models means current directory; so we can use the name of the file without .py since theyare both in the same directory
from django.utils import timezone

# Create your views here.
def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')



	return render(request,'blog/post_list.html',{'posts': posts}
		)
