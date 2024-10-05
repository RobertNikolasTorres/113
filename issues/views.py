from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)
from .models import Issue, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)

class IssueListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Issue

class IssueDetailView(LoginRequiredMixin, DetailView):
    template_name = "issues/detail.html"
    model = Issue

class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = [
        "name", "summary", "description",
        "assignee", "status"
    ]

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class IssueUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = [
        "name", "summary", "description",
        "assignee", "status"
    ]

class IssueDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("list")