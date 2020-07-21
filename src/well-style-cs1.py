import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

df = pd.read_csv('../data/wellbeing-lifestyle-cs1.csv')

#print('BEFORE CLEANING:\n') 
#print(df.info())
#print(df.describe())
#print(df.head(50))

df.drop(axis=1, index=10005, inplace=True) #this row had an invalid entry for daily_stress

def clean_data(df):
    
    df['bal_score'] = df.sum(axis=1)
    df.columns = map(str.lower, df.columns)
    df.rename(columns={'gender':'male_female'}, inplace=True)
    df_fix = df.astype({'daily_stress':'int64'})
    df_fix.replace('Less than 20', '20 or less', inplace=True)
    return df_fix
    
#print(clean_data(df).info()) 
#print(clean_data(df).describe())
#print(clean_data(df).head())

mf_age_group = clean_data(df).groupby(['male_female', 'age'])
mf_group = clean_data(df).groupby('male_female')
ages_group = clean_data(df).groupby('age')

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

    '''ages = group to get out of the four ages - str
        
        returns - list of balance scores for the four age ranges '''

    group_of_ages = ages_group.get_group(f'{ages}')
    bal_ages = group_of_ages.iloc[:, 21:24:2]
    bal_ages.rename(columns={'age':f'{ages}'})
    balscore_list_age = bal_ages['bal_score'].tolist()
    return balscore_list_age

def convert_to_list():

    '''returns the balance score column as list'''

    return clean_data(df)['bal_score'].tolist()

def get_means(lst):

    '''returns means of whole/sample balance scores'''

    return np.mean(lst)
    
def get_standard_deviations(lst):

    '''returns standard deviation of whole/sample balance scores'''

    return np.std(lst)

def norm_dist(mean, std): #NEEDS ATTENTION
    pass
    
def plot_bal_by_age():
    
    x = sort_20
    x1 = sort_21
    x2 = sort_36
    x3 = sort_51

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
    
    x = sort_males
    x1 = sort_females
  
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

    sort_20 = sort_age('20 or less')

    sort_21 = sort_age('21 to 35')

    sort_36 = sort_age('36 to 50')
    
    sort_51 = sort_age('51 or more')

    bal_scores_to_list = convert_to_list()

    mean_whole_list = get_means(bal_scores_to_list)

    std_whole_list = get_standard_deviations(bal_scores_to_list)

    mean_male_bal = get_means(sort_males)
        
    mean_female_bal = get_means(sort_females)
    
    mean_20_bal = get_means(sort_20)

    mean_21_bal = get_means(sort_21)

    mean_36_bal = get_means(sort_36)

    mean_51_bal = get_means(sort_51)

    std_male_bal = get_standard_deviations(sort_males)

    std_female_bal = get_standard_deviations(sort_females)

    std_20_bal = get_standard_deviations(sort_20)

    std_21_bal = get_standard_deviations(sort_21)

    std_36_bal = get_standard_deviations(sort_36)

    std_51_bal = get_standard_deviations(sort_51)

    #norm_dist_51 = norm_dist(mean_male_bal, std_male_bal)
    #print(f'Normal Distribution for 51 or more: {norm_dist_51}')

    #plot_bal_ages = plot_bal_by_age()
    #plot_bal_m_f =  plot_bal_by_mf()
    #plot_bal_mf_a = plot_bal_by_mf_age()