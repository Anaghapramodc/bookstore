

from django.urls import path

from .import views
from .views import booklist, bookcreate, bookview, BoookCheckoutView, PaymentComplete, SearchResultsView, \
    cart, add_to_cart, remove_from_cart, contact, bookDelete

urlpatterns = [
    path('index', views.index, name='index'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('home', views.home, name='home'),
    path('', booklist.as_view(), name='booklist'),
    path('gallary', booklist.as_view(), name='gallary'),
    path('book_create/', bookcreate.as_view(), name='book-create'),
    path('delete/<int:pk>/', bookDelete.as_view(), name='task-delete'),
    path('book_view/<int:pk>/', bookview.as_view(), name='book-view'),
    path('book_checkout/<int:pk>/', BoookCheckoutView.as_view(), name='book-checkout'),
    path('complete/', PaymentComplete, name = 'complete' ),
    path('cart/',cart,name = 'mycart'),
    path('cart/add/<int:book_id>/',add_to_cart,name="add_to_cart"),
    path('cart/remove/<int:book_id>/', remove_from_cart, name="remove_from_cart"),
    path('contact_us/', contact.as_view(), name='contact-us'),
    path('review', views.review, name='review'),
]
