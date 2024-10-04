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
