from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy


class AdminPermissionRequiredMixin(PermissionRequiredMixin):
    redirect_field_name = ""
    login_url = reverse_lazy("index")
