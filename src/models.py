#place holder for machine learning models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from life_well_main import clean_data
import seaborn as sns
import pandas as pd

def encoding(df, cats_dummie, cats_rename):

    '''
    RETURN A ONE HOT ENCODED DATAFRAMe FOR AGE AND GENDER
    '''

    encode_me = pd.get_dummies(data=df, columns=cats_dummie, dtype=int)
    encode_me.rename(columns=cats_rename, inplace=True)

    return encode_me

def scale_norm(df):

    '''
    SCALES/NORMALIZES THE DF AFTER OHE
    '''

    mmscaled_df = MinMaxScaler().fit_transform(df.values[:, :-1])
    standard_df = StandardScaler().fit_transform(df.values[:, :-1])

    print(mmscaled_df)
    print('34545yerhfghgdfas')
    print(standard_df)


def getX_y(df):

    '''
    RETURNS X, y TO BE USED IN SPLITTING
    df - PANDAS DATAFRAME
    '''

    columns = ['bal_score']
    print(df)
    print(type(df))
    X = df.copy()
    y = X['bal_score']
    X = df.drop(columns=columns, axis=1)

    return X, y

def train_split(X, y):
    '''
    RETURNS TRAING AND TESTING SPLITS
    X - DATAFRAME WITH PREDICTORS
    y - SERIES TO BE PREDICTED
    '''

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1,
                                                        train_size=0.80, test_size=0.20)

    return X_train, X_test, y_train, y_test


def pipe_line():

    '''
    GETS THE PIPELINE GOING FOR EASE OF MODELING
    '''

    pip_me_up = Pipeline()
    pass



def main():

    #GET AND CLEAN DATA
    df = pd.read_csv('data/wellbeing-lifestyle-cs1.csv')
    well_life_df = clean_data(df)

    cat_cols = ['age', 'male_female']
    # numeric_cols = ['fruits_veggies', 'daily_stress', 'places_visited',
    #                 'core_circle', 'supporting_others', 'social_network', 'achievement',
    #                 'donation', 'bmi_range', 'todo_completed', 'flow', 'daily_steps',
    #                 'live_vision', 'sleep_hours', 'lost_vacation', 'daily_shouting',
    #                 'sufficient_income', 'personal_awards', 'time_for_passion',
    #                 'daily_meditation',  'bal_score']
    cols_rename = {'age_20 or less':'age_20_or_less', 'age_21 to 35':'age_21_to_35',
            'age_36 to 50':'age_36_to_50', 'age_51 or more':'age_51_or_more',
            'male_female_Female':'female', 'male_female_Male':'male'}


    #ONE HOT ENCODE AGES AND GENDER
    onehottie = encoding(well_life_df, cat_cols, cols_rename)
    #SCALE/NORMALIZE DUE TO DIFFERENT VALUES FOR SOME COLUMNS
    scalynormy = scale_norm(onehottie)

    # #GETTING X, y AND SPLITTING
    # X, y = getX_y(scalynormy)
    # X_train, X_test, y_train, y_test = train_split(X, y)
    # print(X_train.shape)
    # print(y_train.shape)
    # print(X_test.shape)
    # print(y_test.shape)

    # pipes = pipe_line()


if __name__ == '__main__':
    main()