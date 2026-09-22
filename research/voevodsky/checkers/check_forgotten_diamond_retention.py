"""Smallest lossless-retention test on the actual two-event recorder.

Standard library and the existing exact source-record verifier only.
The section is linear on this fixed vacuum corner, not a claimed
multiplicative or source-bimodule splitting.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
import runpy,json
ROOT=Path(__file__).resolve().parents[3]
v=runpy.run_path(str(ROOT/'research/voevodsky/certificates/verify_filtered_obstruction.py'))
clean=v['clean'];rho_column=v['rho_column'];rank=v['rank']
p=((0,1),(0,0));q=((1,0),(0,0))
P={p:Fraction(1)};Q={q:Fraction(1)}
def add(x,y):
    out=dict(x)
    for key,value in y.items():out[key]=out.get(key,Fraction(0))+value
    return clean(out)
def neg(x):return {key:-value for key,value in x.items()}
def rho(x):
    assert set(x).issubset({p,q})
    return rho_column(0,x)
def sigma(record):
    assert set(record).issubset({()})
    return clean({p:record.get((),Fraction(0))})
def retain(x):
    visible=rho(x)
    residual=add(x,neg(sigma(visible)))
    return visible,residual
def restore(state):
    visible,residual=state
    assert not rho(residual)
    return add(sigma(visible),residual)
def encode_source(x):
    primes=(2,3)
    result=[]
    for (word,marks),value in sorted(x.items()):
        vertices=[2]
        for event in word:vertices.append(vertices[-1]*primes[event])
        result.append({'event_primes':[primes[e] for e in word],
          'vertices':vertices,'marks':list(marks),'coefficient':str(value)})
    return result
h=add(P,neg(Q))
assert h and P!=Q and rho(P)==rho(Q)=={():Fraction(1)}
assert rho(h)==rho({})=={}
assert rank([P,Q])==2 and rank([rho(P),rho(Q)])==1
assert sigma(rho(P))==P
# Linear identities on a source basis prove reconstruction on the entire
# rational two-path span, not just on the sample values below.
for x in (P,Q):assert restore(retain(x))==x
assert retain(P)!=retain(Q) and retain(h)!=retain({})
assert retain(P)[1]=={} and retain(Q)[1]==neg(h)
# In coordinates x=a*p+b*q, the retained pair is (a+b,b), where b is
# the coefficient of q-p in the residual. Its matrix has determinant one.
retention_matrix=[[1,1],[0,1]]
assert retention_matrix[0][0]*retention_matrix[1][1]-retention_matrix[0][1]*retention_matrix[1][0]==1
samples=0
for a,b in product(map(Fraction,('-2','-1/2','0','1/3','1')),repeat=2):
    x=clean({p:a,q:b});visible,residual=retain(x)
    assert not rho(residual)
    assert restore((visible,residual))==x
    samples+=1
# Deletion really loses data: choosing the canonical lift after erasing
# the residual sends q to p and h to zero, neither of which is its input.
assert sigma(rho(Q))==P and sigma(rho(Q))!=Q
assert sigma(rho(h))=={} and sigma(rho(h))!=h
report={'passed':True,'source_corner':[2,12],
 'source_basis':[encode_source(P),encode_source(Q)],
 'invisible_nonzero_source':encode_source(h),
 'source_dimension':2,'terminal_rank':1,'terminal_kernel_dimension':1,
 'section':'terminal vacuum coefficient times the sorted forgotten path (2,3)',
 'retained_coordinates':'(a+b,b) for source a*p+b*q; residual=b*(q-p)',
 'retention_matrix':retention_matrix,'retention_determinant':1,
 'checks':{'distinct_paths_same_terminal_record':True,
   'nonzero_diamond_same_terminal_record_as_zero':True,
   'linear_basis_reconstruction_identity':True,
   'residual_is_an_actual_kernel_element':True,
   'deleting_residual_destroys_distinguishability':True},
 'additional_rational_samples':samples,
 'scope':'Exact linear reconstruction on this fixed two-path source corner. Demonstrates necessity of retaining distinguishing information here; does not certify arbitrary later transitions, physical source reconstruction, or a canonical equivariant splitting.'}
path=ROOT/'research/voevodsky/results/forgotten-diamond-retention.json'
path.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
