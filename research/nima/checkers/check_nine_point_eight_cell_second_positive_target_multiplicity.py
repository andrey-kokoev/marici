"""Independently classify all cube inverse sheets at a second positive E target."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_eight_cell_positive_supported_multiplicity as first
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
new=first.new;cube=new.cube;trace=first.prior.trace
vars=new.vars;w2,w4,w5,w6,w7,w8,t,u=vars;Z,K=new.Z,new.K
T=new.T;a,b,c,d,q=new.a,new.b,new.c,new.d,new.q
p=dict(zip(vars,map(s.Rational,(2,3,1,4,2,5,s.Rational(7,2),s.Rational(3,2)))))
Y=cube.E['E'][:,list(new.retained)].subs(p)*Z
B=Y[:,:2].inv()*Y[:,2:]
z=Z[:,2:]-Z[:,:2]*B;h=Z[:,:2]
sets={'F_B':tuple(first.five.bir.pairs),'F':((1,2),(2,3),(1,3),(4,5),(6,7)),
      'F_C':new.pairs['F_C'],'F_D':new.pairs['F_D']}
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def positive(point):
 return all(point[v]>0 for v in vars[:6]) and point[u]>0 and point[t]>point[u]
def inverse(name,pairs):
 cell=cube.F[name][:,list(new.retained)]
 start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
 def lifted(i,j):
  poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(v)*v for v in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
 assert M.rank()==4
 left=[s.factor((v.T*rhs)[0]) for v in M.T.nullspace()]
 active=next(v for v in left if s.diff(v,q)!=0)
 qr=s.factor(-active.subs(q,0)/s.diff(active,q))
 assert all(s.factor(v.subs(q,qr))==0 for v in left)
 sol=M.gauss_jordan_solve(rhs.subs(q,qr))[0]
 assert s.factor(qr-sol[0]*sol[3]+sol[1]*sol[2])==0
 gauge=(start+T.subs(dict(zip((a,b,c,d),sol)))*K)
 gauge=gauge[:,[0,2]].inv()*gauge
 point=dict(zip(vars,(gauge[1,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
          -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
 assert gauge==cell.subs(point)
 return cell,point
def row(name,cell,point):
 J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
 assert J!=0
 signs={str(v):str(s.sign(point[v])) for v in vars[:6]}
 signs['u']=str(s.sign(point[u]));signs['t-u']=str(s.sign(point[t]-point[u]))
 minor35=s.factor(cell[:,[1,3]].det().subs(point))
 coefficient=s.factor(cube.orient[name]*minor35**4*(cell.subs(point)*h).det()**4/
                (s.prod(point[v] for v in vars[:6])*point[u]*(point[t]-point[u])*J))
 return {'cell':name,'positive':bool(positive(point)),'source_signs':signs,
         'oriented_local_degree':int(cube.orient[name]*s.sign(J)) if positive(point) else 0,
         'chi3_power4_chi5_power4_coefficient':str(coefficient)}
rows=[]
for name,pairs in sets.items():rows.append(row(name,*inverse(name,pairs)))
for name in ('E_B','E_C','E_D'):
 point=trace.inverse_one_sheet(Y,trace.bir.square.source[name],trace.bir.zero_sets[name])
 rows.append(row(name,cube.E[name][:,list(new.retained)],point))
sheets=list(trace.G.fibre(trace.D.subs(p),Z))
assert len(sheets)==2
for _,point in sheets:rows.append(row('E',cube.E['E'][:,list(new.retained)],point))
assert len(rows)==9
count=sum(v['positive'] for v in rows);degree=sum(v['oriented_local_degree'] for v in rows)
supported=s.factor(sum(s.Rational(r['chi3_power4_chi5_power4_coefficient']) for r in rows if r['positive']))
meromorphic=s.factor(sum(s.Rational(r['chi3_power4_chi5_power4_coefficient']) for r in rows))
assert count==3 and degree==1 and supported!=0 and meromorphic!=supported
report={'schema':'marici.nima.nine-point-eight-cell-second-positive-target-multiplicity.v1',
 'passed':True,'positive_E_source':'(2,3,1,4,2,5,7/2,3/2)',
 'nine_algebraic_inverse_sheets':rows,
 'positive_source_sheet_count':count,'oriented_local_degree':degree,
 'positive_supported_chi3_power4_chi5_power4':str(supported),
 'nine_sheet_meromorphic_chi3_power4_chi5_power4':str(meromorphic),
 'scope':'All eight cube cells and all nine algebraic inverse sheets at a second exact positive E target; distinct nonzero positive-supported and full meromorphic chi3 components, not global form, contour or coverage.'}
(OUT/'nine-point-eight-cell-second-positive-target-multiplicity.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_sheets':count,'oriented_degree':degree,
 'positive_cells':[r['cell'] for r in rows if r['positive']],
 'supported_vs_meromorphic_distinct':supported!=meromorphic},indent=2))
