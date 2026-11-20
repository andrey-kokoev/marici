"""Same labeled four-port record, different legality of the same labeled extension."""
from itertools import combinations


def valid(vertices, red, k):
    def mono(s, color):
        return all((frozenset(p) in red) == color for p in combinations(s, 2))
    return not any(mono(t, True) for t in combinations(vertices, 3)) and not any(
        mono(t, False) for t in combinations(vertices, k))


def check(k):
    A = ['a1', 'a2']; B = [f'b{i+1}' for i in range(k-2)]; V = A+B+['w']
    records, outcomes = [], []
    for selected in A:
        red = {frozenset(A), frozenset(('w', selected)), frozenset(('w', B[0]))}
        assert valid(V, red, k)
        a,b = [[frozenset(('w',v)) in red for v in group] for group in (A,B)]
        records.append(('w', not all(a), all(b), not all(b), not any(a)))
        added = {frozenset(('z',v)) for v in ('w','a1','b2')}
        outcomes.append(valid(V+['z'], red|added, k))
    assert records[0]==records[1] and outcomes==[False,True]
    print(k,records[0],outcomes)

if __name__=='__main__':
    for k in (6,7): check(k)
