
import pandas as pd
import numpy as np

# 1. Loading dataset
df = pd.read_csv(
    r"C:\Users\admin\Desktop\pyhton\Numpy\Part 2\indian employee dataset\employees.csv"
)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("Column Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

# 2. Checking missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Replace infinite values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# 4. Fill missing salary values
if 'salary' in df.columns:
    df['salary'] = pd.to_numeric(df['salary'], errors='coerce')
    df['salary'] = df['salary'].fillna(df['salary'].mean())

# 5. Fill performance rating if the column exists
if 'performance rating' in df.columns:
    df['performance rating'] = pd.to_numeric(
        df['performance rating'], errors='coerce'
    )
    df['performance rating'] = df['performance rating'].fillna(
        df['performance rating'].median()
    )

# 6. Fill missing values in other numeric columns
numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].fillna(
    df[numeric_cols].mean()
)

# 7. Remove duplicate records
df.drop_duplicates(inplace=True)

# 8. Replace negative salaries with the mean of valid salaries
if 'salary' in df.columns:
    valid_salaries = df.loc[df['salary'] >= 0, 'salary']

    if not valid_salaries.empty:
        salary_mean = valid_salaries.mean()

        df.loc[df['salary'] < 0, 'salary'] = salary_mean

        # 9. Calculate salary mean and standard deviation
        salary_mean = df['salary'].mean()
        salary_std = df['salary'].std()

        # 10. Remove salary outliers
        if pd.notna(salary_std) and salary_std > 0:
            lower_bound = salary_mean - (3 * salary_std)
            upper_bound = salary_mean + (3 * salary_std)

            df = df[
                (df['salary'] >= lower_bound) &
                (df['salary'] <= upper_bound)
            ]

# 11. Save cleaned dataset
df.to_csv("Cleaned_indian_emp_data.csv", index=False)

print("\nCleaned_indian_emp_data.csv saved successfully!")
print("Final dataset shape:", df.shape)

# 12. Check missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
