#might place mean, std, and norm data here
from well_life_main import *

def get_means(lst):

    '''returns means of whole/sample balance scores'''

    return np.mean(lst)

def get_standard_deviations(lst):

    '''returns standard deviation of whole/sample balance scores'''

    return np.std(lst)

def norm_dist(mean, std):
    return stats.norm(loc=mean,scale=std)

def get_norm_coef(): #needs attention
    mean_male_bal = get_means(sort_males)
    sqrt_m = np.sqrt(len(sort_males))
    std = std_male_bal/sqrt_m
    return mean_male_bal, std

a, b = get_norm_coef()
norm_males = norm_dist(a, b)
x2 = np.linspace(a-6*b,a*b,500)
t_test = stats.ttest_ind(sort_males, equal_var=False)

# Distribution of means plots
fig, ax = plt.subplots(figsize=(12,8))
x = np.linspace(2600,3600,2000)
ax.plot(x,norm_males.pdf(x),color= '#4586AC',label='29')

mean_male_bal = get_means(sort_males)
mean_female_bal = get_means(sort_females)

mean_20_bal = get_means(sort_20)
mean_21_bal = get_means(sort_21)
mean_36_bal = get_means(sort_36)
mean_51_bal = get_means(sort_51)

mean_20m_bal = get_means(sort_male_20)
mean_21m_bal = get_means(sort_male_21)
mean_35m_bal = get_means(sort_male_20)
mean_51m_bal = get_means(sort_male_20)

mean_20f_bal = get_means(sort_female_20)
mean_21f_bal = get_means(sort_female_21)
mean_35f_bal = get_means(sort_female_20)
mean_51f_bal = get_means(sort_female_20)

std_male_bal = get_standard_deviations(sort_males)
std_female_bal = get_standard_deviations(sort_females)

std_20_bal = get_standard_deviations(sort_20)
std_21_bal = get_standard_deviations(sort_21)
std_36_bal = get_standard_deviations(sort_36)
std_51_bal = get_standard_deviations(sort_51)

std_20m_bal = get_standard_deviations(sort_male_20)
std_21m_bal = get_standard_deviations(sort_male_21)
std_35m_bal = get_standard_deviations(sort_male_36)
std_51m_bal = get_standard_deviations(sort_male_51)

std_20f_bal = get_standard_deviations(sort_female_20)
std_21f_bal = get_standard_deviations(sort_female_21)
std_35f_bal = get_standard_deviations(sort_female_36)
std_51f_bal = get_standard_deviations(sort_female_51)

norm_dist_m = norm_dist(mean_male_bal, std_male_bal)
