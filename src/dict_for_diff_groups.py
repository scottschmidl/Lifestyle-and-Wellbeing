#this function was used to get the males/females/age ranges into dictionaries.
#it is no longer being used for the sake of condensed code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from random import sample
import numpy as np
import scipy.stats as stats

def group_to_dic_gender(gender):

    '''
    returns dictionary with group as the key and a subset of the
    balance score list as the value

    gender - string, either Male or Female
    '''

    male_dict = {}
    female_dict = {}

    if gender == 'Male':

        for m in mal_bal.iloc[:, 22:24]:
            male_dict[m] = male_balacc_list
            return mal_dict

    else:

        for f in femal_bal.iloc[:, 22:24]:
            female_dict[f] = female_balacc_list
            return femal_dict

def group_to_dic_age(age):

    '''
    returns dictionary with group as the key and a subset of the
    balance score list as the value

        age - string
    '''

    dict_20 = {}
    dict_21 = {}
    dict_36 = {}
    dict_51 = {}

    if age == '20 or less':
        for a in bal_20.iloc[0:, 0:1]:
            dict_20[a] = balacc_list_20
            return dict_20

    elif age == '21 to 35':
        for a in bal_21.iloc[0:, 0:1]:
            dict_21[a] = balacc_list_21
            return dict_21

    elif age == '36 to 50':
        for a in bal_36.iloc[0:, 0:1]:
            dict_36[a] = balacc_list_36
            return dict_36

    else:
        for a in bal_51.iloc[0:, 0:1]:
            dict_51[a] = balacc_list_51
            return dict_51

def main():

    lst_ages = ['20 or less', '21 to 35', '36 to 50', '51 or more']
    lst_gender = ['Male', 'Female']

    dic_male = group_to_dic_gender(lst_gender[0])
    dic_female = group_to_dic_gender(lst_gender[1])

    dic_20 = group_to_dic_age(lst_ages[0])
    dic_21 = group_to_dic_age(lst_ages[1])
    dic_36 = group_to_dic_age(lst_ages[2])
    dic_51 = group_to_dic_age(lst_ages[3])

    all_dict = {'dic_male':dic_male, 'dic_femaile':dic_female,'dict_20': dic_20, 'dict_21': dic_21, 'dict_36':dic_36, 'dict_51':dic_51}

    return all_dict

if __name__ == '__main__':
    main()
