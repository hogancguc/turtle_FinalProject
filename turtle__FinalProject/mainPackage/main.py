# Name:Chase McClure
# email:mcclurc2@mail.uc.edu
# Assignment Number: Assignment Final Project
# Due Date: April 23
# Course/Section: ADV APP DEV (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: 
# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this.
# Citations: canvas slides
# Anything else that's relevant: as of right now filing this out none


from locationPackage.locationFunciton import *
from moviePackage.movieFunction import *
from imageArchivePackage.imageArchive import *

# Example usage:
if __name__ == "__main__":
    # Load English words from UCEnglish.txt (adjust the file path accordingly)
    english_words = load_english_words("UCEnglish.txt")

    # Provided indices for "Turtle"
    indices = ["38905", "22147", "42061", "103568", "6643", "46342", "42133", "1430",
               "37192", "6636", "28420", "9465", "2756", "41688"]

    # Decrypt the location
    decrypted_location = decrypt_location(indices, english_words)
    print(f"Decrypted location: {decrypted_location}")
    
    print(decrypted_message)
    
    
    my_image = load_image("../imageArchivePackage/UCTurtleProject.jpg")
    my_image.show(my_image)