from rest_framework import serializers
from .models import ClientData

class ClientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientData
        fields = '__all__'

    # def send_error_to_ai(self, error):
    #     """
    #     Send error to AI for analysis.
    #     @param error:
    #     @return:
    #     """
    #     url = "https://ai.example.com/error"
    #     payload = {"error": error}
    #     headers = {"Content-Type": "application/json"}
    #     response = requests.post(url, json=payload, headers=headers)
    #     return response.status_code