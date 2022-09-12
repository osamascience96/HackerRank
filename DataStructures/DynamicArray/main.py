def Perform(n, queries):
    MultArr = [] #Multidimensional Arr
    
    lastAnswer = 0
    lastAnswerArr = [] #single dimenstion arr

    # init the n values in resultArr
    for _ in range(n):
        MultArr.append([])
    
    
    # iterate the queries
    for query in queries:
        type = query[0]
        x = query[1]
        y = query[2]

        if type == 1:
            index = ( (x ^ lastAnswer) % n)
            MultArr[index].append(y)
        elif type == 2:
            index = ( (x ^ lastAnswer) % n)
            lastAnswer = MultArr[index][(y % len(MultArr[index]))]
            lastAnswerArr.append(lastAnswer)

    return lastAnswerArr;

n = 2
queries = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]

# Call the function to perform
result = Perform(n, queries)
print(result)