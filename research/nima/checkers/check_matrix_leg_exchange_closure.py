"""Exact rational closure hostile for the trace-of-shared-matrix-legs adapter."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/nima/results/matrix-leg-exchange-closure.json'
out.unlink(missing_ok=True)

def rank(rows):
    a=[[F(x) for x in r] for r in rows]; k=0
    for j in range(len(a[0])):
        pivot=next((i for i in range(k,len(a)) if a[i][j]),None)
        if pivot is None: continue
        a[k],a[pivot]=a[pivot],a[k]
        s=a[k][j]; a[k]=[x/s for x in a[k]]
        for i in range(len(a)):
            if i!=k:
                s=a[i][j]; a[i]=[x-s*y for x,y in zip(a[i],a[k])]
        k+=1
        if k==len(a): break
    return k

def mul(a,b): return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def trace(a): return a[0][0]+a[1][1]
def det(a): return a[0][0]*a[1][1]-a[0][1]*a[1][0]
X=[[[1,0],[0,1]],[[1,0],[0,-1]],[[0,1],[1,0]],[[0,1],[-1,0]]]
Y=[[[F(x[j][i],2) for j in range(2)] for i in range(2)] for x in X]
assert all(det(m)!=0 for m in X+Y)
W=[[trace(mul(Y[j%4],X[i%4])) for j in range(11)] for i in range(11)]
assert rank(W)==4
assert all(W[i][j]==int(i%4==j%4) for i,j in product(range(11),repeat=2))
# Every individual cell direction is transverse: duplicated row/column classes
# give null witnesses with nonzero pairing against the addressed coordinate.
for i,j in product(range(11),repeat=2):
    ii=next(t for t in range(11) if t!=i and t%4==i%4)
    jj=next(t for t in range(11) if t!=j and t%4==j%4)
    assert W[ii]==W[i]
    assert all(row[jj]==row[j] for row in W)
    changed=[r.copy() for r in W]; changed[i][j]+=F(1,7)
    assert rank(changed)==5

E=[(a,b) for a,b in product(range(4),repeat=2) if a!=b and (a,b)!=(0,1)]
e=[[F(i==j) for j in range(4)] for i in range(4)]
arrows=[[e[b][k]-e[a][k] for k in range(4)] for a,b in E]
assert rank(arrows)==3
features=[[x*y for x in a for y in b] for a,b in product(arrows,repeat=2)]
features += [[x*y for x in a for y in b] for a,b in product(e,repeat=2)]
norms=[F(20)]*121+[F(11)]*16
G=[[F(10*(i==j)+1) for j in range(4)] for i in range(4)]
metric=[[G[i][k]*G[j][l] for k,l in product(range(4),repeat=2)] for i,j in product(range(4),repeat=2)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(A,x): return [dot(row,x) for row in A]
def signal(z,i): return dot(features[i],mv(metric,z))/norms[i]
def anchor(z,w): return [z[k]+sum(features[i][k]*w[i]/norms[i] for i in range(137)) for k in range(16)]
def budget(z,w): return dot(z,mv(metric,z))+dot(w,w)
def exchange(z,w,i):
    delta=w[i]-signal(z,i)
    z=[x+v*delta/norms[i] for x,v in zip(z,features[i])]
    w=w.copy(); w[i]-=delta
    return z,w

for reference_trace in (F(0),F(4)):
    block=[[x-reference_trace for x in row] for row in W]
    assert rank(block)==4  # cannot equal a rank<=3 carrier arrow-response block
    seed=[x for row in block for x in row]
    seed += [F(i==j)-reference_trace for i,j in product(range(4),repeat=2)]
    z=[F(0)]*16; w=seed.copy()
    initial_anchor=anchor(z,w); initial_budget=budget(z,w)
    z,w=exchange(z,w,0)
    reconstructed=[[w[11*i+j]+reference_trace for j in range(11)] for i in range(11)]
    assert rank(reconstructed)==5
    assert anchor(z,w)==initial_anchor and budget(z,w)==initial_budget
    # Explicit completion: keep prepared legs/reference, a correction at each
    # record port and the ordered event history. Do not refactor the new w.
    z_direct=[F(0)]*16; w_direct=seed.copy()
    z_packet=z_direct.copy(); correction=[F(0)]*137
    history=[]
    for i in (0,1,121,20,0):
        z_direct,w_direct=exchange(z_direct,w_direct,i)
        current=[b+c for b,c in zip(seed,correction)]
        z_packet,next_records=exchange(z_packet,current,i)
        correction=[v-b for v,b in zip(next_records,seed)]
        history.append(i)
        assert z_packet==z_direct
        assert [b+c for b,c in zip(seed,correction)]==w_direct
        assert anchor(z_direct,w_direct)==initial_anchor
        assert budget(z_direct,w_direct)==initial_budget
    assert history==[0,1,121,20,0] and any(correction)

result={
 'status':'passed',
 'classification':'trace_shared_leg_preparation_not_exchange_closed_retained_correction_completion',
 'arithmetic':'exact rational',
 'checks':{'invertible_matrix_leg_preparation_rank4':True,'all121_single_cell_transverse_controls':True,
           'carrier_arrow_feature_rank3':True,'raw_and_fixed_reference_hostiles':True,
           'retained_correction_word_adapter':True,'conserved_anchor_and_budget':True},
 'ranks':{'prepared_trace_block':4,'carrier_arrow_response_upper_bound':3,'one_exchange_trace_block':5},
 'conclusion':'The direct trace-of-shared-2x2-legs record adapter is not closed under exchange. Retaining independent record corrections and ordered history completes this conditional preparation, but adds state beyond current leg composites.',
 'missing':['native authorization for independent record memory','native source operation on the extended packet',
            'physical selection and normalization'],
 'next_falsifier':'Check whether existing retained comparison witnesses already furnish the required record corrections and update operation, without redefining the prepared leg composites.'
}
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
