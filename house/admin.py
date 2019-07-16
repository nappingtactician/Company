from django.contrib import admin
from .models import asset,work,worker,allocatework

admin.site.register(asset),
admin.site.register(worker),
admin.site.register(work),
admin.site.register(allocatework),


