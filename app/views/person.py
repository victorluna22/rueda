# conding: utf-8
import json
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.core import serializers
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from app.models import Person


class PersonListView(ListView):
	template_name = 'person/list.html'
	model = Person
	paginate_by = 500

	def get_context_data(self, *args, **kwargs):
		context = super(PersonListView, self).get_context_data(*args, **kwargs)
		context['pages_range'] = range(1, context['page_obj'].paginator.num_pages+ 1)
		return context


class PersonUpdateView(UpdateView):
	template_name = 'person/manage.html'
	success_url = reverse_lazy('person_list')
	model = Person


class PersonDeleteView(DeleteView):
	model = Person
	success_url = reverse_lazy('person_list')

	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)


class PersonCreateView(CreateView):
	template_name = 'person/manage.html'
	model = Person
	success_url = reverse_lazy('person_list')

def person_search(request):
	if request.GET and request.GET.get('term'):
		# import pdb;pdb.set_trace()
		persons = list(Person.objects.extra(select={'label': 'text'}).values('id', 'label').filter(text__contains=request.GET.get('term')))
		# return HttpResponse(serializers.serialize("json", persons), content_type="application/json")
		return HttpResponse(json.dumps(persons), content_type="application/json")
