#place holder for machine learning models
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from life_well_main import (clean_data, cleaned_groups, sort_mf_age, sort_mf, sort_age)
import pandas as pd







def main():

    df = pd.read_csv('data/wellbeing-lifestyle-cs1.csv')

    well_life_df = clean_data(df)
    print(well_life_df.info())

    mf_age_group, mf_group, ages_group = cleaned_groups(df)

    mf_ages_bal = sort_mf_age(mf, ages, m_f, mfa_group)
    mf_bal = sort_mf(mf, m_f, mf_group)
    bal_ages = sort_age(ages, ages_group)



if __name__ == '__main__':
    main()