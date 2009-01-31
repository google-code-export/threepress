import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template
from django.core.paginator import Paginator

import bookworm.search.epubindexer as epubindexer
import bookworm.search.constants as constants
from bookworm.search.forms import EpubSearchForm
from bookworm.library.models import HTMLFile

log = logging.getLogger('search.views')

@login_required
def search(request):

    if not 'q' in request.GET:
        return direct_to_template(request, 'results.html')

    form = EpubSearchForm(request.GET)

    if not form.is_valid():
        return direct_to_template(request, 'results.html', { 'search_form': form })     

    html_res = HTMLFile.objects.filter(words__search=form.cleaned_data['q'],
                                       archive__user_archive__user=request.user).distinct()
    if len(html_res) == 0:
        return direct_to_template(request, 'results.html', { 'term': form.cleaned_data['q'] } )        

    page = 1

    if 'page' in request.GET:
        try:
            page = int(request.GET['page'])
        except ValueError:
            pass


    res = Paginator(html_res, constants.RESULTS_PER_PAGE)
    
    return direct_to_template(request, 'results.html', 
                              { 'results':res,
                                'page':res.page(page),
                                'term':form.cleaned_data['q']}) 

