from django.shortcuts import render,HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.views.generic import ListView
# Create your views here.
def home(request):
    recipes= models.Recipe.objects.all()
    context={
        'recipes': recipes
    }
    return render(request,'recipes/recipe_list.html',context)

class RecipeListView(ListView):
    model= models.Recipe
    template_name='recipes/recipe_list.html'
    context_object_name='recipes'
class RecipeDetailView(DetailView):
    model=models.Recipe

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model= models.Recipe
    fields=['name','description','ingredients']
    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    
class RecipeUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model= models.Recipe
    fields=['name','description','ingredients']

    def test_func(self):
        recipe= self.get_object()
        return self.request.user == recipe.author
    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)
class RecipeDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model= models.Recipe
    success_url=reverse_lazy('recipes-home')

    def test_func(self):
        recipe= self.get_object()
        return self.request.user == recipe.author
    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    

def about(request):
    return render(request,'recipes/about.html',{'title':'about us page'})