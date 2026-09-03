#!/usr/bin/env python3
"""Exact sparse elimination DAG on a bounded actual Rees row prefix."""
import contextlib,hashlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';source=B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(source))
rows=g['rows'];m0=g['m0'];_,cols=m0.column_packet();PREFIX=60
inputs=[{cols[k]:v for k,v in row.items()} for _,row in rows[:PREFIX]];labels=[label for label,_ in rows[:PREFIX]]
def clean(r):return {k:v for k,v in r.items() if v}
def axpy(r,a,b):
 for k,v in b.items():r[k]=r.get(k,F(0))-a*v
 return clean(r)
basis={};records=[];edge_count=0
for i,src in enumerate(inputs):
 r=dict(src);steps=[]
 while r:
  p=min(r)
  if p not in basis:break
  a=r[p];steps.append((p,a));edge_count+=1;r=axpy(r,a,basis[p])
 if r:
  p=min(r);scale=F(1,1)/r[p];r={k:scale*v for k,v in r.items()};basis[p]=r;status='pivot'
 else:p=None;scale=None;status='dependent'
 records.append({'input':i,'status':status,'pivot':p,'steps':steps,'scale':scale})
def qstr(q):return f'{q.numerator}/{q.denominator}'
payload=[(x['input'],x['status'],x['pivot'],[(p,qstr(a)) for p,a in x['steps']],None if x['scale'] is None else qstr(x['scale'])) for x in records];digest=hashlib.sha256(repr(payload).encode()).hexdigest()
def proj(q,p):return q.numerator*pow(q.denominator,-1,p)%p
def replay(p):
 mb={};fail=[]
 for rec,src in zip(records,inputs):
  r={k:proj(v,p) for k,v in src.items() if proj(v,p)}
  for pivot,a in rec['steps']:
   aa=proj(a,p)
   for k,v in mb[pivot].items():r[k]=(r.get(k,0)-aa*v)%p
   r={k:v for k,v in r.items() if v}
  if rec['status']=='pivot':
   if not r or min(r)!=rec['pivot']:fail.append({'input':rec['input'],'kind':'pivot','got':None if not r else min(r),'want':rec['pivot']});break
   s=proj(rec['scale'],p);r={k:s*v%p for k,v in r.items() if s*v%p};want={k:proj(v,p) for k,v in basis[rec['pivot']].items() if proj(v,p)}
   if r!=want:fail.append({'input':rec['input'],'kind':'row','residual_nnz':sum((r.get(k,0)-want.get(k,0))%p!=0 for k in set(r)|set(want))});break
   mb[rec['pivot']]=r
  elif r:fail.append({'input':rec['input'],'kind':'dependence'});break
 return {'prime':p,'checkpoint_count':len(records),'basis_rank':len(mb),'failures':fail,'matches':not fail and len(mb)==len(basis)}
comparisons=[replay(p) for p in [101,103,107]];assert all(x['matches'] for x in comparisons)
out={'schema':'marici.benincasa.cosmology-rees-exact-checkpointed-elimination.v1','problem':'test a sparse exact elimination certificate on actual labelled Rees rows without dense provenance expansion','bold_conjecture':'a bounded exact elimination DAG has a stable pivot schedule and reproduces its normalized checkpoint rows modulo three primes','rivals':['exact denominators destabilize modular pivots','dense provenance is necessary','sparse checkpoint replay suffices'],'risky_consequences':'each recorded elimination edge, pivot, normalization, and dependence decision must replay exactly at 101, 103, and 107','strongest_falsification_attempt':{'stream_prefix_rows':PREFIX,'input_label_digest':hashlib.sha256(repr(labels).encode()).hexdigest(),'checkpoint_digest':digest,'rank':len(basis),'edge_count':edge_count,'dense_provenance_vectors_materialized':False,'comparisons':comparisons},'exact_residual':'all 60 checkpoints and normalized basis rows replay with no pivot, row, or dependence failure at three primes','conjecture_disposition':'retained for the complete twisted-derivative family prefix','certificate_kind':'sparse exact operation DAG with normalized-row checkpoints','scope':'60-row twisted-derivative block only; not all 2524 rows and not a target physical relation','next_conjecture':'streaming block checkpoints extend through K- and q-multiplication families while retaining a prime-stable pivot schedule','next_falsifier':'process all families in bounded blocks and compare rank, pivots, and checkpoint digests at three primes','passed':True};(R/'cosmology_rees_exact_checkpointed_elimination.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
