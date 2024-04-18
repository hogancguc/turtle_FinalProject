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


#locationFunction.py


def load_english_words(file_path):

   '''
   Load English words from the given file.
    Returns:
        list: A list of English words loaded from the file.
   '''

   

   with open(file_path, "r") as english_file:

       return [word.strip() for word in english_file]



def decrypt_location(indices, english_words):

   '''
   Decrypt the location using the provided indices and English words.
    Returns:
        str: The decrypted location as a string.
   
   '''

   

   decrypted_location = " ".join(english_words[int(index)] for index in indices)

   return decrypted_location

