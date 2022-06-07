experiment = [1, 2, 3, 4, 5]
count = len(experiment)

for i in range(count - 1):
    experiment.insert(2*i+1, (experiment[2*i] + experiment[2*i+1])/2)

print(experiment)