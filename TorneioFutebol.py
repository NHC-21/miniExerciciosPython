times = []
j = l = 0

for c in range(0, 3):
    times.append(str(input('Digite um time de futebol: ')))
for i in range(0, 1):
    for j in range(0, 2):
        j += 1
        print(times[i], ' [] x [] ', times[j])
for i in range(1, 2):
    for j in range(0, 2):
        print(times[i], ' [] x [] ', times[l])
        l += 2
for i in range(2, 3):
    l = 0
    for j in range(1, 3):
        print(times[i], ' [] x [] ', times[l])
        l += 1
#print(times[0], times[1])
#print(times[0], times[2])
#print(times[1], times[0])
#print(times[1], times[2])
#print(times[2], times[0])
#print(times[2], times[1])
