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




from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO

def load_image( filename ) :
    '''
    Load an image file from disk
    @param: filename The file to load
    @return: the image object
    '''
   

    try:
        myimage = Image.open(filename)
        myimage.load()
        
    except:
        
        #if we get here, an excepttion has taken
        #eat the exception
        return None
    
    return myimage

def save_image( imageObject, outfilename ) :
    '''
    Save an image to disk
    @param imageObject The Image to save
    @param outfilename The target file
    @return: none
    '''
    try:
        imageObject.save( outfilename )
    except:
        return None
def crop_image(fileName):
    '''
    crop an image
    @param the file name containing the image to be cropped
    @return cropped image
    '''
    
    try:
        im = Image.open(fileName)
        im_c = im.crop((200,300,400,500)) # (left, top, right, bottom) it's a tuple!
        #im_c.show()
    except:
        return None
    return im_c #reutunr the cforp image to the calling function

