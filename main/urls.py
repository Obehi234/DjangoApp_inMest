from django.urls import  path


from .views import*

urlpatterns = [
    path("say_hello/", say_hello),
    path("user_profile/",  user_profile),
    path("all_queries", all_queries),
    path("user_query/<int:query_id>/", user_query),
    path("queries/", QueryView.as_view(), name="query-view"),
]