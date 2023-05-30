from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from ads.models import Categorie, Ad


# @method_decorator(csrf_exempt, name='dispatch')
# class IndexView(View):
#     def get(self, request):
#         return JsonResponse({ "status": "ok"}, status=200)

def index(request):
    return JsonResponse({"status": "ok"}, status=200)

@method_decorator(csrf_exempt, name='dispatch')
class CategorieView(View):
    def get(self, request):
        categories = Categorie.objects.all()
        response = []
        for categorie in categories:
            response.append(
                {
                    "id": categorie.id,
                    "name": categorie.name
                }
            )
        return JsonResponse(response, safe=False, status=200)

class AdListView(ListView):
    model = Ad
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        response = []
        for ad in self.object_list:
            response.append(
                {
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "price": ad.price
                }
            )
        return JsonResponse(response, safe=False, status=200)

class CategorieEntityView(View):
    def get(self, request, id):
        categorie = get_object_or_404(Categorie, id=id)
        return JsonResponse({"id": categorie.id, "name": categorie.name}, status=200)

class AdDetailView(DetailView):
    model = Ad
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        try:
            ad = self.get_object()
        except Ad.DoesNotExist:
            return JsonResponse({"error": "page not found"}, status=404)
        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            }, status=200
        )




