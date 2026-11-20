"""Check the fourth coordinate functional and the two meanings of a mark."""
from itertools import permutations

points = tuple(range(1, 8))
labels = ('A', 'B', 'AB', 'C', 'AC', 'BC', 'ABC')

def bit(r, x):
    return (r & x).bit_count() % 2

def permute(r, p):
    return sum(((r >> i) & 1) << j for i, j in enumerate(p))

def main():
    invariant = [r for r in points if all(permute(r, p) == r for p in permutations(range(3)))]
    assert invariant == [7]
    covectors = (1, 2, 4, 7)
    words = [tuple(bit(r, x) for r in covectors) for x in points]
    assert len(set(words)) == 7 and all(sum(w) in (2, 4) for w in words)
    for mark in (0, 1):
        support = [label for x,label in zip(points, labels) if bit(7, x) == mark]
        print('fourth row, mark at', mark, support)
    incidence = [{x for x in points if not bit(r, x)} for r in covectors]
    assert all(len(s) == 3 for s in incidence)
    assert all(len(s & t) == 1 for i,s in enumerate(incidence) for t in incidence[i+1:])
    assert [sum(x in s for s in incidence) for x in points] == [2,2,2,2,2,2,0]
    print('coordinate words',words,'Fano degrees', [sum(x in s for s in incidence) for x in points])

if __name__ == '__main__':main()
