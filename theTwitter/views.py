from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm,PostEditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#def home(request):
#    return render(request, 'home.html', {})



class HomeView(ListView):
    model=Post
    template_name = 'home.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model=Post
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        thing=get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes=thing.total_likes()
        context=super(ArticleDetailView , self).get_context_data(*args, **kwargs)
        liked=False
        if thing.follow.filter(id=self.request.user.id).exists():
            liked=True
        context["total_likes"]=total_likes
        context['liked']=liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url=reverse_lazy('home')



def AuthorView(request,pk):
    user = User.objects.get(id=1)
    postsList=Post.objects.filter(author__pk=pk)
    return render(request,"authorPosts.html",{'PostList':postsList})




def FollowView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked=False
    if post.follow.filter(id=request.user.id).exists():
        post.follow.remove(request.user)
        liked=False
    else:
        post.follow.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article_detail',args=[str(pk)]))

def SearchView(request):
    if request.method == 'POST':
        searched=request.POST['Searched']
        Posts=Post.objects.filter(title__contains=searched)
        return render(request,'search.html',{'searched':searched,'object_list':Posts})
    else:
        return render(request,'search.html',{})
