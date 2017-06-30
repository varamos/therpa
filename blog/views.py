from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from blog.forms import *


# Create your views here.
class AjaxListView(ListView):
    def get_template_names(self):
        if self.request.is_ajax():
            app_label = self.object_list.model._meta.app_label
            model_name = self.object_list.model._meta.model_name
            return ['%s/_%s_list.html' %(app_label, model_name)]
        return super(AjaxListView, self).get_template_names()



class AjaxJsonListView(ListView):
    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            post_list =[]
            for post in context['post_list']:
                post_list.append({
                    'id': post.id,
                    'Chem_ID': post.Chem_ID,
                    'Name' : post.Name,
                    'Date': post.Date,
                    'PMID' : post.PMID,
                    'Properties' : post.Properties,
                    'Type' : post.Type,
                    'Effect_to_PrP' : post.Effect_to_PrP,
                    'Effect_to_Diseases_progression' : post.Effect_to_Diseases_progression,
                    'Materials' : post.Materials,
                    'Information_of_Materials' : post.Information_of_Materials,
                    'Treatement' : post.Treatement,
                    'Binding_site' : post.Binding_site,
                    'PubChem' : post.PubChem,
                })

            return JsonResponse(post_list, content_type='application/json', safe=False)
        return super(AjaxJsonListView, self).render_to_response(context, **response_kwargs)

post_list = AjaxJsonListView.as_view(model=Post, paginate_by=6005)
post_detail = DetailView.as_view(model=Post)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/post_delete_confirm.html', {
        'post': post,
    })

def main_10_small_molecules(request):
    return render(request, 'blog/main_10_small_molecules.html', {
        'post_list': post_list,
    })

def random2(request):
    return render(request, 'blog/random2.html', {
        'post_list': post_list,
    })

def treemaps(request):
    return render(request, 'blog/treemaps.html', {
        'post_list': post_list,
    })

def real_main(request):
    post_list = Post.objects.all()
    return render(request, 'blog/real_main.html', {
        'post_list': post_list,
    })

def downloads(request):
    post_list = Post.objects.all()
    return render(request, 'blog/downloads.html', {
        'post_list': post_list,
    })

def home(request):
    post_list = Post.objects.all()
    return render(request, 'blog/home.html', {
        'post_list': post_list,
    })

def contact(request):
    return render(request, 'blog/contact.html', {
        'post_list': post_list,
    })

def about(request):
    return render(request, 'blog/about.html', {
        'post_list': post_list,
    })

def treemaps_m(request):
    return render(request, 'blog/treemaps_materials.html', {
        'post_list': post_list,
    })

def pie_chart(request):
    return render(request, 'blog/pie_chart.html', {
        'post_list': post_list,
    })

def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()


    return render(request, 'write.html', {'form' : form})

def list(request):
    submitList = Submit.objects.all()
    return render(request, 'list.html', {'submitList' : submitList})


def view(request, num="1"):
    submit = Submit.objects.get(id=num)
    return render(request, 'view.html',{'submit' : submit})
