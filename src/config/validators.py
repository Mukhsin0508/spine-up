from rest_framework.exceptions import ValidationError
import magic
import subprocess



def phone_validate(phone_number: str) -> None:
    """Validator for checking phone number format."""
    if len(phone_number) != 13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('Invalid phone number format. Please enter a phone number in the format +998XXXXXXXXX')


def validate_file_type(file):
    """Validator for checking allowed file types."""
    file_type = magic.from_buffer(file.read(1024), mime=True)
    file.seek(0)  # Reset file pointer after reading

    allowed_mime_types = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ]

    if file_type not in allowed_mime_types:
        raise ValidationError('Unsupported file type. Allowed types are: PDF, DOC, DOCX.')


def validate_file_size(file):
    """Validator for checking file size (max 5MB)."""
    max_size_mb = 5  # Set max size to 5 MB
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"File size should not exceed {max_size_mb} MB.")


def scan_file_for_viruses(file_path):
    """Run a virus scan using ClamAV."""
    result = subprocess.run(['clamscan', file_path], stdout=subprocess.PIPE)
    if 'Infected files: 0' not in result.stdout.decode('utf-8'):
        raise ValidationError('Virus detected in the uploaded file.')


import magic
from PIL import Image
from io import BytesIO


def validate_staff_image(file):
    """Validator for checking staff image."""
    file.seek(0)
    file_extension = magic.from_buffer(file.read(1024), mime=True)

    # Check if the file is an image
    if not file_extension.startswith('image/'):
        raise ValueError("File must be an image.")

    # Reset file pointer and open image
    # file.seek(0)
    # img = Image.open(BytesIO(file.read()))

    # Check dimensions
    # width, height = img.size
    # if width != 333 or height != 344:
    #     raise ValueError(f"Staff image must be 333x344 pixels. Got {width}x{height}.")

    # Check file format (assuming JPEG or PNG are acceptable)
    if file_extension not in ['image/jpeg', 'image/png']:
        raise ValueError("Изображение персонала должно быть в формате JPEG или PNG.")

    return True


def validate_product_image(file):
    """Validator for checking product image."""
    file.seek(0)
    file_extension = magic.from_buffer(file.read(1024), mime=True)

    # Check if the file is an image
    if not file_extension.startswith('image/'):
        raise ValueError("File must be an image.")

    # Reset file pointer and open image
    # file.seek(0)
    # img = Image.open(BytesIO(file.read()))

    # Check dimensions
    # width, height = img.size
    # if width != 393 or height != 280:
    #     raise ValueError(f"Product image must be 393x280 pixels. Got {width}x{height}.")

    # Check file format (assuming JPEG or PNG are acceptable)
    if file_extension not in ['image/jpeg', 'image/png']:
        raise ValueError("Изображение товара должно быть в формате JPEG или PNG.")

    return True