"""Explore codimension-four paired-column positroid cells in one n=9 target fibre."""
import json
from pathlib import Path
from itertools import combinations
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
witness=json.loads((OUT/'nine-point-minimum-eight-support.json').read_text())['eight_label_source_witness']
labels=witness['retained_labels'];Z=s.Matrix([[j**r for r in range(6)] for j in labels]);C=s.Matrix([[s.Rational(v) for v in row if True] for row in witness['source_rows']])[:,[j-1 for j in labels]]
assert C.shape==(2,8)
L=Z[:6,:].inv();K=s.Matrix.vstack(s.Matrix([list(-Z[6,:]*L)+[1,0]]),s.Matrix([list(-Z[7,:]*L)+[0,1]]))
assert K.shape==(2,8) and K*Z==s.zeros(2,6)
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
def minor(i,j):
 base=C[0,i]*C[1,j]-C[0,j]*C[1,i]
 lin=sum(T[0,p]*(K[p,i]*C[1,j]-K[p,j]*C[1,i])+T[1,p]*(C[0,i]*K[p,j]-C[0,j]*K[p,i]) for p in range(2))
 area=K[0,i]*K[1,j]-K[0,j]*K[1,i]
 return s.expand(base+lin+q*area)
allmin={p:minor(*p) for p in combinations(range(8),2)}
matchings=[[(0,1),(2,3),(4,5),(6,7)],[(1,2),(3,4),(5,6),(0,7)]]
rows=[]
for matching in matchings:
 equations=[allmin[tuple(sorted(p))] for p in matching];matrix,rhs=s.linear_eq_to_matrix(equations,[a,b,c,d,q]);rank=matrix.rank();assert rank==4
 sol=s.linsolve((matrix,rhs),(a,b,c,d,q));vec=list(next(iter(sol)));free=next(iter(set().union(*(v.free_symbols for v in vec))-{a,b,c,d,q})) if False else None
 # linsolve usually leaves q free; identify remaining original variable.
 freevars=set().union(*(z.free_symbols for z in vec)) & {a,b,c,d,q};assert len(freevars)==1
 free=next(iter(freevars));condition=s.factor(vec[4]-vec[0]*vec[3]+vec[1]*vec[2]);poly=s.Poly(condition,free)
 roots=s.solve(poly.as_expr(),free);candidate=[]
 for root in roots:
  numeric=s.N(root,40)
  if abs(s.im(numeric))>s.Float('1e-20'):continue
  subs={free:root};vals=[s.N(form.subs(dict(zip((a,b,c,d,q),(v.subs(subs) for v in vec)))),30) for form in allmin.values()]
  candidate.append({'root':str(root),'root_float':str(s.N(root,18)),
    'negative_minors':sum(1 for v in vals if v<0),'zero_minors':sum(1 for v in vals if v==0),
    'minimum_numeric_minor':str(min(vals))})
 rows.append({'pairing':[[labels[i],labels[j]] for i,j in matching], 'rank':rank,
   'determinantal_polynomial':str(poly.as_expr()),'discriminant':str(s.discriminant(poly.as_expr(),free)),
   'real_candidates':candidate})
result={'schema':'marici.nima.nine-point-eight-support-paired-cell-probe.v1','rows':rows,
 'scope':'Exploratory symbolic candidate roots, numeric minor classification. No source-cell admission until exact radical sign checks and image-rank/form checks.'}
(OUT/'nine-point-eight-support-paired-cell-probe.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
