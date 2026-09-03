#!/usr/bin/env python3
"""Construct exact width-three normal jets and the principal tau_p target."""
import contextlib,hashlib,io,itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results'
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(B/'checkers/check_cosmology_rees_complete_bounded_exact_row_iterator.py'))
f=g['exact_rows'];fg=f.__globals__;m0=g['m0'];offsets=list(m0.OFFSETS);basepoint=(3,6,-3)
def rows_at(point):
 k,q=g['exact_fiber'](*point);fg['k']=k;fg['q']=q;fg['kd']=[g['deriv'](k,a) for a in range(2)];fg['qd']=[[g['deriv'](poly,a) for a in range(2)] for poly in q];return list(f())
samples=[rows_at((basepoint[0],basepoint[1],basepoint[2]+o)) for o in offsets];assert all([x[0] for x in s]==[x[0] for x in samples[0]] for s in samples)
def pmul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def weights(degree):
 out=[]
 for o in offsets:
  num=[F(1)];den=1
  for other in offsets:
   if other!=o:num=pmul(num,[F(-other),F(1)]);den*=o-other
  out.append(num[degree]/den)
 return out
w1,w2=weights(1),weights(2)
def combine(rs,ws):
 out={}
 for r,w in zip(rs,ws):
  for k,v in r.items():out[k]=out.get(k,F(0))+w*v
 return {k:v for k,v in out.items() if v}
jets=[];assembled_digest=hashlib.sha256()
for i in range(len(samples[0])):
 rs=[s[i][1] for s in samples];r0=rs[offsets.index(0)];r1=combine(rs,w1);r2=combine(rs,w2);jets.append((r0,r1,r2))
 for kind,vec in [('shift2',{(2,k):v for k,v in r0.items()}),('upper',{**{(1,k):v for k,v in r0.items()},**{(2,k):v for k,v in r1.items()}}),('jet',{**{(0,k):v for k,v in r0.items()},**{(1,k):v for k,v in r1.items()},**{(2,k):v for k,v in r2.items()}})]:assembled_digest.update(repr((i,kind,sorted((repr(k),str(v)) for k,v in vec.items()))).encode())
# p=x+y+3z vanishes at basepoint and has first normal coefficient 3.
base_label=(0,1,1,1,1,1,(0,0));target={(1,base_label):F(3)}
def proj(v,p):return v.numerator*pow(v.denominator,-1,p)%p
def modular_check(p):
 m=g['configure'](p);_,columns=m.column_packet();gens=[m.raw_relations((basepoint[0],basepoint[1],basepoint[2]+o),columns) for o in offsets];checked=0
 mw1=m.interpolation_weights(1);mw2=m.interpolation_weights(2)
 for i,allrows in enumerate(zip(*gens,strict=True)):
  r0=dict(allrows[offsets.index(0)]);r1=m.combine(allrows,mw1);r2=m.combine(allrows,mw2)
  for got,ex in zip((r0,r1,r2),jets[i]):
   want={columns[k]:proj(v,p) for k,v in ex.items() if proj(v,p)}
   if got!=want:return {'prime':p,'checked':checked,'matches':False,'failure_row':i}
  checked+=1
 return {'prime':p,'checked':checked,'matches':True,'target':{str(len(columns)+columns[base_label]):3%p}}
comparisons=[modular_check(p) for p in [101,103,107]];assert all(x['matches'] and x['checked']==2524 for x in comparisons)
out={'schema':'marici.benincasa.cosmology-rees-exact-normal-jet-target-constructor.v1','problem':'construct the exact assembled normal-jet relation space and a typed principal tau_p coordinate vector','bold_conjecture':'seven exact offset fibers and rational coefficient weights define width-three jets, while p=x+y+3z maps to coefficient 3 in normal grade one at the five-denominator constant column','rivals':['tau_p remains untyped','modular interpolation has no exact lift','the p cell defines a unique labelled jet target'],'risky_consequences':'all r0,r1,r2 rows must project to modular jets at three primes and the target must name its grade, raw column label, and coefficient','strongest_falsification_attempt':{'offsets':offsets,'raw_rows_per_offset':2524,'assembled_relation_rows':7572,'assembled_digest':assembled_digest.hexdigest(),'target_vector':{'normal_grade':1,'raw_column_label':list(base_label[:-1])+[list(base_label[-1])],'coefficient':'3'},'comparisons':comparisons},'exact_residual':'all 7572 exact jet components project without mismatch; tau_p has one explicit labelled coordinate','conjecture_disposition':'retained for the ambient-four width-three normal-jet presentation','target_provenance':['p=-q_g1-q_g2+q_g3','p(basepoint)=0','p(z+offset)=3 offset','coefficient-of-offset occupies normal grade one'],'membership_decidable':True,'membership_computed':False,'scope':'typed algebraic jet target; no row-space membership result or physical period','next_conjecture':'the one-coordinate tau_p target reduces to zero against the exact assembled relation basis and yields a sparse source-row witness','next_falsifier':'perform exact assembled elimination with provenance and retain any nonzero target residual','passed':True};(R/'cosmology_rees_exact_normal_jet_target_constructor.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
