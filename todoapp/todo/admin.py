from django.contrib import admin
from .models import Todo
from rest_framework.pagination import PageNumberPagination


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'text', 'create_date', 'update_date')
    list_display_links = ('id','create_date')
    search_fields = ('id', 'email', 'text','create_date', 'update_date')
    list_editable = ('email',)
    list_filter = ('id',)


admin.site.register(Todo, TodoAdmin)


class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
