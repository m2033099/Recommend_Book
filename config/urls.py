from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # 上のaccountsから探して、なかったらしたのaccountsから探す
    path('accounts/', include('accounts.urls')),
    # urlが何もない時に、Home画面に移動させる。
    path('', RedirectView.as_view(url='book/')),
    path('book/', include('book.urls')),
]
