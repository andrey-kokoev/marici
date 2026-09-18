#!/usr/bin/env python3
"""Exact check of the line-dependent N2MHV prefactor phi."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from momentum_twistor_constructors import four_bracket as br, plane_plane_line_contraction as pp
fixture=json.loads((ROOT/'research/nima/fixtures/n2mhv-phi-plane-intersection-prefactor.v1.json').read_text())
xs=map(s.Integer,(1,2,4,7,11,16,22,29,37));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
def phi(D):
 p,q=fixture['plane_pair']; n1,n2=fixture['numerator_test_lines']; f1,f2=fixture['denominator_four_brackets']; dl=fixture['denominator_test_line']
 line=lambda pair:pp(*(D[i] for i in p),*(D[i] for i in q),*(D[i] for i in pair))
 return s.factor(line(n1)*line(n2)/(br(*(D[i] for i in f1))*br(*(D[i] for i in f2))*line(dl)))
value=phi(Z);weights={}
for i in range(1,10):
 D=dict(Z);D[i]=2*D[i];ratio=s.factor(phi(D)/value);weights[i]=ratio
G=s.Matrix([[1,2,0,1],[0,1,1,0],[2,0,1,1],[1,0,0,1]])
checks={'source_formula_loaded':fixture['formula']=='<45|(123)cap(789)><46|(123)cap(789)>/(<1234><4789><56|(123)cap(789)>)','generic_prefactor_nonzero':value!=0,'projective_weight_zero_all_nine_labels':all(v==1 for v in weights.values()),'gl4_invariant':phi({i:G*z for i,z in Z.items()})==value,'three_line_contractions_nonzero':all(pp(Z[1],Z[2],Z[3],Z[7],Z[8],Z[9],Z[a],Z[b])!=0 for a,b in ((4,5),(4,6),(5,6)))}
out={'schema':'marici.nima.n2mhv-phi-plane-intersection-prefactor.v1','source':'research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex, Table g2n_yangian_invariants','source_fixture':'research/nima/fixtures/n2mhv-phi-plane-intersection-prefactor.v1.json','formula':fixture['formula'],'value':str(value),'rescaling_ratios':{str(k):str(v) for k,v in weights.items()},'checks':checks,'passed':all(checks.values()),'scope':'Exact generic-rational evaluation and projectivity of the source phi prefactor using the public plane-plane line constructor.'}
p=ROOT/'research/nima/results/n2mhv-phi-plane-intersection-prefactor.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
