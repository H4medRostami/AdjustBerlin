from django.db.models import Sum
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import throttling
from rest_framework import permissions
from rest_framework import viewsets
from adjustHT.models import Dataset
from adjustHT.serializer import FilterSerializer,EntrySerializer
from django.db.models import FloatField, ExpressionWrapper, F


# Pagination class using for divide rendering 100 per page
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    # page_size_query_param = 'page_size'
    # max_page_size = 1000


class Filter(viewsets.ViewSet):
    """
    Fetch dynamic search result
    Authentication : (AllowAny)
    """
    pagination_class = StandardResultsSetPagination
    throttle_classes = [throttling.AnonRateThrottle]
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(query_serializer=EntrySerializer,)
    def list(self, request):
        params = self.request.query_params
        filter_args = {}
        date_from = params.get('date_from', None)
        date_to = params.get('date_to', None)
        channel = params.get('channel', None)
        country = params.get('country', None)
        os = params.get('os', None)
        sort_by = params.get('sort_by', None)
        group_by = params.get('group_by', None)
        # response all dataset records if parameters not declared
        queryset = Dataset.objects.all()
        queryset = queryset.annotate(CPI=ExpressionWrapper(F('spend') / F('installs'),
                                                           output_field=FloatField())).values()

        if country:
            filter_args.update({'country__iexact': country})
        if os:
            filter_args.update({'os__iexact': os})
        if channel:
            filter_args.update({'channel__iexact': channel})
        if date_from and date_to:
            filter_args.update({'date__range': [date_from, date_to]})
        if date_from and date_to is None:
            filter_args.update({'date__gte': date_from})
        if date_from is None and date_to:
            filter_args.update({'date__lte', date_to})

        queryset = queryset.filter(**filter_args)

        if group_by:
            group_by_arr = []

            if ',' in group_by:
                group_by_arr = group_by.split(',')
            else:
                group_by_arr.append(group_by)

            queryset = queryset.values(*group_by_arr).annotate(impressions=Sum('impressions')
                                                               , clicks=Sum('clicks'),
                                                               installs=Sum('installs')
                                                               , revenue=Sum('revenue')
                                                               , CPI=Sum('CPI')
                                                               , spend=Sum('spend')
                                                               )
        if sort_by:
            queryset = queryset.order_by(sort_by)

        serializer = FilterSerializer(queryset, read_only=True, many=True)
        return Response(serializer.data)

