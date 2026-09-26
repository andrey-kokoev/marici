"""Check whether three new label-3 square cells have rational one-sheet arbitrary-Y fibres."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_relabelled_four_cell_square as square
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
vars=square.vars;w2,w4,w5,w6,w7,w8,t,u=vars
Z=s.Matrix([[j**deg for deg in range(6)] for j in (1,3,4,5,6,7,8,9)])
K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
zero_sets={'E_B':((0,1),(3,4),(4,5),(3,5),(6,7)),
           'E_C':((0,1),(2,3),(5,6),(6,7),(5,7)),
           'E_D':((0,1),(3,4),(5,6),(6,7),(5,7))}
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
rows=[]
for name,pairs in zero_sets.items():
 S=square.source[name]
 assert all(minor(S,i,j)==0 for i,j in pairs)
 for e in (s.S.One,s.S(2)):
  p=dict(zip(vars,(e,1,1,1,1,1,3,2)))
  C=S.subs(p)
  def lifted(i,j):
   poly=s.Poly(minor(C+T*K,i,j),a,b,c,d)
   assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
   return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
  M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
  left=[s.factor((n.T*rhs)[0]) for n in M.T.nullspace()]
  assert M.rank()==4 and len(left)==1 and s.factor(left[0]/q)!=0
  assert all(v==0 for v in M.gauss_jordan_solve(rhs.subs(q,0))[0])
  Y=C*Z;H=Y[:,:2];B=H.inv()*Y[:,2:]
  z=Z[:,2:]-Z[:,:2]*B
  J=s.Matrix.hstack(*[s.Matrix(list(S.diff(v).subs(p)*z)) for v in vars]).det(method='domain-ge')
  assert J!=0
  rows.append({'cell':name,'positive_w2':str(e),'unique_kernel_source':True,
               'nonzero_target_jacobian':True,'left_null_q_constraint':str(left[0])})
report={'schema':'marici.nima.nine-point-label3-square-three-new-cells-birational-fibres.v1',
 'passed':True,'exact_positive_controls':rows,
 'arbitrary_Y_method':'For each E_B,E_C,E_D cell use five mandatory zero source minors. A rank-two kernel shift C0+T*K makes them linear in four entries T and q=detT. On nonempty regular opens rank4 and a left-null constraint determine q and then T rationally; each fibre has a unique candidate if any. The oriented arbitrary-Y one-sheet coefficient uses its calibrated source sign times det(C*h)^4/[w2w4w5w6w7w8u(t-u)*det(d(C*z)/dv)].',
 'scope':'Rational one-sheet form charts for three new cells on nonempty regular opens. Does not evaluate complete four-cell chi3 traces on a common target or global image canonical form.'}
(OUT/'nine-point-label3-square-three-new-cells-birational-fibres.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'one_sheet_cells':list(zero_sets),'positive_controls':len(rows)},indent=2))
