import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = np.round(df.loc[df['sex']=='Male',['age']].mean(skipna=True),1)['age']

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = np.round(((df.loc[df['education']=='Bachelors',['education']].count()/df['education'].count())*100),1)['education']

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    edu=pd.Series(data=['Bachelors','Masters','Doctorate'])
    educ = df.loc[df['education'].isin(edu) ,['education','salary']]

    # percentage with salary >50K
    higher_education = pd.DataFrame((educ.loc[educ['salary'] == '>50K',['education']].count()/df.loc[df['salary']=='>50K'].count())*100)
    lower_education = pd.DataFrame((educ.loc[educ['salary'] == '<=50K',['education']].count()/df.loc[df['salary']=='>50K'].count())*100)
    higher_education_rich = np.round(higher_education.loc['education'].values,1)
    lower_education_rich = np.round(lower_education.loc['education'].values,1)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    min_hours_df = df.loc[df['hours-per-week'] == min_work_hours]
    min_hours_great_salary = min_hours_df.loc[min_hours_df['salary'] == '>50K']
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(min_hours_great_salary)
    rich_percentage = np.round((len(min_hours_great_salary)/len(min_hours_df))*100,1)

    # What country has the highest percentage of people that earn >50K?
    greater_salary = pd.DataFrame(df.loc[df['salary'] == '>50K',['native-country']].value_counts())
    
    #greater_salary.rename(columns={'count':'total'}, inplace = True)
    highest_earning_country = greater_salary.iloc[0].name

    highest_earning_country_percentage = np.round((greater_salary.iloc[0][0]/df['salary'].value_counts().sum() * 100), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    high_salary = pd.DataFrame(df.loc[df['salary'] == '>50K'])
    Ind = high_salary.loc[high_salary['native-country']=='India',['occupation']].value_counts()
    top_IN_occupation = Ind.index[0][0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
