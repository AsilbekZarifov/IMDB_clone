from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchList(PageNumberPagination):

    page_size = 2
    last_page_strings = 'end'


class WatchListLOPagination(LimitOffsetPagination):
    default_limit =4

class WatchListCPagination(CursorPagination):
    page_size =1