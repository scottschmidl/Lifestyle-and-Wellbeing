#might place mean, std, and norm data here
import life_well_main
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from random import sample

def get_means(lst):
    '''returns means of whole/sample balance scores'''

    return np.mean(lst)

##GET THE MEAN BALANCE SCORES FOR MALE AND FEMALE,
#MALE AND FEMALE BY AGE, AND AGE
def mean_malefemale_bal(sorted_gender):

    for g in sorted_gender:
        if g == sort_males: mean_male_bal = get_means(g).round(2)
        else: mean_female_bal = get_means(g).round(2)

    return mean_male_bal, mean_female_bal

def mean_age_bal(sorted_age):

    for a in sorted_age:

        if a == sort_20: mean_20_bal = get_means(a).round(2)
        elif a == sort_21: mean_21_bal = get_means(a).round(2)
        elif a == sort_36: mean_36_bal = get_means(a).round(2)
        else: mean_51_bal = get_means(a).round(2)

    return mean_20_bal, mean_21_bal, mean_36_bal, mean_51_bal

def mean_MF_age_bal(sorted_ga):

    for ga in sorted_ga:

        if ga == sort_male_20: mean_20m_bal = get_means(ga).round(2)
        elif ga == sort_male_21: mean_21m_bal = get_means(sort_male_21).round(2)
        elif ga == sort_male_36: mean_36m_bal = get_means(sort_male_36).round(2)
        elif ga == sort_male_51: mean_51m_bal = get_means(sort_male_51).round(2)
        elif ga == sort_female_20: mean_20f_bal = get_means(sort_female_20).round(2)
        elif ga == sort_female_21: mean_21f_bal = get_means(sort_female_21).round(2)
        elif ga == sort_female_36: mean_36f_bal = get_means(sort_female_36).round(2)
        else: mean_51f_bal = get_means(sort_female_51).round(2)

    return mean_20m_bal, mean_21m_bal, mean_36m_bal, mean_51m_bal, mean_20f_bal, mean_21f_bal, mean_36f_bal, mean_51f_bal

# def get_standard_deviations(lst):

#     '''returns standard deviation of whole/sample balance scores'''

#     return np.std(lst)

# def norm_dist(mean, std):
#     return stats.norm(loc=mean,scale=std)

# def get_norm_coef(): #needs attention
#     mean_male_bal = get_means(sort_males)
#     sqrt_m = np.sqrt(len(sort_males))
#     std = std_male_bal/sqrt_m
#     return mean_male_bal, std

# def main():
#     a, b = get_norm_coef()
#     norm_males = norm_dist(a, b)
#     x2 = np.linspace(a-6*b,a*b,500)
#     t_test = stats.ttest_ind(sort_males, equal_var=False)

#     # Distribution of means plots
#     fig, ax = plt.subplots(figsize=(12,8))
#     x = np.linspace(2600,3600,2000)
#     ax.plot(x,norm_males.pdf(x),color= '#4586AC',label='29')

    # #MEANS
    # mmfb = mean_malefemale_bal(sort_mf)
    # mag = mean_age_bal(sort_age)
    # mmfab = mean_MF_age_bal(sort_mf_age)

#     std_male_bal = get_standard_deviations(sort_males)
#     std_female_bal = get_standard_deviations(sort_females)

#     std_20_bal = get_standard_deviations(sort_20)
#     std_21_bal = get_standard_deviations(sort_21)
#     std_36_bal = get_standard_deviations(sort_36)
#     std_51_bal = get_standard_deviations(sort_51)

#     std_20m_bal = get_standard_deviations(sort_male_20)
#     std_21m_bal = get_standard_deviations(sort_male_21)
#     std_35m_bal = get_standard_deviations(sort_male_36)
#     std_51m_bal = get_standard_deviations(sort_male_51)

#     std_20f_bal = get_standard_deviations(sort_female_20)
#     std_21f_bal = get_standard_deviations(sort_female_21)
#     std_35f_bal = get_standard_deviations(sort_female_36)
#     std_51f_bal = get_standard_deviations(sort_female_51)

#     norm_dist_m = norm_dist(mean_male_bal, std_male_bal)

if __name__ == '__main__':
    main()
