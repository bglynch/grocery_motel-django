from django.urls import path
import checkout.views as view


urlpatterns = [
    # path('url_pattern', view.view_name, name='url_name'),
    path('', view.sample_view, name='sample'),
    ]
