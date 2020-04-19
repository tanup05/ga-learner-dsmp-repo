# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]
data = pd.read_csv(path)
#Code starts here

#Create a sample of 'data' using "sample()" with n=sample_size and random_state=0 and save it in a variable called 'data_sample'
data_sample = data.sample(n=sample_size, random_state = 0)

#Store the mean of installment column of 'sample_data' in a variable called 'sample_mean'
sample_mean = data_sample['installment'].mean()

#Store the standard deviation of installment column of 'sample_data' in a variable called 'sample_std'

sample_std = data_sample['installment'].std()

#Find the margin of error using 'z_critical'(given),'sample_std' and 'sample_size' and save it in a variable called 'margin_of_error'

margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))

#Find the confindence interval using 'sample_mean' and 'margin_of_error' and save it in a variable called 'confidence_interval'.

upper = sample_mean + margin_of_error
lower = sample_mean - margin_of_error
confidence_interval = (lower, upper)

#Store the mean of installment column of 'data' in a variable called 'true_mean'
true_mean = data['installment'].mean()

#Print and check if 'true_mean' falls in the range of 'confidence_interval'

print("True mean = ", true_mean, "\n Confidence interval", confidence_interval)




# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here

fig, axes = plt.subplots(nrows=3, ncols=1)

for i in range(0, len(sample_size)):
    m = []
    for j in range(1000):
        data_installment = data['installment'].sample(n=sample_size[i]).mean()
        m.append(data_installment)
    mean_series = pd.Series(m)
    axes[i].plot(mean_series)


# --------------
#Importing header files

#The bank manager believes that people with purpose as 'small_business' have been given int.rate more due to the risk assosciated

#Let's do a hypothesis testing(one-sided) on that belief

#Null Hypothesis H0:μ=H_0: \mu =H0​:μ= 12 %

#Meaning: There is no difference in interest rate being given to people with purpose as 'small_business'

#Alternate Hypothesis H1:μ>H_1: \mu >H1​:μ>12 %

#Meaning: Interest rate being given to people with purpose as 'small_business' is higher than the average interest rate

from statsmodels.stats.weightstats import ztest

#Code starts here

#From the column int.rate of 'data', remove the % character and convert the column into float.

data['int.rate'] = data['int.rate'].map(lambda x: x.rstrip('%'))
data['int.rate'] = data['int.rate'].astype('float')

#After that divide the values of int.rate with 100 and store the result back to the column 'int.rate'

data['int.rate'] = data['int.rate']/100

#Apply "ztest()" with x1 as data[data['purpose']=='small_business']['int.rate'] and value as data['int.rate'].mean(), alternative='larger'(WHY?) and save the results in 'z_statistic' and 'p_value' respectively

z_statistic, p_value = ztest(x1 = data[data['purpose']=='small_business']['int.rate'], value = data['int.rate'].mean(), alternative = 'larger')

if p_value< 0.05:
    print('Reject')
else:
    print('Accept')




# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#The bank thinks that monthly installments (installment) customers have to pay might have some sort of effect on loan defaulters

#Let's do hypothesis testing(two-sided) on that

#Code starts here

z_statistic, p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'], x2=data[data['paid.back.loan']=='Yes']['installment'])

if p_value < 0.05:
    print('Reject')
else:
    print('Accept')


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here

#Create a variable 'yes' which is the value counts of purpose when paid.back.loan in 'data' is Yes

yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()

#Create a variable 'no' which is the value counts of purpose when paid.back.loan in 'data' is No

no = data[data['paid.back.loan']=='No']['purpose'].value_counts()

#Concat 'yes.transpose()'(transpose of 'yes') and 'no.transpose()'(transpose of 'no') along axis=1 with keys= ['Yes','No'] and store it in a variable called 'observed'

observed = pd.concat([yes.transpose(), no.transpose()], axis = 1, keys = ['Yes', 'No'])

#Apply "chi2_contingency()" on 'observed' and store the result in variables named chi2, p, dof, ex respectively.

chi2, p, dof, ex = chi2_contingency(observed)

#Compare chi2 with critical_value(given)

if chi2 > critical_value:
    print('Reject')
else:
    print('Accept')




