#place holder for machine learning models
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from life_well_main import clean_data
import pandas as pd







def main():

    df = pd.read_csv('data/wellbeing-lifestyle-cs1.csv')
    well_life_df = clean_data(df)

    print(well_life_df.head())
    print(well_life_df.tail())
    print(well_life_df.info())

if __name__ == '__main__':
    main()