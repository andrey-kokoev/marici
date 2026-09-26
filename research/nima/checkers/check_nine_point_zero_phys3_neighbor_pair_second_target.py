"""Check independent-target positive overlap and signed degrees of the outside-cube EB/FB pair."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_zero_phys3_relabelled_cube_neighbors as first
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
old=first.old;cube=first.cube;Z,K=first.Z,first.K;vars=first.vars
w2,w4,w5,w6,w7,w8,t,u=vars
a,b,c,d,q=first.a,first.b,first.c,first.d,first.q;T=first.T
p=dict(zip(old.inside.vars,map(s.Rational,(2,3,1,4,2,5,s.Rational(7,2),s.Rational(3,2)))))
Y=cube.E['E'].subs(p)*old.Z9
B=Y[:,:2].inv()*Y[:,2:];z=Z[:,2:]-Z[:,:2]*B
start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
rows=[]
for name in ('E_B','F_B'):
 C=(cube.E if name.startswith('E') else cube.F)[name][:,first.old_columns]
 pairs=first.zeros[name]
 def lifted(i,j):
  P=s.Poly(old.minor(start+T*K,i,j),a,b,c,d)
  assert P.coeff_monomial(a*d)==-P.coeff_monomial(b*c)
  return P.coeff_monomial(1)+sum(P.coeff_monomial(v)*v for v in (a,b,c,d))+P.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
 assert M.rank()==4
 left=[s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]
 active=next(v for v in left if s.diff(v,q)!=0)
 qr=s.factor(-active.subs(q,0)/s.diff(active,q))
 assert all(s.factor(v.subs(q,qr))==0 for v in left)
 sol=M.gauss_jordan_solve(rhs.subs(q,qr))[0]
 assert s.factor(qr-sol[0]*sol[3]+sol[1]*sol[2])==0
 source=start+T.subs(dict(zip((a,b,c,d),sol)))*K
 gauge=source[:,[0,2]].inv()*source
 point=dict(zip(vars,(gauge[0,1] if name.startswith('E') else gauge[1,1],
           gauge[1,3],-gauge[0,4],-gauge[0,5],-gauge[0,6],-gauge[0,7],
           -gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
 assert all(s.factor(v)==0 for v in gauge-C.subs(point))
 signs=[str(s.sign(point[v])) for v in vars[:6]]+[str(s.sign(point[u])),str(s.sign(point[t]-point[u]))]
 positive=all(x=='1' for x in signs)
 J=s.Matrix.hstack(*[s.Matrix(list(C.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
 assert J!=0
 rows.append({'cell':name,'source_signs':signs,'positive':positive,
              'target_jacobian_sign':int(s.sign(J)),
              'relative_oriented_degree':int(cube.orient[name]*s.sign(J)) if positive else 0})
report={'schema':'marici.nima.nine-point-zero-phys3-neighbor-pair-second-target.v1',
 'passed':True,'second_positive_E_source':'(2,3,1,4,2,5,7/2,3/2)',
 'outside_cube_zero_phys3_pair':rows,
 'scope':'Two relabelled zero-physical3 geometric cells on second exact target, not established physical contour terms, independent global form or exhaustive n9 cell inventory.'}
(OUT/'nine-point-zero-phys3-neighbor-pair-second-target.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'pair':[{k:r[k] for k in ('cell','positive','relative_oriented_degree')} for r in rows]},indent=2))
