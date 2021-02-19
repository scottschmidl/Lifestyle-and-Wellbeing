#extra information: not sure if i will use
from life_well_main import cleaned_data

def convert_to_list(df):

    '''returns the balance score column as list'''

    return df['bal_score'].tolist()

bal_scores_to_list = convert_to_list(cleaned_data)

print(bal_scores_to_list)