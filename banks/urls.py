from django.contrib.auth.decorators import login_required
from django.urls import path

from banks.views import AddBank, BankIdDetails, AddBranch, BranchIdDetails, AllBanks, EditBranch

urlpatterns = [
    path('add/', AddBank.as_view()),
    path('<str:bank_id>/details/', BankIdDetails.as_view()),
    path('<str:bank_id>/branches/add/', AddBranch.as_view()),
    path('branch/<str:branch_id>/details/', BranchIdDetails.as_view()),
    path('all/', AllBanks.as_view()),
    path('branch/<str:branch_id>/edit/', EditBranch.as_view()),

]
