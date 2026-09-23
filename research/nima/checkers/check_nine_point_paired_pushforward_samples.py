"""Exact local target eight-form coefficients and branch census for paired source cell."""
from itertools import combinations
from pathlib import Path
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'nine-point-paired-source-form.json').read_text());assert prior['passed']
labels=prior['retained_labels'];Z=s.Matrix([[j**d for d in range(6)] for j in labels]);K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
w2,w4,w5,w6,w7,w8,t,u=s.symbols('w2 w4 w5 w6 w7 w8 t u');variables=(w2,w4,w5,w6,w7,w8,t,u)
D=s.Matrix([[1,w2,0,0,-w5,-w6,-w7,-w8],
            [0,0,1,w4,w5*t,w6*t,w7*u,w8*u]])
def minor(M,i,j):return s.expand(M[0,i]*M[1,j]-M[0,j]*M[1,i])
matching=((0,1),(2,3),(4,5),(6,7))
def chart(point):
 C=D.subs(point);Y=C*Z;A=Y[:,[0,1]];R=A.inv();B=R*Y[:,2:]
 columns=[]
 for variable in variables:
  dY=D.diff(variable).subs(point)*Z
  dB=R*(dY[:,2:]-dY[:,[0,1]]*B)
  columns.append(s.Matrix([dB[i,j] for i in range(2) for j in range(4)]))
 J=s.factor(s.Matrix.hstack(*columns).det());assert J!=0
 weight=s.prod(point[z] for z in variables[:6]);source=s.factor(-s.S.One/(point[u]*weight*(point[t]-point[u])))
 target=s.factor(source/J)
 # Generic source-fibre equations are linear in four row-kernel parameters
 # plus q; realizability gives one quadratic and possibly two sheets.
 a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
 def affine(i,j):
  linear=sum(T[0,p]*(K[p,i]*C[1,j]-K[p,j]*C[1,i])+T[1,p]*(C[0,i]*K[p,j]-C[0,j]*K[p,i]) for p in range(2))
  return s.expand(minor(C,i,j)+linear+q*(K[0,i]*K[1,j]-K[0,j]*K[1,i]))
 mat,rhs=s.linear_eq_to_matrix([affine(*pair) for pair in matching],(a,b,c,d));assert mat.det()!=0
 coeff=[s.factor(x) for x in mat.inv()*rhs];P=s.Poly(s.factor(q-coeff[0]*coeff[3]+coeff[1]*coeff[2]),q);assert P.degree()==2 and P.eval(0)==0
 roots=s.solve(P.as_expr(),q);assert len(roots)==2
 branches=[]
 for root in roots:
  values=dict(zip((a,b,c,d),(z.subs(q,root) for z in coeff)))
  M=C+T.subs(values)*K
  measures=[minor(M,i,j) for i,j in combinations(range(8),2)]
  strict=all(v>0 for idx,v in zip(combinations(range(8),2),measures) if idx not in matching)
  assert all(minor(M,*p)==0 for p in matching)
  branches.append({'kernel_area':str(root),'positive_paired_cell':bool(strict),
    'negative_other_minors':sum(1 for idx,v in zip(combinations(range(8),2),measures) if idx not in matching and v<0)})
 assert sum(b['positive_paired_cell'] for b in branches)==1
 return {'weights':list(map(str,(point[z] for z in variables[:6]))),'t':str(point[t]),'u':str(point[u]),
  'target_chart_jacobian':str(J),'source_form_coefficient':str(source),
  'pushed_local_target_coefficient':str(target),'branches':branches}
points=[{w2:1,w4:1,w5:1,w6:1,w7:1,w8:1,t:3,u:2},
        {w2:2,w4:3,w5:1,w6:4,w7:2,w8:5,t:s.Rational(7,2),u:s.Rational(3,2)}]
rows=[chart(p) for p in points]
result={'schema':'marici.nima.nine-point-paired-pushforward-samples.v1','passed':True,'rows':rows,
 'target_coordinates':'B=(CZ[:,0:2])^-1 CZ[:,2:6], row-major; source orientation (w2,w4,w5,w6,w7,w8,t,u)',
 'scope':'Exact local pushforward eight-form coefficients at two rational cell points, with all real fibre branches classified there. No global rational form identity, physical nine-point history comparison, or cell coverage.'}
(OUT/'nine-point-paired-pushforward-samples.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
