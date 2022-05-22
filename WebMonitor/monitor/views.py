from pickle import EMPTY_LIST
from django.shortcuts import redirect, render
from django.views.generic import UpdateView, DeleteView, DetailView
from .forms import WebPageModelForm
from .models import WebPage, Failure
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


# Create your views here.
def monitor_view(request):
    WebPages = WebPage.objects.all()
    context = {
        'WebPages': WebPages,
        
    }
    
    return render(request, 'monitor/monitoring.html', context)

def broken_webpages_view(request): 
    WebPages = WebPage.objects.filter(IsWorking=False)
    context = {
        'WebPages': WebPages,
    }
    return render(request, 'monitor/BrokenWebpages.html', context)


def AddWebPageView(request):
    form = WebPageModelForm(request.POST or None, request.FILES or None, )

    if request.method == 'POST':
        if form.is_valid():
            
            form.save()
            return redirect('monitor:main')

    context = {
        'form': form,
        }

    return render(request, 'monitor/AddNewWebPage.html', context)


class WebPageDeleteView(DeleteView):
    model = WebPage
    template_name = 'monitor/confirm_delete.html'
    success_url = reverse_lazy('monitor:main')

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = WebPage.objects.get(pk=pk)
        return obj


class WebPageUpdateView(UpdateView):
    form_class = WebPageModelForm
    model = WebPage
    template_name = 'monitor/update.html'
    success_url = reverse_lazy('monitor:main')

    def form_valid(self, form):
        return super().form_valid(form)

class WebPageDetailView(DetailView):
    model = WebPage
    template_name = 'monitor/WebPage_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        page = WebPage.objects.get(pk=pk)
        QFailures = page.Failures.all()
        context['page'] = page
        context['QFailures'] = QFailures
        return context