def solution(numbers):
    answer = ''
    new_arr = []
    numbers = sorted(numbers, key = lambda x : str(x)*4, reverse=True)

    for n in numbers:
        answer += str(n)
    return str(int(answer))