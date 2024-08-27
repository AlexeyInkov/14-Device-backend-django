from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from ..models import Organization

# from ..producer import send_message


# Create your views here.
# def message_view(request: HttpRequest):
#
#     message = "Hello"
#     send_message("my_topic", message.encode())
#     context = {"message": message}
#     return render(request, "device/message.html", context=context)


class OrganizationListView(LoginRequiredMixin, ListView):
    model = Organization

    def get_queryset(self):
        cur_user = self.request.user

        if cur_user.is_staff:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(user=cur_user.pk)


class OrganizationCreateView(LoginRequiredMixin, CreateView):
    model = Organization


class OrganizationDetailView(LoginRequiredMixin, DetailView):
    model = Organization


class OrganizationUpdateView(LoginRequiredMixin, UpdateView):
    model = Organization


class OrganizationDeleteView(LoginRequiredMixin, DeleteView):
    model = Organization
