"""Build polarities from a marked stationary edge and an affine chart on the other five. No endpoint constraints in construction. Compare poles only afterward."""
from itertools import combinations
X=list(combinations(range(1,5),2));P=list(combinations(range(6),2));T=[t for t in combinations(P,3) if len(set(sum(t,())))==6];cycle=[X.index(x) for x in [(1,2),(3,4),(1,3),(2,4)]];fixed=[X.index(x) for x in [(1,4),(2,3)]];pair=lambda i,j:tuple(sorted((i,j)))
for pole in fixed:
 for mult in (2,3):
    chart={pow(mult,i,5):v for i,v in enumerate(cycle)};chart[0]=next(x for x in fixed if x!=pole);star={pair(pole,v):{pair(pole,v),pair(chart[(k-1)%5],chart[(k+1)%5]),pair(chart[(k-2)%5],chart[(k+2)%5])} for k,v in chart.items()};ds=[]
    for p in P:
        if p in star:t=star[p]
        else:t,=[set(t) for t in T if all(bool(set(t)&u)==set(p).isdisjoint(q) for q,u in star.items())]
        ds.append(15+T.index(tuple(sorted(t))))
    D=ds+[ds.index(j) for j in range(15,30)];assert all((P[i] in T[j-15])==(P[D[j]] in T[D[i]-15]) for i in range(15) for j in range(15,30));print('star',X[pole],'multiplier',mult,'images of half-stepped poles',D[14],D[26])
