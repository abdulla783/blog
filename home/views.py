from django.shortcuts import render, HttpResponse
from django.contrib import messages
from . models import Contact
from blog.models import Post

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    # messages.success(request, 'Welcome to contact!')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # print(name, email, phone, content)
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 2:
            messages.error(request, 'Please fill your form correctly:')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent. We will get back to you soon, Thanks')
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')

def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allPosts = Post.objects.none()
    else:     
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
         messages.warning(request, 'No search results found please check your query.')
    context = {
        'allPosts': allPosts,
        'query': query,
    }
    return render(request, 'home/search.html', context)