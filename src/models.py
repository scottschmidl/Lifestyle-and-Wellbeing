#place holder for machine learning models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from life_well_main import clean_data
import seaborn as sns
import pandas as pd

def getX_y(df):

    '''
    RETURNS X, y TO BE USED IN SPLITTING
    df - PANDAS DATAFRAME
    '''

    columns = ['bal_score']

    X = df.copy()
    y = X['bal_score']
    X = df.drop(columns=columns, axis=1)

    return X, y

def encoding(df, cats_dummie, cats_rename):

    '''
    RETURN A ONE HOT ENCODED DATAFRAME FOR AGE AND GENDER
    '''

    encode_me = pd.get_dummies(data=df, columns=cats_dummie, dtype=int)
    encode_me.rename(columns=cats_rename, inplace=True)

    return encode_me

def scale_norm(df):

    '''
    SCALES/NORMALIZES THE DF AFTER OHE
    '''

    vals = df.values
    mmscaled_df = MinMaxScaler(feature_range=(0, 1)).fit_transform(vals)

    return mmscaled_df

def train_split(X, y):
    '''
    RETURNS TRAING AND TESTING SPLITS
    X - DATAFRAME WITH PREDICTORS
    y - SERIES TO BE PREDICTED
    '''

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1,
                                                        train_size=0.80, test_size=0.20)

    return X_train, X_test, y_train, y_test

def models(X_train, X_test, y_train, y_test):
    pass


def main():

    #GET AND CLEAN DATA
    filepath = 'data/wellbeing-lifestyle-cs1.csv'
    df = pd.read_csv(filepath)
    well_life_df = clean_data(df)

    cat_cols = ['age', 'male_female']
    cols_rename = {'age_20 or less':'age_20_or_less', 'age_21 to 35':'age_21_to_35',
            'age_36 to 50':'age_36_to_50', 'age_51 or more':'age_51_or_more',
            'male_female_Female':'female', 'male_female_Male':'male'}

    #GETTING X, y AND SPLITTING
    X, y = getX_y(well_life_df)

    #ONE HOT ENCODE AGES AND GENDER
    onehottie = encoding(X, cat_cols, cols_rename)

    #SCALE/NORMALIZE DUE TO DIFFERENT VALUES FOR SOME COLUMNS
    scalynormy = scale_norm(onehottie)

    #SPLIT INTO TRAINING AND TESTING
    X_train, X_test, y_train, y_test = train_split(scalynormy, y)
    print(X_train.shape)
    print(y_train.shape)
    print(X_test.shape)
    print(y_test.shape)



if __name__ == '__main__':
    main()