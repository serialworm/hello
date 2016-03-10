from django.contrib import admin
from registration.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'address1', 'address2', 'city', 'state',
        'zipcode', 'date'
    )

    def get_queryset(self, request):
        return User.objects.all().order_by('-date')

admin.site.register(User, UserAdmin)
