"""Construct exact kernel representatives for filtered squared-axis quotient maps."""
from __future__ import annotations
import json,sys
from collections import Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_filtered_quotient_colon_saturation as colon
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_filtered_transport_kernel_classification.json'
def add(r,b,a):
 for c,v in b.items():
  z=r.get(c,Fraction())+a*v
  if z:r[c]=z
  else:r.pop(c,None)
def reduce(row,basis):
 r={c:Fraction(v) for c,v in row.items() if v}
 while r and min(r) in basis:add(r,basis[min(r)],-r[min(r)])
 return r
def insert_track(row,combo,basis):
 r=dict(row);w=dict(combo)
 while r:
  p=min(r)
  if p not in basis:
   inv=1/r[p];basis[p]=({c:v*inv for c,v in r.items()},{c:v*inv for c,v in w.items()});return None
  br,bw=basis[p];a=r[p];add(r,br,-a);add(w,bw,-a)
 return w
def enc_label(l):return list(l)
def main():
 gate=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text());point=tuple(gate['test_point_xyz']);data={A:colon.build(A,point) for A in (12,14,16)};expected=json.loads((RES/'cosmology_filtered_quotient_colon_saturation.json').read_text());exp={(x['source_A'],x['grade'],x['axis']):x['induced_kernel_dimension'] for x in expected['exact_checks']};groups=[];total=0
 for A,B in ((12,14),(14,16)):
  colsA,invA,sa=data[A];colsB,invB,sb=data[B]
  for g in (6,7,8):
   piv=set(sa[g]['basis']);free=[i for i in sa[g]['columns'] if i not in piv]
   for axis,label in ((0,'x2'),(1,'y2')):
    mb={};kernels=[]
    for fi,i in enumerate(free):
     l=list(invA[i]);e=list(l[-1]);e[axis]+=2;l[-1]=tuple(e);j=colsB[tuple(l)];res=reduce({j:1},sb[g]['basis']);dep=insert_track(res,{fi:1},mb)
     if dep is not None:
      terms=[];parities=set()
      mapped={}
      for q,a in sorted(dep.items()):
       ci=free[q];lab=invA[ci];terms.append({'column_label':enc_label(lab),'numerator':a.numerator,'denominator':a.denominator});parities.add(tuple(x%2 for x in lab[-1]));ml=list(lab);me=list(ml[-1]);me[axis]+=2;ml[-1]=tuple(me);mapped[colsB[tuple(ml)]]=mapped.get(colsB[tuple(ml)],Fraction())+a
      assert not reduce(mapped,sb[g]['basis']);kernels.append({'terms':terms,'term_count':len(terms),'exponent_parities':[list(x) for x in sorted(parities)]})
    assert len(kernels)==exp[(A,g,label)];total+=len(kernels);groups.append({'source_A':A,'target_A':B,'grade':g,'axis':label,'kernel_dimension':len(kernels),'generators':kernels})
 assert total==24
 term_census=Counter(k['term_count'] for x in groups for k in x['generators']);parity_census=Counter(len(k['exponent_parities']) for x in groups for k in x['generators']);persistence=json.loads((RES/'cosmology_filtered_A16_persistence_induction.json').read_text());assert persistence['strongest_falsification']['A16_nonzero_paths']==48
 out={'schema':'marici.voevodsky.cosmology-filtered-transport-kernel-classification.v1','status':'twenty_four_exact_kernel_generators_constructed','kernel_groups':groups,'total_kernel_dimension':total,'representative_term_count_census':{str(k):v for k,v in sorted(term_census.items())},'parity_support_count_census':{str(k):v for k,v in sorted(parity_census.items())},'distinguished_class_relation':'Each of the twelve distinguished one-dimensional class rays avoids the immediate x2/y2 kernels on every tested A12 and A14 step, since all 24 A14 and 48 A16 transported classes are nonzero. This does not establish injectivity on their full two-variable cyclic span.','decision':'Global kernels are explicit but do not contain any tested distinguished class ray. A span-level cyclic-submodule intersection test remains necessary.','claim_boundary':'Exact ordered quotient coordinates in the algebraic pole filtration; no DNC or geometric meaning.','next_gate':'test-twelve-class-cyclic-span-kernel-intersection','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='kernel_groups'},indent=2))
if __name__=='__main__':main()
