# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
#
# from departments.models import Department
#
#
# # Create your views here.
# def home_page(request: HttpRequest) -> HttpResponse:
#     total_departments_count = Department.objects.count()
#     latest_book = Book.objects.order_by('-publishing_date').first()
#
#     context = {
#         'total_books_count': total_books_count,
#         'latest_book': latest_book,
#         'page_title': 'Home'
#     }
#
#     return render(request, 'books/landing_page.html', context)
