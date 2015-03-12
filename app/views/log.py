#coding: utf-8
from django.views.generic.list import ListView
from app.models import Log

class LogListView(ListView):
	template_name = 'log/list.html'
	model = Log
	paginate_by = 500

	def get_queryset(self):
		if self.request.GET.get('q'):
			return Log.objects.filter(text__icontains=self.request.GET.get('q'))
		return super(LogListView, self).get_queryset()

	def get_context_data(self, *args, **kwargs):
		context = super(LogListView, self).get_context_data(*args, **kwargs)
		context['pages_range'] = range(1, context['page_obj'].paginator.num_pages+ 1)
		return context