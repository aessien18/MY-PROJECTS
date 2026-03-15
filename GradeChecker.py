import re

raw = input("Enter your score(s), separated by spaces or commas: ")
parts = [p.strip() for p in re.split(r"[\s,]+", raw.strip()) if p.strip()]

scores = []
for token in parts:
    try:
        scores.append(float(token))
    except ValueError:
        print(f"Skipping invalid score: {token}")

if not scores:
    print("No valid numeric scores entered.")
else:
    total = sum(scores)
    count = len(scores)
    average = total / count if count > 0 else 0

    def calculate_grade(score):
        if 70 <= score <= 100:
            return "A", "Excellent"
        elif 60 <= score < 70:
            return "B", "Good"
        elif 50 <= score < 60:
            return "C", "Satisfactory"
        elif 40 <= score < 50:
            return "D", "Unsatisfactory"
        else:
            return "F", "Fail"

    print("\nGrades for each score:")
    for score in scores:
        grade, feedback = calculate_grade(score)
        print(f"Score: {score} -> Grade: {grade} ({feedback})")

    avg_grade, avg_feedback = calculate_grade(average)
    print(f"\nTotal: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")
    print(f"Average Grade: {avg_grade} ({avg_feedback})")
