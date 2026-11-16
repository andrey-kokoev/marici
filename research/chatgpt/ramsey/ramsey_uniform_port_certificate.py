"""Exact, dependency-free certificates for two recursive port restrictions.

No claim that R(3,10) is determined. Numeric Ramsey inputs in the article:
R(3,8)=28; e(3,8,27)=85 (external published results).
"""
from itertools import combinations

U = (0, 1, 2)
D = (3, 4, 5)
k = 6
supports = [(i,) for i in U]
supports += [tuple(sorted((i, j))) for i in U for j in D]
supports += [tuple(sorted(p)) for p in combinations(D, 2)]
supports += [(0, 1, 2)]
assert len(supports) == 16
assert all(sum(a in s for s in supports) == 5 for a in range(k))
ss = {s: i for i, s in enumerate(supports)}
X = {ss[(i,)] for i in U}

def independent_by_matching(indices):
    match = {}
    def aug(i, seen):
        for a in supports[i]:
            if a in seen: continue
            seen.add(a)
            if a not in match or aug(match[a], seen):
                match[a] = i
                return True
        return False
    return all(aug(i, set()) for i in indices)

def is_circuit(C):
    return not independent_by_matching(C) and all(
        independent_by_matching(tuple(i for i in C if i != j)) for j in C)

def eligible(C):
    return {tuple(sorted((i,j))) for i,j in combinations(C,2)
            if set(supports[i]).isdisjoint(supports[j])}

circuits = []
for i in U:
    for a,b in combinations(D,2):
        C=(ss[(i,)], ss[tuple(sorted((i,a)))],
           ss[tuple(sorted((i,b)))], ss[(a,b)])
        E=eligible(C)
        assert is_circuit(C)
        assert E == {(ss[(i,)],ss[(a,b)])} or E == {(ss[(a,b)],ss[(i,)])}
        circuits.append((C,E,1))
for j in D:
    for i in U:
        C=(ss[(i,)],) + tuple(ss[tuple(sorted((a,j)))] for a in U) + (ss[(0,1,2)],)
        E=eligible(C)
        assert is_circuit(C) and len(E)==2
        assert all((i0 in X) != (i1 in X) for i0,i1 in E)
        circuits.append((C,E,1))
C=tuple(ss[(i,)] for i in U)+(ss[(0,1,2)],)
E=eligible(C)
assert is_circuit(C) and len(E)==3
assert all(i in X and j in X for i,j in E)
circuits.append((C,E,2))

weights={}
for c,edges,w in circuits:
    for edge in edges:weights[edge]=weights.get(edge,0)+w
for edge,w in weights.items():
    cap=sum(x in X for x in edge)
    assert w <= cap,(edge,w,cap)

weighted_demand=sum(w for _,_,w in circuits)
capacity=sum(k-len(supports[x]) for x in X)
assert weighted_demand==20 and capacity==15
print('EXACT 6-PORT DUAL: weighted circuit demand =',weighted_demand,
      '> singleton degree capacity =',capacity)
print('Circuits:',len(circuits),'(9 forced four-vertex, 9 fifth-order, 1 internal four-vertex)')
print('All weighted edge coefficients <= number of endpoints in singleton core: VERIFIED')

print('\nUNIFORM 3-SINGLETON FAN INEQUALITY:')
for K,r in [(6,3),(7,3),(8,3),(9,3),(9,4),(9,5),(9,6),(12,5)]:
    assert r+3 <= K
    demand=3*r*(r-1)//2 + 3*r + 2
    capacity=3*(K-1)
    print(f'k={K}, outside_labels={r}: demand={demand}, capacity={capacity},',
          'EXCLUDED' if demand>capacity else 'not excluded')

# The recursive 'contact' inequality for k-regular n=40,k=9, with
# published e(3,8,27)=85. For p=7, R has order 27.
n,k,p=40,9,7
B=n-k-1
H_edges=n*k//2-k*k
R_count=B-1-(k-p)
min_R_edges=85
min_neighbors=p*(k-p)
assert (B,H_edges,R_count,min_neighbors)==(30,99,27,14)
assert min_R_edges+min_neighbors==H_edges
print('\n40-VERTEX REGULAR CONTACT: H edges=99, p=7 residual=27 vertices,')
print('e(residual)>=85, neighbors contribute >=14, hence both bounds are equalities.')
print('This does not eliminate a 40-vertex graph; it gives a rigid necessary condition.')

# A symmetric two-neighborhood inequality on any hypothetical 40-vertex
# triangle-free graph with independence number at most nine:
# mu(u,v) <= deg(u)+deg(v)-11 for all nonadjacent u,v.
R38=28; N40=40; k40=9
assert R38+1-N40 == -11
print('\nSYMMETRIC CODEGREE CAP: common_neighbors(u,v) <= degree(u)+degree(v)-11')
print('Two vertices of degree <=5 cannot be nonadjacent; at most two such vertices exist.')
