from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView , CreateView_Zgloszenie
from .views import DetailsView

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^georest/$', CreateView_Zgloszenie.as_view(), name="create"),
    url(r'^georest/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)