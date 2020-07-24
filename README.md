![happy girl](http://www.authentic-happiness.com/_/rsrc/1514760169721/home/The%20Authentic%20Happiness%20Project%202018.jpg)


# Table of Contents
1. [Background and Motivation](#BackGround-and-Motivation)
2. [Questions](#Questions)
3. [Data](#Data)
4. [Closer Look](#Closer-Look)
5. [Visualization](#Visualization)
6. [Conclusion](#Conclusion)
7. [Photo and Data Credits](#Photo-and-Data-Credits)
8. [Extras](#Extras)

# Background and Motivation

For most of my life I have been into exercising, but for most of my life I was not consistent
and I never got into lifting weights. It was not until the fall of 2017 were it became
important to me as a lifestyle and now I do it almost every day. My motivation was I had
realized how much better I felt after a good workout. It was then that I put the pieces
together; those of exercising, eating right, the various stimulus one might encounter in a
day and how one reacts to said stimulus can affect your day to day wellness.
I strongly believe that one can prevent even conquer ailments such as stress and depression with the above remedies.
This is what guided me to finding the ‘Lifestyle_and_Wellbeing_Data’ on kaggle.com.

# Data

The ‘Lifestyle_and_Wellbeing_Data’ was gathered using 12,757 survey responses, from July
2015 until February 2020.

![](https://github.com/scottschmidl/Lifestyle-and-Wellbeing/blob/master/images/columns.png)

# Hypothesis

I am interested in discovering which groups have the better or worse work-life balance according to this test.

Which brings me to my hypothesis:

1) Males have a work-life balance that is not as good as females. I believe that, in general, males put more energy into work and females split there energy into work-life.

2) Ages 21 to 35 have a worse work-life balance then the other age groups. I believe that due to the stresses of graduating college, starting a career,  beginning a family, and possibly moving to a new city this age range as a harder time managing their work-life balance.

3) If my first two hypothesis are correct, then I deduced that males who are 51 or more had a poor work life balance when compared to others, due to mid life crisis which can happen between 45 and 64 in males and last up to 10 years which is about twice as long as females.

# Closer Look

With these questions in mind I begin to take a closer look at my data. The first thing I did was look at the columns and inspect for areas with bad data. I added a 'bal_score' column which is the sum of the answers to each question, as they are numerical in nature, and found the min and max possible scores. I, then, isolated the data three times and by the columns: males and females, age ranges, and finally by males and females by ages.

From min_max_poss.py:

min possible score = 4
max possible score = 169

Upon completion I moved on to inspect the means of those three areas described below:

Means to note: 'males' are lower than females, '21 to 35' is lower than the others, and 21m to 35 is lower than the others. The latter is not what I initially expected.

![](https://github.com/scottschmidl/Lifestyle-and-Wellbeing/blob/master/images/compare_means.png)

# Visualization

The above results lead me to the below distributions. All of the results below are around 80 +- 5 over and 3 under. It appeared that this had the potential to be normally distributed, since 80 is about half. 

As I was unsure of the exact distribution I decided to plot against a kernel density estimation. KDE is a non-parametric estimate of the PDF. Non-parametrized means that the data distrubtion is unknown or known but with uncertain parameters. As you can see from the below graphs the data is nearly normal distributed with some quite large standard deviations.

![](https://github.com/scottschmidl/capstone-1/blob/master/images/compare_balscores_mf.png)

Figure 1: Comparing the balance scores of males and females

![](https://github.com/scottschmidl/capstone-1/blob/master/images/compare_balscores_ages.png)

Figure 2: Comparing the balance scores of four age ranges

![](https://github.com/scottschmidl/capstone-1/blob/master/images/compare_balscores_mf_age.png)

Figure 3: Comparing the balance scores of males and females by age

The above distributions, while nice, left me wanting a slightly better way to visualize what was actually gone on with the work-life balance scores. I made the below box plots to extract the min, first quartile, median, third quartile, and max values easily visible.

![](https://github.com/scottschmidl/capstone-1/blob/master/images/box_mf.png)

Figure 4: Comparing 5-number summary of males and females

![](https://github.com/scottschmidl/capstone-1/blob/master/images/box_ages.png)

Figure 5: Comparing 5-number summary of four age ranges

![](https://github.com/scottschmidl/capstone-1/blob/master/images/box_mf_age.png)

Figure 6: Comparing 5-number summary of males and females by age

# Conclusion

On figure 4 one can see that the females have a plot that is more nestled and with a higher mean. This leads me to conclude that more of their values are around the mean with stronger values in the north than in the south. If you compare this to the males who are more spread out to the south when compared to the females, then to north, one can conclude that the females have a much better handle on their work-life balance. These results lead me to not rejecting my eariler hypothesis.

On figure 5 one can see that not only is the mean lower on ages '21 to 35', but their plot also has less values to the north of the mean. Ages '51 or more' have the highest mean. I am compeled to conclude that ages '21 to 35' have the hardest time managing their work-balance, and therefore I can not reject my earlier hypothesis.

On figure 6 one can see that 'males, 21 to 35' have the lowest mean and overall lower values with 'males 36 to 50' and 'females 51 or more' leading the pack. These results are not what I expected and compele me to reject my earlier hypothesis and now I am interested to know why this is the case.

# Photo and Data Credits

The picture in my heading was webscraped from the main website:

Link to main website:

http://www.authentic-happiness.com/

The data was acquired from:

https://www.kaggle.com/ydalat/lifestyle-and-wellbeing-data

# Extras

Link to Work-Life Balance Test:

http://www.authentic-happiness.com/your-life-satisfaction-score

Questions and range of respones on test:

Q1) How many steps(in thousads) do you typically walk everyday?

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q2) How many people are very close to you?

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

Q3) How many people are very close to you?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q4) With how many people do you interact during a typical day?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q5) How many times do you donate your time or money to good causes?

[0, 1, 2, 3, 4, 5]

Q6) How sufficient is your income to cover basic life expensives?

[1, 2]

Q7) Of how many remarkable achievements are you proud?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q8) How many hours do you spend everyday doing about what you are passionate?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q9) In a typical week, how many times do you have the opportunity to think about yourself?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q10) How many recognitions have you received in your life?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q11) For how many years ahead is your life vision very clear?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q12) How many days of vacation do you typically lose every year?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q13) What is your body mass index range?

[1, 2] #1(below 25); 2(above 25)

Q14) How many new places do you visit?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q15) How well do you complete your weekly to-do lists?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q16) How many people do you help achieve a better life?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q17) How many fruits or vegetables do you eat everyday?

[0, 1, 2, 3, 4, 5]

Q18) In a typical day, how many hours do you experience 'flow'?

flow - mental state, in which you are fully immersed in peforming an activity. You then experience a feeling of energized focus, full involvement, and enjoyment in the process of this activity.

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Q19) How much stress do you typically experience everyday?

[0, 1, 2, 3, 4, 5]

Q20) How often do you shout or sulk at somebody?

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

