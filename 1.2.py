candidates = [1, 2, 3, 5]
target = 6
for i in range(len(candidates)):
    a = [candidates[i]]
    x = candidates[i]
    if x == target:
        print(x)
        continue
    for j in range(len(candidates)):
        if i == j:
            continue
        x += candidates[j]
        a.append(candidates[j])
        if x == target:
            print(a)
        elif x > target:
            break
