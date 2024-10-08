from django.contrib import admin
from django.urls import path
from qflapp import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('notice-board/', views.notice_board, name='notice-board'),
    path('add-notice/', views.add_notice, name='add-notice'),
    path('delete-notice/<int:notice_id>/', views.delete_notice, name='delete-notice'),
    path('edit-notice/<int:notice_id>/', views.edit_notice, name='edit-notice'),
    path('patron-board/', views.patron_board, name='patron-board'),
    path('add-patron/', views.add_patron, name='add-patron'),
    path('delete-patron/<int:patron_id>/', views.delete_patron, name='delete-patron'),
    path('edit-patron/<int:patron_id>/', views.edit_patron, name='edit-patron'),
    path('patrons-page/', views.patrons_page, name='patron-page'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('person-board/', views.person_board, name='person-board'),
    path('add-person/', views.add_person, name='add-person'),
    path('delete-person/<int:person_id>/', views.delete_person, name='delete-person'),
    path('edit-person/<int:person_id>/', views.edit_person, name='edit-person'),
    path('committeemember-board/', views.committeemember_board, name='committeemember-board'),
    path('add-committeemember/', views.add_committeemember, name='add-committeemember'),
    path('delete-committeemember/<int:committeemember_id>/', views.delete_committeemember, name='delete-committeemember'),
    path('edit-committeemember/<int:committeemember_id>/', views.edit_committeemember, name='edit-committeemember'),
    path('committeemembers-page/', views.committeemember_page, name='committeemember-page'),
    path('book-board/', views.book_board, name='book-board'),
    path('add-book/', views.add_book, name='add-book'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete-book'),
    path('edit-book/<int:book_id>/', views.edit_book, name='edit-book'),
    path('books-page/', views.books_page, name='book-page'),

]