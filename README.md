# tdsGA7-q7
# Employee Department Distribution Visualization

This project demonstrates a simple data visualization of employee department distributions using Python, pandas, seaborn, and mpld3. The interactive visualization is saved as an HTML file for web deployment.

---

## Dataset

`employee_data.csv` contains information about 100 employees across departments and regions. Columns:

- `employee_id` – Unique identifier  
- `department` – Employee department (IT, Finance, R&D, etc.)  
- `region` – Geographic region  
- `performance_score` – Performance score  
- `years_experience` – Years of experience  
- `satisfaction_rating` – Satisfaction rating  

Sample:

employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,IT,Europe,88.92,3,3.5
EMP002,Finance,Africa,71.95,1,4.9
EMP003,R&D,Africa,92.5,12,3.1
EMP004,IT,Middle East,79.05,8,4.8
EMP005,R&D,Europe,87.83,15,4.3


---

## Python Script

**employee_visualization.py**:

1. Loads the dataset  
2. Prints frequency of IT department employees  
3. Creates a department distribution histogram  
4. Saves the visualization as `department_distribution.html`  

**Verification Email:** 23f3003731@ds.study.iitm.ac.in

---

## How to Run

```bash
pip install pandas matplotlib seaborn mpld3
python employee_visualization.py
