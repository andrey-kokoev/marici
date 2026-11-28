"""Two ablations on the minimizing six-root incidence pattern. Local labels 0..5 are roots."""
from itertools import combinations
from functools import reduce
from operator import or_
w=[1,2,3,5,8,16,19,20,24,26,32,34,36,37,40,60]
g=[529216,168320,2892288,3195904,2160640,4128768,3375105,2369026,2172931,231557,661640,1312528,1377299,1180052,983064,787034,21344,26210,55460,50213,14440,508]
assert [a&63 for a in g[6:]]==w and all(not(g[i]>>i&1) and all((g[i]>>j&1)==(g[j]>>i&1) for j in range(22)) for i in range(22))
assert not any(g[i]&g[j] for i,j in combinations(range(22),2) if g[i]>>j&1)
for name in ('all disjoint supports joined','triangle-free control'):
    n6=0;fail=None
    for k in range(1,17):
        for s in combinations(range(16),k):
            if any((not(w[i]&w[j]) if name.startswith('all') else g[i+6]>>(j+6)&1) for i,j in combinations(s,2)):continue
            n6+=k==6
            if reduce(or_,(w[i] for i in s)).bit_count()<k and fail is None:fail=s
    print(name,'exterior independent sixes',n6,'first Hall violation',fail)
