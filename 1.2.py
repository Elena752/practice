def combination(candidates, target):
    candidates.sort()
    result = []
    def backtrack(start, path, target):
        if target == 0:
            result.append(path.copy())
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            path.append(candidates[i])
            backtrack(i + 1, path, target - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result

candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(combination(candidates, target))