from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.views import AddressList, AddressDetail, Healthz, Root
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import verify_jwt_token

schema_view = get_swagger_view(title='Reece Address Book API')
app_name = "api"
urlpatterns = {
    url(r'^address/$', AddressList.as_view(), name="addressList"),
    url(r'^address/(?P<pk>[0-9]+)/$', AddressDetail.as_view(), name="addressDetail"),
    url(r'^healthz$', Healthz.as_view(), name="healthz"),
    url(r'^docz$', schema_view, name="schema"),
    url(r'^$', Root.as_view(), name="root"),
    #url(r'^api-token-verify/', verify_jwt_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)
