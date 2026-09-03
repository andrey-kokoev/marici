#!/usr/bin/env python3
"""Block-streaming exact elimination covering every bounded Rees raw row."""
import contextlib,hashlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
rows=g['rows'];m0=g['m0'];_,cols=m0.column_packet();BLOCK=64
inputs=[(label,{cols[k]:v for k,v in row.items()}) for label,row in rows]
def clean(r):return {k:v for k,v in r.items() if v}
def axpy(r,a,b):
 for k,v in b.items():r[k]=r.get(k,F(0))-a*v
 return clean(r)
def eliminate(block):
 basis={};records=[];edges=0
 for label,src in block:
  r=dict(src);steps=[]
  while r and min(r) in basis:
   p=min(r);a=r[p];steps.append((p,a));edges+=1;r=axpy(r,a,basis[p])
  if r:p=min(r);s=F(1)/r[p];r={k:s*v for k,v in r.items()};basis[p]=r;records.append((p,s,steps))
  else:records.append((None,None,steps))
 return basis,records,edges
def proj(q,p):return q.numerator*pow(q.denominator,-1,p)%p
def replay(block,basis,records,p):
 mb={}
 for (_,src),(pivot,scale,steps) in zip(block,records):
  r={k:proj(v,p) for k,v in src.items() if proj(v,p)}
  for pp,a in steps:
   aa=proj(a,p)
   for k,v in mb[pp].items():r[k]=(r.get(k,0)-aa*v)%p
   r={k:v for k,v in r.items() if v}
  if pivot is None:
   if r:return False
  else:
   if not r or min(r)!=pivot:return False
   s=proj(scale,p);r={k:s*v%p for k,v in r.items() if s*v%p};want={k:proj(v,p) for k,v in basis[pivot].items() if proj(v,p)}
   if r!=want:return False
   mb[pivot]=r
 return len(mb)==len(basis)
blocks=[inputs[i:i+BLOCK] for i in range(0,len(inputs),BLOCK)];summaries=[];all_ok={p:True for p in [101,103,107]};total_edges=0;rank_sum=0
for bi,block in enumerate(blocks):
 basis,records,edges=eliminate(block);total_edges+=edges;rank_sum+=len(basis);matches={str(p):replay(block,basis,records,p) for p in all_ok}
 for p in all_ok:all_ok[p]&=matches[str(p)]
 rec_digest=hashlib.sha256(repr([(x[0],None if x[1] is None else (x[1].numerator,x[1].denominator),[(q,(a.numerator,a.denominator)) for q,a in x[2]]) for x in records]).encode()).hexdigest()
 summaries.append({'block':bi,'start':bi*BLOCK,'rows':len(block),'rank':len(basis),'edges':edges,'first_family':block[0][0][0],'last_family':block[-1][0][0],'checkpoint_digest':rec_digest,'matches':matches})
assert all(all_ok.values()) and sum(x['rows'] for x in summaries)==2524
out={'schema':'marici.benincasa.cosmology-rees-all-family-streaming-elimination.v1','problem':'cover all exact Rees source rows by bounded sparse elimination checkpoints','bold_conjecture':'fixed-size exact blocks cover all 2524 rows with prime-stable pivots and checkpoint replay without dense provenance','rivals':['later q blocks destabilize pivots','cross-family boundaries obstruct replay','bounded block certificates cover the stream'],'risky_consequences':'every one of 40 block schedules must replay at 101, 103, and 107 and the blocks must cover every row exactly once','strongest_falsification_attempt':{'block_size':BLOCK,'block_count':len(blocks),'rows_covered':sum(x['rows'] for x in summaries),'block_rank_sum_not_global_rank':rank_sum,'operation_edge_count':total_edges,'dense_provenance_vectors_materialized':False,'all_prime_replays':{str(k):v for k,v in all_ok.items()},'blocks':summaries},'exact_residual':'all 40 blocks, including both family crossings, replay at all three primes; no rows are omitted','conjecture_disposition':'retained for block-local streaming elimination across the full source stream','scope':'block ranks do not determine global rank or an exact target relation because bases are reset at checkpoints','next_conjecture':'checkpoint bases can be merged by a second exact reduction layer to recover the global row-space rank and a target certificate','next_falsifier':'reduce the union of block bases exactly and compare its global pivot schedule and rank at three primes','passed':True};(R/'cosmology_rees_all_family_streaming_elimination.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='strongest_falsification_attempt'}|{'summary':{k:v for k,v in out['strongest_falsification_attempt'].items() if k!='blocks'}},indent=2))
