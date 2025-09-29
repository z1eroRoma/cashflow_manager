from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CashFlow, Type, Status, Category, Subcategory
from .forms import CashFlowForm
from django.http import JsonResponse
from django.views import View


class CashFlowListView(ListView):
    model = CashFlow
    template_name = 'cashflow/list.html'
    context_object_name = 'cashflows'

    def get_queryset(self):
        queryset = super().get_queryset()
        date_from = self.request.GET.get('date_from')
        date_to = self.request.GET.get('date_to')
        status = self.request.GET.get('status')
        type_id = self.request.GET.get('type')
        category_id = self.request.GET.get('category')
        subcategory_id = self.request.GET.get('subcategory')

        if date_from:
            queryset = queryset.filter(date__gte=date_from)
        if date_to:
            queryset = queryset.filter(date__lte=date_to)
        if status:
            queryset = queryset.filter(status=status)
        if type_id:
            queryset = queryset.filter(type_id=type_id)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        if subcategory_id:
            queryset = queryset.filter(subcategory_id=subcategory_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Type.objects.all()
        context['statuses'] = Status.objects.all()
        context['categories'] = Category.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        return context

class CashFlowCreateView(CreateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cashflow/form.html'
    success_url = reverse_lazy('cashflow:list')

class CashFlowUpdateView(UpdateView):
    model = CashFlow
    form_class = CashFlowForm
    template_name = 'cashflow/form.html'
    success_url = reverse_lazy('cashflow:list')

class CashFlowDeleteView(DeleteView):
    model = CashFlow
    template_name = 'cashflow/delete.html'
    success_url = reverse_lazy('cashflow:list')

class GetSubcategories(View):
    def get(self, request):
        category_id = request.GET.get('category')
        subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
        return JsonResponse(list(subcategories), safe=False)