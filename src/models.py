#place holder for machine learning models
from sklearn.model_selection import (train_test_split, RandomizedSearchCV, GridSearchCV)
from sklearn.metrics import (mean_absolute_error, explained_variance_score)
from sklearn.preprocessing import (StandardScaler, MinMaxScaler)
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
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

def baseline(y_train):

    act_pred_error = pd.DataFrame({"actual": y_train})
    act_pred_error["baseline_prediction"] = y_train.mean()
    basline_mae = mean_absolute_error(act_pred_error["actual"], act_pred_error["baseline_prediction"])

    return basline_mae

def grid_search(X_train, y_train):

    '''
    Performs RANDOMIZED SEARCH CV TO FIND THE BEST PARAMETERS OR RANDOM FOREST
    '''

    random_forest_grid = {'n_estimators': [20, 40, 50, 100, 200],
                            'criterion': ['squared_error', 'absolute_error'],
                            'max_depth': [3, 5,10, None],
                            'min_samples_split': [2, 4, 6],
                            'min_samples_leaf':[1, 2, 4],
                            'max_features': ['auto', 'sqrt', 'log2', None],
                            'bootstrap': [True, False],
                            'random_state': [1],
                            'warm_start': [True, False],
                            'max_samples': [1, 2, 4, None]}

    rf_gridsearch = RandomizedSearchCV(RandomForestRegressor(),
                                param_distributions=random_forest_grid,
                                n_iter = 100,
                                n_jobs=-1,
                                refit="neg_root_mean_squared_error",
                                verbose=1,
                                scoring=["neg_mean_absolute_error", "neg_root_mean_squared_error"])

    rf_gridsearch.fit(X_train, y_train)

    print("Random Forest best parameters:", rf_gridsearch.best_params_)

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

    # BEST PARAMETERS FROM GRID SEARCH USING RANDOMIZED SEARCH CV
    rf = RandomForestRegressor(n_estimators=200, criterion='absolute_error', max_depth=None, min_samples_split=4,
                                min_samples_leaf=2, max_features='sqrt', bootstrap=False, n_jobs=4,
                                random_state=1, warm_start=False, max_samples=None)

    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    evs = explained_variance_score(y_test, y_pred)

    return mae, evs

def main():

    #GET AND CLEAN DATA
    filepath = '../data/wellbeing-lifestyle-cs1.csv'
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

    #BASELINE
    print(f"Baseline MAE: {round(baseline(y_train), )}")

    #GRIDSEARCH FOR BEST PARAMETERS
    # TODO: grid search needs to be rerun when there is time.
    # best_rf_model = grid_search(X_train, y_train)
        # BEST PARAMETERS ARE CURRENTLY BEING USING
        # BEST ESTIMATOR:
        # RandomForestRegressor(bootstrap=False, max_features='sqrt', min_samples_split=6,
        #                     n_jobs=4, random_state=1, warm_start=True)

    #RUN MODELS AND PRINT RESULTS
    print(f"Mean Absolute Error:  {round(models(X_train, X_test, y_train, y_test)[0], 1)}")
    # print('explained variance: ', models(X_train, X_test, y_train, y_test)[1])

if __name__ == '__main__':
    main()