
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

print(max(student_scores)) # This will bring the higher value from the list

max_score = 0
for score in student_scores:
    if score > max_score: # This function will do the same as the 'max' function
        max_score = score

print(max_score)