"""Compute the full Grassmannian fibre degree of positive vertical-column-2 cell V."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_mass_global_target_trace_by_recentring as g
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=g.D,g.variables
w2,w4,w5,w6,w7,w8,t,u=vars
Z=s.Matrix([[j**degree for degree in range(6)] for j in (1,2,4,5,6,7,8,9)])
K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
rows=[]
for e in (s.Rational(1,20),s.Rational(1,40),s.Rational(1,100)):
 p=dict(zip(vars,(e,1,1,1,1,1,3,2)))
 C=D.subs(p).copy();C[0,1]=0;C[1,1]=e
 def lifted(i,j):
  poly=s.Poly(minor(C+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 minors=((1,2),(2,3),(1,3),(4,5),(6,7))
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in minors],(a,b,c,d))
 left=[s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]
 assert M.rank()==4 and len(left)==1 and s.factor(left[0]/q)!=0
 assert all(v==0 for v in M.gauss_jordan_solve(rhs.subs(q,0))[0])
 assert s.factor(s.det(T.subs({a:0,b:0,c:0,d:0})))==0
 H=(C*Z)[:,:2];assert H.det()!=0
 B=H.inv()*(C*Z)[:,2:]
 z=Z[:,2:]-Z[:,:2]*B;h=Z[:,:2]
 V=D.copy();V[0,1]=0;V[1,1]=w2
 Jz=s.Matrix.hstack(*[s.Matrix(list(V.diff(v).subs(p)*z)) for v in vars]).det(method='domain-ge')
 assert Jz!=0 and (C*h).det()!=0
 source=s.S.One/(s.prod(p[v] for v in vars[:6])*p[u]*(p[t]-p[u]))
 pushed=s.factor(source*(C*h).det()**4/Jz)
 assert pushed!=0
 rows.append({'positive_V_w2':str(e),'linear_lift_rank':M.rank(),
              'linear_lift_augmented_rank':M.row_join(rhs).rank(),
              'left_null_constraints':list(map(str,left)),
              'unique_fibre_solution_T_zero':True,
              'nonzero_single_sheet_arbitrary_Y_target_coefficient':str(pushed)})
report={'schema':'marici.nima.nine-point-vertical-cell-fibre-degree.v1','passed':True,'controls':rows,
 'arbitrary_Y_rational_single_sheet_form':'On the generic V image, take first-pivot Y=[I2|B], z=Zret_last4-Zret_first2*B, h=Zret_first2. The five mandatory vanishing minors (1,2),(2,3),(1,3),(4,5),(6,7) in a rank-two kernel shift C0+T*K lift linearly in (a,b,c,d,q=detT). The 5x4 linear system has rank4 and its left-null relation determines q uniquely on an open set, hence T and the unique V source rationally. The one-sheet oriented coefficient is +det(C_V*h)^4/[w2*w4*w5*w6*w7*w8*u*(t-u)*det(d(C_V*z)/dv)].',
 'scope':'Birational one-sheet source trace on a nonempty regular open near three positive V controls. This is not the complete nine-point image form or a global positivity/coverage statement.'}
(OUT/'nine-point-vertical-cell-fibre-degree.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
