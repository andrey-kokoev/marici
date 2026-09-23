"""Compact universal arbitrary-Y two-sheet coefficient via an SL6 target recentering."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_paired_trace_samples as old
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,variables=old.D,old.variables
prior=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text());assert prior['passed']
# For ANY first-pivot target B, the exact SL6 matrix below sends
# [I2|B] to sourced Y0, with the new U-chart equal to B'-B.
B=s.Matrix(2,4,s.symbols('B0:8'));Bprime=s.Matrix(2,4,s.symbols('Bprime0:8'))
G=(-B).row_join(s.eye(2)).col_join(s.eye(4).row_join(s.zeros(4,2)))
assert G.det()==1
assert s.eye(2).row_join(B)*G==s.zeros(2,4).row_join(s.eye(2))
assert s.eye(2).row_join(Bprime)*G==(Bprime-B).row_join(s.eye(2))
# This identity makes the B-to-new-U oriented 8x8 Jacobian +1.
assert s.Matrix(list(Bprime-B)).jacobian(list(Bprime)).det()==1
q,a,b,c,d=s.symbols('q a b c d');T=s.Matrix([[a,b],[c,d]])
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def fibre(C,Z):
 K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
 assert K*Z==s.zeros(2,6)
 def lifted(i,j):
  poly=s.Poly(minor(C+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
 assert M.det()!=0
 sol=M.inv()*rhs;P=s.Poly(q-sol[0]*sol[3]+sol[1]*sol[2],q)
 assert P.degree()==2 and P.eval(0)==0
 roots=s.solve(P.as_expr(),q);assert len(roots)==2 and all(r.is_Rational for r in roots)
 for root in roots:
  source=C+T.subs(dict(zip((a,b,c,d),(v.subs(q,root) for v in sol))))*K
  gauge=source[:,[0,2]].inv()*source
  point=dict(zip(variables,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7],
                            -gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert gauge==D.subs(point)
  yield root,point
rows=[]
for sample_index in range(3):
 if sample_index<2:
  row=prior['rows'][sample_index]
  weights=[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]
  Z=old.Z
 else:
  row=None;weights=[s.Rational(x) for x in (2,3,1,4,2,5)]+[s.Rational(7,2),s.Rational(3,2)]
  Z=s.Matrix([[j**degree for degree in range(6)] for j in range(1,9)])
 initial=dict(zip(variables,weights));C=D.subs(initial)
 Y=C*Z;A0=Y[:,0:2];B0=A0.inv()*Y[:,2:6]
 z=Z[:,2:6]-Z[:,0:2]*B0;h=Z[:,0:2]
 G0=(-B0).row_join(s.eye(2)).col_join(s.eye(4).row_join(s.zeros(4,2)))
 assert G0.det()==1 and Z*G0==z.row_join(h)
 assert (s.eye(2).row_join(B0))*G0==s.zeros(2,4).row_join(s.eye(2))
 assert z.rank()==4 and Z.rank()==6
 sheet=[]
 for root,point in fibre(C,Z):
  Ci=D.subs(point);Ai=Ci*h
  assert Ci*z==s.zeros(2,4) and Ai.det()!=0
  jzcols=[];jbcols=[]
  for v in variables:
   dz=D.diff(v).subs(point)*z
   jzcols.append(s.Matrix([dz[i,j] for i in range(2) for j in range(4)]))
   db=Ai.inv()*dz
   jbcols.append(s.Matrix([db[i,j] for i in range(2) for j in range(4)]))
  Jz=s.Matrix.hstack(*jzcols).det(method='domain-ge')
  Jb=s.Matrix.hstack(*jbcols).det(method='domain-ge')
  assert Jz!=0 and s.factor(Jb-Jz/Ai.det()**4)==0
  src=-s.S.One/(s.prod(point[v] for v in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
  compact=s.factor(src*Ai.det()**4/Jz)
  assert compact==s.factor(src/Jb)
  if row is not None:
   oldsheet=next(item for item in row['sheets'] if s.Rational(item['kernel_area'])==root)
   assert compact==s.Rational(oldsheet['continued_target_coefficient'])
  sheet.append(compact)
 trace=s.factor(sum(sheet))
 if row is not None:assert trace==s.Rational(row['two_sheet_algebraic_trace_coefficient'])
 rows.append({'sample_index':sample_index,'external_Z_rank_six_positive':bool(Z[:6,:].det()>0),
  'two_simple_fibre_sheets':True,'sheetwise_compact_trace_agrees_direct_target_Jacobian':True,
  'complete_target_eight_form_coefficient':str(trace)})
report={'schema':'marici.nima.four-mass-global-target-trace-by-recentring.v1','passed':True,
 'universal_SL6_recentring':'For Y=[I2|B], G(B)=[[-B,I2],[I4,0]] has det=1 and Y(Bprime)G(B)=[Bprime-B|I2]. New external data are [z|h]=[Z_last4-Z_first2 B|Z_first2]. The oriented B-to-new-U coordinate Jacobian is +1.',
 'global_compact_rational_coefficient':'omega_B(B;Z)=Tr_{two solutions C(v)z=0}[-det(C(v)h)^4/{w2 w4 w5 w6 w7 w8 u(t-u) det(d(C(v)z)/dv)}]. All denominators and the quadratic trace are rational in B,Z on the simple-fibre open set. This is a compact rational field-trace expression, not an expanded numerator.',
 'exact_witnesses':rows,
 'scope':'An explicit arbitrary-Y rank-six positive-data global target-chart rational trace via finite quadratic algebra and exact source/target orientation. No expanded numerator/pole factorization, all-Y image coverage or authored nine-point generalized-R history asserted.'}
(OUT/'four-mass-global-target-trace-by-recentring.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'global_compact_trace':True,'independent_external_Z_witnesses':2,
 'evaluated_target_samples':len(rows),'expanded_numerator':False},indent=2))
