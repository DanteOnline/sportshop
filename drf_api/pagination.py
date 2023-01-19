from rest_framework import pagination
from rest_framework.response import Response


class PageCountPaginator(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'title': 'Custom paginator',
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'page count': self.page.paginator.num_pages,
            'current page': self.page.number,
            'results': data
        })