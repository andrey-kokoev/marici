"""Exact three-contact and four-contact extension nerves over the C13
triangle-free R(3,5)-critical A-graph. Pure standard-library proof.
A iff cyclic distance is +/-2 or +/-3 modulo 13. B is complement.
"""
from itertools import combinations

N0 = 13
DIFF = {2, 3, 10, 11}
C = (
    (0, 1, 5, 6),
    (0, 1, 6, 7),
    (1, 2, 6, 7),
    (2, 3, 7, 8),
    (3, 4, 8, 9),
)


def build(contacts):
    n = N0 + len(contacts)
    adj = [0] * n
    def add(u,v):
        assert u != v
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    for i in range(N0):
        for j in range(i+1,N0):
            if (j-i)%N0 in DIFF:
                add(i,j)
    for k,S in enumerate(contacts):
        assert len(S)==len(set(S))
        assert all((v-u)%N0 not in DIFF for u,v in combinations(S,2))
        for v in S:
            add(N0+k,v)
    return adj


def independence_number(adj):
    # Exhaust exact maximum independent sets by bitset dynamic recursion.
    n=len(adj)
    allmask=(1<<n)-1
    memo={0:0}
    def alpha(mask):
        if mask not in memo:
            bit=mask&-mask;v=bit.bit_length()-1
            memo[mask]=max(alpha(mask^bit),1+alpha((mask^bit)&~adj[v]))
        return memo[mask]
    return alpha(allmask)


def valid(contacts,m):
    adj=build(contacts)
    assert all(not (adj[i]&adj[j]) for i in range(len(adj)) for j in range(i+1,len(adj)) if adj[i]>>j&1)
    return independence_number(adj)<m

base=build([])
assert independence_number(base)==4
assert all((base[i]>>((i+2)%13))&1 for i in range(13))  # A single cycle
assert all(not(base[i]>>((i+1)%13))&1 for i in range(13))  # B single cycle

# The three proposed fillers are internally B-connected.
BAD=(C[0],C[1],C[2]); GOOD=(C[0],C[1],C[3])
for tag,trial,expected in [('missing',BAD,False),('filled',GOOD,True)]:
    faces={s for k in range(4) for s in combinations(range(3),k) if valid([trial[i] for i in s],7)}
    assert set(combinations(range(3),0))|set(combinations(range(3),1))|set(combinations(range(3),2))<=faces
    assert ((0,1,2) in faces)==expected
    print(tag,'extension nerve f-vector',tuple(sum(len(s)==d for s in faces) for d in range(4)),
          'alpha with all three', independence_number(build(trial)))

T=(3,4,8,9)
assert all(not any(u in S for u in T) for S in BAD)
assert all(not(base[i]>>j&1) for i,j in combinations(T,2))
print('Missing 2-simplex is witnessed by complete B7 on',T,'+', (13,14,15))

# Four proposed fillers have all subsets simultaneously admissible under R(3,7).
FOUR=(C[0],C[1],C[3],C[4])
for k in range(5):
    for ids in combinations(range(4),k):
        assert valid([FOUR[i] for i in ids],7),(ids,k)
A17=build(FOUR)
assert independence_number(A17)==6
assert sum(x.bit_count() for x in A17)//2==42
A_cycle=(0,10,12,2,15,3,5,13,1,11,8,16,4,6,9,7,14)
B_cycle=tuple(range(17))
for cycle,kind in [(A_cycle,True),(B_cycle,False)]:
    assert len(set(cycle))==len(A17)
    assert all(bool(A17[cycle[i]]>>(cycle[(i+1)%len(cycle)]&31)&1)==kind for i in range(len(cycle)))
print('Certified 17-node R(3,7) lower-bound graph, 42 A edges, alpha=6; both A and B Hamiltonian')
print('A-cycle:',A_cycle)
print('B-cycle:',B_cycle)
print('4-fillers:',FOUR)

# Exact universal capacity formulation: for each old B-clique T, the number
# of chosen newborns missing every vertex of T cannot exceed m-|T|-1.
old_b_faces=[s for s in range(1<<N0)
             if all(not(base[u]>>v&1)
                    for u,v in combinations((j for j in range(N0) if s>>j&1),2))]
assert max(s.bit_count() for s in old_b_faces)==4

def capacities_allow(contacts,indices,m):
    contact_masks=[sum(1<<v for v in C) for C in contacts]
    for T in old_b_faces:
        missing=sum((contact_masks[i]&T)==0 for i in indices)
        if missing>m-T.bit_count()-1:
            return False
    return True

for m, contacts in [(7,BAD),(7,GOOD),(7,FOUR)]:
    for k in range(len(contacts)+1):
        for indices in combinations(range(len(contacts)),k):
            assert capacities_allow(contacts,indices,m)==valid([contacts[i] for i in indices],m)

# A 3-simplex boundary S^2: all triples of contacts admissible for m=8,
# but all four produce B8 on the common untouched B4.
TET=(C[0],C[1],C[2],(1,2,6,10))
assert len(set(TET))==4
assert all(not any(v in S for v in T) for S in TET)
for k in range(5):
    for inds in combinations(range(4),k):
        expected=(k<4)
        assert valid([TET[i] for i in inds],8)==expected
        assert capacities_allow(TET,inds,8)==expected
assert independence_number(build(TET))==8
print('m=8: 4 distinct fillers yield f-vector (1,4,6,4,0), boundary of 3-simplex S^2')
print('Every exact clique-capacity check agrees with independent-set enumeration.')
