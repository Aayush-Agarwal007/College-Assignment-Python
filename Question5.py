def calculate_average_percentage(scores):
    if not scores:
        return 0

    total_score = sum(scores.values())

    number_of_subjects = len(scores)
    average_percentage = total_score / number_of_subjects
    
    return average_percentage
student_scores = {
    'Math': 85,
    'Science': 90,
    'English': 78,
    'History': 88,
    'Geography': 92
}

average = calculate_average_percentage(student_scores)
print(f"The average percentage of the student is: {average:.2f}%")
