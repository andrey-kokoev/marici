"""Reconstruct complete zero-phys3 A fibre at positive V targets across common w2 facet."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_mass_global_target_trace_by_recentring as g
 import check_nine_point_two_composite_neighbors_target_sides as sides
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=g.D,g.variables
w2,w4,w5,w6,w7,w8,t,u=vars
Z=s.Matrix([[j**d for d in range(6)] for j in (1,2,4,5,6,7,8,9)])
K=s.Matrix([list(-Z[6,:]*Z[:6,:].inv())+[1,0],list(-Z[7,:]*Z[:6,:].inv())+[0,1]])
assert K*Z==s.zeros(2,6)
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def fibreV(C):
 def lifted(i,j):
  poly=s.Poly(minor(C+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((0,1),(2,3),(4,5),(6,7))],(a,b,c,d))
 assert M.det()!=0
 sol=M.inv()*rhs
 P=s.Poly(q-sol[0]*sol[3]+sol[1]*sol[2],q);assert P.degree()==2
 disc=s.discriminant(P.as_expr(),q)
 solutions=[]
 for root in s.solve(P.as_expr(),q):
  if root.is_real is False:continue
  source=C+T.subs(dict(zip((a,b,c,d),(v.subs(q,root) for v in sol))))*K
  gauge=source[:,[0,2]].inv()*source
  point=dict(zip(vars,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
           -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
  assert all(abs(complex(s.N(x,25)).imag)<1e-15 for x in point.values())
  assert all(abs(complex(s.N((gauge-D.subs(point))[i,j],18)))<1e-12 for i in range(2) for j in range(8))
  weights={str(x):str(s.sign(s.radsimp(point[x]))) for x in vars[:6]}
  weights['u']=str(s.sign(s.radsimp(point[u])))
  weights['t-u']=str(s.sign(s.radsimp(point[t]-point[u])))
  assert set(weights.values())<= {'1','-1','0'},weights
  positivity=all(value=='1' for value in weights.values())
  solutions.append({'w2':str(s.N(point[w2],12)),
    'positive_source_weights':positivity,
    'exact_positive_inequality_signs':weights})
 return disc,solutions
rows=[]
for e in (s.Rational(1,20),s.Rational(1,40),s.Rational(1,100)):
 p=dict(zip(vars,(e,1,1,1,1,1,3,2)))
 V=D.subs(p).copy();V[0,1]=0;V[1,1]=e
 assert V*Z!=D.subs(p)*Z
 full=s.Matrix.hstack(V[:,:2],s.zeros(2,1),V[:,2:])
 assert all(s.factor(s.det(full[:,[i,j]]))>=0
            for i in range(9) for j in range(i+1,9))
 Y=V*Z;H=Y[:,:2];B=H.inv()*Y[:,2:]
 symbolic=D.copy();symbolic[0,1]=0;symbolic[1,1]=w2
 cols=[]
 for param in vars:
  delta=symbolic.diff(param).subs(p)*Z
  cols.append(s.Matrix(list(H.inv()*(delta[:,2:]-delta[:,:2]*B))))
 J=s.Matrix.hstack(*cols).det(method='domain-ge');assert J!=0
 discr,sheets=fibreV(V)
 rows.append({'w2_V':str(e),'discriminant_sign':str(s.sign(discr)),
              'number_of_real_A_sheets':len(sheets),
              'positive_A_sheets':sum(z['positive_source_weights'] for z in sheets),
              'A_sheets':sheets})
report={'schema':'marici.nima.nine-point-opposite-side-positive-target-zero-column-fibre.v1',
 'passed':True,'positive_V_target_fibre_controls':rows,
 'scope':'Complete algebraic two-sheet zero-column A fibre for the three specified positive V targets and fixed positive moment-curve external data. Finite witnesses do not establish global nine-point image coverage or canonical form.'}
(OUT/'nine-point-opposite-side-positive-target-zero-column-fibre.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'rows':[{k:r[k] for k in ('w2_V','discriminant_sign','number_of_real_A_sheets','positive_A_sheets')} for r in rows]},indent=2))
