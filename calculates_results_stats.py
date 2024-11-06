#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Maymoona A Bani Oudeh
# DATE CREATED: 6 Nov 2024                                        
# REVISED DATE: 
# PURPOSE: This script calculates the statistics of the program run results, 
#          based on the classifier's model architecture for classifying images.
#          The function calculates counts and percentages for various results
#          and stores them in a dictionary, `results_stats_dic`, for analysis.
#
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results using classifier's model to classify
    pet images, and returns a dictionary with result statistics.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int) where 1 = match between pet image and 
                            classifier labels, and 0 = no match between labels
                    idx 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int) where 1 = classifier classifies image 
                            'as-a' dog and 0 = classifier classifies image 
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains statistics with keys for 
                         counts (`n_*`) and percentages (`pct_*`).
    """        
    # Initialize statistics dictionary
    results_stats_dic = {
        'n_dogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0
    }
    
    # Process each item in results_dic
    for key in results_dic:
        # Count label matches
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        # Count correct breed classification for dog images
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1

        # Count dog images and correct dog classifications
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1

        # Count correct NOT-dog classifications
        elif results_dic[key][4] == 0:
            results_stats_dic['n_correct_notdogs'] += 1

    # Total number of images
    results_stats_dic['n_images'] = len(results_dic)
    # Number of non-dog images
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']

    # Calculate percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0

    return results_stats_dic
