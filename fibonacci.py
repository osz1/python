# s = [0, 1]
# def fibonacci(s, l):
    # if s[-1] < l:
        # sll = s[-2]
        # sl = s[-1]
        # s.append(sll + sl)
        # if s[-1] < l:
            # fibonacci(s, l)
    # return s
# print(fibonacci(s, 144))

# def fibonacciszam(n, s1=0, s2=1, b=[]):
    # if n in (s1, s2):
        # b.append(True)
    # if s2 < n:
        # fibonacciszam(n, s2, (s1 + s2), b)
    # return bool(b)
# print(fibonacciszam(144))

def szamfibonacci(n):
    s1 = 0
    s2 = 1
    while s2 < n:
        sll = s2
        sl = s1 + s2
        s1 = sll
        s2 = sl
    return n in (s1, s2)
print(szamfibonacci(144))