#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Maymoona A Bani Oudeh
# DATE CREATED: 6 Nov 2024                             
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
    
    
"""
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
"""
   # Imports necessary module
from os import listdir

def get_pet_labels(image_dir):
    """
    Generates a dictionary (results_dic) with filenames as keys and the pet label
    (extracted from the filename) as the associated value. Pet labels are derived
    from filenames by stripping numbers and converting to lowercase, ensuring they
    represent the pet's breed/type.

    Parameters:
     image_dir - The directory containing pet images (string)
    
    Returns:
      results_dic - Dictionary with:
                    Key   : image filename (string)
                    Value : List containing pet image label (string)
    """
    # List all files in the given directory
    in_files = listdir(image_dir)
    
    # Initialize an empty dictionary to hold results
    results_dic = {}

    # Process each file to extract and format pet labels
    for filename in in_files:
        # Skip any files that are hidden (start with ".")
        if filename[0] != ".":
            # Split filename into words, excluding file extensions
            pet_label_parts = filename.lower().split("_")
            
            # Filter and join only alphabetic parts to form pet label
            pet_label = " ".join([word for word in pet_label_parts if word.isalpha()]).strip()

            # Check if filename is already in dictionary to avoid duplicates
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
            else:
                print(f"** Warning: Duplicate file found: {filename}")

    # Return the completed dictionary with pet labels
    return results_dic