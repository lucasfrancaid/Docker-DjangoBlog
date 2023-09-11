from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListView.as_view(), name="list_authors"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail_author"),
    path("create/", views.CreateView.as_view(), name="create_author"),
    path("update/<int:pk>/", views.UpdateView.as_view(), name="update_author"),
    path("delete/<int:pk>/", views.DeleteView.as_view(), name="delete_author"),
]
