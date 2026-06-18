import pandas as pd
import numpy as np
import random

# Required seeds
random.seed(123)
np.random.seed(123)

# Configuration
NUM_RECORDS = 100

course_names = [
    "Intro to Analytics",
    "Python for Beginners",
    "SQL Basics",
    "Tableau Fundamentals",
    "Statistics 101"
]

# Realistic grade distribution
grades = ["F", "D", "C", "B", "A"]
grade_probs = [0.03, 0.07, 0.35, 0.40, 0.15]

# Realistic completion status distribution
statuses = ["Completed", "Dropped", "In Progress"]
status_probs = [0.80, 0.10, 0.10]

records = []

for i in range(NUM_RECORDS):

    enrollment_id = f"ENR-{100000 + i:06d}"

    course_name = random.choice(course_names)

    enrollment_year = random.randint(2022, 2026)

    final_grade = np.random.choice(grades, p=grade_probs)

    # Hours studied centered around 30 hours
    hours_studied = round(max(5, np.random.normal(loc=30, scale=8)), 1)

    completion_status = np.random.choice(statuses, p=status_probs)

    records.append({
        "enrollment_id": enrollment_id,
        "course_name": course_name,
        "enrollment_year": enrollment_year,
        "final_grade": final_grade,
        "hours_studied": hours_studied,
        "completion_status": completion_status
    })

# Assemble final DataFrame using Pandas
enrollments_df = pd.DataFrame(records)

# Save dataset
enrollments_df.to_csv("skyline_enrollments.csv", index=False)

# Output required information
print("First 10 Rows:")
print(enrollments_df.head(10))

print("\nShape:")
print(enrollments_df.shape)

print("\nColumn Types:")
print(enrollments_df.dtypes)