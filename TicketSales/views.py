from audioop import reverse
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Concert, Location, Time
from django.contrib.auth.decorators import login_required
from .forms import SearchForm, ConcertForm
import TicketSales


def concert_list(request):
    searchform = SearchForm(request.GET)
    if searchform.is_valid():
        q = searchform.cleaned_data['query']
        concerts = Concert.objects.filter(name__icontains=q)
    else:
        concerts = Concert.objects.all()
    context = {
        'concerts': concerts,
        'concert_count': concerts.count(),
        'searchform': searchform,
    }
    return render(request, 'TicketSales/concert_list.html', context)


def concert_detail(request, concert_id):
    concert = get_object_or_404(Concert, pk=concert_id)
    return render(request, 'TicketSales/concert_detail.html',
                  {'concert_detail': concert})


@login_required
def concert_location(request):
    location = Location.objects.all()
    return render(request, 'TicketSales/concert_location.html', {'location': location})


@login_required
def time_list(request):
    # if request.user.is_authenticated and request.user.is_active:
    time_list = Time.objects.all()
    context = {'time_list': time_list}
    return render(request, 'TicketSales/time_list.html', context)
    # else:
    #     return HttpResponseRedirect(reverse('accounts:log_in'))


@login_required
def concert_edit(request, concert_id):
    """ Edit an existing Concert """
    concert = Concert.objects.get(pk=concert_id)
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES, instance=concert)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = ConcertForm(instance=concert)
    context = {'concert': concert, 'form': form}
    return render(request, 'TicketSales/concert_edit.html', context)
