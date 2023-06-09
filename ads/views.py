import json

from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Category, Ad
from hw_27.settings import TOTAL_ON_PAGE


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        response = []
        for category in self.object_list.order_by('name'):
            response.append(
                {
                    "id": category.id,
                    "name": category.name
                }
            )
        return JsonResponse(response, safe=False, status=200)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        category = self.get_object()
        return JsonResponse({"id": category.id, "name": category.name}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)
        try:
            category = Category.objects.create(name=data.get("name"))
        except IntegrityError:
            return JsonResponse({"error": "this column does not exist"})
        return JsonResponse({"id": category.id, "name": category.name}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)
        self.object.name = category_data["name"]
        self.object.save()
        return JsonResponse({"id": self.object.id, "name": self.object.name}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        total_ads = self.object_list.count()
        page = request.GET.get("page")
        self.object_list = self.object_list.order_by('price')
        # offset = page * TOTAL_ON_PAGE
        # if offset > total_ads:
        #     self.object_list = []
        # elif offset:
        #     self.object_list = self.object_list.order_by('-price')[offset:offset + TOTAL_ON_PAGE]
        # else:
        #     self.object_list = self.object_list.order_by('-price')[:TOTAL_ON_PAGE]
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_obj = paginator.get_page(page)
        ads = []
        for ad in page_obj:
            ads.append(
                {
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author_id,
                    "price": ad.price,
                    "description": ad.description,
                    "is_published": ad.is_published,
                    "image": ad.image.url if ad.image else None,
                    "category": ad.category_id
                }
            )
        response = {
            "items": ads,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
        }
        return JsonResponse(response, safe=False, status=200)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        ad = self.get_object()
        return JsonResponse(
            {
                "id": ad.id,
                "name": ad.name,
                "author": ad.author_id,
                "price": ad.price,
                "description": ad.description,
                "image": ad.image.url if ad.image else None,
                "is_published": ad.is_published,
                "category": ad.category_id
            }, status=200
        )


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ["name", "author", "price", "description", "image", "category"]

    def post(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        data = json.loads(request.body)
        ad = Ad.objects.create(name=data.get("name"), author_id=data.get("author"), price=data.get("price"),
                               description=data.get('description'), image=data.get("image"),
                               category_id=data.get("category"))
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category": ad.category_id
        }, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name", "author", "price", "description", "image", "is_published", "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        self.object.name = ad_data["name"]
        self.object.author_id = ad_data["author"]
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]
        self.object.category_id = ad_data["category"]

        self.object.save()
        return JsonResponse({"id": self.object.id,
                             "name": self.object.name,
                             "author": self.object.author_id,
                             "price": self.object.price,
                             "description": self.object.description,
                             "category_id": self.object.category_id
                             }, status=200)


# views.py


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ad
    fields = ["name", "image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get("image", None)
        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "category": self.object.category_id,
            "image": self.object.image.url
        }, status=200)
