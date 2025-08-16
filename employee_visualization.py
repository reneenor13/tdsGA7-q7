import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Email for verification: 23f3003731@ds.study.iitm.ac.in

def load_and_analyze_data():
    """Load employee data and perform department analysis"""
    
    # Load the dataset
    df = pd.read_csv('employee_data.csv')
    
    # Calculate frequency count for IT department
    it_count = df[df['department'] == 'IT'].shape[0]
    print(f"Frequency count for IT department: {it_count}")
    
    # Create department distribution visualization
    plt.figure(figsize=(12, 8))
    
    # Create histogram of departments
    department_counts = df['department'].value_counts()
    
    # Create a professional-looking histogram
    sns.set_style("whitegrid")
    colors = sns.color_palette("viridis", len(department_counts))
    
    plt.figure(figsize=(14, 8))
    bars = plt.bar(department_counts.index, department_counts.values, color=colors)
    
    # Styling for executive presentation
    plt.title('Employee Distribution Across Departments\nFinance Company Workforce Analysis', 
              fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Department', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Employees', fontsize=14, fontweight='bold')
    
    # Add value labels on bars
    for bar, count in zip(bars, department_counts.values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                str(count), ha='center', va='bottom', fontweight='bold')
    
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('department_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return df, it_count, department_counts

if __name__ == "__main__":
    # Contact email: 23f3003731@ds.study.iitm.ac.in
    df, it_count, dept_counts = load_and_analyze_data()
    
    print("\nDepartment Distribution Summary:")
    print(dept_counts)
    
    print(f"\nTotal employees analyzed: {len(df)}")
    print(f"IT department represents {(it_count/len(df)*100):.1f}% of workforce")
