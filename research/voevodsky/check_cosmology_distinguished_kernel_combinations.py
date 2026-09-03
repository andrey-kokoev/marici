"""Recover exact killed combinations in distinguished grade-7/8 x2 spans."""
from __future__ import annotations
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_distinguished_kernel_combinations.json'
def freeze(x):return tuple(freeze(y) for y in x) if isinstance(x,list) else x
def row(r):return {freeze(t['column_label']):Fraction(t['numerator'],t['denominator']) for t in r['residual_terms']}
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,Fraction())+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def relations(rows):
 basis={};deps=[]
 for i,raw in enumerate(rows):
  r=dict(raw);w={i:Fraction(1)}
  while r:
   p=min(r)
   if p not in basis:
    inv=1/r[p];basis[p]=({c:v*inv for c,v in r.items()},{c:v*inv for c,v in w.items()});break
   br,bw=basis[p];a=r[p];add(r,br,-a);add(w,bw,-a)
  if not r:deps.append(w)
 return len(basis),deps
def normalize(v):
 p=min(v);q=v[p];return {i:a/q for i,a in v.items()}
def combine(rows,coef):
 out={}
 for i,a in coef.items():add(out,rows[i],a)
 return out
def coeff_insert(v,basis):
 r=dict(v)
 while r:
  p=min(r)
  if p not in basis:
   q=1/r[p];basis[p]={i:a*q for i,a in r.items()};return True
  add(r,basis[p],-r[p])
 return False
def terms(v,records):return [{'target_id':records[i]['target_id'],'path':records[i]['axis_square'],'numerator':a.numerator,'denominator':a.denominator} for i,a in sorted(normalize(v).items())]
def main():
 a=json.loads((RES/'cosmology_filtered_classification_transport.json').read_text());b=json.loads((RES/'cosmology_filtered_A16_persistence_induction.json').read_text());A12=a['A12_classes'];A14=a['A14_transports'];A16=b['A16_classes'];l14={(x['target_id'],x['axis_square']):x for x in A14};l16={(x['target_id'],x['axis_square']):x for x in A16};groups=[]
 for A,g in ((12,7),(12,8),(14,7),(14,8)):
  if A==12:
   src=[x for x in A12 if x['grade']==g];img=[l14[(x['target_id'],'x2')] for x in src]
  else:
   src=[x for x in A14 if x['grade']==g];path={'x2':'xx','y2':'yx'};img=[l16[(x['target_id'],path[x['axis_square']])] for x in src]
  sr=[row(x) for x in src];ir=[row(x) for x in img];rs,ns=relations(sr);ri,ni=relations(ir);assert rs==3 and ri==1
  cb={};[coeff_insert(v,cb) for v in ns];killed=[]
  for v in ni:
   if coeff_insert(v,cb):
    vn=normalize(v);assert combine(sr,vn) and not combine(ir,vn);killed.append(terms(vn,src))
  assert len(killed)==2;survivor=next(i for i,r in enumerate(ir) if r);groups.append({'source_A':A,'target_A':A+2,'grade':g,'source_elements':len(src),'source_rank':rs,'image_rank':ri,'source_nullity':len(ns),'image_nullity':len(ni),'killed_basis':killed,'surviving_image_representative':{'target_id':src[survivor]['target_id'],'path':src[survivor]['axis_square']}})
 # Compare normalized coefficient patterns after forgetting target ids.
 patterns=Counter(tuple(tuple((t['path'],t['numerator'],t['denominator']) for t in v) for v in x['killed_basis']) for x in groups)
 out={'schema':'marici.voevodsky.cosmology-distinguished-kernel-combinations.v1','status':'exact_two_dimensional_killed_subspaces_constructed','groups':groups,'kernel_dimension_per_group':2,'recurring_coefficient_pattern_count':len(patterns),'decision':'At grades 7 and 8, x2 collapses each rank-three distinguished span to one dimension at both tested steps. Exact bases for the two-dimensional killed subspaces are recorded.','swap_boundary':'The target set is x/y-swap closed, but the second-tangent derivative is not swap-invariant; no symmetry identification of x2 kernels with y2 maps is asserted.','claim_boundary':'Finite algebraic pole-filtered quotient coordinates only; no all-even, DNC, or geometric interpretation.','next_gate':'derive-grade-seven-eight-surviving-line-transport','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='groups'},indent=2))
if __name__=='__main__':main()
