from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

from rest_framework.response import Response

class LargePageNumberPagination(PageNumberPagination):
    page_size=5
    page_size_query_param='page_size'
    max_page_size=100

class LargeLimitOffsetPagination(LimitOffsetPagination):
    default_limit=2
    max_limit=3

class PostCursorPagination(CursorPagination):
    page_size=5
    ordering='-created'

class CustomPagination(PageNumberPagination):
    page_size=3
    def get_paginated_response(self, data):
        return Response(
            {
                'links':{'next':self.get_next_link(),'prev':self.get_previous_link()},
                'total':self.page.paginator.count,
                'posts':data
            }
        )