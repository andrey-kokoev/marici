"""Find rational inverse/form degrees for the two remaining positive label3 cube cells F_C,F_D."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_oriented_eight_cell_cube as cube
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=cube.vars;w2,w4,w5,w6,w7,w8,t,u=vars
Z=s.Matrix([[j**degree for degree in range(6)] for j in (1,3,4,5,6,7,8,9)])
K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
retained=(0,2,3,4,5,6,7,8)
pairs={'F_C':((1,2),(2,3),(1,3),(5,6),(6,7),(5,7)),
       'F_D':((1,2),(3,4),(5,6),(6,7),(5,7))}
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
rows=[]
for name,zeros in pairs.items():
 cell=cube.F[name][:,list(retained)]
 assert all(minor(cell,i,j)==0 for i,j in zeros)
 for raw in ((1,1,1,1,1,1,3,2),(2,3,1,4,2,5,s.Rational(7,2),s.Rational(3,2))):
  p=dict(zip(vars,map(s.Rational,raw)));C=cell.subs(p)
  def lifted(i,j):
   poly=s.Poly(minor(C+T*K,i,j),a,b,c,d)
   assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
   return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
  M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in zeros],(a,b,c,d))
  null=[s.factor((n.T*rhs)[0]) for n in M.T.nullspace()]
  assert M.rank()==4 and len(null)==len(zeros)-4
  assert all(x==0 or s.factor(x/q)!=0 for x in null)
  assert any(x!=0 for x in null)
  assert all(x==0 for x in M.gauss_jordan_solve(rhs.subs(q,0))[0])
  Y=C*Z;H=Y[:,:2];B=H.inv()*Y[:,2:]
  z=Z[:,2:]-Z[:,:2]*B
  J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(p)*z)) for v in vars]).det(method='domain-ge')
  assert J!=0 and (C*Z[:,:2]).det()!=0
  density=cube.orient[name]/(s.prod(p[v] for v in vars[:6])*p[u]*(p[t]-p[u]))
  coeff=s.factor(density*(C*Z[:,:2]).det()**4/J)
  assert coeff!=0
  rows.append({'cell':name,'source_w2':str(p[w2]),'mandatory_zero_minors':zeros,
    'lift_rank':4,'left_null_q_constraints':list(map(str,null)),
    'one_sheet_nonzero_oriented_bosonic_coefficient':str(coeff)})
report={'schema':'marici.nima.nine-point-remaining-vertical-label3-cells-birational-forms.v1',
 'passed':True,'exact_positive_controls':rows,
 'arbitrary_Y_fibre_result':'F_C and F_D have unique rational source inverses on nonempty regular image opens. Their six/five mandatory minors lift to linear constraints in four T variables and q=detT, rank4 with nonzero left-null q condition, forcing a unique candidate. On arbitrary first-pivot Y the complete fermionic numerator is (C*chi_ret)^8 and oriented one-sheet coefficient is sign*det(C*h)^4/[w2w4w5w6w7w8u(t-u)*det(d(C*z)/dv)].',
 'scope':'Together with previous E two-sheet and E_B,E_C,E_D,F,F_B birational charts, this completes fibre DEGREE classification for eight sourced cube cells on regular opens. Not a full 8-cell target image trace, contour or global nine-point form.'}
(OUT/'nine-point-remaining-vertical-label3-cells-birational-forms.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'new_birational_cells':list(pairs),'controls':len(rows)},indent=2))
