students = [
 {'group': 'A', 'scores': [3,5,4,4,5]},
 {'group': 'B', 'scores': [3,5,2,4,4,5,5]},
 {'group': 'C', 'scores': [5,5,5,5,5,5,5]}]
#print (sum(scores))
score_sum = 0
score_count = 0
for group_data in students:
    # group_data = {'group': 'A', 'scores': [3,5,4,4,5]}
    score_sum += sum(group_data['scores'])
    score_count += len(group_data['scores'])
print(score_sum/score_count)

for group_data in students:
    score_sum = sum(group_data['scores'])
    score_count = len(group_data['scores'])
    print(score_sum/score_count)

