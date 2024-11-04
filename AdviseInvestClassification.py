import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn import tree

df = pd.read_csv('adviseinvest.csv')

pd.set_option('display.max_columns', None)

print(df.head())

# benchmark accuracy - majority class classifier
print(df['answered'].mean())

df_new = df[['answered', 'income']]

print(df_new.head())
print(df_new.describe())

df_clean = df_new[df_new['income'] > 0]

print(df_clean.head())

print(df_clean.describe())

# declare x and y variables
x = df_clean[['income']]
y = df_clean[['answered']]

# create first tree with no train/test split
income_tree = DecisionTreeClassifier(criterion='entropy', max_depth=2, random_state=10)
income_tree = income_tree.fit(x, y)

pred = income_tree.predict(x)

print(f'Accuracy income_tree: {metrics.accuracy_score(y, pred)}')

# create train/test data split to train the model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

income_tree_2 = DecisionTreeClassifier(criterion='entropy', max_depth=2)

income_tree_2 = income_tree_2.fit(x_train, y_train)

pred = income_tree_2.predict(x_test)

print(f'Accuracy income_tree_2: {metrics.accuracy_score(y_test, pred)}')
