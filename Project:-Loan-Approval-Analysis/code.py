# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank = pd.DataFrame(bank_data)
categorical_var = bank.select_dtypes(include = 'object')
#print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
#print(numerical_var)
banks = bank.drop(['Loan_ID'],axis=1)

bank_mode = banks.mode()
for x in banks.columns.values:
        banks[x]=banks[x].fillna(value=bank_mode[x].iloc[0])

avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values=['LoanAmount'],aggfunc=np.mean)

percentage_se = 9.12
percentage_nse = 59.61
bid_loan_term = 554
loan_groupby = banks.groupby('Loan_Status')

mean_values = loan_groupby.mean()


print(mean_values)








