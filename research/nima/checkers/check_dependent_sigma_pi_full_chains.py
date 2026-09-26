"""Lossless two-level dependent distributivity, with complete intermediate chains.
Finite dependent families model sets; this is not a machine-checked HoTT proof.
"""
from itertools import product
from pathlib import Path
import json

I=(0,1)
def J(i):return tuple(range(2 if i==0 else 1))
def K(i,j):return tuple(range(1+j+i))
def L(i,j,k):return tuple(range(2 if k==0 else 1))
def B(i,j,k,l):return tuple(range(1+((i+j+k+l)%2)))

def local_sources(i,j):
    return tuple(product(*(tuple((l,b) for l in L(i,j,k) for b in B(i,j,k,l))
                           for k in K(i,j))))

def sources():
    # Pi i. Sigma j. Pi k. Sigma l. B(i,j,k,l)
    return tuple(product(*(tuple((j,v) for j in J(i) for v in local_sources(i,j)) for i in I)))

def outer_first(x):
    # Stage 1: Sigma f. Pi i. Pi k:K(i,f(i)). Sigma l. B
    f=tuple(j for j,v in x)
    residual=tuple(v for j,v in x)
    stage1=(f,residual)
    # Stage 2: Sigma f. Pi i. Sigma g_i. Pi k. B
    pointwise=tuple((tuple(l for l,b in v),tuple(b for l,b in v)) for v in residual)
    stage2=(f,pointwise)
    # Stage 3: Sigma f. Sigma g. Pi i. Pi k. B
    g=tuple(h for h,w in pointwise);w=tuple(w for h,w in pointwise)
    return (x,stage1,stage2,(f,g,w))

def inner_first(x):
    # Stage 1: Pi i. Sigma j. Sigma h_i. Pi k. B
    stage1=tuple((j,tuple(l for l,b in v),tuple(b for l,b in v)) for j,v in x)
    # Stage 2: bundle each local dependent choice c_i=(j,h_i).
    stage2=tuple(((j,h),w) for j,h,w in stage1)
    # Stage 3: Sigma c:(Pi i. Sigma j. Pi k:K(i,j).L(...)). Pi i. Pi k. B
    c=tuple(choice for choice,w in stage2)
    witnesses=tuple(w for choice,w in stage2)
    stage3=(c,witnesses)
    # Stage 4: apply dependent distributivity to c, retaining witnesses.
    f=tuple(j for j,h in c);g=tuple(h for j,h in c)
    return (x,stage1,stage2,stage3,(f,g,witnesses))

def reconstruct(n):
    f,g,w=n
    return tuple((j,tuple(zip(h,v))) for j,h,v in zip(f,g,w))

def target_values():
    # Independent enumeration of all legally dependent f,g,w, not image of source.
    out=[]
    for f in product(*(J(i) for i in I)):
        for g in product(*(tuple(product(*(L(i,f[i],k) for k in K(i,f[i])))) for i in I)):
            for w in product(*(tuple(product(*(B(i,f[i],k,g[i][k]) for k in K(i,f[i])))) for i in I)):
                out.append((f,g,w))
    return tuple(out)

def valid_target(n):
    f,g,w=n
    if len(f)!=len(I) or len(g)!=len(I) or len(w)!=len(I):return False
    for i in I:
        if f[i] not in J(i):return False
        ks=K(i,f[i])
        if len(g[i])!=len(ks) or len(w[i])!=len(ks):return False
        for k in ks:
            if g[i][k] not in L(i,f[i],k) or w[i][k] not in B(i,f[i],k,g[i][k]):return False
    return True

source=sources();target=target_values()
outer_chains=[outer_first(x) for x in source]
inner_chains=[inner_first(x) for x in source]
assert len(source)==len(set(source)) and len(target)==len(set(target))
assert {chain[-1] for chain in outer_chains}==set(target)
assert {chain[-1] for chain in inner_chains}==set(target)
for x,a,b in zip(source,outer_chains,inner_chains):
    assert a[-1]==b[-1] and valid_target(a[-1])
    assert reconstruct(a[-1])==x and reconstruct(b[-1])==x
    # Every stage retains enough data for reconstruction, not just endpoints.
    f,residual=a[1];assert tuple(zip(f,residual))==x
    f,local=a[2];assert tuple((j,tuple(zip(h,w))) for j,(h,w) in zip(f,local))==x
    assert tuple((j,tuple(zip(h,w))) for j,h,w in b[1])==x
    assert tuple((j,tuple(zip(h,w))) for (j,h),w in b[2])==x
    c,w=b[3];assert tuple((j,tuple(zip(h,v))) for (j,h),v in zip(c,w))==x
for n in target:
    assert outer_first(reconstruct(n))[-1]==n
# An index erasure control: a valid two-entry dependent fibre cannot be silently
# treated as a fixed single entry merely because another f choice has one entry.
example=next(n for n in target if n[0][0]==1)
f,g,w=example
bad=(f,(g[0][:1],)+g[1:],(w[0][:1],)+w[1:])
assert not valid_target(bad)
report={'passed':True,'source_values':len(source),'independently_enumerated_target_values':len(target),
 'outer_route_stages':len(outer_chains[0]),'inner_route_stages':len(inner_chains[0]),
 'every_stage_losslessly_reconstructs_source':True,'two_complete_routes_agree':True,
 'wrong_fixed_index_shortcut_rejected':True,
 'sample_source':source[-1],'sample_outer_chain':outer_chains[-1],'sample_inner_chain':inner_chains[-1],
 'scope':'Finite dependent-set illustration of two full distributivity routes, with a separate written HoTT specification. No nontrivial higher path or automatic self-applicability theorem.'}
root=Path(__file__).resolve().parents[3]
(root/'research/nima/results/dependent-sigma-pi-full-chains.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if not k.startswith('sample')},indent=2))
