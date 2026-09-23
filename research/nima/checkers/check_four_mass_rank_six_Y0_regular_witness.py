"""Exact regular Y0-chart witness at rank-six positive external data."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_paired_trace_samples as old
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())
Z,K,D,variables=old.Z,old.K,old.D,old.variables
assert prior['passed']
q,a,b,c,d=s.symbols('q a b c d');T=s.Matrix([[a,b],[c,d]])
def fibre(C):
 def lifted(i,j):
  f=s.Poly(old.minor(C+T*K,i,j),a,b,c,d)
  return f.coeff_monomial(1)+sum(f.coeff_monomial(v)*v for v in (a,b,c,d))+f.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
 sol=M.inv()*rhs;P=s.Poly(q-sol[0]*sol[3]+sol[1]*sol[2],q)
 roots=s.solve(P.as_expr(),q);assert len(roots)==2 and all(v.is_Rational for v in roots)
 for root in roots:
  source=C+T.subs(dict(zip((a,b,c,d),(v.subs(q,root) for v in sol))))*K
  gauge=source[:,[0,2]].inv()*source
  point=dict(zip(variables,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7],
                            -gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert gauge==D.subs(point)
  yield root,point
rows=[]
for row in prior['rows']:
 init=dict(zip(variables,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(init);Y=C*Z;A=Y[:,0:2];assert A.det()!=0
 kernel=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*kernel,*[right[:,j] for j in range(2)])
 G[:,0]=G[:,0]/G.det()
 assert G.det()==1 and Y*G==s.Matrix([[0,0,0,0,1,0],[0,0,0,0,0,1]])
 Zprime=Z*G
 assert Zprime.rank()==6 and Zprime[:6,:].det()==Z[:6,:].det()>0
 A_four=G[2:6,0:4]
 chart_jac=s.factor(A.det()**4*A_four.det()**2)
 assert chart_jac!=0
 values=[]
 for root,point in fibre(C):
  mapped=D.subs(point)*Zprime
  assert mapped[:,0:4]==s.zeros(2,4)
  H=mapped[:,4:6];assert H.det()!=0
  cols=[]
  for v in variables:
   deriv=H.inv()*(D.diff(v).subs(point)*Zprime)[:,0:4]
   cols.append(s.Matrix([deriv[i,j] for i in range(2) for j in range(4)]))
  Ju=s.Matrix.hstack(*cols).det(method='domain-ge');assert Ju!=0
  source=-s.S.One/(s.prod(point[x] for x in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
  coeffU=s.factor(source/Ju)
  oldsheet=next(z for z in row['sheets'] if s.Rational(z['kernel_area'])==root)
  coeffB=s.Rational(oldsheet['continued_target_coefficient'])
  assert s.factor(coeffB/coeffU-chart_jac)==0
  values.append(coeffU)
 traced=s.factor(sum(values))
 assert traced!=0 and s.factor(traced*chart_jac-s.Rational(row['two_sheet_algebraic_trace_coefficient']))==0
 rows.append({'initial_source_weights':row['weights'],'new_external_six_brackets_positive':True,
              'external_SL6_change_of_basis':True,'Y0_both_sheet_target_jacobians_nonzero':True,
              'Y0_chart_two_sheet_coefficient':str(traced),
              'B_to_U_oriented_chart_jacobian':str(chart_jac)})
report={'schema':'marici.nima.four-mass-rank-six-Y0-regular-witness.v1','passed':True,'witnesses':rows,
 'scope':'Two exact rank-six POSITIVE external SL6-transformed data sets have Y0 as a regular two-sheet image target with nonzero traced U-chart coefficient. This does NOT prove the global form regular for generic Z or at nilpotent bosonized external data; no Berezin component equality is inferred.'}
(OUT/'four-mass-rank-six-Y0-regular-witness.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'rank_six_Y0_witnesses':len(rows),'bosonized_specialization_proved':False},indent=2))
