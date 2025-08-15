# department_distribution.py
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

# Your email for verification
email = "23f3003731@ds.study.iitm.ac.in"

# Sample dataset
data = pd.DataFrame({
    "employee_id": ["EMP001","EMP002","EMP003","EMP004","EMP005","EMP006","EMP007","EMP008","EMP009","EMP010"],
    "department": ["IT","Finance","R&D","IT","R&D","IT","Finance","IT","R&D","IT"],
    "region": ["Europe","Africa","Africa","Middle East","Europe","Asia","Europe","Africa","Asia","Europe"]
})

# Calculate frequency count for IT
it_count = data['department'].value_counts().get('IT', 0)
print(f"Frequency count for IT department: {it_count}")  # This must appear in HTML as text too

# Plot histogram
fig, ax = plt.subplots()
data['department'].value_counts().plot(kind='bar', color="#66c2a5", ax=ax)
ax.set_title(f"Department Distribution of Employees (IT count = {it_count})")
ax.set_xlabel("Department")
ax.set_ylabel("Number of Employees")

# Export as interactive HTML using mpld3
html_str = mpld3.fig_to_html(fig)
with open("department_distribution.html", "w") as f:
    f.write(html_str)
    # Append your email to HTML for verification
    f.write(f"<p>Email: {email}</p>")
