from django.views.generic import ListView
from .models import Post
from django.shortcuts import redirect


# Create your views here.
class IndexPageView(ListView):
    model = Post
    template_name = 'posts/index.html'

    posts = Post.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['greeting1'] = 'Hello World!'
    #     context['greeting2'] = 'Hola Monde!'
    #     return context

    extra_context = {'posts': posts}


class DetailsPageView(ListView):
    model = Post
    template_name = 'posts/comments.html'

    def get_context_data(self, **kwargs):
        try:
            super(DetailsPageView, self).get_context_data(**kwargs)

            post_id = self.kwargs.get('post_id')
            comments = Post.objects.get(id=post_id).comments.all()  # Using related_name in
                                                                    # model
            if (comments):
                context = {'comments': comments}
                return context

        except Post.DoesNotExist:
            print('Error: Post does not exist!')    # I want to redirect to root url(index) in this condition,
            redirect('/')                           # however, this is not working ~Aniket Aryamane
