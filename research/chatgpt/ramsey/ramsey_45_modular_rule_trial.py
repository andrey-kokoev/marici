"""Fixed coefficient rules at order 24. No target offset list is input."""
from itertools import combinations


def eta_product(factors, limit):
    shift, rem = divmod(sum(d * power for d, power in factors), 24)
    assert rem == 0
    a = [int(i == shift) for i in range(limit + 1)]
    for d, power in factors:
        for k in range(d, limit + 1, d):
            for _ in range(power):
                for i in range(limit, k - 1, -1):
                    a[i] -= a[i - k]
    return a


def count(offsets, k):
    # Translate an incident vertex to zero; each k-clique is counted k times.
    neighbors = [i for i in range(1, 24) if min(i, 24-i) in offsets]
    rooted = sum(all(min(j-i, 24-j+i) in offsets for i,j in combinations(t,2))
                 for t in combinations(neighbors, k-1))
    total, rem = divmod(rooted * 24, k)
    assert not rem
    return total


if __name__ == '__main__':
    ds = set(range(1,13))
    for name, factors in [('eta24', [(d,1) for d in (2,4,6,12)]), ('Delta', [(1,24)])]:
        a = eta_product(factors, 12)
        print(name, a[1:])
        for rule, fn in [('positive', lambda x:x>0), ('negative', lambda x:x<0), ('odd', lambda x:x%2)]:
            r = {i for i in ds if fn(a[i])}
            for label, red in [(rule,r), ('not '+rule,ds-r)]:
                print(name,label,'red K4',count(red,4),'blue K5',count(ds-red,5))
