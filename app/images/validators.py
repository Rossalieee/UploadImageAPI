from django.core.exceptions import ValidationError


def validate_expiration_time(value):
    min_exp_time = 300
    max_exp_time = 30000

    if value < min_exp_time or value > max_exp_time:
        raise ValidationError('Expiration time must be between 300 and 30,000 seconds.')
