#locationFunction.py


def load_english_words(file_path):

   """Load English words from the given file."""

   

   with open(file_path, "r") as english_file:

       return [word.strip() for word in english_file]



def decrypt_location(indices, english_words):

   """Decrypt the location using the provided indices and English words."""

   

   decrypted_location = " ".join(english_words[int(index)] for index in indices)

   return decrypted_location

