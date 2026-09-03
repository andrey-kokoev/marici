#!/usr/bin/env python3
"""Merge all exact Rees checkpoint rows into one global sparse basis."""
import contextlib,hashlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
rows=g['rows'];m0=g['m0'];_,cols=m0.column_packet();inputs=[(label,{cols[k]:v for k,v in row.items()}) for label,row in rows]
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
def proj(q,p):return q.numerator*pow(q.denominator,-1,p)%p
def replay(p):
 mb={};failure=None
 for i,((_,src),(pivot,scale,steps)) in enumerate(zip(inputs,records)):
  r={k:proj(v,p) for k,v in src.items() if proj(v,p)}
  for pp,a in steps:
   aa=proj(a,p)
   for k,v in mb[pp].items():r[k]=(r.get(k,0)-aa*v)%p
   r={k:v for k,v in r.items() if v}
  if pivot is None:
   if r:failure={'input':i,'kind':'dependence'};break
  else:
   if not r or min(r)!=pivot:failure={'input':i,'kind':'pivot','got':None if not r else min(r),'want':pivot};break
   s=proj(scale,p);r={k:s*v%p for k,v in r.items() if s*v%p};want={k:proj(v,p) for k,v in basis[pivot].items() if proj(v,p)}
   if r!=want:failure={'input':i,'kind':'row'};break
   mb[pivot]=r
 return {'prime':p,'rank':len(mb),'failure':failure,'matches':failure is None and len(mb)==len(basis)}
comparisons=[replay(p) for p in [101,103,107]];assert all(x['matches'] for x in comparisons)
payload=[(p,None if s is None else (s.numerator,s.denominator),[(q,(a.numerator,a.denominator)) for q,a in st]) for p,s,st in records]
out={'schema':'marici.benincasa.cosmology-rees-global-checkpoint-basis-merge.v1','problem':'merge block-covered exact Rees rows into one global sparse row-space certificate','bold_conjecture':'the second exact reduction layer has a prime-stable global pivot schedule and rank','rivals':['block-local compatibility fails globally','global fractions alter modular pivots','one exact global basis survives'],'risky_consequences':'all 2524 rows must receive one exact pivot/dependence decision that replays at 101, 103, and 107','strongest_falsification_attempt':{'input_rows':len(inputs),'global_rank':len(basis),'dependent_rows':len(inputs)-len(basis),'operation_edges':edges,'maximum_intermediate_row_nnz':max_nnz,'checkpoint_digest':hashlib.sha256(repr(payload).encode()).hexdigest(),'comparisons':comparisons},'exact_residual':'global rank, pivots, normalized rows, and dependence decisions replay without failure at all three primes','conjecture_disposition':'retained for the ambient-four exact row space','scope':'global source row-space certificate only; no provenance combination selecting the principal target column and no physical generator lift','next_conjecture':'a target-column membership reduction against this exact basis yields a sparse exact witness tied to source-row checkpoint references','next_falsifier':'reduce the principal three-wall target vector, require zero residual, and replay its witness at three primes','passed':True};(R/'cosmology_rees_global_checkpoint_basis_merge.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
