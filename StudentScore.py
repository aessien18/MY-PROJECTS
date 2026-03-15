import matplotlib.pyplot as plt


Students  = {
    "John": [85, 90, 78, 92,98,67,89,90],
    "Alice": [67, 17, 95, 12,76,45,67,34],
    "Bob": [78, 82, 85, 80,90,88,92,91],
    "Eve": [90, 95, 48, 67,75,80,58,44],
    "Angela":[ 88, 90, 92, 85,80,78,84,89],
    "Michael":[ 85, 88, 90, 92, 80,78,84,89],
    "David":[ 90, 92, 85, 80,78,84,89,91],
    "Sarah":[ 88, 55, 80,48,84,89,56,90],
    "Tom":[ 85, 80,78,84,89,91,90,88],
    "Emily":[ 80,78,84,69,91,67,88,85],
    "Jessica":[ 78,12,89,61,24,88,85,80],
    "Wendy":[ 84,37,91,47,88,85,45,78],
    "Daniel":[ 89,91,90,88,85,60,45,84],
    "Sophia":[ 91,90,45,85,70,78,84,89],
    "James":[ 90,45,85,40,78,84,74,91],
    "Maria":[ 45,85,50,56,84,89,91,90],
}

# Calculate average scores for each student
average_scores = {student: sum(scores) / len(scores) for student, scores in Students.items()}
# Sort students by average score
name = list(average_scores.keys())
avg = list(average_scores.values())
# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(name, avg, color='skyblue')
plt.xlabel('Students')
plt.ylabel('Average Score')
plt.title('Average Scores of Students')
plt.xticks(rotation=45)
plt.ylim(0, 100)
plt.show()