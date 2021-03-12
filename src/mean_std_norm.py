#might place mean, std, and norm data here
from life_well_main import clean_sort
import scipy.stats as stats
from random import sample
import numpy as np


def get_means(lst):

    '''
    returns means of whole/sample balance scores
    '''

    return np.mean(lst)

##GET THE MEAN OF THE BALANCE SCORES
def mean_malefemale_bal(sorted_gender):

    sort_males, sort_females = sorted_gender

    mean_male_bal = get_means(sort_males).round(2)
    mean_female_bal = get_means(sort_females).round(2)

    return mean_male_bal, mean_female_bal

def mean_age_bal(sorted_age):

    sort_20, sort_21, sort_36, sort_51 = sorted_age

    mean_20_bal = get_means(sort_20).round(2)
    mean_21_bal = get_means(sort_21).round(2)
    mean_36_bal = get_means(sort_36).round(2)
    mean_51_bal = get_means(sort_51).round(2)

    return mean_20_bal, mean_21_bal, mean_36_bal, mean_51_bal

def mean_MF_age_bal(sorted_ga):

    sort_male_20, sort_male_21, sort_male_36, sort_male_51, sort_female_20, sort_female_21, sort_female_36, sort_female_51 = sorted_ga

    mean_20m_bal = get_means(sort_male_20).round(2)
    mean_21m_bal = get_means(sort_male_21).round(2)
    mean_36m_bal = get_means(sort_male_36).round(2)
    mean_51m_bal = get_means(sort_male_51).round(2)
    mean_20f_bal = get_means(sort_female_20).round(2)
    mean_21f_bal = get_means(sort_female_21).round(2)
    mean_36f_bal = get_means(sort_female_36).round(2)
    mean_51f_bal = get_means(sort_female_51).round(2)

    return mean_20m_bal, mean_21m_bal, mean_36m_bal, mean_51m_bal, mean_20f_bal, mean_21f_bal, mean_36f_bal, mean_51f_bal

##GET THE STANDARD DEVIATIONS OF THE BALANCE SCORES
def get_standard_deviations(lst):

    '''
    returns standard deviation of whole/sample balance scores
    '''

    return np.std(lst)

def std_malefemale_bal(sorted_gender):

    sort_males, sort_females = sorted_gender

    std_male_bal = get_standard_deviations(sort_males)
    std_female_bal = get_standard_deviations(sort_females)

    return std_male_bal, std_female_bal

def std_age_bal(sorted_age):

    sort_20, sort_21, sort_36, sort_51 = sorted_age

    std_20_bal = get_standard_deviations(sort_20)
    std_21_bal = get_standard_deviations(sort_21)
    std_36_bal = get_standard_deviations(sort_36)
    std_51_bal = get_standard_deviations(sort_51)

    return std_20_bal, std_21_bal, std_36_bal, std_51_bal

def std_MF_age_bal(sorted_ga):

    sort_male_20, sort_male_21, sort_male_36, sort_male_51, sort_female_20, sort_female_21, sort_female_36, sort_female_51 = sorted_ga

    std_20m_bal = get_standard_deviations(sort_male_20)
    std_21m_bal = get_standard_deviations(sort_male_21)
    std_36m_bal = get_standard_deviations(sort_male_36)
    std_51m_bal = get_standard_deviations(sort_male_51)
    std_20f_bal = get_standard_deviations(sort_female_20)
    std_21f_bal = get_standard_deviations(sort_female_21)
    std_36f_bal = get_standard_deviations(sort_female_36)
    std_51f_bal = get_standard_deviations(sort_female_51)

    return std_20m_bal, std_21m_bal, std_36m_bal, std_51m_bal, std_20f_bal, std_21f_bal, std_36f_bal, std_51f_bal

def main():

    sort_mf_age, sort_mf, sort_age = clean_sort()

    ##MEANS
    mmfab = mean_MF_age_bal(sort_mf_age)
    print(mmfab)

    mmfb = mean_malefemale_bal(sort_mf)
    print(mmfb)

    mag = mean_age_bal(sort_age)
    print(mag)

    ##STD
    stdmfab = std_MF_age_bal(sort_mf_age)
    print(stdmfab)

    stdmfb = std_malefemale_bal(sort_mf)
    print(stdmfb)

    stdmag = std_age_bal(sort_age)
    print(stdmag)

if __name__ == '__main__':
    main()




# def norm_dist(mean, std):
#     return stats.norm(loc=mean,scale=std)

# def get_norm_coef(): #needs attention
#     mean_male_bal = get_means(sort_males)
#     sqrt_m = np.sqrt(len(sort_males))
#     std = std_male_bal/sqrt_m
#     return mean_male_bal, std

#     norm_males = norm_dist(a, b)
#     a, b = get_norm_coef()
#     x2 = np.linspace(a-6*b,a*b,500)
#     t_test = stats.ttest_ind(sort_males, equal_var=False)

#     # Distribution of means plots
#     fig, ax = plt.subplots(figsize=(12,8))
#     x = np.linspace(2600,3600,2000)
#     ax.plot(x,norm_males.pdf(x),color= '#4586AC',label='29')

#     norm_dist_m = norm_dist(mean_male_bal, std_male_bal)

