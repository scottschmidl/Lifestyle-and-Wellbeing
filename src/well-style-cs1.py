import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

df = pd.read_csv('../data/wellbeing-lifestyle-cs1.csv')

#print('BEFORE CLEANING:\n') 
#print(df.info())
#print(df.describe())
#print(df.head(50))

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
#print(df_fix.describe())

#sorting data

mf_age_group = df_fix.groupby(['male_female', 'age'])
mf_group = df_fix.groupby('male_female')
ages_group = df_fix.groupby('age')

def sort_mf_age(mf, ages, m_f):
    '''mf = group to get out of Male or Female - str
       ages = age range to get our of 20 or less, 21 to 35, 36 to 50, 51 or more - str
       m_f = rename male_female column as either males or females - str
        
        returns - list of balance scores depending on which group'''

    mf_ages = mf_age_group.get_group((f'{mf}', f'{ages}'))
    mf_ages_bal = mf_ages.iloc[:, 21:24]
    mf_ages_bal.rename(columns={'male_female':f'{m_f}'}, inplace=True)
    mf_ages_scores = mf_ages_bal['bal_score'].tolist()
    return mf_ages_scores

def sort_mf(mf, m_f):
    '''mf = group to get out of Male or Female - str
       m_f = rename male_female column as either males or females - str
       
       returns - list of balance scores for either all males or females'''

    male_female = mf_group.get_group(f'{mf}')
    mf_bal = male_female.iloc[:, 22:24]
    mf_bal.rename(columns={'male_female':f'{m_f}'}, inplace=True)
    mf_bal_scores = mf_bal['bal_score'].tolist()
    return mf_bal_scores

def sort_age(ages):
    pass

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

def convert_to_list():

    '''returns the balance score column as list'''

    return df_fix['bal_score'].tolist()

def get_means(lst):

    '''returns means of whole/sample balance scores'''

    return np.mean(lst)
    
def get_standard_deviations(lst):

    '''returns standard deviation of whole/sample balance scores'''

    return np.std(lst)

def group_to_dict(group):
  
    '''returns dictionary with group as the key and a subset of the
       balance score list as the value'''

    if group == '20 or less':
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

def norm_dist(mean, std): #NEEDS ATTENTION

    norm = stats.norm(mean, std)

    return norm.cdf(90)
    
def plot_bal_by_age():
    
    x = dict_20['20 or less']
    x1 = dict_21['21 to 35']
    x2 = dict_36['36 to 50']
    x3 = dict_51['51 or more']

    fig, axes = plt.subplots(2, 2, figsize=(6, 5))
    ax0, ax1, ax2, ax3 = axes.flatten()
       
    ax0.hist(x, 100)
    ax0.axis([0, 169.5, 0, 205])
    ax0.set_title('20 or less')
    ax0.set_xlabel('Balance Score')

    ax1.hist(x1, 100)
    ax1.axis([0, 169.5, 0, 205])
    ax1.set_title('21 to 36')
    ax1.set_xlabel('Balance Score')

    ax2.hist(x2, 100)
    ax2.axis([0, 169.5, 0, 205])
    ax2.set_title('36 To 50')
    ax2.set_xlabel('Balance Score')

    ax3.hist(x3, 100)
    ax3.axis([0, 169.5, 0, 205])
    ax3.set_title('51 Or More')
    ax3.set_xlabel('Balance Score')

    plt.tight_layout()
    plt.show()

def plot_bal_by_mf():
    
    x = male_dict['males']
    x1 = female_dict['females']
  
    fig, axes = plt.subplots(2, 1, figsize=(6, 5))
    ax0, ax1 = axes.flatten()
       
    ax0.hist(x, 100)
    ax0.axis([0, 169.5, 0, 350])
    ax0.set_xlabel('males')
    ax0.set_ylabel('Balance Score')

    ax1.hist(x1, 100)
    ax1.axis([0, 169.5, 0, 350])
    ax1.set_xlabel('females')
    ax1.set_ylabel('Balance Score')

    plt.tight_layout()
    plt.show()

def plot_bal_by_mf_age():
    pass

def plot_male_female_mean_var_std():
    pass

if __name__ == '__main__':

    sort_male_20 = sort_mf_age('Male', '20 or less', 'males')
    
    sort_male_21 = sort_mf_age('Male', '21 to 35', 'males')

    sort_male_36 = sort_mf_age('Male', '36 to 50', 'males')

    sort_male_51 = sort_mf_age('Male', '51 or more', 'males')

    sort_female_20 = sort_mf_age('Female', '20 or less', 'females')

    sort_female_21 = sort_mf_age('Female', '21 to 35', 'females')

    sort_female_36 = sort_mf_age('Female', '36 to 50', 'females')

    sort_female_51 = sort_mf_age('Female', '51 or more', 'females')

    sort_males = sort_mf('Male', 'males')

    sort_females = sort_mf('Female', 'females')
    print('\n',sort_females)

    bal_scores_to_list = convert_to_list()

    mean_whole_list = get_means(bal_scores_to_list)

    std_whole_list = get_standard_deviations(bal_scores_to_list)

    mean_male_bal = get_means(sort_males)
        
    mean_female_bal = get_means(sort_females)
    
    mean_20_bal = get_means(balacc_list_20)

    mean_21_bal = get_means(balacc_list_21)

    mean_36_bal = get_means(balacc_list_36)

    mean_51_bal = get_means(balacc_list_51)

    std_male_bal = get_standard_deviations(sort_males)

    std_female_bal = get_standard_deviations(sort_females)

    std_20_bal = get_standard_deviations(balacc_list_20)

    std_21_bal = get_standard_deviations(balacc_list_21)

    std_36_bal = get_standard_deviations(balacc_list_36)

    std_51_bal = get_standard_deviations(balacc_list_51)

    male_dict = group_to_dict('Male')

    female_dict = group_to_dict('Female')

    dict_20 = group_to_dict('20 or less')    

    dict_21 = group_to_dict('21 to 35')    

    dict_36 = group_to_dict('36 to 50')    

    dict_51 = group_to_dict('51 or more')    

    #norm_dist_51 = norm_dist(mean_male_bal, std_male_bal)
    #print(f'Normal Distribution for 51 or more: {norm_dist_51}')

    #plot_bal_ages = plot_bal_by_age()
    #plot_bal_m_f =  plot_bal_by_mf()
    #plot_bal_mf_a = plot_bal_by_mf_age()