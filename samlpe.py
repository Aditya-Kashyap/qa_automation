def solution(xs):
    # Your code here
    sol = 1
    p = 1
    n = 1
    pos = []
    neg = []

    if max(xs) == 0 and min(xs) > 0:
        return str(0)
    elif max(xs) == 0 and min(xs) == 0:
        return str(0)

    for i in xs:
        if i > 0:
            pos = pos.append(i)
        elif i < 0:
            neg = neg.appned(i)

    neg = neg.sort()
    if neg.len() % 2 == 1:
        neg = neg.remove(neg[len(neg) - 1])

    for j in pos:
        p = p * i

    for k in pos:
        n = n * i

    sol = n * p
    return str(sol)


if __name__ == "__main__":
    case0 = [2, 0, 2, 2, 0]
    print("\nCase 0:\n ", case0, "\n\n  Expected: 8\nCalculated:", solution(case0))
