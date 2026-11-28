"""Test odd-order Bonferroni lower certificates for missed six-blades."""
from math import comb
from pathlib import Path
from collections import Counter
from itertools import combinations

def test(line):
    n=ord(line[0])-63; assert n==22
    bits=''.join(f'{ord(c)-63:06b}' for c in line[1:]); a=[0]*n
    for z,(j,i) in zip(bits,((j,i) for j in range(n) for i in range(j))):
        if z=='1':a[i]|=1<<j;a[j]|=1<<i
    def ind(p,s):
        yield s
        while p:
            b=p&-p;p^=b;yield from ind(p&~a[b.bit_length()-1],s|b)
    sets=list(ind((1<<n)-1,0));six=[s for s in sets if s.bit_count()==6];assert max(map(int.bit_count,sets))==6
    worst=[10**6]*5
    for N in sets:
        if any(not(N>>v&1 or N&a[v]) for v in range(n)):continue
        h=Counter((s&N).bit_count() for s in six)
        # Pointwise remainder for j>=1: truncated sum = -C(j-1,r) for odd r.
        vals=[h[0]-sum(c*comb(j-1,r) for j,c in h.items() if j>r) for r in (1,3,5)]+[h[0]]
        # A cubic major improvement: neighboring integer roots make the quadratic nonnegative.
        vals.append(max(-(-sum(c*(1-j)*(b-j)*(b+1-j) for j,c in h.items())//(b*(b+1))) for b in range(2,6)))
        worst=list(map(min,worst,vals))
    return worst

if __name__=='__main__':
    lines=(Path(__file__).resolve().parents[1]/'chatgpt/ramsey/pauli-realization-catalogues/r37_22.g6').read_text().splitlines()
    out=list(map(test,lines));print('order 1,3,5,exact,adaptive cubic (rounded up) minima',list(map(min,zip(*out))));print('graphs certified >=10', [sum(v>=10 for v in col) for col in zip(*out)])
