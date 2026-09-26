"""Derive arbitrary-Y one-sheet form of the positive vertical label3 B-cell F_B."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_vertical_label3_B_neighbor_cancels_lower_EB_pole as neighbor
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=neighbor.vars;w2,w4,w5,w6,w7,w8,t,u=vars
FB=neighbor.FB;retained=(0,2,3,4,5,6,7,8)
cell=FB[:,list(retained)]
Z=s.Matrix([[j**degree for degree in range(6)] for j in (1,3,4,5,6,7,8,9)])
K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
pairs=((1,2),(3,4),(4,5),(3,5),(6,7))
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
assert all(minor(cell,i,j)==0 for i,j in pairs)
rows=[]
for raw in [(1,1,1,1,1,1,3,2),
            (2,3,1,4,2,5,s.Rational(7,2),s.Rational(3,2))]:
 p=dict(zip(vars,map(s.Rational,raw)));C=cell.subs(p)
 def lifted(i,j):
  poly=s.Poly(minor(C+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
 left=[s.factor((n.T*rhs)[0]) for n in M.T.nullspace()]
 assert M.rank()==4 and len(left)==1 and s.factor(left[0]/q)!=0
 assert all(x==0 for x in M.gauss_jordan_solve(rhs.subs(q,0))[0])
 Y=C*Z;H=Y[:,:2];B=H.inv()*Y[:,2:]
 z=Z[:,2:]-Z[:,:2]*B;h=Z[:,:2]
 J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(x).subs(p)*z)) for x in vars]).det(method='domain-ge')
 assert J!=0 and (C*h).det()!=0
 density=s.S.One/(s.prod(p[x] for x in vars[:6])*p[u]*(p[t]-p[u]))
 pushed=s.factor(density*(C*h).det()**4/J)
 assert pushed!=0
 rows.append({'source_w2':str(p[w2]),'rank_four_lift_unique':True,
              'left_null_q_constraint':str(left[0]),
              'one_sheet_oriented_bosonic_coefficient':str(pushed)})
report={'schema':'marici.nima.nine-point-vertical-label3-B-cell-birational-form.v1',
 'passed':True,'F_B_zero_minor_set_zero_based_retained_labels':pairs,
 'arbitrary_Y_form':'On a nonempty regular open, five minor equations in C0+T*K are linear in four T entries and q=detT. Rank4 and a nonzero left-null q coefficient give a unique rational inverse. For arbitrary Y=[I2|B], z=Zret_last4-Zret_first2*B,h=Zret_first2; the oriented F_B coefficient is +det(C_F_B*h)^4/[w2w4w5w6w7w8u(t-u)*det(d(C_F_B*z)/dv)]. Full fermionic numerator is (C_F_B*chi_ret)^8.',
 'positive_exact_controls':rows,
 'scope':'F_B is birational and has a rational arbitrary-Y one-sheet form. Its common-target algebraic trace cancellation against E_B lower wall and full n9 contour still require separate checks.'}
(OUT/'nine-point-vertical-label3-B-cell-birational-form.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_regular_one_sheet_controls':len(rows)},indent=2))
