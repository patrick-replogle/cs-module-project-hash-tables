"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


def sum_diff(nums):
    add_table = {}
    minus_table = {}

    for i in q:
        for j in q:
            add_table[(i, j)] = f(i) + f(j)

    for i in q:
        for j in q:
            minus_table[(i, j)] = f(i) - f(j)

    for k1, v1 in add_table.items():
        for k2, v2 in minus_table.items():
            if add_table[k1] == minus_table[k2]:
                print(
                    f"f({k1[0]}) + f({k1[1]}) = f({k2[0]} - f({k2[1]}) = {v1})")


sum_diff(q)
