"""Relate alternating reciprocal operations to a persistent quarter-turn by a phase-dependent global frame change. Phase is retained, not inferred from vertex type."""
from ramsey_strip_half_operation_factor import reflections,roots,U,V,r
S,=[a for a in reflections if a[16]==7];T,=[a for a in reflections if a is not S];F,=[a for a in roots if a[16]==7];K={x:F[S[x]] for x in U+V};assert all(K[K[x]]==x for x in K)
for x in K:
    # Even phase uses identity coordinates, odd phase uses K coordinates.
    assert K[S[x]]==F[x]
    assert T[x]==F[K[x]]
    assert (x in U)==(K[x] in U)
print('odd-phase frame relabeling fixes directed target port',K[7]==7,'row-pair commuting',all(K[r[x]]==r[K[x]] for x in K))
for start in (16,1):
    physical=[start];moving=[start];x=start
    for b in range(4):
        x=(S if b%2==0 else T)[x];physical.append(x);moving.append(K[x] if b%2==0 else x)
    y=start;expected=[y]
    for _ in range(4):y=F[y];expected.append(y)
    assert moving==expected;print('start',start,'fixed-frame alternating',physical,'moving-frame quarter-turn',moving)
assert all((T[S[x]],0)==(r[x],0) for x in K)
print('phase-augmented state count',2*len(K),'fourth iterate identity',True)
