from django.views.generic import ListView
from .models import Post


# Create your views here.
class IndexPageView(ListView):
    model = Post
    template_name = 'posts/index.html'
    posts = Post.objects.get(id=1)
    comments = posts.comments.all()

    extra_context = {'comments': comments}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['greeting1'] = 'Hello World!'
    #     context['greeting2'] = 'Hola Monde!'
    #     return context
