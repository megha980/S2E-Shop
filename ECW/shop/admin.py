from django.contrib import admin
from .models import Contact

from .models import Orders,OrderUpdate

# Register your models here.
from .models import Product

admin.site.register(Product)

admin.site.register(Contact)


admin.site.register(Orders)
admin.site.register(OrderUpdate)