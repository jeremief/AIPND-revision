#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Jeremie Faye
# DATE CREATED: 06/02/2020                              
# REVISED DATE: 06/02/2020  
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    dognames = open(dogfile)
    # print("dognames is {}".format(dognames))
    dogs_dic = {}
    for line in dognames:
        # dogs_list.append(1)
        # print("line is {}".format(line))
        line_list = line.split(",")
        for i in range(len(line_list)):
            line_item = line_list[i].lstrip().rstrip()
            if line_item not in dogs_dic:
                dogs_dic[line_item] = 1
            # else:
                # print("{} is already in the dictionary.".format(line_item))

    print("dogs_list is {}".format(dogs_dic))

    for key in results_dic:
        image_label = results_dic[key][0]
        classifier_label = results_dic[key][1]
        # print(image_label, classifier_label)
        #Set up image and classifier label flags 
        flags = [0,0]
        print("*************** Working on {} with image_label {} and classifier_label {}".format(key, image_label, classifier_label))
        results_dic[key].extend(flags)
        # for dog_description_string in dognames:
        # # for j in range(len(dognames)):
        #     dog_description_list = dog_description_string.lower().split(",")
        #     # dog_description_list = dognames[j].lower().split(",")
        #     print("dog_description_list is {}".format(dog_description_list))
        #     for i in range(len(dog_description_list)):
        #         text_label = dog_description_list[i].lstrip().rstrip()
        #         # print("image_label is {} and text_label is{}".format(image_label, text_label))

        #         if image_label == text_label:
        #             results_dic[key][3] = 1
        #         if text_label in classifier_label:
        #             results_dic[key][4] = 1

        # print("For {}, the result is {}".format(key, results_dic[key]))

        if image_label in dogs_dic:
            results_dic[key][3] = 1
        classifier_label_list = classifier_label.split(",")
        for classifier_label_item in classifier_label_list:
            classifier_label_item = classifier_label_item.lstrip().rstrip()
            if classifier_label_item in dogs_dic:
                results_dic[key][4] = 1

        print("For {}, the result is {}".format(key, results_dic[key]))

                # break
            # else:
                # print("is NOT a dog" + " " + dogname)

    None
