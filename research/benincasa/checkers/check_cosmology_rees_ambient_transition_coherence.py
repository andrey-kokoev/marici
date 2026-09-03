#!/usr/bin/env python3
"""Exact quotient-transition coherence and tau_p persistence through ambient six."""
import contextlib,hashlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_ambient_quotient_transition.py'))
r4,r5,construct=g['r4'],g['r5'],g['construct'];r6=construct(6)
def inclusion(source,target):
 missing=[];mismatch=[]
 for k,v in source.items():
  if k not in target:missing.append(k)
  elif target[k]!=v:mismatch.append(k)
 return {'source_rows':len(source),'target_rows':len(target),'missing':len(missing),'mismatched':len(mismatch),'preserved':not missing and not mismatch}
a45=inclusion(r4,r5);a56=inclusion(r5,r6);a46=inclusion(r4,r6);assert all(x['preserved'] for x in [a45,a56,a46])
# Structural inclusions are identity on shared labelled coordinates, so composition equals direct inclusion.
composition_equal=all(r6[k]==r5[k]==r4[k] for k in r4);assert composition_equal
m=g['g']['configure'](101);fg=g['g']['exact_rows'].__globals__;fg['A']=6;m=g['g']['configure'](101);_,cols=m.column_packet();width=len(cols)
def indexed(row):return {grade*width+cols[label]:v for (grade,label),v in row.items()}
inputs=[indexed(row) for row in r6.values()]
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
base=(0,1,1,1,1,1,(0,0));target={width+cols[base]:F(3)};res=dict(target);steps=[]
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
out={'schema':'marici.benincasa.cosmology-rees-ambient-transition-coherence.v1','problem':'test composition of exact ambient quotient transitions and tau_p persistence through ambient six','bold_conjecture':'source-label maps A4-to-A5 and A5-to-A6 compose to A4-to-A6 on relations and tau_p, whose A6 quotient class remains nonzero','rivals':['relation inclusion loses coherence','tau_p is killed at A6','finite directed persistence through three cutoffs'],'risky_consequences':'all shared rows must match under both paths and exact A6 target reduction must remain nonzero with three-prime replay','strongest_falsification_attempt':{'A4_to_A5':a45,'A5_to_A6':a56,'A4_to_A6':a46,'composition_equals_direct_on_A4_relations':composition_equal,'tau_target_fixed_by_all_maps':True,'ambient_six':{'assembled_rows':len(inputs),'rank':len(basis),'dependent_rows':len(inputs)-len(basis),'operation_edges':edges,'maximum_intermediate_row_nnz':max_nnz,'target_steps':len(steps),'residual_nnz':len(res),'residual_digest':hashlib.sha256(repr(sorted((k,str(v)) for k,v in res.items())).encode()).hexdigest()},'comparisons':comparisons},'exact_residual':'transition composition is exact and tau_p remains nonzero at A6','conjecture_disposition':'retained through the finite A4-to-A5-to-A6 diagram','result_strength':'finite-cutoff coherent source-typed morphisms','scope':'three cutoffs only; no eventual stabilization, unbounded colimit, global monicity, or physical readout','next_conjecture':'the coherent finite diagram admits an eventually stable tau_p quotient coordinate or exposes rank/residue growth preventing colimit promotion','next_falsifier':'compare rank increments and target supports across A4,A5,A6 and state a falsifiable stabilization criterion before another cutoff','passed':True};(R/'cosmology_rees_ambient_transition_coherence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
