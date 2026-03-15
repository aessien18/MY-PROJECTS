scores = list(map(float, input("Enter your score: ").split()))

scores =[score for score in scores ]
total = sum(scores)
count = len(scores)
average = total / count if count > 0 else 0

def calculate_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score < 70:   # 60–69
        return "B"
    elif 50 <= score < 60:   # 50–59
        return "C"
    elif 40 <= score < 50:   # 40–49
        return "D"
    else:                    # Anything below 40
        return "F"

print("\nGrades for each score:")
for score in scores:
    print(f"Score: {score} -> Grade:{calculate_grade(score)}")
print(f"\nTotal: {total}")
print(f"Count: {count}")
print(f"Average: {average:.2f}")
print(f"Average Grade:{calculate_grade(average)}")
