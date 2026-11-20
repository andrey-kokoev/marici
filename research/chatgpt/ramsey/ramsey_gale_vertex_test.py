"""Exact circle signs on a regular 23-gon. No floating point or SAT solver."""
from itertools import combinations

N = 23

def side(i, j):
    d = (j - i) % N
    return 0 if d == 0 else (1 if d <= 11 else -1)

def main():
    assert all(sum(side(i,j)==s for j in range(N))==11
               for i in range(N) for s in (-1,1))
    assert all(side(i,j)==-side(j,i) for i,j in combinations(range(N),2))
    # A 5-cycle cannot admit opposite test orientations at adjacent vertices.
    for mask in range(32):
        assert any(((mask>>i) ^ (mask>>((i+1)%5))) & 1 == 0 for i in range(5))
    # A hemisphere of eleven certified nonneighbors need not contain an independent six.
    H = list(range(1,12))
    edges = {tuple(sorted((H[i],H[(i+1)%11]))) for i in range(11)}
    assert all(side(0,i)==1 for i in H)
    assert not any(all(p in edges for p in combinations(t,2)) for t in combinations(H,3))
    assert not any(all(p not in edges for p in combinations(t,2)) for t in combinations(H,6))
    print('11 points per open side; signs antisymmetric; odd-cycle and C11 checks passed.')

if __name__=='__main__':main()
