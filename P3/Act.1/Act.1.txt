def doubly_not_less(n):
    def rev(s):
        return str(int(s[::-1]))
    digits = list(n)
    for i in range(len(digits) - 1, -1, -1):
        for d in range(int(digits[i]), 10):
            digits[i] = str(d)
            for j in range(i + 1, len(digits)):
                digits[j] = '9'
            candidate = ''.join(digits)
            if candidate >= n and rev(candidate) >= n:
                return candidate
        digits[i] = '0'
    return '9' * len(n)