import pandas as pd
import regex as re

## CLEAN DATA AND GET CLEANED GROUPS
def clean_data(df):

    '''
    clean data and get a new datafram
    df - pandas dataframe
    '''

    df['bal_score'] = df.sum(axis=1)
    df.columns = map(str.lower, df.columns)
    df.rename(columns={'gender':'male_female'}, inplace=True)
    df.drop(axis=1, index=10005, inplace=True) #this row had an invalid entry for daily_stress
    df_fix = df.astype({'daily_stress':'int64'})
    df_fix.replace('Less than 20', '20 or less', inplace=True)
    df_fix['timestamp'] = pd.to_datetime(df_fix['timestamp'], infer_datetime_format=True).dt.date.astype('datetime64')
    df_fix = df_fix.iloc[:, 1:]

    return df_fix

def cleaned_groups(df):

    cleaned_data = clean_data(df)

    mf_age_group = cleaned_data.groupby(['male_female', 'age'])
    mf_group = cleaned_data.groupby('male_female')
    ages_group = cleaned_data.groupby('age')

    return mf_age_group, mf_group, ages_group

## SORT MALE, FEMALE BY AGE
def sort_mf_age(mf, ages, m_f, mfa_group):

    '''
    mf = group to get out of Male or Female - str
    ages = age range to get our of 20 or less, 21 to 35, 36 to 50, 51 or more - str
    m_f = rename male_female column as either males or females - str

    returns - list of balance scores depending on which group
    '''

    mf_ages = mfa_group.get_group((f'{mf}', f'{ages}'))
    mf_ages_bal = mf_ages.iloc[:, 20:23]
    mf_ages_bal.rename(columns={'male_female':f'{m_f}'}, inplace=True)

    return mf_ages_bal

def sort_malefemale_age(mfa_group):

    sort_male_20 = sort_mf_age('Male', '20 or less', 'males', mfa_group)['bal_score'].to_list()
    sort_male_21 = sort_mf_age('Male', '21 to 35', 'males', mfa_group)['bal_score'].to_list()
    sort_male_36 = sort_mf_age('Male', '36 to 50', 'males', mfa_group)['bal_score'].to_list()
    sort_male_51 = sort_mf_age('Male', '51 or more', 'males', mfa_group)['bal_score'].to_list()

    sort_female_20 = sort_mf_age('Female', '20 or less', 'females', mfa_group)['bal_score'].to_list()
    sort_female_21 = sort_mf_age('Female', '21 to 35', 'females', mfa_group)['bal_score'].to_list()
    sort_female_36 = sort_mf_age('Female', '36 to 50', 'females', mfa_group)['bal_score'].to_list()
    sort_female_51 = sort_mf_age('Female', '51 or more', 'females', mfa_group)['bal_score'].to_list()

    return sort_male_20, sort_male_21, sort_male_36, sort_male_51, sort_female_20, sort_female_21, sort_female_36, sort_female_51

## SORT MALE, FEMALE
def sort_mf(mf, m_f, mf_group):

    '''
    mf = group to get out of Male or Female - str
    m_f = rename male_female column as either males or females - str

    returns - list of balance scores for either all males or females
    '''

    male_female = mf_group.get_group(f'{mf}')
    mf_bal = male_female.iloc[:, 21:23]
    mf_bal.rename(columns={'male_female':f'{m_f}'}, inplace=True)

    return mf_bal

def sort_male_female(mf_group):

    sort_males = sort_mf('Male', 'males', mf_group)['bal_score'].to_list()
    sort_females = sort_mf('Female', 'females', mf_group)['bal_score'].to_list()

    return sort_males, sort_females

## SORT AGE
def sort_age(ages, ages_group):

    '''
    ages = group to get out of the four ages - str

    returns - list of balance scores for the four age ranges
    '''

    group_of_ages = ages_group.get_group(f'{ages}')
    bal_ages = group_of_ages.iloc[:, 20:24:2]
    bal_ages.rename(columns={'age':f'{ages}'})

    return bal_ages

def sort_ages(ages_group):

    sort_20 = sort_age('20 or less', ages_group)['bal_score'].to_list()
    sort_21 = sort_age('21 to 35', ages_group)['bal_score'].to_list()
    sort_36 = sort_age('36 to 50', ages_group)['bal_score'].to_list()
    sort_51 = sort_age('51 or more', ages_group)['bal_score'].to_list()

    return sort_20, sort_21, sort_36, sort_51

def clean_sort(df):

    #CLEAN
    mf_age_group, mf_group, ages_group = cleaned_groups(df)

    #SORT
    sort_mf_age = sort_malefemale_age(mf_age_group)
    sort_mf = sort_male_female(mf_group)
    sort_age = sort_ages(ages_group)

    return sort_mf_age, sort_mf, sort_age

def main():

    df = pd.read_csv('data/wellbeing-lifestyle-cs1.csv')
    clean_sort(df)

if __name__ == '__main__':
    main()
