# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Does least-change return compose through families of families?

Source families partition137 slots. Their induced update metric is diagonal
with member counts. Compare direct, weighted staged, and naive staged returns.
"""
from itertools import product
from collections import defaultdict
import numpy as np

vertices=range(4)
edges=[(a,b) for a,b in product(vertices,repeat=2) if a!=b and (a,b)!=(0,1)]
slots=[('arrow',a,b) for a,b in product(edges,repeat=2)]
slots += [('state',a,b) for a,b in product(vertices,repeat=2)]


def partition(endpoint):
    groups=defaultdict(list)
    for i,(kind,a,b) in enumerate(slots):
        key=(kind,a[endpoint],b[endpoint]) if kind=='arrow' else (kind,a,b)
        groups[key].append(i)
    keys=sorted(groups)
    return keys,[groups[k] for k in keys]


def mean_matrix(groups,n):
    A=np.zeros((len(groups),n))
    for i,members in enumerate(groups): A[i,members]=1/len(members)
    return A


rng=np.random.default_rng(137)
x=rng.normal(size=137)
keys,groups=partition(0)
A=mean_matrix(groups,137)
sizes=np.array(list(map(len,groups)),float)
W=np.diag(sizes); Wi=np.diag(1/sizes)
# Upper records group first-level families by block and first source label.
upper_keys=sorted(set((k[0],k[1]) for k in keys))
upper_groups=[[i for i,k in enumerate(keys) if (k[0],k[1])==key] for key in upper_keys]
B=np.zeros((len(upper_groups),len(groups)))
for i,indices in enumerate(upper_groups):
    B[i,indices]=sizes[indices]/sum(sizes[indices])
C=B@A
leaf_groups=[[j for i in indices for j in groups[i]] for indices in upper_groups]
assert np.max(np.abs(C-mean_matrix(leaf_groups,137))) < 1e-12
# Requested upper changes deliberately vary so naive equal-family cost matters.
delta=np.linspace(.1,.8,len(upper_groups))
y=C@x+delta
Aplus=A.T@W
assert np.max(np.abs(A@Aplus-np.eye(len(groups))))<1e-12
direct=x+C.T@np.linalg.solve(C@C.T,y-C@x)
weighted_family_delta=Wi@B.T@np.linalg.solve(B@Wi@B.T,y-B@A@x)
staged=x+Aplus@weighted_family_delta
assert np.max(np.abs(direct-staged))<1e-12
naive_family_delta=B.T@np.linalg.solve(B@B.T,y-B@A@x)
naive=x+Aplus@naive_family_delta
assert np.max(np.abs(C@naive-y))<1e-12
assert np.linalg.norm(naive-direct)>1e-3
assert np.linalg.norm(naive-x)**2>np.linalg.norm(direct-x)**2
# Third level, one global mean: weights remain original member counts.
upper_sizes=np.array(list(map(len,leaf_groups)),float)
D=(upper_sizes/137)[None,:]
assert np.max(np.abs(D@C-np.ones((1,137))/137))<1e-12
upper_shift=np.full(len(upper_groups),.7)
family_shift=Wi@B.T@np.linalg.solve(B@Wi@B.T,upper_shift)
third=x+Aplus@family_shift
assert np.max(np.abs(third-(x+.7)))<1e-12
# Source and target routes to the same block means yield the same leaf update.
route_updates=[]
for endpoint in (0,1):
    ks,gs=partition(endpoint)
    Ar=mean_matrix(gs,137); nr=np.array(list(map(len,gs)),float)
    Wr=np.diag(nr); Wir=np.diag(1/nr)
    Br=np.array([[nr[i]/sum(nr[j] for j,k in enumerate(ks) if k[0]==kind)
                  if key[0]==kind else 0 for i,key in enumerate(ks)] for kind in ('arrow','state')])
    change=np.array([.3,-.2])
    change_r=Wir@Br.T@np.linalg.solve(Br@Wir@Br.T,change)
    route_updates.append(Ar.T@Wr@change_r)
assert np.max(np.abs(route_updates[0]-route_updates[1]))<1e-12
# Overlapping source+target families require the full quotient metric.
At=mean_matrix(partition(1)[1],137)
O=np.vstack((A,At))
assert np.linalg.matrix_rank(O)==47
M=O@O.T
assert np.count_nonzero(np.abs(M[:32,32:])>1e-12)>0
# Average equivalent source/target block readouts; use the induced full metric.
all_keys=keys+partition(1)[0]
all_sizes=np.r_[sizes,np.array(list(map(len,partition(1)[1])),float)]
Bover=np.array([[all_sizes[i]/(2*(121 if kind=='arrow' else 16))
                if key[0]==kind else 0 for i,key in enumerate(all_keys)]
               for kind in ('arrow','state')])
request=np.array([.3,-.2])
intermediate=M@Bover.T@np.linalg.solve(Bover@M@Bover.T,request)
assert np.max(np.abs(O@np.linalg.pinv(O)@intermediate-intermediate))<1e-12
via_overlap=np.linalg.pinv(O)@intermediate
direct_overlap=np.linalg.pinv(Bover@O)@request
assert np.max(np.abs(via_overlap-direct_overlap))<1e-12
print('32 source families ->8 upper families ->1 global family: weighted return composition passed.')
print(f'Direct/weighted staged discrepancy={np.max(np.abs(direct-staged)):.3g}')
print(f'Naive/direct discrepancy norm={np.linalg.norm(naive-direct):.12g}')
print(f'Squared edit costs: direct={np.linalg.norm(direct-x)**2:.12g}; naive={np.linalg.norm(naive-x)**2:.12g}')
print('Source-indexed and target-indexed routes agree for the same block-mean request.')
print('Overlapping64-family readout has rank47: full quotient-metric return also matches direct return.')
print('Use (O O^T)^+ on its image, not diagonal member counts.')
