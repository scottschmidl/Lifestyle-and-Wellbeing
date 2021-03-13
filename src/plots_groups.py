from mean_std_norm import (mean_malefemale_bal, mean_age_bal, mean_MF_age_bal)
from life_well_main import clean_sort
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import warnings

def bar_means(y):
    x = ['male', 'female', '20' , '21', '36', '51', 'm20',
                'm21', 'm36', 'm51', 'f20', 'f21', 'f36', 'f51']

    _, ax = plt.subplots(figsize=(12, 4))

    ax.bar(x, y, width=0.3)
    plt.xticks(rotation=20, fontsize=14)
    plt.hlines(80, ['male'], ['f51'], linestyles='dashed')
    ax.set_ylabel('mean', fontsize=14)
    plt.yticks([0, 20, 50, 80, 110, 140, 170], fontsize=14)

    #plt.savefig('images/compare_means.png')
    plt.show()

def hist_bal_by_age(x):

    titles = [['20 or less', '21 to 35'], ['36 to 50', '51 or more']]
    _, ax = plt.subplots(2, 2, figsize=(12, 5))

    for i in range(2):

        for j in range(2):

            sns.histplot(x[i][j], bins=50, kde=True, ax=ax[i][j])
            ax[i][j].set_title(titles[i][j])
            ax[i][j].set_xlabel('Balance Score')
            ax[i][j].set_ylabel('Kernel Density Estimation')
            ax[i][j].set_xlim(4, 170)
            ax[i][j].set_xticks([20, 40, 60, 80, 100, 120, 140, 160])

    plt.tight_layout()
    #plt.savefig('../images/compare_balscores_ages.png')
    plt.show()

def box_ages(x1):

    _, ax = plt.subplots(figsize=(6,5), sharey=True)
    ax.boxplot(x1, positions=[1,2,3,4], labels=['20 or less', '21 to 35', '36 to 50', '51 or more'])
    ax.set_title('5-number summary of ages')
    ax.set_ylabel('Balance Score')
    #plt.savefig('../images/box_ages.png')
    plt.show()

def hist_bal_by_mf(x):

    titles = ['males', 'females']
    _, ax = plt.subplots(1, 2, figsize=(6,5))

    for i in range(2):
        sns.histplot(x[i], bins=50, kde=True, ax=ax[i])
        ax[i].set_title(titles[i])
        ax[i].set_xlabel('Balance Score')
        ax[i].set_ylabel('Kernel Density Estimation')
        ax[i].set_xlim(4, 170)
        ax[i].set_xticks([20, 40, 60, 80, 100, 120, 140, 160])

    plt.tight_layout()
    #plt.savefig('../images/compare_balscores_mf.png')
    plt.show()

def box_mf(x1):

    _, ax = plt.subplots(figsize=(6,5), sharey=True)
    ax.boxplot(x1, positions=[1,2], labels=['males','females'])
    ax.set_title('5-number summary of males and females')
    ax.set_ylabel('Balance Score')
    #plt.savefig('../images/box_mf.png')
    plt.show()

def hist_bal_by_mf_age(x):

    titles = [['m: 20 or less', 'm: 21 to 35', 'm: 36 to 50', 'm: 51 or more'],
                ['f: 20 or less', 'f: 21 to 35', 'f: 36 to 50', 'f: 51 or more']]
    _, ax = plt.subplots(2, 4, figsize=(13, 4))

    for i in range(2):

        for j in range(4):

            sns.histplot(x[i][j], bins=50, kde=True, ax=ax[i][j])
            ax[i][j].set_title(titles[i][j])
            ax[i][j].set_xlabel('Balance Score')
            ax[i][j].set_ylabel('Kernel Density Estimation')
            ax[i][j].set_xlim(4, 170)
            ax[i][j].set_xticks([30,60,90,120,150])

    plt.tight_layout()
    #plt.savefig('../images/compare_balscores_mf_age.png')
    plt.show()

def box_mf_age(x):

    _, ax = plt.subplots(figsize=(13,5), sharey=True)
    ax.boxplot(x, labels=['m:20 or less','m:21 to 35', 'm:36 to 50', 'm:51 or more', 'f:20 or less',
                            'f:21 to 35', 'f:36 to 50', 'f:51 or more'])
    ax.set_title('5-number summary of males and females by age')
    ax.set_ylabel('Balance Score')
    #plt.savefig('../images/box_mf_age.png')
    plt.show()

def get_y_plots(df):

    # UNPACK FOR CLEANED AND SORTED
    sort_mf_age, sort_mf, sort_age = clean_sort(df)

    sort_male_20, sort_male_21, sort_male_36, sort_male_51,\
    sort_female_20, sort_female_21, sort_female_36, sort_female_51 = sort_mf_age
    sort_males, sort_females = sort_mf
    sort_20, sort_21, sort_36, sort_51 = sort_age

    # UNPACK FOR MEANS
    mean_20m_bal, mean_21m_bal, mean_36m_bal, mean_51m_bal, mean_20f_bal,\
    mean_21f_bal, mean_36f_bal, mean_51f_bal = mean_MF_age_bal(sort_mf_age)
    mean_male_bal, mean_female_bal = mean_malefemale_bal(sort_mf)
    mean_20_bal, mean_21_bal, mean_36_bal, mean_51_bal = mean_age_bal(sort_age)

    # DEFINING VARIABLES FOR PLOTTING
    bar_y = [mean_male_bal, mean_female_bal, mean_20_bal, mean_21_bal, mean_36_bal, mean_51_bal, mean_20m_bal,
            mean_21m_bal, mean_36m_bal, mean_51m_bal, mean_20f_bal, mean_21f_bal, mean_36f_bal, mean_51f_bal]
    hist_age_x = [[sort_20, sort_21], [sort_36, sort_51]]
    box_ages_x1 = [sort_20, sort_21, sort_36, sort_51]
    hist_mf_x = [sort_males, sort_females]
    box_mf_x1 = [sort_males, sort_females]
    hist_mf_age_x = [[sort_male_20, sort_male_21, sort_male_36, sort_male_51],
                    [sort_female_20, sort_female_21, sort_female_36, sort_female_51]]
    box_mf_age_x = [sort_male_20, sort_male_21, sort_male_36, sort_male_51,\
                    sort_female_20, sort_female_21, sort_female_36, sort_female_51]


    return bar_y, hist_age_x, box_ages_x1, hist_mf_x, box_mf_x1, hist_mf_age_x, box_mf_age_x

def main():

    filepath = '../data/wellbeing-lifestyle-cs1.csv'

    df = pd.read_csv(filepath)

    # VARIABLES FOR PLOT
    bar_y, hist_age_y, box_ages_y, hist_mf_y, box_mf_y, hist_mf_age_y, box_mf_age_y = get_y_plots(df)

    # PLOTS
    bar_means(bar_y)
    hist_bal_by_age(hist_age_y)
    box_ages(box_ages_y)
    hist_bal_by_mf(hist_mf_y)
    box_mf(box_mf_y)
    hist_bal_by_mf_age(hist_mf_age_y)
    box_mf_age(box_mf_age_y)
    plt.show()

if __name__ == '__main__':
    main()