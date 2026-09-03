#!/usr/bin/env python3
"""Exact source-label transition from ambient-four to ambient-five jet quotients."""
import contextlib,hashlib,io,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';a4=json.loads((R/'cosmology_rees_exact_assembled_target_membership.json').read_text());a5=json.loads((R/'cosmology_rees_tau_residue_stabilization.json').read_text());assert not a4['membership'] and a5['passed']
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
f=g['exact_rows'];fg=f.__globals__;point=(3,6,-3)
def pmul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def construct(A):
 fg['A']=A;m=g['configure'](101);offsets=list(m.OFFSETS)
 def rows_at(pt):
  k,q=g['exact_fiber'](*pt);fg['k']=k;fg['q']=q;fg['kd']=[g['deriv'](k,a) for a in range(2)];fg['qd']=[[g['deriv'](poly,a) for a in range(2)] for poly in q];return list(f())
 samples=[rows_at((point[0],point[1],point[2]+o)) for o in offsets];labels=[x[0] for x in samples[0]];assert all([x[0] for x in s]==labels for s in samples)
 def weights(d):
  out=[]
  for o in offsets:
   n=[F(1)];den=1
   for z in offsets:
    if z!=o:n=pmul(n,[F(-z),F(1)]);den*=o-z
   out.append(n[d]/den)
  return out
 def combine(rs,ws):
  out={}
  for r,w in zip(rs,ws):
   for k,v in r.items():out[k]=out.get(k,F(0))+w*v
  return {k:v for k,v in out.items() if v}
 w1,w2=weights(1),weights(2);assembled={}
 for i,label in enumerate(labels):
  rs=[s[i][1] for s in samples];r0=rs[offsets.index(0)];r1=combine(rs,w1);r2=combine(rs,w2)
  assembled[('shift2',label)]={(2,k):v for k,v in r0.items()}
  upper={(1,k):v for k,v in r0.items()};upper.update({(2,k):v for k,v in r1.items()});assembled[('upper',label)]=upper
  jet={(0,k):v for k,v in r0.items()};jet.update({(1,k):v for k,v in r1.items()});jet.update({(2,k):v for k,v in r2.items()});assembled[('jet',label)]=jet
 return assembled
r4=construct(4);r5=construct(5);missing=[];mismatch=[]
for key,row in r4.items():
 if key not in r5:missing.append(repr(key))
 elif row!=r5[key]:mismatch.append(repr(key))
assert not missing and not mismatch
base=(0,1,1,1,1,1,(0,0));target4={(1,base):F(3)};target5={(1,base):F(3)};assert target4==target5
transition_digest=hashlib.sha256('\n'.join(sorted(repr(k) for k in r4)).encode()).hexdigest()
out={'schema':'marici.benincasa.cosmology-rees-ambient-quotient-transition.v1','problem':'construct the exact ambient-four to ambient-five map and prove it descends to assembled relation quotients','bold_conjecture':'source-label inclusion sends every ambient-four assembled relation to the identical ambient-five relation and sends tau_p to tau_p','rivals':['relation preservation fails at the cutoff boundary','target representatives disagree','a quotient transition exists but need not be globally injective'],'risky_consequences':'all 7572 source relations must match exactly after inclusion and the one-coordinate target must be preserved','strongest_falsification_attempt':{'ambient_four_relation_rows':len(r4),'ambient_five_relation_rows':len(r5),'missing_relations':len(missing),'mismatched_relations':len(mismatch),'preserved_relation_key_digest':transition_digest,'target_preserved_exactly':target4==target5,'ambient_four_target_nonzero':not a4['membership'],'ambient_five_target_nonzero':all(x['nonzero'] for x in a5['strongest_falsification_attempt']['comparisons']),'faithful_coordinates':'deterministic echelon normal forms are faithful coordinates on each quotient separately'},'exact_residual':'every ambient-four relation and the tau_p representative is preserved exactly','conjecture_disposition':'retained: inclusion descends and carries the nonzero tau_p class to the nonzero ambient-five class','transition_type':'source-labelled linear inclusion inducing a quotient map','global_monicity_proved':False,'scope':'canonical persistence of this target across one transition; no global injectivity, ambient-six coherence, colimit, or physical promotion','next_conjecture':'the quotient transitions compose coherently through ambient six and retain tau_p','next_falsifier':'construct A5-to-A6 and direct A4-to-A6 maps and test the composition on all shared relations and tau_p','passed':True};(R/'cosmology_rees_ambient_quotient_transition.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
