import re

def validate_input(input_string, validation_type):
    """
    Validate input based on the specified validation type.

    :param input_string: The input string to validate
    :param validation_type: The type of validation ('email', 'bangladesh_mobile', 'usa_telephone', 'password')
    :return: Boolean indicating if the input is valid
    """
    patterns = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'bangladesh_mobile': r'^\+8801[3-9]\d{8}$',  # Format: +8801XXXXXXXXX
        'usa_telephone': r'^\+1[2-9]\d{2}[2-9]\d{6}$',  # Format: +1XXXYYYXXXX
        'password': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
    }

    pattern = patterns.get(validation_type)
    if pattern:
        return bool(re.match(pattern, input_string))
    else:
        raise ValueError("Invalid validation type provided.")

# Example usage
email = "example@gmail.com"
bangladesh_mobile = "+8801234567890"
usa_telephone = "+11234567890"
password = "Abcdefgh!2345678"

print("Email valid:", validate_input(email, 'email'))
print("Bangladesh Mobile valid:", validate_input(bangladesh_mobile, 'bangladesh_mobile'))
print("USA Telephone valid:", validate_input(usa_telephone, 'usa_telephone'))
print("Password valid:", validate_input(password, 'password'))
