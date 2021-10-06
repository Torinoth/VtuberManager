from django.urls import reverse_lazy
from django.views import generic
from .forms import TalentCreateForm

from .models import Talent


class ListView(generic.ListView):
    model = Talent
    template_name = 'list.html'


class TalentDetailView(generic.DetailView):
    model = Talent
    template_name = 'talent_detail.html'


class TalentCreateView(generic.CreateView):
    model = Talent
    template_name = 'talent_create.html'
    form_class = TalentCreateForm
    success_url = reverse_lazy('VM:list')

    def form_valid(self, form):
        talent = form.save(commit=False)
        talent.save()
        return super().form_valid(form)


class TalentUpdateView(generic.UpdateView):
    model = Talent
    template_name = 'talent_update.html'
    form_class = TalentCreateForm

    def get_success_url(self):
        return reverse_lazy('VM:talentDetail',
                            kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        return super().form_valid(form)


class TalentDeleteView(generic.DeleteView):
    model = Talent
    template_name = 'talent_delete.html'
    success_url = reverse_lazy('VM:list')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
