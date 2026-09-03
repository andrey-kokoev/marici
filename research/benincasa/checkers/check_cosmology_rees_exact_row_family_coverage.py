#!/usr/bin/env python3
"""DPC exact projection coverage for all Rees row families and interpolation."""
import importlib,itertools,json,os,sys
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';sys.path.insert(0,str(B))
prior=json.loads((R/'cosmology_rees_bounded_exact_row_backend.json').read_text());assert prior['passed']
point=(3,6,-3);x,y,z=point;e=x+y+z;x2,y2,z2,c2=x*x,y*y,z*z,e*e
k={(4,0):x2,(2,2):-(x2+y2-z2),(0,4):y2,(2,0):x2*(x2-y2-z2)+c2*(y2-x2-z2),(0,2):y2*(y2-x2-z2)+c2*(x2-y2-z2),(0,0):z2*c2*c2+c2*z2*(z2-x2-y2)+z2*x2*y2};q1={(0,1):1,(0,0):-y-z};levels=(1,)*5
def add(row,key,v):row[key]=row.get(key,F(0))+v
krow={(0,*levels,(0,0)):F(1)}
for term,c in k.items():add(krow,(1,*levels,term),F(-c))
raised=list(levels);raised[0]=2;qrow={(0,*levels,(0,0)):F(1)}
for term,c in q1.items():add(qrow,(0,*raised,term),F(-c))
def project(v,p):return (v.numerator*pow(v.denominator,-1,p))%p
def poly_mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def exact_weights(offsets,degree):
 out=[]
 for o in offsets:
  num=[F(1)];den=1
  for other in offsets:
   if other!=o:num=poly_mul(num,[F(-other),F(1)]);den*=o-other
  out.append(num[degree]/den)
 return out
def actual(p):
 os.environ.update(MARICI_FIELD_PRIME=str(p),MARICI_AMBIENT='4',MARICI_POINT='2,3,-5')
 for n in ['check_rank26_total_energy_triple_relation_module','g12_g31_residue_chart_transition','physical_four_mark_residue_twisted_derham']:sys.modules.pop(n,None)
 m=importlib.import_module('check_rank26_total_energy_triple_relation_module');m.charts.GAMMA=-(pow(2,-1,p))%p;_,cols=m.column_packet();mons=m.base.monomials_at_most(m.AMBIENT);first=m.charts.K_DEPTH*2*len(mons);kcount=m.charts.K_DEPTH*(m.charts.Q_DEPTH**len(m.NAMES))*len(m.base.monomials_at_most(m.AMBIENT-4));gen=m.raw_relations(point,cols);picked={}
 for idx,row in enumerate(gen):
  if idx==first:picked['K_multiplication']=row
  if idx==first+kcount:picked['q_multiplication']=row;break
 expected={'K_multiplication':{cols[k]:project(v,p) for k,v in krow.items() if project(v,p)},'q_multiplication':{cols[k]:project(v,p) for k,v in qrow.items() if project(v,p)}}
 families={name:{'actual_nnz':len(picked[name]),'exact_nnz':len(expected[name]),'matches':picked[name]==expected[name],'residual_nnz':len({c for c in set(picked[name])|set(expected[name]) if (picked[name].get(c,0)-expected[name].get(c,0))%p})} for name in picked}
 weights={}
 for degree in [1,2]:
  ew=exact_weights(m.OFFSETS,degree);mw=m.interpolation_weights(degree);weights[str(degree)]={'exact':[str(v) for v in ew],'matches':mw==[project(v,p) for v in ew]}
 return {'prime':p,'families':families,'interpolation_weights':weights}
comparisons=[actual(p) for p in [101,103,107]];assert all(all(x['matches'] and x['residual_nnz']==0 for x in c['families'].values()) and all(x['matches'] for x in c['interpolation_weights'].values()) for c in comparisons)
out={'schema':'marici.benincasa.cosmology-rees-exact-row-family-coverage.v1','problem':'test prime-independent exact representatives for every remaining raw-row family and interpolation interface','bold_conjecture':'K-multiplication, q-multiplication, and interpolation weights have common rational constructions matching three prime fields','rivals':['first-family coincidence only','prime-dependent interpolation obstruction','uniform rational backend'],'risky_consequences':'both remaining row families and degree-one/two interpolation weights must agree coefficientwise at 101, 103, and 107','strongest_falsification_attempt':{'exact_K_row_nnz':len(krow),'exact_q_row_nnz':len(qrow),'comparisons':comparisons},'exact_residual':'all row residual counts vanish and every interpolation-weight list matches','conjecture_disposition':'retained for one representative per family at ambient degree four','all_raw_relation_families_covered_by_representative':True,'interpolation_prime_independent_rational_lift':True,'full_exact_backend_constructed':False,'actual_generator_constructed':False,'next_conjecture':'a shared exact-row iterator can emit stable labels and project to the complete modular raw_relations stream on a bounded ambient presentation','next_falsifier':'compare every row, order, label, and coefficient at ambient degree two or four across exact and modular iterators','passed':True};(R/'cosmology_rees_exact_row_family_coverage.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
