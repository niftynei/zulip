from django.conf.urls import url, include
from zerver.lib.rest import rest_dispatch
import zilencer.views

i18n_urlpatterns = [
    # SSO dispatch page for desktop app with SSO
    # Allows the user to enter their email address only,
    # and then redirects the user to the proper deployment
    # SSO-login page
    url(r'^accounts/deployment_dispatch$',
        zilencer.views.account_deployment_dispatch,
        {'template_name': 'zerver/login.html'},
        name='zilencer.views.account_deployment_dispatch',)
]

# Zilencer views following the REST API style
v1_api_and_json_patterns = [
    url('^deployment/feedback$', rest_dispatch,
        {'POST': 'zilencer.views.submit_feedback'}),
    url('^deployment/report_error$', rest_dispatch,
        {'POST': 'zilencer.views.report_error'}),
    url('^deployment/endpoints$', zilencer.views.lookup_endpoints_for_user,
        name='zilencer.views.lookup_endpoints_for_user'),
    url('^remotes/push/register$', rest_dispatch,
          {'POST': 'zilencer.views.remote_server_register_push'}),
    url('^remotes/push/unregister$', rest_dispatch,
          {'POST': 'zilencer.views.remote_server_unregister_push'}),
    url('^remotes/push/message$', rest_dispatch,
          {'POST': 'zilencer.views.remote_server_push_message'}),
    url('^remotes/update$', rest_dispatch,
          {'POST': 'zilencer.views.update_remote_server'}),
]

urlpatterns = [
    url(r'^api/v1/', include(v1_api_and_json_patterns)),
    url(r'^json/', include(v1_api_and_json_patterns)),
] + i18n_urlpatterns
