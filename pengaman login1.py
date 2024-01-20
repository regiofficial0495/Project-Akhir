import base64
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def generate_captcha():
    # Generate random string
    random_string = generate_random_string(20)

    # Pseudo Random Number Generator (PRNG)
    random.seed(42)  # Seed for reproducibility, you may change it
    random_numbers = [random.randint(0, 255) for _ in range(len(random_string))]

    # XOR each character with corresponding random number
    encrypted_string = ''.join([chr(ord(char) ^ rand_num) for char, rand_num in zip(random_string, random_numbers)])

    # Encoding using Base64
    encoded_string = base64.b64encode(encrypted_string.encode()).decode()

    # Truncate to the first 10 characters from the left
    captcha = encoded_string[:10]

    return captcha

# Example usage
captcha_result = generate_captcha()
print("CAPTCHA:", captcha_result)
