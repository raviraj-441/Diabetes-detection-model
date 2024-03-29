# -*- coding: utf-8 -*-
"""Diabetes_detection_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UY-g6kfHGmKJ-XpYaWf06qXG3PAfwbm6

#Data Collection
"""

import pandas as pd

df = pd.read_csv('diabetes.csv')
df.head()

"""#Data Preprocessing"""

df_cleaned = df.dropna()

"""#Exploratory Data Analysis (EDA)"""

import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(df_cleaned, hue='Outcome', diag_kind='kde')
plt.show()

corr_matrix = df_cleaned.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

"""#Feature Selection/Engineering"""

features = df_cleaned[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]

"""#Model Selection"""

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

model_rf = RandomForestClassifier(max_depth=30,min_samples_leaf=2,min_samples_split=10, n_estimators=200)
model_gb = GradientBoostingClassifier(learning_rate=0.1,max_depth=3, min_samples_leaf= 4, min_samples_split= 5, n_estimators= 50)

"""#Model Training"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, df_cleaned['Outcome'], test_size=0.2, random_state=42)

model_rf.fit(X_train, y_train)
model_gb.fit(X_train, y_train)

"""#Model Evaluation"""

from sklearn.metrics import accuracy_score

predictions_rf_test = model_rf.predict(X_test)
accuracy_rf_test = accuracy_score(y_test, predictions_rf_test)
print(f"Random Forest Testing Accuracy: {accuracy_rf_test}")

predictions_gb_test = model_gb.predict(X_test)
accuracy_gb_test = accuracy_score(y_test, predictions_gb_test)
print(f"Gradient Boosting Testing Accuracy: {accuracy_gb_test}")

"""#Validation"""

X_validation, X_unused, y_validation, y_unused = train_test_split(X_test, y_test, test_size=0.5, random_state=42)

predictions_rf_validation = model_rf.predict(X_validation)
accuracy_rf_validation = accuracy_score(y_validation, predictions_rf_validation)
print(f"Random Forest Validation Accuracy: {accuracy_rf_validation}")

predictions_gb_validation = model_gb.predict(X_validation)
accuracy_gb_validation = accuracy_score(y_validation, predictions_gb_validation)
print(f"Gradient Boosting Validation Accuracy: {accuracy_gb_validation}")

"""#Interpretability"""

feature_importance_rf = model_rf.feature_importances_
print(f"Random Forest Feature Importance: {feature_importance_rf}")
feature_importance_gb = model_gb.feature_importances_
print(f"Gradient Boosting Feature Importance:{feature_importance_gb}")

"""#Additional Visualization"""

sns.boxplot(x='Outcome', y='Age', data=df_cleaned)
plt.title('Boxplot for Age and Outcome')
plt.show()

sns.countplot(x='Outcome', data=df_cleaned)
plt.title('Outcome Distribution')
plt.show()