"""Complete eight-cell cube chi3^4 chi5^4 arbitrary-Y meromorphic trace at common target."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_remaining_vertical_label3_cells_birational_forms as new
 import check_nine_point_five_cell_two_internal_walls_and_label3_remainder as five
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
vars=new.vars;w2,w4,w5,w6,w7,w8,t,u=vars
Z,K=new.Z,new.K
T=new.T;a,b,c,d,q=new.a,new.b,new.c,new.d,new.q
cell=new.cube.F['F_D'][:,list(new.retained)]
pairs=new.pairs['F_D']
p=dict(zip(vars,map(s.Rational,(1,1,1,1,1,1,3,2))))
Y=new.cube.E['E'][:,list(new.retained)].subs(p)*Z
start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def lifted(i,j):
 poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
 assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
 return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
assert M.rank()==4
left=s.factor((M.T.nullspace()[0].T*rhs)[0]);assert s.diff(left,q)!=0
qval=s.factor(-left.subs(q,0)/s.diff(left,q))
sol=M.gauss_jordan_solve(rhs.subs(q,qval))[0]
assert s.factor(qval-sol[0]*sol[3]+sol[1]*sol[2])==0
source=start+T.subs(dict(zip((a,b,c,d),sol)))*K
gauge=source[:,[0,2]].inv()*source
point=dict(zip(vars,(gauge[1,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
         -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
assert gauge==cell.subs(point)
H=Y[:,:2];B=H.inv()*Y[:,2:]
z=Z[:,2:]-Z[:,:2]*B;h=Z[:,:2]
J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge')
assert J!=0 and (cell.subs(point)*h).det()!=0
assert s.factor(cell[:,[1,3]].det()-w2*w4/t)==0
rho=-s.S.One/(s.prod(point[v] for v in vars[:6])*point[u]*(point[t]-point[u]))
FD=s.factor(rho*(point[w2]*point[w4]/point[t])**4*(cell.subs(point)*h).det()**4/J)
F=new.cube.F['F'][:,list(new.retained)]
FC=new.cube.F['F_C'][:,list(new.retained)]
assert F[:,[1,3]].det()==FC[:,[1,3]].det()==0
prior=s.Rational(five.report['arbitrary_Y_common_E_target_e_one']['five_cell_full_chi3_power4_chi5_power4_trace'])
full=s.factor(prior+FD)
assert FD!=0 and full!=0
signs={str(v):str(s.sign(point[v])) for v in vars[:6]}
signs['u']=str(s.sign(point[u]));signs['t-u']=str(s.sign(point[t]-point[u]))
report={'schema':'marici.nima.nine-point-full-eight-cell-cube-chi3-trace.v1',
 'passed':True,'exact_common_positive_target':'E source (w2,w4,w5,w6,w7,w8,t,u)=(1,1,1,1,1,1,3,2), positive moment-curve retained labels (1,3,4,5,6,7,8,9)',
 'F_D_unique_inverse_source_positivity_signs':signs,
 'F_D_one_sheet_chi3_power4_chi5_power4_coefficient':str(FD),
 'prior_five_cell_complete_component':str(prior),
 'F_and_F_C_identically_zero_component':True,
 'complete_eight_cell_oriented_meromorphic_chi3_power4_chi5_power4_trace':str(full),
 'trace_nonzero':True,
 'consequence':'The complete oriented eight-positive-cell cube arbitrary-Y meromorphic chi3^4 chi5^4 component, incorporating E two sheets and the seven other one-sheet inverses, is nonzero at an exact positive common target, hence generically nonzero on a rational simple-fibre open. The source cube incidence cancellation and ten regular-edge local superpole cancellations do not imply full target-form cancellation.',
 'scope':'One exact target and one fermionic component; physical contour weights, image coverage and full nine-point image canonical form remain unknown.'}
(OUT/'nine-point-full-eight-cell-cube-chi3-trace.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'complete_eight_cell_chi3_component_nonzero':True,
 'F_D_positive_source':all(z=='1' for z in signs.values())},indent=2))
