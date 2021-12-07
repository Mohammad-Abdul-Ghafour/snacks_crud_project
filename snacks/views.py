from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from snacks.models import Snack
from django.urls import reverse_lazy

# Create your views here.
class SnackListView(ListView):
    template_name = "snacks_list.html"
    model = Snack

class SnackDetailsView(DetailView):
    template_name = "snack_details.html"
    model = Snack

class CreateSnackView(CreateView):
    template_name = "create_snack.html"
    model = Snack
    fields = ['title', 'purchaser', 'description', 'Register']

class DeleteSnackView(DeleteView):
    template_name = "delete_snack.html"
    model = Snack
    success_url = reverse_lazy('snack_list')

class UpdateSnackView(UpdateView):
    template_name = "update_snack.html"
    model = Snack
    fields = ['title', 'purchaser', 'description']