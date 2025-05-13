
student_scores = [123, 312 ,456 ,363 ,234 ,123 ,423 ,68, 630 ,342]

total_exam_score = sum(student_scores)

# These are the same thing

sum = 0
for score in student_scores:
    sum += score

print(f"This is the sum with the function: {total_exam_score}")
print(f"This is the sum out of the function: {sum}")