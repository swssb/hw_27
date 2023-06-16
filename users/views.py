from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserCreateSerializer, LocationSerializer, \
    UserSerializer


# class UserListView(ListView):
#     model = User
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         self.object_list = self.object_list.filter(ad__is_published=True).annotate(total_ads=Count('ad'))
#
#         page = int(request.GET.get("page", 0))
#         paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
#         page_obj = paginator.get_page(page)
#
#         users = []
#         for user in page_obj:
#             users.append({
#                 "id": user.id,
#                 "username": user.username,
#                 "first_name": user.first_name,
#                 "last_name": user.last_name,
#                 "role": user.role,
#                 "age": user.age,
#                 "location": user.location.name,
#                 "total_ads": user.total_ads
#             })
#         response = {
#             "items": users,
#             "total": paginator.count,
#             "num_pages": paginator.num_pages
#         }
#         return JsonResponse(response, safe=False, status=200)
#
#
# class UserDetailView(DetailView):
#     model = User
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         self.object = self.get_object()
#         return JsonResponse({
#             "id": self.object.id,
#             "username": self.object.username,
#             "first_name": self.object.first_name,
#             "last_name": self.object.last_name,
#             "role": self.object.role,
#             "age": self.object.age,
#             "location": self.object.location.name
#         }, status=200)


# @method_decorator(csrf_exempt, name='dispatch')
# class UserCreateView(CreateView):
#     model = User
#     fields = ["username", "password", "first_name", "last_name", "role", "age", "location"]
#
#     def post(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         user_data = json.loads(request.body)
#         user = User.objects.create(username=user_data["username"],
#                                    password=user_data["password"],
#                                    first_name=user_data["first_name"],
#                                    last_name=user_data['last_name'],
#                                    role=user_data['role'],
#                                    age=user_data['age'],
#                                    location_id=user_data['location'])
#         return JsonResponse({
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#             "role": user.role,
#             "age": user.age,
#             "location": user.location_id
#         }, status=200)

# class UserGenericView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# @method_decorator(csrf_exempt, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ["username", "password", "first_name", "last_name", "role", "age", "location"]
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         user_data = json.loads(request.body)
#         self.object.username = user_data["username"]
#         self.object.first_name = user_data["first_name"]
#         self.object.last_name = user_data["last_name"]
#         self.object.age = user_data["age"]
#         self.object.location_id = user_data["location"]
#         self.object.save()
#
#         return JsonResponse({
#             "id": self.object.id,
#             "username": self.object.username,
#             "first_name": self.object.first_name,
#             "last_name": self.object.last_name,
#             "role": self.object.role,
#             "age": self.object.age,
#             "location": self.object.location_id
#         }, status=200)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class UserDeleteView(DeleteView):
#     model = User
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, kwargs)
#         return JsonResponse({"status": "ok"}, status=200)

class UserGenericListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGenericRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGenericCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


#
class UserGenericUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserGenericDestroyView(DestroyAPIView):
    queryset = User.objects.all()


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
