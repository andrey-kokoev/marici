#!/usr/bin/env python3
"""Exact membership reduction of the principal tau_p normal-jet target."""
import contextlib,hashlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_exact_normal_jet_target_constructor.py'))
jets=g['jets'];m0=g['m0'];_,cols=m0.column_packet();width=len(cols);base_label=g['base_label']
def idxrow(parts):
 out={}
 for grade,row in parts:
  for k,v in row.items():out[grade*width+cols[k]]=v
 return out
inputs=[]
for i,(r0,r1,r2) in enumerate(jets):inputs.extend([(('shift2',i),idxrow([(2,r0)])),(('upper',i),idxrow([(1,r0),(2,r1)])),(('jet',i),idxrow([(0,r0),(1,r1),(2,r2)]))])
def clean(r):return {k:v for k,v in r.items() if v}
def axpy(r,a,b):
 for k,v in b.items():r[k]=r.get(k,F(0))-a*v
 return clean(r)
basis={};records=[];edges=0;max_nnz=0
for i,(label,src) in enumerate(inputs):
 r=dict(src);steps=[]
 while r and min(r) in basis:
  p=min(r);a=r[p];steps.append((p,a));edges+=1;r=axpy(r,a,basis[p]);max_nnz=max(max_nnz,len(r))
 if r:p=min(r);s=F(1)/r[p];r={k:s*v for k,v in r.items()};basis[p]=r;records.append((p,s,steps))
 else:records.append((None,None,steps))
target={width+cols[base_label]:F(3)};residual=dict(target);target_steps=[]
while residual and min(residual) in basis:
 p=min(residual);a=residual[p];target_steps.append((p,a));residual=axpy(residual,a,basis[p])
member=not residual
# Reachable basis DAG nodes from target reductions.
pivot_record={p:i for i,(p,_,_) in enumerate(records) if p is not None};stack=[p for p,_ in target_steps];reachable=set()
while stack:
 p=stack.pop();i=pivot_record[p]
 if i in reachable:continue
 reachable.add(i);stack.extend(pp for pp,_ in records[i][2])
def proj(q,p):return q.numerator*pow(q.denominator,-1,p)%p
def replay_target(p):
 r={k:proj(v,p) for k,v in target.items() if proj(v,p)}
 for pp,a in target_steps:
  aa=proj(a,p);br={k:proj(v,p) for k,v in basis[pp].items() if proj(v,p)}
  for k,v in br.items():r[k]=(r.get(k,0)-aa*v)%p
  r={k:v for k,v in r.items() if v}
 want={k:proj(v,p) for k,v in residual.items() if proj(v,p)};return {'prime':p,'residual_nnz':len(r),'matches_exact_residual':r==want,'zero':not r}
comparisons=[replay_target(p) for p in [101,103,107]];assert all(x['matches_exact_residual'] for x in comparisons)
payload=[(p,None if s is None else (s.numerator,s.denominator),[(q,(a.numerator,a.denominator)) for q,a in st]) for p,s,st in records]
out={'schema':'marici.benincasa.cosmology-rees-exact-assembled-target-membership.v1','problem':'decide exact row-space membership of the typed principal tau_p target','bold_conjecture':'the one-coordinate normal-grade-one target reduces to zero against the exact assembled relations and admits a replayable sparse provenance DAG','rivals':['target lies in the relation span','target survives in the quotient','modular zero is caused by a bad prime'],'risky_consequences':'exact reduction must have empty residual and the same result must replay at 101, 103, and 107','strongest_falsification_attempt':{'assembled_input_rows':len(inputs),'assembled_rank':len(basis),'dependent_rows':len(inputs)-len(basis),'operation_edges':edges,'maximum_intermediate_row_nnz':max_nnz,'basis_checkpoint_digest':hashlib.sha256(repr(payload).encode()).hexdigest(),'target_steps':len(target_steps),'reachable_basis_nodes':len(reachable),'exact_residual_nnz':len(residual),'exact_residual':{str(k):str(v) for k,v in residual.items()},'comparisons':comparisons},'exact_residual':('zero' if member else 'nonzero target residue retained explicitly'),'conjecture_disposition':('retained' if member else 'falsified: tau_p survives this bounded assembled relation quotient'),'membership':member,'witness_kind':('checkpoint DAG over source relation rows' if member else None),'scope':'ambient-four, second normal jet, chosen source point and exact p-cell normalization; no physical-period promotion','next_conjecture':('the exact witness descends to a primitive integral source lift after denominator clearing' if member else 'the nonzero tau_p residue is the primitive quotient class and must be compared with the claimed rank-26 target sector'),'next_falsifier':('clear denominators, divide content, replay the primitive integer witness, and test its physical readout map' if member else 'compare the residue against an independently derived quotient coordinate and test ambient stabilization'),'passed':True};(R/'cosmology_rees_exact_assembled_target_membership.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
