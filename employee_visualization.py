# employee_viz.py
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Your email for verification
email = "23f3003731@ds.study.iitm.ac.in"

# Sample dataset
data = {
    "employee_id": ["EMP001","EMP002","EMP003","EMP004","EMP005","EMP006","EMP007","EMP008","EMP009","EMP010"],
    "department": ["IT","Finance","R&D","IT","R&D","IT","Finance","IT","R&D","IT"],
    "region": ["Europe","Africa","Africa","Middle East","Europe","Asia","Europe","Middle East","Asia","Europe"],
    "performance_score": [88.92,71.95,92.5,79.05,87.83,91.2,75.5,83.7,88.0,90.1],
    "years_experience": [3,1,12,8,15,5,2,7,10,4],
    "satisfaction_rating": [3.5,4.9,3.1,4.8,4.3,3.9,4.2,4.0,3.8,4.5]
}

df = pd.DataFrame(data)

# Calculate IT frequency
it_count = df[df["department"] == "IT"].shape[0]
print(f"Frequency of IT department: {it_count}")

# Plot department histogram
plt.figure(figsize=(8,6))
df['department'].value_counts().plot(kind='bar', color="#66c2a5")
plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

# Save to HTML using mpld3
html_str = mpld3.fig_to_html(plt.gcf())
# Add email and IT count in HTML
html_str = f"<p>Email: {email}</p>\n<p>IT Department Count: {it_count}</p>\n" + html_str

with open("department_distribution.html", "w") as f:
    f.write(html_str)

print("HTML file saved with visualization, email, and IT count!")
