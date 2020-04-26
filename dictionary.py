scores = {'John': 1000, 'booby': 2000, "Jany": 4200}
print(scores)
print(scores['booby'])

scores['Roger'] = 3200
print(scores)

points = {}
points['mr_A'] = 10.2
points['mr_B'] = 15.4
points['mr_C'] = 22.8
print(points)

for k, v in scores.items():
    print(k, v)
