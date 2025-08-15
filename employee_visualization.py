# employee_visualization.py
# Data Visualization: Employee Department Distribution
# Email for verification: 23f3003731@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3

# Load dataset
data = pd.read_csv('employee_data.csv')

# Count frequency of the "IT" department
it_count = data[data['department'] == 'IT'].shape[0]
print(f'Number of employees in IT department: {it_count}')

# Create a histogram of department distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='department', data=data, palette='Set2')
plt.title('Department Distribution of Employees', fontsize=16)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Number of Employees', fontsize=12)

# Save visualization as HTML
html_file = 'department_distribution.html'
mpld3.save_html(plt.gcf(), html_file)
print(f'Histogram saved as {html_file}')

# Show plot (optional)
# mpld3.show()
