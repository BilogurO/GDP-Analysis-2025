import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer

# Якщо запускаєш локально (не з Power BI), раскоментуй / відредагуй шлях:
# dataset = pd.read_csv('../data/2020-2025.csv')

# Pivot the data from long to wide format for modeling
df_wide = dataset.pivot_table(index='Country', columns='Year', values='GDP', aggfunc='sum')
df_wide = df_wide.reset_index()
df_wide.columns.name = None
df_wide = df_wide.rename(columns={'Country': 'Country'})

# IMPORTANT FIX: Encode Country on the entire dataset BEFORE splitting
le = LabelEncoder()
df_wide['Country_encoded'] = le.fit_transform(df_wide['Country'])

# Separate data for 2025 and earlier years
df_2025 = df_wide[['Country', 2025]].dropna()

# Drop rows where target (2025) is missing
df_train = pd.merge(df_wide.drop(columns=[2025]), df_2025, on='Country', how='inner')

# Features & Target
features_list = ['Country_encoded', 2020, 2021, 2022, 2023, 2024]
X_train = df_train[features_list]
y_train = df_train[2025]

# IMPORTANT FIX: Convert column names to strings
X_train.columns = X_train.columns.astype(str)

# Handle missing values
imputer = SimpleImputer(strategy="mean")
X_train = imputer.fit_transform(X_train)
y_train = np.array(y_train)

# Train the model (using Random Forest as a robust choice)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Make predictions for all countries in the original dataset
df_predict = df_wide.copy()

# IMPORTANT FIX: Convert column names to strings for prediction
df_predict.columns = df_predict.columns.astype(str)
X_predict = df_predict[list(map(str, features_list))]

y_pred = model.predict(X_predict)
df_predict['Predicted_2025_GDP'] = y_pred

# Merge predictions back with the original long-format dataset
final_df = pd.merge(dataset, df_predict[['Country', 'Predicted_2025_GDP']], on='Country', how='left')

# Return the new DataFrame to Power BI
output = final_df
