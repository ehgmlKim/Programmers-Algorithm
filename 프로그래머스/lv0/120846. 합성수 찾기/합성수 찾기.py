def solution(n):
    answer = []
    for i in range(1, n+1) :
        count = 0
        for j in range(1, n+1) :
            if i%j==0 :
                count += 1
            if count >= 3 :
                answer.append(i)
    return len(set(answer))