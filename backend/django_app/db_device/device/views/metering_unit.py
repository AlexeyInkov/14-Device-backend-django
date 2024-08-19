from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from device.models import MeteringUnit


class MeteringUnitListView(LoginRequiredMixin, ListView):
    model = MeteringUnit

    def get_queryset(self):
        cur_user = self.request.user

        if cur_user.is_staff:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(
                Q(consumer__user=cur_user.pk)
                | Q(service_organization__user=cur_user.pk)
            )


class MeteringUnitCreateView(LoginRequiredMixin, CreateView):
    model = MeteringUnit


class MeteringUnitDetailView(LoginRequiredMixin, DetailView):
    model = MeteringUnit


class MeteringUnitUpdateView(LoginRequiredMixin, UpdateView):
    model = MeteringUnit


class MeteringUnitDeleteView(LoginRequiredMixin, DeleteView):
    model = MeteringUnit
