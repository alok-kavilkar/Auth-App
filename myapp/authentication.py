from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from keycloak import KeycloakOpenID
import requests
from django.contrib.auth.models import User


class KeycloakAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None
        
        token = auth_header.split('Bearer ')[-1]
        if not token:
            raise AuthenticationFailed('Token is missing')
        
        # Keycloak settings
        keycloak_server_url = "http://localhost:8081"  # base URL for Keycloak
        keycloak_realm = "my-realm"
        keycloak_client_id = "django-app"
        keycloak_client_secret = "cVsaiEsyncBzRTxs4XV4B31KdM9X810I"

        keycloak_openid = KeycloakOpenID(server_url=keycloak_server_url,client_id=keycloak_client_id,realm_name=keycloak_realm,client_secret_key=keycloak_client_secret,verify=True)

        try:
            token_info = keycloak_openid.introspect(token)
            if not token_info.get('active'):
                raise AuthenticationFailed('Token is invalid or expired')

            user_id = token_info.get('sub')
            username = token_info.get('preferred_username')
            user, created = User.objects.get_or_create(username=username)
            print(user)
            return (user, token_info)

        except Exception as e:
            raise AuthenticationFailed(f'Authentication failed: {str(e)}')

        return None
