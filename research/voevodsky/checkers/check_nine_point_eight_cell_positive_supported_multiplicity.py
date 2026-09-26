"""Compare positive-supported eight-cell sheet multiplicity with full meromorphic cube trace."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_full_eight_cell_cube_chi3_trace as full
 import check_nine_point_label3_square_positive_supported_vs_trace_multiplicity as prior
 import check_nine_point_five_cell_lower_internal_full_trace_cancellation as five
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
new=full.new;vars=new.vars;w2,w4,w5,w6,w7,w8,t,u=vars
Z,K=new.Z,new.K;T=new.T;a,b,c,d,q=new.a,new.b,new.c,new.d,new.q
p=dict(zip(vars,map(s.Rational,(1,1,1,1,1,1,3,2))))
Y=new.cube.E['E'][:,list(new.retained)].subs(p)*Z
H=Y[:,:2];B=H.inv()*Y[:,2:]
z=Z[:,2:]-Z[:,:2]*B
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def inverse(name,pairs):
 cell=new.cube.F[name][:,list(new.retained)]
 start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
 def lifted(i,j):
  poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
 assert M.rank()==4
 left=[s.factor((n.T*rhs)[0]) for n in M.T.nullspace()]
 active=next(v for v in left if s.diff(v,q)!=0)
 qr=s.factor(-active.subs(q,0)/s.diff(active,q))
 assert all(s.factor(v.subs(q,qr))==0 for v in left)
 sol=M.gauss_jordan_solve(rhs.subs(q,qr))[0]
 assert s.factor(qr-sol[0]*sol[3]+sol[1]*sol[2])==0
 source=start+T.subs(dict(zip((a,b,c,d),sol)))*K
 gauge=source[:,[0,2]].inv()*source
 point=dict(zip(vars,(gauge[1,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
          -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
 assert gauge==cell.subs(point)
 J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
 assert J!=0
 signs={str(v):str(s.sign(point[v])) for v in vars[:6]}
 signs['u']=str(s.sign(point[u]));signs['t-u']=str(s.sign(point[t]-point[u]))
 return {'cell':name,'positive':all(v=='1' for v in signs.values()),
         'exact_source_positivity_signs':signs,'target_jacobian_nonzero':True}
F=inverse('F',((1,2),(2,3),(1,3),(4,5),(6,7)))
FC=inverse('F_C',new.pairs['F_C'])
base=prior.rows[0]
assert base['target']=='first'
assert base['positive_preimages_per_cell']=={'E':1,'E_B':1,'E_C':0,'E_D':0}
FBpoint,_,FBjac=five.inverse_at(s.S.One)
assert FBjac!=0 and all(FBpoint[v]>0 for v in vars[:6]) and FBpoint[u]>0 and FBpoint[t]>FBpoint[u]
FDsigns=full.signs
assert not all(v=='1' for v in FDsigns.values())
positive_count=3+int(F['positive'])+int(FC['positive'])
Epositive=s.Rational(next(sheet['chi3_component'] for sheet in base['all_inverse_sheet_signs']['E']
                         if sheet['positive']))
EBpositive=s.Rational(base['all_inverse_sheet_signs']['E_B'][0]['chi3_component'])
FBpositive=s.Rational(full.five.report['arbitrary_Y_common_E_target_e_one']
                      ['F_B_one_sheet_chi3_power4_chi5_power4_trace'])
supported=s.factor(Epositive+EBpositive+FBpositive)
meromorphic=s.Rational(full.report['complete_eight_cell_oriented_meromorphic_chi3_power4_chi5_power4_trace'])
assert supported!=0 and supported!=meromorphic
report={'schema':'marici.nima.nine-point-eight-cell-positive-supported-multiplicity.v1','passed':True,
 'exact_positive_common_E_target':'w2,w4,w5,w6,w7,w8,t,u=(1,1,1,1,1,1,3,2); external moment labels (1,3,4,5,6,7,8,9)',
 'F_source_sheet':F,'F_C_source_sheet':FC,
 'F_D_source_positivity_signs':FDsigns,
 'complete_eight_cell_positive_source_sheet_count':positive_count,
 'complete_eight_cell_positive_supported_chi3_power4_chi5_power4_coefficient':str(supported),
 'complete_eight_cell_meromorphic_chi3_power4_chi5_power4_coefficient':str(meromorphic),
 'supported_and_meromorphic_differ':True,
 'scope':'Exact common-target positivity of ALL inverse sheets of eight cells and comparison of chi3 component, not correct physical contour, all-cell image coverage or global nine-point canonical form.'}
(OUT/'nine-point-eight-cell-positive-supported-multiplicity.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_eight_cell_sheets':positive_count,
 'F_positive':F['positive'],'F_C_positive':FC['positive'],
 'supported_and_meromorphic_differ':True},indent=2))
