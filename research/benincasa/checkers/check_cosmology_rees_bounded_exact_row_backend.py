#!/usr/bin/env python3
"""DPC exact rational construction of one actual Rees raw row."""
import importlib,itertools,json,os,sys
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'research/benincasa';R=B/'results';sys.path.insert(0,str(B))
prior=json.loads((R/'cosmology_rees_actual_row_integral_lift_interface.json').read_text());assert prior['passed']
point=(3,6,-3);x,y,z=point;energy=x+y+z;x2,y2,z2,c2=x*x,y*y,z*z,energy*energy
k={(4,0):x2,(2,2):-(x2+y2-z2),(0,4):y2,(2,0):x2*(x2-y2-z2)+c2*(y2-x2-z2),(0,2):y2*(y2-x2-z2)+c2*(x2-y2-z2),(0,0):z2*c2*c2+c2*z2*(z2-x2-y2)+z2*x2*y2}
kd0={(a-1,b):a*c for (a,b),c in k.items() if a};names=['g1','g2','g3','g23','g31'];levels=(1,)*5;label={'family':'twisted_derivative','k_pole':0,'levels':list(levels),'axis':0,'exponent':[0,0]}
def add(row,key,value):row[key]=row.get(key,F(0))+value
exact={}
for term,c in kd0.items():add(exact,(1,*levels,term),F(-1,2)*c)
for qi in [1,2,4]:
 raised=list(levels);raised[qi]+=1;add(exact,(0,*raised,(0,0)),F(-1))
exact={k:v for k,v in exact.items() if v}
def project(q,p):return (q.numerator*pow(q.denominator,-1,p))%p
def actual(p):
 os.environ.update(MARICI_FIELD_PRIME=str(p),MARICI_AMBIENT='2',MARICI_POINT='2,3,-5')
 for name in ['check_rank26_total_energy_triple_relation_module','g12_g31_residue_chart_transition','physical_four_mark_residue_twisted_derham']:sys.modules.pop(name,None)
 m=importlib.import_module('check_rank26_total_energy_triple_relation_module');m.charts.GAMMA=-(pow(2,-1,p))%p;_,cols=m.column_packet();exponents=m.base.monomials_at_most(m.AMBIENT);idx=exponents.index((0,0));row=next(itertools.islice(m.raw_relations(point,cols),idx,idx+1));expected={cols[k]:project(v,p) for k,v in exact.items() if project(v,p)};return {'prime':p,'column_count':len(cols),'actual_nnz':len(row),'exact_projected_nnz':len(expected),'matches':row==expected,'residual':{k:(row.get(k,0)-expected.get(k,0))%p for k in set(row)|set(expected) if (row.get(k,0)-expected.get(k,0))%p}}
comparisons=[actual(p) for p in [101,103,107]];assert all(c['matches'] and not c['residual'] for c in comparisons)
out={'schema':'marici.benincasa.cosmology-rees-bounded-exact-row-backend.v1','problem':'construct one source-faithful rational Rees row and compare its modular projections with raw_relations','bold_conjecture':'the first twisted-derivative row has one rational half-twist normalization whose projections reproduce the existing modular row at three primes','rivals':['prime-specific rows have no common lift','coefficientwise rational lift exists','matching dimensions without coefficient identity'],'risky_consequences':'every labelled coefficient must agree after projection at 101, 103, and 107; any mismatch is retained as a sparse residual','strongest_falsification_attempt':{'row_label':label,'exact_coefficients':{str(k):str(v) for k,v in exact.items()},'comparisons':comparisons},'exact_residual':'all three sparse coefficient residuals are empty','conjecture_disposition':'retained for one bounded actual row','source_faithful_features':['structural column labels','deterministic relation-family row label','exact integer fiber polynomial','half twist -1/2','coefficientwise modular projection'],'scope':'one row at ambient degree two; no full exact backend, generator, boundary, or connecting image','next_conjecture':'the exact backend extends to every row family without introducing prime-dependent interpolation coefficients','next_falsifier':'construct one representative from each remaining raw_relations family and compare across the same primes','passed':True};(R/'cosmology_rees_bounded_exact_row_backend.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
