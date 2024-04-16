

from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, key):
    """
    Decrypts the provided encrypted message using the provided key.
    Args:
        encrypted_message (bytes): The encrypted message to decrypt.
        key (bytes): The encryption key.

    Returns:
        str: The decrypted message.
    """
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message)
    return decrypted_message.decode()

# Example usage:
encrypted_message = b'gAAAAABlTNM6TGjW5Tsw2sZviokTYGpyIdV0Fet4EaopCXrk5DRnFGjYqqtVXfqx7h6OjBFeWNIkn0fvVnBETa3CkoZpR5NDLQ=='
key = b'BQrousuHvfUBm2r6pJ4Q7od6IwoTVyHhnvgOEX3myl8='

decrypted_message = decrypt_message(encrypted_message, key)

