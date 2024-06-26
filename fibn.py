def fibn(start, n):
    def fibnocci(n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return fibnocci(n - 1) + fibnocci(n - 2)

    return [fibnocci(i) for i in range(start, start + n)]
