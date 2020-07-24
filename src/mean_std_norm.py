#might place mean, std, and norm data here
#import well_life_cs1

# def get_means(lst):

#     '''returns means of whole/sample balance scores'''

#     return np.mean(lst)

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

# a, b = get_norm_coef()
# norm_males = norm_dist(a, b)
# x2 = np.linspace(a-6*b,a*b,500)
# t_test = stats.ttest_ind(sort_males, equal_var=False)

# # Distribution of means plots
# fig, ax = plt.subplots(figsize=(12,8))
# x = np.linspace(2600,3600,2000)
# ax.plot(x,norm_males.pdf(x),color= '#4586AC',label='29')
# mean_male_bal = get_means(sort_males)
# print('males mean: ', mean_male_bal)
# mean_female_bal = get_means(sort_females)
# print('females mean: ', mean_female_bal)

# mean_20_bal = get_means(sort_20)
# print('20 or less mean: ', mean_20_bal)
# mean_21_bal = get_means(sort_21)
# print('21 or 35 mean: ', mean_21_bal)
# mean_36_bal = get_means(sort_36)
# print('36 or 50 mean: ', mean_36_bal)
# mean_51_bal = get_means(sort_51)
# print('51 or more mean: ', mean_51_bal)

# mean_20m_bal = get_means(sort_male_20)
# print('20m or less mean: ', mean_20m_bal)
# mean_21m_bal = get_means(sort_male_21)
# print('21m to 35 mean: ', mean_20m_bal)
# mean_35m_bal = get_means(sort_male_20)
# print('36m to 51 mean: ', mean_35m_bal)
# mean_51m_bal = get_means(sort_male_20)
# print('51m or more mean: ', mean_51m_bal)

# mean_20f_bal = get_means(sort_female_20)
# print('20f or less mean: ', mean_20f_bal)
# mean_21f_bal = get_means(sort_female_21)
# print('21f to 35 mean: ', mean_21f_bal)
# mean_35f_bal = get_means(sort_female_20)
# print('36f to 51 mean: ', mean_35f_bal)
# mean_51f_bal = get_means(sort_female_20)
# print('51f or more mean: ', mean_51f_bal)

# std_male_bal = get_standard_deviations(sort_males)
# print('males std: ', std_male_bal)
# std_female_bal = get_standard_deviations(sort_females)
# print('females std: ' ,std_female_bal)

# std_20_bal = get_standard_deviations(sort_20)
# print('20 or less std: ',std_20_bal)
# std_21_bal = get_standard_deviations(sort_21)
# print('21 to 35 std: ',mean_21_bal)
# std_36_bal = get_standard_deviations(sort_36)
# print('36 to 50 std: ', mean_36_bal)
# std_51_bal = get_standard_deviations(sort_51)
# print('51 or more std: ', mean_51_bal)

# std_20m_bal = get_standard_deviations(sort_male_20)
# print('20m or less mean: ', std_20m_bal)
# std_21m_bal = get_standard_deviations(sort_male_21)
# print('21m to 35 mean: ', std_21m_bal)
# std_35m_bal = get_standard_deviations(sort_male_36)
# print('36m to 51 mean: ', std_35m_bal)
# std_51m_bal = get_standard_deviations(sort_male_51)
# print('51m or more mean: ', std_51m_bal)

# std_20f_bal = get_standard_deviations(sort_female_20)
# print('20f or less mean: ', std_20f_bal)
# std_21f_bal = get_standard_deviations(sort_female_21)
# print('21f to 35 mean: ', std_21f_bal)
# std_35f_bal = get_standard_deviations(sort_female_36)
# print('36f to 51 mean: ', std_35f_bal)
# std_51f_bal = get_standard_deviations(sort_female_51)
# print('51f or more mean: ', std_51f_bal)

# norm_dist_m = norm_dist(mean_male_bal, std_male_bal)
# print(norm_dist_m)