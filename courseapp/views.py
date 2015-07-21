
# Create your views here.
from django_datatables_view.base_datatable_view import BaseDatatableView
from .models import Courses

class OrderListJson(BaseDatatableView):
    # The model we're going to show
    model = Courses

    # define the columns that will be returned
    columns = ['CRN', 'term', 'year', 'note', 'course', 'title', 'xlist', 'instructor', 'group', 'graduate_level',
               'year_long', 'subject', 'status', 'units', 'days', 'time', 'location', 'add_me']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['CRN', 'term', 'year', 'note', 'course', 'title', 'xlist', 'instructor', 'group',
                     'graduate_level', 'year_long', 'subject', 'status', 'units', 'days', 'time', 'location', 'add_me']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 50

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'user':
            return '{0} {1}'.format(row.customer_firstname, row.customer_lastname)
        else:
            return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)
            return qs
