# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Editable family means and least-change return on137 retained slot records.

Source/target groups retain their full members; scalar means are additional
editable readouts. Euclidean member metric and full correction are explicit
choices. This does not derive a physical energy or coupling constant.
"""
from itertools import product
from collections import defaultdict
import numpy as np

V=range(4)
edges=[(a,b) for a,b in product(V,repeat=2) if a!=b and (a,b)!=(0,1)]
slots=[('arrow',a,b) for a,b in product(edges,repeat=2)]
slots += [('state',a,b) for a,b in product(V,repeat=2)]


def membership(endpoint):
    groups=defaultdict(list)
    for i,(kind,a,b) in enumerate(slots):
        key=(kind,a[endpoint],b[endpoint]) if kind=='arrow' else (kind,a,b)
        groups[key].append(i)
    return [indices for _,indices in sorted(groups.items())]


def operators(groups):
    A=np.zeros((len(groups),137)); Q=A.copy()
    for i,indices in enumerate(groups):
        A[i,indices]=1/len(indices)
        Q[i,indices]=1/np.sqrt(len(indices))
    assert np.max(np.abs(Q@Q.T-np.eye(len(groups)))) < 1e-12
    return A,Q.T@Q


source,target=membership(0),membership(1)
As,Ps=operators(source); At,Pt=operators(target)
A=np.vstack((As,At))
_,singular,Vh=np.linalg.svd(A,full_matrices=True)
rank=int(np.sum(singular>1e-10)); assert rank==47
R=Vh[:rank].T
P=R@R.T; K=np.eye(137)-P
T=(np.eye(137)-Pt)@(np.eye(137)-Ps)
active_radius=max(abs(np.linalg.eigvals(R.T@T@R)))
assert active_radius<1
assert np.max(np.abs(T@K-K))<1e-12
feedback=Ps+Pt-Pt@Ps
assert np.max(np.abs(T-(np.eye(137)-feedback)))<1e-12
# Geometry of grouping determines cross-index response of a unit family edit.
# A source group change delta shifts each member by delta; a target group
# then reads intersection_size/target_size times that delta.
for i,s in enumerate(source):
    edit=np.zeros(137); edit[s]=1
    for j,t in enumerate(target):
        assert abs((At@edit)[j]-len(set(s)&set(t))/len(t))<1e-12

rng=np.random.default_rng(137)
x0=rng.normal(size=137); desired=rng.normal(size=137)
ys,yt=As@desired,At@desired
# Global least-norm correction solves all compatible means at once.
corrected=x0+np.linalg.pinv(A)@(np.r_[ys,yt]-A@x0)
assert np.max(np.abs(A@corrected-np.r_[ys,yt]))<1e-10
assert np.max(np.abs(K@(corrected-x0)))<1e-10
x=x0.copy()
start=np.linalg.norm(A@(x-desired))
for step in range(1,31):
    before=x-desired
    x-=Ps@(x-desired)
    assert np.max(np.abs(As@x-ys))<1e-10
    x-=Pt@(x-desired)
    assert np.max(np.abs(At@x-yt))<1e-10
    assert np.linalg.norm(x-desired)<=np.linalg.norm(before)+1e-10
    if step in (1,2,5,10,30):
        print(f'Cycle{step}: mean residual={np.linalg.norm(A@(x-desired)):.12g}')
assert np.linalg.norm(A@(x-desired))<1e-10
assert np.linalg.norm(x-corrected)<1e-9
assert np.linalg.norm(K@(x-x0))<1e-10
# Conflicting edit: nonzero sum of source arrow means weighted by size,
# but zero target arrow total. Both cannot describe one member table.
bad=np.zeros(64); bad[0]=1
assert np.linalg.norm(A@np.linalg.pinv(A)@bad-bad)>1e-3
print(f'Families:32 source+32 target; independent means={rank}; hidden member directions={137-rank}.')
print(f'Active residual spectral radius per source-target cycle={active_radius:.12g}')
print(f'Cross-pass noncommutation norm={np.linalg.norm(Ps@Pt-Pt@Ps):.12g}')
print('Compatible edits converge to the joint least-change solution; hidden detail is preserved.')
print('An inconsistent source/target edit is rejected by the joint readout image test.')
print('Return gains are intersection_size/target_size for this chosen mean/Euclidean return contract.')
