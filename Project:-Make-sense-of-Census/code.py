# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#Load the dataset and store it in a variable called data using np.genfromtxt()

data = np.genfromtxt(path, delimiter=",", skip_header=1)
print("Data: \n\n", data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

census = np.concatenate((data, new_record), axis=0)
print("Census", census)


# --------------
#Code starts here

#Create a new array called 'age' by taking only age column(age is the column with index 0) of 'census' array.
age = census[0:, :1]
print("Age array:", age)

#Find the max age and store it in a variable called 'max_age'.
max_age = age.max()
#print("Max age", max_age)
#Find the min age and store it in a variable called 'min_age'.
min_age = age.min()

#Find the mean of age and store it in a variable called 'age_mean'.
age_mean = age.mean()

#Standard deviation of the age and store it in the variable 'age_std'.
age_std = np.std(age)


# --------------
#Code starts here
#------------#

#Create four different arrays by subsetting 'census' array by Race column(Race is the column with index 2) and save them in 'race_0','race_1', 'race_2', 'race_3' and 'race_4' respectively(Meaning: Store the array where 'race'column has value 0 in 'race_0', so on and so forth)#

#------------#

#race_0: race column having value 0.
race0_cond = np.where(census[:, 2]==0)
race_0 = census[race0_cond, 2]
print("race_0", race_0)

#race_1: race column having value 1.
race1_cond = np.where(census[:, 2]==1)
race_1 = census[race1_cond, 2]
print("race_1", race_1)

#race_2: race column having value 2.
race2_cond = np.where(census[:, 2]==2)
race_2 = census[race2_cond, 2]
print("race_2", race_2)

#race_3: race column having value 3.
race3_cond = np.where(census[:, 2]==3)
race_3 = census[race3_cond, 2]
print("race_3", race_3)

#race_4: race column having value 4.
race4_cond = np.where(census[:, 2]==4)
race_4 = census[race4_cond, 2]
print("race_4", race_4)

#Store the length of the above created arrays in len_0 ... len_4 respectively.
len_0 = race_0.size
print("len_0", len_0)

len_1 = race_1.size
print("len_1", len_1)

len_2 = race_2.size
print("len_2", len_2)

len_3 = race_3.size
print("len_3", len_3)

len_4 = race_4.size
print("len_4", len_4)

#Find out which is the race with minimum no. of citizens.
min_citizen = [len_0, len_1, len_2, len_3, len_4]

minority_race = min_citizen.index(min(min_citizen))
print(minority_race)


# --------------
#Code starts here

seniors = np.where(census[:, 0] > 60)
#print(seniors)

senior_citizens = census[seniors, 0]
print("Senior citizens:", senior_citizens)

#working_hours = census[:, 6]

working_hours_sum = census[seniors, 6].sum()

print("Working hours sum", working_hours_sum)

senior_citizens_len = senior_citizens.size
print("Length of senior_citizens", senior_citizens_len)

avg_working_hours = working_hours_sum/senior_citizens_len
print("Average working hours:", avg_working_hours)


# --------------
#Code starts here

#Creating a subset 'high' by filtering census according to education-num>10.

high_education = np.where(census[:, 1] > 10)
high = census[high_education, 1]
#print("high:", high)

#Creating a subset 'high' by filtering census according to education-num>10.

low_education = np.where(census[:, 1] <= 10)
low = census[low_education, 1]
#print("low:", low)

#Find the mean of income column(income is the column with index 7) of 'high' array.

high_income = census[high_education, 7]
avg_pay_high = high_income.mean()
print("Average pay for highly educated:", avg_pay_high)

#Find the mean of income column(income is the column with index 7) of 'high' array.

low_income = census[low_education, 7]
avg_pay_low = low_income.mean()
print("Average pay for lower educated:", avg_pay_low)


