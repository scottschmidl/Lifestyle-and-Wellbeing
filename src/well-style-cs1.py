import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

df = pd.read_csv('../data/wellbeing-lifestyle-cs1.csv')

#################################before cleaning of data################################

#print('BEFORE CLEANING:\n') 
#print(df.info(), '\n')
#print(df.describe())
#print(df.head(50))
#print(df.tail(50))
#print(df.sample(50))

#################################cleaning of data################################

def clean_data():
    pass

df['bal_score'] = df.sum(axis=1)
df.columns = map(str.lower, df.columns)
df.drop(axis=1, index=10005, inplace=True) #this row had an invalid entry for daily_stress
df.rename(columns={'gender':'male_female'}, inplace=True)
df_fix = df.astype({'daily_stress':'int64'})
df_fix.replace('Less than 20', '20 or less', inplace=True)
#print('AFTER CLEANING:\n')
#print(df_fix.info())
#print(df.describe())

########################sorting data by what i want to plot########################

def sort_data():
    pass

df2 = df_fix.groupby('male_female').sum()
#print(df2)

df3 = df_fix.groupby('age').sum()
#print(df3)

df1_ = df_fix.sort_values(by=['male_female', 'age'])
#print(df1)

df2_ = df_fix.sort_values(by='male_female', axis=0)
#print(df2_)

df3_ = df_fix.sort_values(by='age', axis=0, ascending=False)
#print(df3_)

df4_ = df_fix.sort_values(by='bal_score', axis=0, ascending=False)
#print(df4_)

df9 = df_fix.groupby(['male_female', 'age'])
male_age_20 = df9.get_group(('Male','20 or less'))
#print(male_age_20)

male_age_21 = df9.get_group(('Male', '21 to 35'))
#print(male_age_21)

male_age_36 = df9.get_group(('Male', '36 to 50'))
#print(male_age_36)

male_age_51 = df9.get_group(('Male', '51 or more'))
#print(male_age_51)

female_age_20 = df9.get_group(('Female','20 or less'))
#print(female_age_20)

female_age_21 = df9.get_group(('Female', '21 to 35'))
#print(female_age_21)

female_age_36 = df9.get_group(('Female', '36 to 50'))
#print(female_age_36)

female_age_51 = df9.get_group(('Female', '51 or more'))
#print(female_age_51)

m_f_group = df_fix.groupby('male_female')
ages_group = df_fix.groupby('age')

male_group = m_f_group.get_group('Male')
male_bal = male_group.iloc[:, 22:24]
male_bal.rename(columns={'male_female':'males'}, inplace=True)
male_bal_scores_list = male_bal['bal_score'].tolist()

female_group = m_f_group.get_group('Female')
female_bal = female_group.iloc[:, 22:24]
female_bal.rename(columns={'male_female':'females'}, inplace=True)
female_bal_scores_list = female_bal['bal_score'].tolist()

group_20 = ages_group.get_group('20 or less')
bal_20 = group_20.iloc[:, 21:24:2]
bal_20.rename(columns={'age':'20 or less'}, inplace=True)
balacc_list_20 = bal_20['bal_score'].tolist()

group_21 = ages_group.get_group('21 to 35')
bal_21 = group_21.iloc[:, 21:24:2]
bal_21.rename(columns={'age':'21 to 35'}, inplace=True)
balacc_list_21 = bal_21['bal_score'].tolist()

group_36 = ages_group.get_group('36 to 50')
bal_36 = group_36.iloc[:, 21:24:2]
bal_36.rename(columns={'age':'36 to 50'}, inplace=True)
balacc_list_36 = bal_36['bal_score'].tolist()

group_51 = ages_group.get_group('51 or more')
bal_51 = group_51.iloc[:, 21:24:2]
bal_51.rename(columns={'age':'51 or more'}, inplace=True)
balacc_list_51 = bal_51['bal_score'].tolist()

##########################indexing into data to visualize##########################

df5 = df2_.iloc[:,22:24]
df6 = df3_.iloc[:, 21:24]
df7 = df4_.iloc[:, 23]
df8 = df1_.iloc[:, 21:24] 
#print(f'sorted by male_female:\n {df5} \n')
#print(f'sorted by age:\n {df6} \n')
#print(f'sorted by bal_score:\n {df7}')
#print(f'sorted by ages and male_female:\n {df1_}')

def convert_to_list(col):

    '''returns the balance score column as list'''

    return df_fix[f'{col}'].tolist()

def group_to_dict(group):

    '''returns dictionary with group as the key and a subset of the
       balance score list as the value'''

    if group == 'Male':
        male_dict = {}
        for m in male_bal.iloc[0:, 0:1]:
            male_dict[m] = male_bal_scores_list
            return male_dict
    
    elif group == 'Female':
        female_dict = {}
        for f in female_bal.iloc[0:, 0:1]:
            female_dict[f] = female_bal_scores_list
            return female_dict

    elif group == '20 or less':
        dict_20 = {}
        for a in bal_20.iloc[0:, 0:1]:
            dict_20[a] = balacc_list_20
            return dict_20

    elif group == '21 to 35':
        dict_21 = {}
        for a in bal_21.iloc[0:, 0:1]:
            dict_21[a] = balacc_list_21
            return dict_21

    elif group == '36 to 50':
        dict_36 = {}
        for a in bal_36.iloc[0:, 0:1]:
            dict_36[a] = balacc_list_36
            return dict_36

    elif group == '51 or more':
        dict_51 = {}
        for a in bal_51.iloc[0:, 0:1]:
            dict_51[a] = balacc_list_51
            return dict_51

    return 'not a valid group'

def get_means(lst):

    '''returns means of whole/sample balance scores'''

    return np.mean(lst)
    
def get_standard_deviations(lst):

    '''returns standard deviation of whole/sample balance scores'''

    return np.std(lst)

def norm_dist(mean, std): #NEEDS ATTENTION
    
    norm = stats.norm(mean, std)
    return norm.cdf(90)
    
##################################plotting data##################################

def age_vs_bal():
    pass

def m_f_vs_bal():
    pass

def age_ranges_mean_var_std():
    pass

def male_female_mean_var_std():
    pass

################################answers to the 20 question work-life-balance test################################

def find_min_max_possible(q1_a, q2_a, q3_a, q4_a, q5_a, q6_a, q7_a, q8_a, q9_a, q10_a, q11_a, q12_a, q13_a, q14_a, q15_a, q16_a, q17_a, q18_a, q19_a, q20_a):

    '''returns the min and max possible scores'''

    min_possible_score = q1_a[0] + q2_a[0] + q3_a[0] + q4_a[0] + q5_a[0] + q6_a[0] + q7_a[0] + q8_a[0] + q9_a[0] + q10_a[0] + q11_a[0] + q12_a[0] + q13_a[0] + q14_a[0] + q15_a[0] + q16_a[0] + q17_a[0] + q18_a[0] + q19_a[0] + q20_a[0]
    max_possible_score = q1_a[-1] + q2_a[-1] + q3_a[-1] + q4_a[-1] + q5_a[-1] + q6_a[-1] + q7_a[-1] + q8_a[-1] + q9_a[-1] + q10_a[-1] + q11_a[-1] + q12_a[-1] + q13_a[-1] + q14_a[-1] + q15_a[-1] + q16_a[-1] + q17_a[-1] + q18_a[-1] + q19_a[-1] + q20_a[-1]
    return [min_possible_score, max_possible_score]

#####################################INEMB#####################################

if __name__ == '__main__':
    bal_scores_to_list = convert_to_list('bal_score')

    ##########################mean/std for full balance score##########################

    mean_whole_list = get_means(bal_scores_to_list)
    #print(f'Mean of whole balance scores: {mean_whole_list}\n')

    std_whole_list = get_standard_deviations(bal_scores_to_list)
    #print(f'Standard Deviation of balance scores: {std_whole_list}\n')

    ##########################means/std for male_female balance score subsets##########################

    mean_male_bal = get_means(male_bal_scores_list)
    #print(f'Mean of male balance scores: {mean_male_bal}\n')
        
    mean_female_bal = get_means(female_bal_scores_list)
    #print(f'Mean of female balance scores: {mean_female_bal}\n')
    
    mean_20_bal = get_means(balacc_list_20)
    #print(f'Mean of 20 or less balance scores: {mean_20_bal}\n')

    mean_21_bal = get_means(balacc_list_21)
    #print(f'Mean of 21 to 36 balance scores: {mean_21_bal}\n')

    mean_36_bal = get_means(balacc_list_36)
    #print(f'Mean of 36 to 51 balance scores: {mean_36_bal}\n')

    mean_51_bal = get_means(balacc_list_51)
    #print(f'Mean of 51 or more balance scores: {mean_51_bal}\n')

    std_male_bal = get_standard_deviations(male_bal_scores_list)
    #print(f'Standard Deviation of male balance scores: {std_male_bal}\n')

    std_female_bal = get_standard_deviations(female_bal_scores_list)
    #print(f'Standard Deviation of female balance scores: {std_female_bal}\n')

    std_20_bal = get_standard_deviations(balacc_list_20)
    #print(f'Standard Deviation of males: {std_20_bal}\n')

    std_21_bal = get_standard_deviations(balacc_list_21)
    #print(f'Standard Deviation of males: {std_21_bal}\n')

    std_36_bal = get_standard_deviations(balacc_list_36)
    #print(f'Standard Deviation of males: {std_36_bal}\n')

    std_51_bal = get_standard_deviations(balacc_list_51)
    #print(f'Standard Deviation of males: {std_51_bal}')

    ##########################dictionary for all balance score subsets##########################

    male_dict = group_to_dict('Male')
    #print(f'Dictionary of male and their balance scores list: {male_dict}\n')

    female_dict = group_to_dict('Female')
    #print(f'Dictionary of female and their balance scores list: {female_dict}\n')

    dict_20 = group_to_dict('20 or less')    
    #print(f'Dictionary of ages 20 or less and their balance scores list:{dict_20}\n')

    dict_21 = group_to_dict('21 to 35')    
    #print(f'Dictionary of ages 21 to 35 and their balance scores list:{dict_21}\n')

    dict_36 = group_to_dict('36 to 50')    
    #print(f'Dictionary of ages 36 to 50 and their balance scores list:{dict_36}\n')

    dict_51 = group_to_dict('51 or more')    
    #print(f'Dictionary of ages 51 or more and their balance scores list:{dict_51}\n')

    ##########################normal distribution##########################
    norm_dist_51 = norm_dist(mean_male_bal, std_male_bal)
    #print(f'Normal Distribution for 51 or more: {norm_dist_51}')

    ##########################calculates min/max possible values for balance score##########################

    min_max_possible_scores = find_min_max_possible(q1_a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q2_a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q3_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                                    q4_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q5_a=[0, 1, 2, 3, 4, 5], q6_a=[1, 2], q7_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                                    q8_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q9_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q10_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                                    q11_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q12_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q13_a=[1, 2], q14_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                                    q15_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q16_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q17_a=[0, 1, 2, 3, 4, 5],
                                                    q18_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], q19_a=[0, 1, 2, 3, 4, 5], q20_a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #print(f'here are the possible min and max values: {min_max_possible_scores}')