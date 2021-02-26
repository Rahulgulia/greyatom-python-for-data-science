# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census = np.concatenate([data,new_record])
age = np.array([census[:,0]])
max_age = np.max(age)
min_age = np.min(age)
age_mean = age.mean()
age_std = np.std(age)
race = np.array([census[:,2]])
race_0 = np.array([row for row in census if row[2] == 0])
race_1 = np.array([row for row in census if row[2] == 1])
race_2 = np.array([row for row in census if row[2] == 2])
race_3 = np.array([row for row in census if row[2] == 3])
race_4 = np.array([row for row in census if row[2] == 4])
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
mino = [len_0,len_1,len_2,len_3,len_4]
minoa = np.array(mino)
minority_race = mino.index(np.min(minoa))
print(minority_race)
senior_citizens = np.array([row for row in census if row[0] > 60])
working_hours_sum = np.sum(np.array([senior_citizens[:,6]]))
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)
high = np.array([row for row in census if row[1] > 10])
low = np.array([row for row in census if row[1] <= 10])
avg_pay_high = np.mean(np.array([high[:,7]]))
avg_pay_low = np.mean(np.array([low[:,7]]))
print(avg_pay_high,'/n',avg_pay_low)


