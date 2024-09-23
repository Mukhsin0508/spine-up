from rest_framework.exceptions import  ValidationError

def phone_validate(phone_number: str) -> None:
    if len(phone_number) !=13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('Invalid phone number format. Please enter a phone number in the format +998XXXXXXXXX')
