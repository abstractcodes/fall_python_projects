scores_file = open("student.txt", "r")
for line in scores_file:
    student_info = line.split()
    student_name = student_info[0]
    total_score = 0.0
    score_count = 3
    for i in range(0, score_count):
        total_score += float(student_info[i + 1])
    average = total_score/score_count
    print(student_name, average)