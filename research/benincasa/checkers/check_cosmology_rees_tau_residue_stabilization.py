#!/usr/bin/env python3
"""Ambient-four to ambient-five stabilization test for the exact tau_p residue."""
import contextlib,hashlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';prior=json.loads((R/'cosmology_rees_exact_assembled_target_membership.json').read_text());assert prior['passed'] and not prior['membership']
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
A=5;f=g['exact_rows'];fg=f.__globals__;fg['A']=A;m=g['configure'](101);_,cols=m.column_packet();width=len(cols);offsets=list(m.OFFSETS);point=(3,6,-3)
def rows_at(pt):
 k,q=g['exact_fiber'](*pt);fg['k']=k;fg['q']=q;fg['kd']=[g['deriv'](k,a) for a in range(2)];fg['qd']=[[g['deriv'](poly,a) for a in range(2)] for poly in q];return list(f())
samples=[rows_at((point[0],point[1],point[2]+o)) for o in offsets];labels=[x[0] for x in samples[0]];assert all([x[0] for x in s]==labels for s in samples)
def pmul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def weights(d):
 out=[]
 for o in offsets:
  n=[F(1)];den=1
  for z in offsets:
   if z!=o:n=pmul(n,[F(-z),F(1)]);den*=o-z
  out.append(n[d]/den)
 return out
w1,w2=weights(1),weights(2)
def combine(rs,ws):
 out={}
 for r,w in zip(rs,ws):
  for k,v in r.items():out[k]=out.get(k,F(0))+w*v
 return {k:v for k,v in out.items() if v}
def index(parts):
 out={}
 for grade,row in parts:
  for k,v in row.items():out[grade*width+cols[k]]=v
 return out
inputs=[]
for i in range(len(labels)):
 rs=[s[i][1] for s in samples];r0=rs[offsets.index(0)][1] if False else rs[offsets.index(0)];r1=combine(rs,w1);r2=combine(rs,w2);inputs.extend([index([(2,r0)]),index([(1,r0),(2,r1)]),index([(0,r0),(1,r1),(2,r2)])])
def clean(r):return {k:v for k,v in r.items() if v}
def axpy(r,a,b):
 for k,v in b.items():r[k]=r.get(k,F(0))-a*v
 return clean(r)
basis={};edges=0;max_nnz=0
for src in inputs:
 r=dict(src)
 while r and min(r) in basis:
  p=min(r);a=r[p];edges+=1;r=axpy(r,a,basis[p]);max_nnz=max(max_nnz,len(r))
 if r:p=min(r);s=F(1)/r[p];basis[p]={k:s*v for k,v in r.items()}
base_label=(0,1,1,1,1,1,(0,0));target={width+cols[base_label]:F(3)};res=dict(target);steps=[]
while res and min(res) in basis:
 p=min(res);a=res[p];steps.append((p,a));res=axpy(res,a,basis[p])
def proj(q,p):return q.numerator*pow(q.denominator,-1,p)%p
def replay(p):
 r={k:proj(v,p) for k,v in target.items()}
 for pp,a in steps:
  aa=proj(a,p)
  for k,v in basis[pp].items():r[k]=(r.get(k,0)-aa*proj(v,p))%p
  r={k:v for k,v in r.items() if v}
 want={k:proj(v,p) for k,v in res.items() if proj(v,p)};return {'prime':p,'residual_nnz':len(r),'matches':r==want,'nonzero':bool(r)}
comparisons=[replay(p) for p in [101,103,107]];assert res and all(x['matches'] and x['nonzero'] for x in comparisons)
# Faithful coordinate is the deterministic nonpivot-column normal form at each ambient.
out={'schema':'marici.benincasa.cosmology-rees-tau-residue-stabilization.v1','problem':'test persistence and quotient typing of tau_p under ambient enlargement from four to five','bold_conjecture':'the exact tau_p class remains nonzero in the ambient-five assembled quotient under deterministic faithful normal-form coordinates','rivals':['ambient-four residue is truncation artifact','tau_p remains nonzero at ambient five','equal modular signatures without exact persistence'],'risky_consequences':'ambient-five exact reduction must retain a nonzero residue and project coefficientwise at three primes','strongest_falsification_attempt':{'ambient_four':{'rank':prior['strongest_falsification_attempt']['assembled_rank'],'residual_nnz':prior['strongest_falsification_attempt']['exact_residual_nnz']},'ambient_five':{'raw_rows_per_offset':len(labels),'assembled_rows':len(inputs),'rank':len(basis),'dependent_rows':len(inputs)-len(basis),'operation_edges':edges,'maximum_intermediate_row_nnz':max_nnz,'target_steps':len(steps),'residual_nnz':len(res),'residual_digest':hashlib.sha256(repr(sorted((k,str(v)) for k,v in res.items())).encode()).hexdigest()},'faithful_coordinate':'deterministic echelon normal form on the exact quotient','comparisons':comparisons},'exact_residual':'tau_p remains nonzero at ambient five; its normal form changes dimension and is retained by exact labelled coordinates','conjecture_disposition':'retained for nonvanishing persistence from ambient four to five','canonical_identity_boundary':'both residues are images of the same source-derived one-coordinate tau_p target, but no colimit stabilization theorem is proved','scope':'two finite cutoffs only; not unbounded, canonical-colimit, or physical/readout promotion','next_conjecture':'the tau_p class persists at one further ambient cutoff or admits a proved transition map between quotient normal forms','next_falsifier':'construct the ambient-five to ambient-six quotient transition and test the target image','passed':True};(R/'cosmology_rees_tau_residue_stabilization.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
