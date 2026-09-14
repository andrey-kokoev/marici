#!/usr/bin/env python3
"""VC2f: exact characteristic-zero weighted-overlap reconstruction via shifted-wall Bezout."""
import hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s, itertools
data=json.loads((ROOT/'research/benincasa/results/cleared-relative-shape-jet.json').read_text());a,b,c=s.symbols('a b c');L={'a':a,'b':b,'c':c};q=[b+c+1,a+c+1,b+c+2,a+c+2];names=['g1','g2','s23','s31'];edges=list(itertools.combinations(range(4),2));cof=[s.expand(s.prod(q[k] for k in range(4) if k not in e)) for e in edges]
N23=s.sympify(data['terms']['G12_g23']['cleared_numerator'],locals=L);N31=s.sympify(data['terms']['G12_g31']['cleared_numerator'],locals=L);N=s.expand(N23*q[3]**3-N31*q[2]**3)
signs=[1,0, -1,-1,0,1] # edges 01,02,03,12,13,23
bezout=s.expand(sum(z*f for z,f in zip(signs,cof)));weights=[s.expand(z*N) for z in signs];reconstructed=s.expand(sum(w*f for w,f in zip(weights,cof)))
swap={a:b,b:a};checks={'shift_relations':s.expand(q[2]-q[0]-1)==0 and s.expand(q[3]-q[1]-1)==0,'bezout_identity':bezout==1,'exact_target_reconstruction':reconstructed==N,'four_nonzero_weights':sum(w!=0 for w in weights)==4,'weight_degree_17':max(s.Poly(w,a,b,c).total_degree() for w in weights if w)==17,'target_exchange_odd':s.expand(N.xreplace(swap)+N)==0}
assert all(checks.values()),checks
payload=[{'overlap':f'{names[i]}|{names[j]}','weight':s.sstr(w),'weight_degree':(-1 if w==0 else s.Poly(w,a,b,c).total_degree())} for (i,j),w in zip(edges,weights)]
out={'schema':'marici.benincasa.G12-exact-weighted-overlap-reconstruction.v1','prospective_action':'VC2f_exact_weighted_overlap_reconstruction','bezout_identity':'(s23*s31)-(g2*s23)-(g1*s31)+(g1*g2)=1','edge_signs':dict(zip([x['overlap'] for x in payload],signs)),'exact_weights':payload,'target_numerator_sha256':hashlib.sha256(s.sstr(N).encode()).hexdigest(),'identity':'sum_edge weight_edge*P/(q_i*q_j)=N_odd exactly over Q','resolution':'++','interface_added':'exact_weighted_overlap_solution','degree_comparison':{'modular_minimum_with_d0':15,'explicit_Bezout_solution':17,'interpretation':'exact existence is proved; minimum-degree exact reconstruction is not claimed'},'next':'Run signed-minor restrictions on this explicit degree-17 solution; update infinity decay from r^-7 to r^-5.','checks':checks,'passed':True};p=ROOT/'research/benincasa/results/G12_exact_weighted_overlap_reconstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'resolution':'++','degree':17,'nonzero_weights':4,'next':out['next']}))
