import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

df = pd.read_csv('adviseInvest.csv')

answered_map = {0:'no', 1:'yes'}

df['answered'] = df['answered'].map(answered_map)
df['answered'] = df['answered'].astype('category')

print(df.info())

grouped_data = df.groupby('answered')['num_accts'].sum().reset_index()

plt.bar(grouped_data['answered'], grouped_data['num_accts'], color=['blue', 'orange'])

plt.title("Answered by Number of Accounts")
plt.xlabel('Answered (Yes | No)')
plt.ylabel('Number of Accounts')
plt.show()

print(df['mobile'].value_counts())

df['mobile'] = df['mobile'].map({0: 'No', 1: 'Yes'}).astype('category')

# Calculate counts for each combination of 'mobile' and 'answered'
count_table = df.groupby(['mobile', 'answered']).size().unstack(fill_value=0)

# Calculate proportions of total customers
proportion_table = count_table / count_table.values.sum()

# Plot the proportion chart
proportion_table.plot(kind='bar', stacked=True, color=['orange', 'blue'], figsize=(8, 6))

# Add title and labels
plt.title('Proportion of Total Customers Who Answered by Mobile Ownership')
plt.xlabel('Mobile Ownership')
plt.ylabel('Proportion of Total Customers')
plt.legend(title='Answered', labels=['No', 'Yes'])

# Display the chart
plt.xticks(rotation=0)
plt.show()

print(df.head())

