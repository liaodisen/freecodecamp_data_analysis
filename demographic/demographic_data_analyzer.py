import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    filepath = 'adult.data.csv'
    chart = pd.read_csv(filepath)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = chart['race']

    # What is the average age of men?
    men = chart[chart['sex'] == 'Male']
    average_age_men = round(men['age'].sum()/men['age'].count(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    degree = chart[chart['education'] == 'Bachelors']
    percentage_bachelors = round(degree['education'].count()*100/chart['education'].count(),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    advanced_ed = chart.loc[chart['education'].isin(advanced)]
    higher_education = round(advanced_ed['education'].count()*100/chart['education'].count(),1)
    lower_education = round(chart.loc[~(chart['education'].isin(advanced))].count()*100/chart['education'].count(),1)

    # percentage with salary >50K
    no_ad = chart.loc[~(chart['education'].isin(advanced))]
    higher_education_rich = round(advanced_ed[advanced_ed['salary'] == ">50K"].shape[0]*100/advanced_ed.shape[0],1)
    lower_education_rich = round(no_ad[no_ad['salary'] == ">50K"].shape[0]*100/no_ad.shape[0],1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = chart["hours-per-week"].min()
    
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = chart[chart["hours-per-week"] == 1].shape[0]

    rich_percentage = chart[(chart["hours-per-week"] == 1) & (chart['salary'] == '>50K')].shape[0]*100/num_min_workers

    # What country has the highest percentage of people that earn >50K?
    country = chart["native-country"].value_counts()
    times = ["a", 0]
    for i, j in country.items():
        percentage = round(chart[(chart['native-country']==i) & (chart['salary']=='>50K')].shape[0]*100/chart[chart['native-country']==i].shape[0],1)
        if percentage > times[1]:
            times[0] = i
            times[1] = percentage
    highest_earning_country = times[0]
    highest_earning_country_percentage = times[1]

    # Identify the most popular occupation for those who earn >50K in India.
    india = chart[(chart['native-country']=='India')&(chart['salary'] == '>50K')]
    top_IN_occupation = india["occupation"].value_counts().idxmax()

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
