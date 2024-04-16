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