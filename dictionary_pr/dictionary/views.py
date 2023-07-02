from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from dictionary.forms import DictForm
from dictionary.models import Word


class DictView(ListView):
    paginate_by = 5
    model = Word
    template_name = 'dictionary/dictionary_list.html'
    context_object_name = 'dict'


class DictDetailView(DetailView):
    model = Word
    template_name = 'dictionary/dictionary_detail.html'
    context_object_name = 'dict_detail'


class Search(ListView):

    template_name = 'dictionary/dictionary_list.html'
    context_object_name = 'dict'
    paginate_by = 5

    def get_queryset(self):
        return Word.objects.filter(name__iregex=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def create(request):
    if request.method == 'POST':
        form = DictForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dictionary:dict')

    form = DictForm()

    data = {
        'form': form
    }
    return render(request, 'dictionary/create.html', data)


class DictUpdateView(UpdateView):
    model = Word
    template_name = 'dictionary/create.html'

    form_class = DictForm


class DictDeleteView(DeleteView):
    model = Word
    success_url = '/dictionary/'
    template_name = 'dictionary/dictionary_delete.html'
