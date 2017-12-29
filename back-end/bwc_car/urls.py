from django.conf.urls import patterns, include, url
import xadmin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'bwc_car.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(xadmin.site.urls), name='xadmin'),
                       url(r'^', include('accounts.urls', namespace='account')),
                       url(r'^car_manage/', include('car_manage.urls', namespace='car_manage')),
                       )
