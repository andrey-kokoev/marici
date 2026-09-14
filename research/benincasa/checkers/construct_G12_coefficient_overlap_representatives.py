#!/usr/bin/env python3
"""VC2b1a: realize labelled pair overlaps in the common numerator module."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
domain=json.loads((ROOT/'research/benincasa/results/G12_source_labelled_overlap_domain.json').read_text());pres=json.loads((ROOT/'research/benincasa/results/G12_char0_H1_presentation.json').read_text())
a,b,c=s.symbols('a b c');qs=[b+c+1,a+c+1,b+c+2,a+c+2];names=['g1','g2','s23','s31'];P=s.expand(s.prod(qs));edges=list(itertools.combinations(range(4),2));rows=[(i,j,d-i-j) for d in range(19) for i in range(d+1) for j in range(d-i+1)];ridx={e:i for i,e in enumerate(rows)}
columns=[]
for i,j in edges:
 coeff=s.expand(s.prod(qs[k] for k in range(4) if k not in (i,j))) # P/(qi qj), without rational cancellation
 entries=[{'row':ridx[e],'exponent':list(e),'coefficient':str(x)} for e,x in s.Poly(coeff,a,b,c,domain=s.QQ).terms()]
 columns.append({'overlap':f'{names[i]}|{names[j]}','formula':s.sstr(coeff),'entries':entries})
# Exchange permutation (0 1)(2 3); transported oriented edge includes sorting sign.
perm={0:1,1:0,2:3,3:2};transport={}
for i,j in edges:
 image=[perm[i],perm[j]];sign=-1 if image[0]>image[1] else 1;target=tuple(sorted(image));transport[f'{names[i]}|{names[j]}']={'target':f'{names[target[0]]}|{names[target[1]]}','sign':sign}
checks={'six_domain_edges':len(columns)==6,'target_rows_match_presentation':len(rows)==pres['shape'][0]==1330,'all_coefficients_polynomial':all('/' not in x['formula'] for x in columns),'cofactor_identity':all(s.expand(s.sympify(x['formula'])*qs[i]*qs[j]-P)==0 for x,(i,j) in zip(columns,edges)),'exchange_transport_complete':len(transport)==6,'parallel_overlap_coefficients_present':{x['overlap'] for x in columns}>={'g1|s23','g2|s31'}}
assert all(checks.values()),checks
out={'schema':'marici.benincasa.G12-coefficient-valued-overlap-representatives.v1','prospective_action':'VC2b1a_construct_coefficient_valued_overlap_representatives','ambient':'C1=Q[a,b,c]_{degree<=18}, row order total-degree then a,b','common_log_denominator':'P=g1*g2*s23*s31','representative_rule':'[q_i|q_j] maps to P/(q_i*q_j), the coefficient of dlog(q_i) wedge dlog(q_j) in the common denominator frame','columns':columns,'exchange_transport':transport,'resolution':'++','interface_added':'coefficient_overlap_representatives','scope':'Constructs the canonical logarithmic coefficient columns. Their classes in coker(d0), twisted K0 compatibility, and ability to lower the target are separate VC2b2 tests.','next':'Project the six exact columns and target into coker(d0) over the two fast finite-field fibers; test span membership before rational reconstruction.','checks':checks,'passed':True};d=ROOT/'research/benincasa/results/G12_coefficient_overlap_representatives.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'++','columns':6,'nnz':sum(len(x['entries']) for x in columns),'next':'fast modular cokernel span test'}))
