from django.conf.urls import url
from voterapp import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'register/',views.register,name='register'),
    url(r'^login/',views.login_user,name='login'),
    url(r'^logout/',views.logout_user,name='logout'),
    url(r'^add-new/',views.add_new_voter,name='add-new-voter'),
    url(r'^(?P<pk>[0-9]+)/vote/',views.vote_detail,name='vote-detail'),
    url(r'^voter_one/(?P<pk>[0-9]+)/',views.increment_voter_one,name='increment_voter_one'),
    url(r'^voter_two/(?P<pk>[0-9]+)/',views.increment_voter_two,name='increment_voter_two'),
    url(r'^my_voters/',views.my_voters,name='my-voters'),
]
