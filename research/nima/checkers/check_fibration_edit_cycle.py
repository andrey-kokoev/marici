# /// script
# dependencies = ["numpy>=2,<3"]
# ///
"""Edit transport around source/target presentations of retained slot records.

Full presentations retain every leaf identity and are related by permutations.
Mean-only paths are projections, not invertible transports. Tests distinguish
true presentation holonomy from loss through incomplete readout interfaces.
"""
from itertools import product
from collections import defaultdict
import numpy as np

V=range(4)
edges=[(a,b) for a,b in product(V,repeat=2) if a!=b and (a,b)!=(0,1)]
slots=[('arrow',a,b) for a,b in product(edges,repeat=2)]
slots += [('state',a,b) for a,b in product(V,repeat=2)]


def grouping(endpoint):
    groups=defaultdict(list)
    for i,(kind,a,b) in enumerate(slots):
        key=(kind,a[endpoint],b[endpoint]) if kind=='arrow' else (kind,a,b)
        groups[key].append(i)
    return [groups[k] for k in sorted(groups)]


def presentation(groups):
    order=[i for members in groups for i in members]
    R=np.eye(137)[order]
    A=np.zeros((len(groups),137))
    for j,members in enumerate(groups): A[j,members]=1/len(members)
    return R,A


Rs,As=presentation(grouping(0)); Rt,At=presentation(grouping(1))
R0=np.eye(137)
# 0->source->target->0 presentation maps, retaining individual row identities.
T_s0=Rs; T_ts=Rt@Rs.T; T_0t=Rt.T
cycle=T_0t@T_ts@T_s0
assert np.array_equal(cycle,R0)
rng=np.random.default_rng(137)
x=rng.normal(size=137); edit=rng.normal(size=137)
assert np.max(np.abs(cycle@(x+edit)-(x+edit)))<1e-12
# Any leaf readout can be expressed in each full presentation. Least-change
# return then agrees after transporting the Euclidean leaf metric.
readout=np.vstack((As[:4],At[-4:]))
request=rng.normal(size=8)
base_return=np.linalg.pinv(readout)@request
for R in (R0,Rs,Rt):
    local_readout=readout@R.T
    local_return=np.linalg.pinv(local_readout)@request
    assert np.max(np.abs(R.T@local_return-base_return))<1e-12

# Mean-only source -> leaf minimum lift -> target -> leaf lift -> source
# is not an invertible presentation cycle. Exhibit an erased original mean.
Ls=np.linalg.pinv(As); Lt=np.linalg.pinv(At)
mean_cycle=As@Lt@At@Ls
assert np.linalg.norm(mean_cycle-np.eye(32))>.1
# Reconcile compatible fixed targets. Corresponding projections fail to
# commute, but are noninvertible; this discrepancy alone is not holonomy.
Ps=Ls@As; Pt=Lt@At
forward=(np.eye(137)-Pt)@(np.eye(137)-Ps)@x
reverse=(np.eye(137)-Ps)@(np.eye(137)-Pt)@x
assert np.linalg.norm(forward-reverse)>.1
# Augment a source mean with its retained residual. This is lossless, with
# residual restricted to ker(As); switch presentations through reconstructed x.
y=As@x; residual=x-Ls@y
assert np.max(np.abs(As@residual))<1e-12
recovered=Ls@y+residual
yt=At@recovered; residual_t=recovered-Lt@yt
roundtrip=Lt@yt+residual_t
assert np.max(np.abs(roundtrip-x))<1e-12
# Likewise retain the invisible component of an edit.
dy=As@edit; de=edit-Ls@dy
assert np.max(np.abs(Ls@dy+de-edit))<1e-12
print('Full record/index cycle is identity on states and edits.')
print('Least-change returns commute with all three complete presentations.')
print(f'Mean-only cycle deviation from identity={np.linalg.norm(mean_cycle-np.eye(32)):.12g}')
print(f'Opposite partial-update orders differ by={np.linalg.norm(forward-reverse):.12g}')
print('Adding retained residuals restores exact state/edit reconstruction across source/target views.')
print('Lossy mean projection and noncommuting corrections are not by themselves invertible transport holonomy.')
