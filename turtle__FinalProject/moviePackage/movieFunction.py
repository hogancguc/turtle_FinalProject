# Name:Chase McClure, Cameron Hogan, RIley Kinkade
# email:mcclurc2@mail.uc.edu
# Assignment Number: Assignment Final Project
# Due Date: April 23
# Course/Section: ADV APP DEV (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: it decrypts messages to allow us to find the secret places to finish the project
# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this. this module will decrypt two things it will find the location and decrypt the movies. it will then produce a picture that we took 
# Citations: canvas slides AI
# Anything else that's relevant: as of right now filing this out none


from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, key):
    '''
    Decrypts the provided encrypted message using the provided key.
    Args:
        encrypted_message (bytes): The encrypted message to decrypt.
        key (bytes): The encryption key.

    Returns:
        str: The decrypted message.
    '''
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    return decrypted_message.decode()

# Example usage:
encrypted_message = b'gAAAAABlTNM6TGjW5Tsw2sZviokTYGpyIdV0Fet4EaopCXrk5DRnFGjYqqtVXfqx7h6OjBFeWNIkn0fvVnBETa3CkoZpR5NDLQ=='
key = b'BQrousuHvfUBm2r6pJ4Q7od6IwoTVyHhnvgOEX3myl8='

decrypted_message = decrypt_message(encrypted_message, key)


