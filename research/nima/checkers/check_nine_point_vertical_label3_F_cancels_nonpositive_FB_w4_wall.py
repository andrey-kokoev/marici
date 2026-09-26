"""F birational inverse cancels F_B's nonpositive-sheet w4 interior meromorphic pole."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_FB_positive_overlap_chamber as fb
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
five=fb.five;trace=five.trace
vars=trace.vars;w2,w4,w5,w6,w7,w8,t,u=vars
Z,K=five.Z,five.K
T=five.T;a,b,c,d,q=five.a,five.b,five.c,five.d,five.q
F=trace.D.copy();F[0,1]=0;F[1,1]=w2
FB=five.cell
assert F.subs(w4,0)==FB.subs(w4,0)
e0=fb.threshold_F_w4
p=dict(zip(vars,(e0,1,1,1,1,1,3,2)))
Y=trace.D.subs(p)*Z
start=(Y*Z[:6,:].inv()).row_join(s.zeros(2,2))
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
def lifted(i,j):
 poly=s.Poly(minor(start+T*K,i,j),a,b,c,d)
 assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
 return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
pairs=((1,2),(2,3),(1,3),(4,5),(6,7))
assert all(minor(F,i,j)==0 for i,j in pairs)
M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in pairs],(a,b,c,d))
assert M.rank()==4
left=s.factor((M.T.nullspace()[0].T*rhs)[0]);assert s.diff(left,q)!=0
qvalue=s.factor(-left.subs(q,0)/s.diff(left,q))
sol=M.gauss_jordan_solve(rhs.subs(q,qvalue))[0]
assert s.factor(qvalue-sol[0]*sol[3]+sol[1]*sol[2])==0
source=start+T.subs(dict(zip((a,b,c,d),sol)))*K
gauge=source[:,[0,2]].inv()*source
point=dict(zip(vars,(gauge[1,1],gauge[1,3],-gauge[0,4],-gauge[0,5],
         -gauge[0,6],-gauge[0,7],-gauge[1,4]/gauge[0,4],-gauge[1,6]/gauge[0,6])))
assert gauge==F.subs(point)
FBpoint,_,_=five.inverse_at(e0)
assert point==FBpoint and point[w4]==0 and point[w2]<0
assert F.subs(point)==FB.subs(point)
H=Y[:,:2];B=H.inv()*Y[:,2:];z=Z[:,2:]-Z[:,:2]*B
def jac(cell):
 return s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars])
JF,JB=jac(F),jac(FB)
df,db=JF.det(method='domain-ge'),JB.det(method='domain-ge')
assert df!=0 and db!=0
assert all(JF[:,j]==JB[:,j] for j in range(8) if j!=1)
other=s.prod(point[v] for v in (w2,w5,w6,w7,w8))*point[u]*(point[t]-point[u])
assert other!=0
for direction in (JF[:,1],JF[:,1]+JF[:,0]/7+JF[:,5]/11):
 speedF=s.factor((JF.inv()*direction)[1]);speedB=s.factor((JB.inv()*direction)[1])
 assert speedF!=0 and speedB!=0 and s.factor(df*speedF-db*speedB)==0
 residueF=s.factor(-1/(other*df*speedF))
 residueB=s.factor(1/(other*db*speedB))
 assert residueF!=0 and s.factor(residueF+residueB)==0
assert s.factor(F[:,[0,1]].det()-w2)==0 # chi1^4 chi3^4 survives
# Exclude additional poles from the four pre-existing square cells at
# the exact same target before promoting the six-cell local statement.
def regular(cell,src):
 J=s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(src)*z)) for v in vars]).det(method='domain-ge')
 return all(src[v]!=0 for v in vars[:6]) and src[u]!=0 and src[t]-src[u]!=0 and J!=0
Esheets=list(trace.G.fibre(trace.D.subs(p),Z))
assert len(Esheets)==2 and all(regular(trace.D,src) for _,src in Esheets)
for name in ('E_B','E_C','E_D'):
 cell=trace.bir.square.source[name]
 src=trace.inverse_one_sheet(Y,cell,trace.bir.zero_sets[name])
 assert regular(cell,src)
report={'schema':'marici.nima.nine-point-vertical-label3-F-cancels-nonpositive-FB-w4-wall.v1',
 'passed':True,'E_positive_source_e':str(e0),
 'F_and_F_B_same_nonpositive_boundary_inverse':{str(v):str(point[v]) for v in vars},
 'both_unique_kernel_lift_inverses':True,
 'both_8x8_target_jacobians_nonzero':True,
 'all_other_four_square_algebraic_sheets_regular_at_target':True,
 'two_transverse_target_directions_cancel_all_fermionic_w4_pole_residues':True,
 'consequence':'The earlier F_B nonpositive-source w4=0 interior E-image pole is canceled in the COMPLETE F_B+F meromorphic one-sheet traces by F\'s unique nonpositive inverse on the identical source facet; orientations are opposite, seven tangents coincide and both Jacobians rank8. All sheets of E,E_B,E_C,E_D are regular there, so the SIX-CELL meromorphic sum also has no simple pole at this target. This includes the chi1^4 chi3^4 component that survives F_B alone.',
 'scope':'One exact nonpositive source facet at an interior positive E target, not global all-target form or physical contour.'}
(OUT/'nine-point-vertical-label3-F-cancels-nonpositive-FB-w4-wall.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'nonpositive_FB_internal_w4_pole_canceled_by_F_full_trace':True},indent=2))
