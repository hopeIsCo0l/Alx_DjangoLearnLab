from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm,PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q




def register(request):
    if request.POST == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})   

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = CustomUserCreationForm(request.POST, instance = request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = CustomUserCreationForm(instance = request.user)

    return render(request, 'blog/profile', {'u_form': u_form})



# ListView for displaying all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# DetailView for displaying a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# CreateView for creating a new post (only for logged-in users)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView for editing a post (only for the author)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DeleteView for deleting a post (only for the author)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    


@login_required
def CommentCreateView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

@login_required
def CommentUpdateView(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.user != comment.author:
        return redirect('post_detail', pk=comment.post.id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form})

@login_required
def CommentDeleteView(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    post_id = comment.post.id
    if request.user == comment.author:
        comment.delete()
    return redirect('post_detail', pk=pk)




def search_posts(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        results = Post.objects.none()
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})





from taggit.models import Tag

def PostByTagListView(request, tag):
    posts = Post.objects.filter(tags__name__in=[tag])
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag': tag})

























