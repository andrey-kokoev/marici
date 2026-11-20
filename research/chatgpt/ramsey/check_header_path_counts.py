"""Exact counterexample to endpoint-free color-word counts. Standard library."""
from itertools import combinations, product


def check(name, red):
    vertices = range(8)
    blue = [set(vertices) - {i} - row for i, row in enumerate(red)]
    assert all(len(r) == 3 for r in red) and all(len(b) == 4 for b in blue)
    assert all(i in red[j] for i in vertices for j in red[i])
    assert not any(all(j in red[i] for i,j in combinations(t,2)) for t in combinations(vertices,3))
    forbidden = [t for t in combinations(vertices,4) if all(j in blue[i] for i,j in combinations(t,2))]
    # Count walks from each header; the other role has the transposed (same) matrix.
    for k in range(7):
        for word in product('RB',repeat=k):
            counts=[1]*8
            for letter in reversed(word):
                counts=[sum(counts[j] for j in r) for r in (red if letter=='R' else blue)]
            assert counts == [3**word.count('R')*4**word.count('B')]*8
    print(name,'blue four-sets:',forbidden)
    return forbidden

if __name__=='__main__':
    assert not check('square with antipodal joins', [{(i-1)%8,(i+1)%8,(i+4)%8} for i in range(8)])
    assert check('cube',[{i^1,i^2,i^4} for i in range(8)]) == [(0,3,5,6),(1,2,4,7)]
