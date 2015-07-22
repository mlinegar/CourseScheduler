
# just some basic examples
from django_datatables_view.base_datatable_view import BaseDatatableView

from .models import Courses, Courses_location

class DumbTable(BaseDatatableView):
    model = Courses

class SlightlyBetterTable(BaseDatatableView):
    model = Courses
    datatable_options = {
        'columns': [
            'CRN',
            ("Course", 'course'),
            'title',
            ("Instructor", 'instructor'),
            'group',
        ]
    }

class GettingCloserTable(BaseDatatableView):
    model = Courses_location
    datatable_options = {
        'columns': [
            ("CRN", 'Courses__CRN'),
            ("Course", 'Courses__course'),
            ("Title", 'Courses__title'),
            ("Instructor", 'Courses__instructor'),
            ("Group", 'Courses__group'),
            'total_time',
            'location',
        ],
    }

