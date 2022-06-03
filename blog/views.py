from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import redirect, render

from .forms import SubscribeForm

from .models import Category, Post

# Create your views here.

#This View is for the landing(HomePage) View
class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-date_added']
    context_object_name = "Post"

    #This Only displays 9 posts per page in order to not overoad 1 page with alot of posts
    paginate_by = 9 

    
#This is the subscribe view that uses the SubscribeForm and submits form to the database 
def Subscribe(request):
    if request.POST:
        form = SubscribeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        return redirect('homepage')
    return render(request, 'subscribe.html', {'form': SubscribeForm})



#This view handles the detailed View of the article(Post) 
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

#This handles displaying the specific posts under a category
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

#This dispayed the list of all available Categories
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


#This Stops Bots(Web crawers etc) from accessing specific parts of the application and indexing it, e.g adminpanel
def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /adminpanelforblog11223344/"
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")