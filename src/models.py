#place holder for machine learning models
from sklearn.model_selection import (train_test_split, RandomizedSearchCV, GridSearchCV)
from sklearn.metrics import (mean_squared_error, mean_absolute_error, explained_variance_score)
from sklearn.preprocessing import (StandardScaler, MinMaxScaler)
from sklearn.ensemble import RandomForestRegressor
from life_well_main import clean_data
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

def grid_search(X_train, X_test, y_train, y_test):

    random_forest_grid = {'max_depth': [3, 5, None],
                        'max_features': ['sqrt', 'log2', None],
                        'min_samples_split': [2, 4],
                        'min_samples_leaf': [1, 5, 10, 15],
                        'bootstrap': [True, False],
                        'n_estimators': [20, 40, 50, 100, 200],
                        'random_state': [1]}

    rf_gridsearch = RandomizedSearchCV(RandomForestRegressor(),
                                random_forest_grid,
                                n_iter = 200,
                                n_jobs=-1,
                                verbose=True,
                                scoring='accuracy')
    rf_gridsearch.fit(X_train, y_train)

    #print("Random Forest best parameters:", rf_gridsearch.best_params_)

    best_rf_model = rf_gridsearch.best_estimator_

    return best_rf_model

def models(X_train, X_test, y_train, y_test):

    '''
    Runs the model to predict a persons lifestyle and wellness score
    X_train - np array
    X_test - np array
    y_train - np array
    y_test - np array
    '''
    rf = RandomForestRegressor(n_estimators=100, criterion='mse', max_depth=10, min_samples_split=2,
                                min_samples_leaf=1, max_features='auto', bootstrap=True, n_jobs=None,
                                random_state=1, warm_start=True, max_samples=X_train.shape[0])
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    mse = mean_squared_error(y_test, y_pred, squared=True)
    evs = explained_variance_score(y_test, y_pred)

    return mse, evs


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

    #RUN MODELS AND PRINT RESULTS
    print('mean squared error: ', models(X_train, X_test, y_train, y_test)[0])
    print('explained variance: ', models(X_train, X_test, y_train, y_test)[1])

if __name__ == '__main__':
    main()