"""Test a sourced outside-cube zero-physical-3 four-pair cell over two positive cube targets."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_eight_cell_second_positive_target_multiplicity as inside
 import check_nine_point_four_mass_loop_embedding as old
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
Z9=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
retained=(0,1,3,4,5,6,7,8);Z=Z9[list(retained),:]
assert Z==old.Z8six
vars=old.variables;w2,w4,w5,w6,w7,w8,t,u=vars
K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
rows=[]
for label,raw in [('first',(1,1,1,1,1,1,3,2)),
                  ('second',(2,3,1,4,2,5,s.Rational(7,2),s.Rational(3,2)))]:
 p=dict(zip(inside.vars,map(s.Rational,raw)))
 Y=inside.cube.E['E'].subs(p)*Z9
 start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
 def lifted(i,j):
  poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
 assert M.rank()==3
 left=[s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]
 assert len(left)==1 and left[0]==-q
 sol,parameters=M.gauss_jordan_solve(rhs.subs(q,0))
 assert len(parameters)==1
 tau=parameters[0]
 poly=s.Poly(s.factor(sol[0]*sol[3]-sol[1]*sol[2]),tau)
 assert poly.degree()==2
 discriminant=s.factor(s.discriminant(poly.as_expr(),tau))
 roots=s.solve(poly.as_expr(),tau) if discriminant>=0 else []
 sheets=[]
 for root in roots:
  source=start+T.subs(dict(zip((a,b,c,d),(s.factor(v.subs(tau,root)) for v in sol))))*K
  gauge=source[:,[0,2]].inv()*source
  point=dict(zip(vars,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
           -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert all(s.factor(v)==0 for v in gauge-old.D.subs(point))
  signs=[str(s.sign(s.radsimp(point[v]))) for v in vars[:6]]
  signs += [str(s.sign(s.radsimp(point[u]))),str(s.sign(s.radsimp(point[t]-point[u])))]
  assert point[w4]<0
  sheets.append({'free_linear_parameter':str(root),'source_parameter_signs':signs,
                 'w4_strictly_negative':True,
                 'strictly_positive':all(z=='1' for z in signs)})
 rows.append({'target':label,'linear_lift_rank':3,'linear_lift_forces_q_zero':True,
              'one_remaining_quadratic_parameter':str(tau),
              'real_discriminant_sign':str(s.sign(discriminant)),
              'real_inverse_sheets':sheets,
              'positive_four_pair_sheets':sum(x['strictly_positive'] for x in sheets)})
report={'schema':'marici.nima.nine-point-zero-phys3-four-pair-outside-cube-fibre.v1',
 'passed':True,'positive_E_cube_target_controls':rows,
 'source_outside_cube':'Sourced 8-point four-mass four-pair positive cell embedded in n9 with physical label3 exactly ZERO and physical label2 retained, not a member of eight zero-physical2 label3 cube.',
 'scope':'Checks one structurally distinct sourced outside-cube candidate at two positive targets; both algebraic inverse sheets have w4<0 in each case, excluding this candidate locally at tested targets. Other outside cells, contour and global coverage remain open.'}
(OUT/'nine-point-zero-phys3-four-pair-outside-cube-fibre.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':[{'target':r['target'],'real_sheets':len(r['real_inverse_sheets']),
 'positive_four_pair_sheets':r['positive_four_pair_sheets']} for r in rows]},indent=2))
