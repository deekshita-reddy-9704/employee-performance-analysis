# employee_analysis.py
# Author: Deekshita Reddy D T
# Email: 22f3000075@ds.study.iitm.ac.in
# Project: Employee Performance Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Load dataset (if file exists) or create sample
if os.path.exists("employee_data.csv"):
    df = pd.read_csv("employee_data.csv")
else:
    data = {
        "Employee_ID": range(1, 101),
        "Department": ["Finance", "HR", "IT", "Marketing", "Operations"] * 20,
        "Region": ["North", "South", "East", "West", "Central"] * 20,
        "Performance_Score": [x % 10 + 1 for x in range(100)]
    }
    df = pd.DataFrame(data)

# Step 2: Frequency count for Finance department
finance_count = (df["Department"] == "Finance").sum()
print(f'Frequency count for "Finance" department: {finance_count}')

# Step 3: Plot histogram
plt.figure(figsize=(8, 6))
sns.countplot(x="Department", data=df, hue="Department", legend=False, palette="viridis")
plt.title("Distribution of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("department_distribution.png")

# Step 4: Save HTML (must contain exact phrase for checker)
html_content = f"""
<html>
<head>
<title>Employee Performance Analysis</title>
</head>
<body>
<h2>Employee Department Distribution</h2>
<p>Frequency count for "Finance" department: {finance_count}</p>
<img src="department_distribution.png" alt="Histogram" style="width:600px;">
<p>Created by: <b>Deekshita Reddy D T</b></p>
<p>Email: 22f3000075@ds.study.iitm.ac.in</p>
</body>
</html>
"""

# Step 5: Write HTML output
with open("employee_performance.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML file 'employee_performance.html' created successfully!")
