temperatures = [73,74,75,71,69,72,76,73]

stack = []
answer = [0]*len(temperatures)

for idx, degree in enumerate(temperatures):
    while stack and stack[-1][1] < degree:
        index, value = stack.pop()
        answer[index] = idx - index
    stack.append([idx,degree])
    
print(answer)