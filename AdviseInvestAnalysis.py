# Code Below:
import pandas as pd

df = pd.read_csv('adviseinvest.csv')
pd.set_option('display.max_columns', None)

print(f'df.head():\n:{df.head()}')

print(f'df.describe():\n{df.describe()}')

df_clean = df.dropna()

print(df_clean['num_accts'].unique())

df_clean = df_clean[(df_clean['num_accts']<=4) & (df_clean['income']>0)]
print(df_clean.describe())

#job, product, chk_acct, sav_acct

job_mapping = {0:'unemployed',1:'entry level position',2:'midlevel position', 3:'management/ self emplyed/ highly qualified employee/ office'}
df_clean['job'] = df_clean['job'].map(job_mapping)
df_clean['job'] = df_clean['job'].astype('category')

product_mapping = {0: 'customer did not answer call', 1: 'customer answered but did not purchase a product', 2:'customer answered and purchased Beginner plan', 3:'customer answered and purchased Intermediate plan', 4:'customer answered and purchased Advanced plan'}
df_clean['product'] = df_clean['product'].map(product_mapping)
df_clean['product'] = df_clean['product'].astype('category')

chk_acct_mapping = {0 :'no checking account', 1:'checking < 200 USD', 2 :'200 < checking < 2000 USD', 3:'2000 < checking < 35000 USD', 4:'>= 3500 USD'}
df_clean['chk_acct'] = df_clean['chk_acct'].map(chk_acct_mapping)
df_clean['chk_acct'] = df_clean['chk_acct'].astype('category')

sav_acct_mapping = {0 :'no savings account', 1 :'100 <= savings < 500 USD', 2 :'500 <= savings < 2000 USD', 3 :'2000 < savings < 35000 USD', 4:' >= 3500 USD'}
df_clean['sav_acct'] = df_clean['sav_acct'].map(sav_acct_mapping)
df_clean['sav_acct'] = df_clean['sav_acct'].astype('category')

print(f'Data frame with new categories:\n{df_clean.head()}')

answered_mean = df_clean['answered'].mean()
print(f'Average answered: {answered_mean}')

# Average answered = 0.5465947998237228