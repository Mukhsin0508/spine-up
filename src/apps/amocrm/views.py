from rest_framework.generics import GenericAPIView
from .serializers import ClientDataSerializer
from amocrm.v2 import Lead, tokens
from rest_framework import status
from rest_framework.response import Response
import os

class ClientDataAPIView(GenericAPIView):
    """
    This view is used to send leads to the amocrm
    """
    permission_classes = ()
    authentication_classes = ()
    serializer_class = ClientDataSerializer

    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    SUBDOMAIN = os.getenv("SUBDOMAIN")
    REDIRECT_URI = os.getenv("REDIRECT_URI")
    AUTH_CODE = os.getenv("AUTH_CODE")

    tokens.default_token_manager(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        subdomain=SUBDOMAIN,
        redirect_url=REDIRECT_URI,
        storage=tokens.FileTokensStorage()
    )
    tokens.default_token_manager.init(code=AUTH_CODE, skip_error=True)

    def post(self, request) -> Response:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data

            lead_data = (f"Имя:{validated_data['name']} \n"
                         f"Номер_телефона:{validated_data['phone']} \n"
                         f"Услуга:{validated_data['service']} \n"
                         f" Платформа:{validated_data['platform']}")
            lead = Lead.objects.create ( name = lead_data )

            return Response("Success", status = status.HTTP_200_OK)
        else:
            return Response("Failed", status = status.HTTP_500_INTERNAL_SERVER_ERROR)