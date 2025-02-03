from django.urls import path
from .views import ActionListCreateView, ActionRetrieveUpdateDeleteView
from .views import save_and_return_actions

urlpatterns = [
    path('actions/', ActionListCreateView.as_view(), name='action-list-create'),
    path('actions/<int:pk>/', ActionRetrieveUpdateDeleteView.as_view(), name='action-detail'),
]

urlpatterns += [
    path('actions/json/', save_and_return_actions, name='save-and-return-actions'),
]