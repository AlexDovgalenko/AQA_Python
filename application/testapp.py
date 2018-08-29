def fibgen(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibgen(n-1) + fibgen(n-2)


def generate_fibonacci(length):

    result = []

    if length == 0:
        result = [0]
    elif length == 1:
        result = [0, 1]
    else:
        for i in range(length):
            result.append(fibgen(i))
    return result


if __name__ == '__main__':
    print(generate_fibonacci(12))

