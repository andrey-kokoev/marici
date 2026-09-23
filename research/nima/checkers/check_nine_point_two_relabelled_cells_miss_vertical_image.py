"""Complete A and E quadratic fibres over positive vertical-neighbor target controls."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_opposite_side_positive_target_zero_column_fibre as old
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=old.D,old.vars
w2,w4,w5,w6,w7,w8,t,u=vars
Z9=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
ZE=Z9[[0,2,3,4,5,6,7,8],:]
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def E_fibre_at(Y):
 start=(Y*ZE[:6,:].inv()).row_join(s.zeros(2,2));assert start*ZE==Y
 K=s.Matrix([list(-ZE[6,:]*ZE[:6,:].inv())+[1,0],list(-ZE[7,:]*ZE[:6,:].inv())+[0,1]])
 assert K*ZE==s.zeros(2,6)
 def lifted(i,j):
  poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
 if M.det()==0:
  assert M.rank()==3 and [s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]==[-q]
  linear=tuple(next(iter(s.linsolve((M,rhs.subs(q,0)),(a,b,c,d)))))
  frees=set().union(*(v.free_symbols for v in linear)) & {a,b,c,d}
  assert len(frees)==1
  free=next(iter(frees))
  P=s.Poly(s.factor(linear[0]*linear[3]-linear[1]*linear[2]),free)
  assert P.degree()==2
  disc=s.discriminant(P.as_expr(),free)
  candidates=[(r,tuple(v.subs(free,r) for v in linear)) for r in s.solve(P.as_expr(),free)]
 else:
  sol=M.inv()*rhs;P=s.Poly(q-sol[0]*sol[3]+sol[1]*sol[2],q)
  assert P.degree()==2
  disc=s.discriminant(P.as_expr(),q)
  candidates=[(r,tuple(v.subs(q,r) for v in sol)) for r in s.solve(P.as_expr(),q)]
 sheets=[]
 for root,coefficients in candidates:
  if root.is_real is False:continue
  source=start+T.subs(dict(zip((a,b,c,d),coefficients)))*K
  inverse=source[:,[0,2]].inv()
  gauge=inverse*source
  point=dict(zip(vars,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
           -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert all(abs(complex(s.N((gauge-D.subs(point))[i,j],20)))<1e-14 for i in range(2) for j in range(8))
  assert all(abs(complex(s.N((D.subs(point)*ZE-inverse*Y)[i,j],20)))<1e-14 for i in range(2) for j in range(6))
  signs={str(v):str(s.sign(s.radsimp(point[v]))) for v in vars[:6]}
  signs['u']=str(s.sign(s.radsimp(point[u])))
  signs['t-u']=str(s.sign(s.radsimp(point[t]-point[u])))
  assert set(signs.values())<= {'1','-1','0'}
  sheets.append({'exact_positivity_signs':signs,'positive':all(z=='1' for z in signs.values())})
 return disc,sheets
rows=[]
for e in (s.Rational(1,20),s.Rational(1,40)):
 p=dict(zip(vars,(e,1,1,1,1,1,3,2)))
 V=D.subs(p).copy();V[0,1]=0;V[1,1]=e
 Y=V*Z9[[0,1,3,4,5,6,7,8],:]
 disc,sheets=E_fibre_at(Y)
 A=next(z for z in old.rows if z['w2_V']==str(e))
 assert A['positive_A_sheets']==0
 rows.append({'positive_V_source_w2':str(e),'E_fibre_quadratic_discriminant_sign':str(s.sign(disc)),
              'A_positive_sheets':0,'E_real_sheets':len(sheets),
              'E_positive_sheets':sum(z['positive'] for z in sheets),'E_sheets':sheets})
report={'schema':'marici.nima.nine-point-two-relabelled-cells-miss-vertical-image.v1',
 'passed':True,'positive_V_target_controls':rows,
 'E_special_fibre_method':'At these V targets the four linear lifted E minor constraints have rank 3 and force q=det(T)=0. Solve their remaining one-dimensional affine line and its exact determinant quadratic; retain all real E sheets and evaluate eight source positivity signs exactly.',
 'consequence':'At w2_V=1/20, A has two nonpositive real sheets and E has no real sheets. At w2_V=1/40, both A and E have two nonpositive real sheets. Since V target Jacobian is nonzero and the algebraic signs/discriminants strict, open positive V target sectors are absent from the union of A and E images.',
 'scope':'Complete zero-column A and relabelled zero-column E fibres at two specified positive V targets. Algebraic fibre signs, not exhaustive global positive image coverage or global form.'}
(OUT/'nine-point-two-relabelled-cells-miss-vertical-image.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':[{k:x[k] for k in ('positive_V_source_w2','E_fibre_quadratic_discriminant_sign','A_positive_sheets','E_real_sheets','E_positive_sheets')} for x in rows]},indent=2))
