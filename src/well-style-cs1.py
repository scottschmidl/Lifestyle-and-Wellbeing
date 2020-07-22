import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

df = pd.read_csv('../data/wellbeing-lifestyle-cs1.csv')

#print('BEFORE CLEANING:\n') 
#print(df.info())
#print(df.describe())
#print(df.head(50))

df.drop(axis=1, index=10005, inplace=True) #this row had an invalid entry for daily_stress

def clean_data():

    df['bal_score'] = df.sum(axis=1)
    df.columns = map(str.lower, df.columns)
    df.rename(columns={'gender':'male_female'}, inplace=True)
    df_fix = df.astype({'daily_stress':'int64'})
    df_fix.replace('Less than 20', '20 or less', inplace=True)
    
    return df_fix
    
cleaned_data = clean_data()

#print(cleaned_data.info()) 
#print(cleaned_data.describe())
#print(cleaned_data.head())

mf_age_group = cleaned_data.groupby(['male_female', 'age'])
#print(mf_age_group.describe())
mf_group = cleaned_data.groupby('male_female')
#print(mf_group.describe())
ages_group = cleaned_data.groupby('age')
#print(ages_group.describe())

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

##############what do i want to do with the below##############
# def convert_to_list():

#     '''returns the balance score column as list'''

#     return clean_data()['bal_score'].tolist()

# def get_means(lst):

#     '''returns means of whole/sample balance scores'''

#     return np.mean(lst)
    
# def get_standard_deviations(lst):

#     '''returns standard deviation of whole/sample balance scores'''

#     return np.std(lst)

# def norm_dist(mean, std): #NEEDS ATTENTION
#     norm = stats.norm(loc=mean, scale=std)
#     return norm.rvs(size=1000)
    
def hist_bal_by_age():

    x = [[sort_20, sort_21], [sort_36, sort_51]]
    titles = [['20 or less', '21 to 35'], ['36 to 50', '51 or more']]
    fig, ax = plt.subplots(2, 2, figsize=(12, 5))
        
    for i in range(2):

        for j in range(2):

            sns.distplot(x[i][j], bins=100, kde=True, ax=ax[i][j])
            ax[i][j].set_title(titles[i][j])
            ax[i][j].set_xlabel('Balance Score')

    plt.tight_layout()
    #plt.savefig('../images/compare_balscores_ages.png')
    #plt.show()

def box_ages():

    x1 = [sort_20, sort_21, sort_36, sort_51]
    fig, ax = plt.subplots(figsize=(6,5), sharey=True)
    ax.boxplot(x1, positions=[1,2,3,4], labels=['20 or less','21 to 35', '36 to 50', '51 or more'])
    ax.set_title('5-number summary of ages')
    #plt.savefig('../images/box_ages.png')    
    #plt.show()
    

def hist_bal_by_mf():
    
    x = [sort_males, sort_females]
    titles = ['males', 'females']
    fig, ax = plt.subplots(2, 1, figsize=(6,5))    
   
    for i in range(2):
        sns.distplot(x[i], bins=100, kde=True, ax=ax[i])
        ax[i].set_title(titles[i])
        ax[i].set_xlabel('Balance Score')

    plt.tight_layout()
    #plt.savefig('../images/compare_balscores_mf.png')
    #plt.show()

def box_mf():

    x1 = [sort_males, sort_females]
    fig, ax = plt.subplots(figsize=(6,5), sharey=True)
    ax.boxplot(x1, positions=[1,2], labels=['males','females'])
    ax.set_title('5-number summary of males and females')
    #plt.savefig('../images/box_mf.png')    
    #plt.show()

def hist_bal_by_mf_age():
    
    x = [[sort_male_20, sort_male_21, sort_male_36, sort_male_51], [sort_female_20, sort_female_21, sort_female_36, sort_female_51]]
    titles = [['m: 20 or less', 'm: 21 to 35', 'm: 36 to 50', 'm: 51 or more'], ['f: 20 or less', 'f: 21 to 35', 'f: 36 to 50', 'f: 51 or more']]
    fig, ax = plt.subplots(2, 4, figsize=(12, 4))
        
    for i in range(2):

        for j in range(4):

            sns.distplot(x[i][j], bins=100, kde=True, ax=ax[i][j])
            ax[i][j].set_title(titles[i][j])
            ax[i][j].set_xlabel('Balance Score')

    plt.tight_layout()
    #plt.savefig('../images/compare_balscores_mf_age.png')
    #plt.show()    


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

    # bal_scores_to_list = convert_to_list()

    # mean_whole_list = get_means(bal_scores_to_list)

    # std_whole_list = get_standard_deviations(bal_scores_to_list)

    # mean_male_bal = get_means(sort_males)
        
    # mean_female_bal = get_means(sort_females)
    
    # mean_20_bal = get_means(sort_20)

    # mean_21_bal = get_means(sort_21)

    # mean_36_bal = get_means(sort_36)

    # mean_51_bal = get_means(sort_51)

    # std_male_bal = get_standard_deviations(sort_males)

    # std_female_bal = get_standard_deviations(sort_females)

    # std_20_bal = get_standard_deviations(sort_20)

    # std_21_bal = get_standard_deviations(sort_21)

    # std_36_bal = get_standard_deviations(sort_36)

    # std_51_bal = get_standard_deviations(sort_51)

    # norm_dist_m = norm_dist(mean_male_bal, std_male_bal)
    # print(f'Normal Distribution for 51 or more: {norm_dist_m}')

    # plot_bal_ages = hist_bal_by_age()
    # ages_box = box_ages()
    # plot_bal_m_f =  hist_bal_by_mf()
    # mf_box = box_mf()
    # plot_bal_mf_a = hist_bal_by_mf_age()
    
    
    