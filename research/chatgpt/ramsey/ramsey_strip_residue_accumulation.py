"""Test whether the union of residual pairs can coexist as a partial matching, and whether a later full matching preserves earlier residual links."""
from collections import Counter
from ramsey_strip_residue_progress import C,core,petals,ids,states,turn
union=set.union(*(set(c) for c in C.values()));degree=Counter(v for e in union for v in e)
assert len(union)==8 and max(degree.values())==1
print('residue union: edges',len(union),'vertices',len(degree),'is partial matching',True)
for i in ids:
    print('track',i,'residues of tracks retained in either orientation',[(j,len(C[j]&states[i,0]),len(C[j]&states[i,1])) for j in ids])
    for j in ids:
        assert len(C[j]&states[i,0])==len(C[j]&states[i,1])==(4 if i==j else 3)
