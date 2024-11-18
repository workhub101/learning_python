scores = [85,92,-1,78,-1,95,88,-1,70]
total_score= 0
count= 0

for score in scores:
    if score == -1:
        continue
    print(score)
    total_score += score
    count += 1
average = total_score / count
print("Average score:",average)