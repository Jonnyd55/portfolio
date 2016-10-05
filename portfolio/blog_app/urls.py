from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(portfolio_app.urls)),
    url(r'^blog/', include(blog_app.urls)),
]
