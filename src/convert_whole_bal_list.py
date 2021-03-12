#extra information: not sure if i will use
from life_well_main import clean_data
import pandas as pd

def convert_to_list(df):

    '''returns the balance score column as list'''

    return df['bal_score'].tolist()

df = pd.read_csv('data/wellbeing-lifestyle-cs1.csv')

bal_scores_to_list = convert_to_list(clean_data(df))

print(bal_scores_to_list)