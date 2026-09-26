"""Compare full E two-sheet and three one-sheet square traces at common arbitrary-Y targets."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_square_three_new_cells_birational_fibres as bir
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=bir.square.source['E'],bir.vars
w2,w4,w5,w6,w7,w8,t,u=vars
Z=bir.Z;K=bir.K
a,b,c,d,q=bir.a,bir.b,bir.c,bir.d,bir.q;T=bir.T
G=bir.square.Etrace.global_trace

def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def point_from(C,cell):
 gauge=C[:,[0,2]].inv()*C
 point=dict(zip(vars,(gauge[0,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
         -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
 assert all(s.cancel((gauge-cell.subs(point))[i,j])==0 for i in range(2) for j in range(8))
 return point

def inverse_one_sheet(Y,cell,pairs):
 start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2));assert start*Z==Y
 def lifted(i,j):
  poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
 assert M.rank()==4
 left=(M.T.nullspace()[0].T*rhs)[0]
 assert s.diff(left,q)!=0
 qr=s.factor(-left.subs(q,0)/s.diff(left,q))
 sol=M.gauss_jordan_solve(rhs.subs(q,qr))[0]
 assert s.factor(qr-sol[0]*sol[3]+sol[1]*sol[2])==0
 source=start+T.subs(dict(zip((a,b,c,d),sol)))*K
 point=point_from(source,cell)
 assert all(s.cancel((source[:,[0,2]].inv()*Y-cell.subs(point)*Z)[i,j])==0
            for i in range(2) for j in range(6))
 return point

def pushed(cell,point,sgn,z,h):
 J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
 assert J!=0 and (cell.subs(point)*h).det()!=0
 denom=s.prod(point[v] for v in vars[:6])*point[u]*(point[t]-point[u])
 return s.factor(sgn*(point[w2]*point[w4])**4*(cell.subs(point)*h).det()**4/(denom*J))
rows=[]
for label,raw in [('first',(1,1,1,1,1,1,3,2)),
                  ('second',(2,3,1,4,2,5,s.Rational(7,2),s.Rational(3,2)))]:
 p=dict(zip(vars,map(s.Rational,raw)));C=D.subs(p);Y=C*Z
 H=Y[:,:2];B=H.inv()*Y[:,2:]
 z=Z[:,2:]-Z[:,:2]*B;h=Z[:,:2]
 terms={}
 E_sheets=list(G.fibre(C,Z));assert len(E_sheets)==2
 terms['E']=s.factor(sum(pushed(D,point,1,z,h) for _,point in E_sheets))
 for name,pairs in bir.zero_sets.items():
  point=inverse_one_sheet(Y,bir.square.source[name],pairs)
  terms[name]=pushed(bir.square.source[name],point,bir.square.sign[name],z,h)
 total=s.factor(sum(terms.values()))
 rows.append({'target':label,'E_two_sheet_chi3_power4_chi5_power4':str(terms['E']),
  'three_one_sheet_terms':{name:str(terms[name]) for name in bir.zero_sets},
  'complete_four_cell_chi3_power4_chi5_power4':str(total),
  'four_cell_component_nonzero':bool(total!=0)})
assert all(r['four_cell_component_nonzero'] for r in rows)
report={'schema':'marici.nima.nine-point-label3-square-full-chi3-target-trace.v1',
 'passed':True,'positive_external_moment_curve_common_arbitrary_Y_targets':rows,
 'consequence':'At two exact common first-pivot targets, the complete TWO-SHEET E chi3^4 chi5^4 trace plus the THREE full ONE-SHEET E_B,E_C,E_D oriented traces is NONZERO. Source-coordinate +/- cancellation and three regular boundary-pole cancellations do not make the complete four-cell form component vanish.',
 'scope':'Exact two target tests imply generic rational nonzero four-cell component on a nonempty open. This does not decide the physical n9 amplitude, contour coefficients, other-cell cancellation or image coverage.'}
(OUT/'nine-point-label3-square-full-chi3-target-trace.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'common_targets':len(rows),
 'complete_four_cell_chi3_component_nonzero':all(x['four_cell_component_nonzero'] for x in rows)},indent=2))
