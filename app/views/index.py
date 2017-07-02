from django.views import generic

from app.models.pizza import Pizza


class IndexView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        retour = super(IndexView, self).get_context_data(**kwargs)
        try:
            pizzas = Pizza.objects.order_by("label")[:10]
        except Pizza.DoesNotExist:
            loteries = None

        retour["pizzas"] = pizzas

        return retour
