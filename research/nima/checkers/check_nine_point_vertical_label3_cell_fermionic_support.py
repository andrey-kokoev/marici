"""Positive vertical label-3 cell F is birational but cannot cancel E's chi3^4 chi5^4 coordinate."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_cell_arbitrary_y_two_sheet_trace as Etrace
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars=Etrace.D,Etrace.vars
w2,w4,w5,w6,w7,w8,t,u=vars
E=Etrace.E.copy();F=E.copy();F[0,2]=0;F[1,2]=w2
assert E[:,1]==F[:,1]==s.zeros(2,1)
assert E.subs(w2,0)==F.subs(w2,0)
retained=(0,2,3,4,5,6,7,8)
VF=D.copy();VF[0,1]=0;VF[1,1]=w2
assert F[:,list(retained)]==VF
assert s.factor(s.det(s.Matrix.hstack(E[:,2],E[:,4])))==w2*w4
assert s.factor(s.det(s.Matrix.hstack(F[:,2],F[:,4])))==0
assert s.factor(s.det(s.Matrix.hstack(F[:,0],F[:,2])))==w2
v=s.symbols('v',positive=True)
for i,j in itertools.combinations(range(9),2):
 det=s.factor(s.det(F[:,[i,j]]).subs(t,u+v))
 poly=s.Poly(det,w2,w4,w5,w6,w7,w8,u,v)
 assert all(c>=0 for c in poly.coeffs()),(i,j,det)
ZE=s.Matrix([[j**deg for deg in range(6)] for j in (1,3,4,5,6,7,8,9)])
K=s.Matrix([list(-ZE[6,:]*ZE[:6,:].inv())+[1,0],list(-ZE[7,:]*ZE[:6,:].inv())+[0,1]])
a,b,c,d,q=s.symbols('a b c d q');T=s.Matrix([[a,b],[c,d]])
def minor(C,i,j):return s.expand(C[0,i]*C[1,j]-C[0,j]*C[1,i])
checks=[]
for e0 in (s.Rational(1,20),s.Rational(1,40)):
 p=dict(zip(vars,(e0,1,1,1,1,1,3,2)));C=VF.subs(p)
 Y=C*ZE;H=Y[:,:2];B=H.inv()*Y[:,2:]
 z=ZE[:,2:]-ZE[:,:2]*B
 J=s.Matrix.hstack(*[s.Matrix(list(VF.diff(x).subs(p)*z)) for x in vars]).det(method='domain-ge')
 assert J!=0
 def lifted(i,j):
  poly=s.Poly(minor(C+T*K,i,j),a,b,c,d)
  assert poly.coeff_monomial(a*d)==-poly.coeff_monomial(b*c)
  return poly.coeff_monomial(1)+sum(poly.coeff_monomial(x)*x for x in (a,b,c,d))+poly.coeff_monomial(a*d)*q
 M,rhs=s.linear_eq_to_matrix([lifted(i,j) for i,j in ((1,2),(2,3),(1,3),(4,5),(6,7))],(a,b,c,d))
 left=[s.factor((n.T*rhs)[0]) for n in M.T.nullspace()]
 assert M.rank()==4 and len(left)==1 and s.factor(left[0]/q)!=0
 assert all(x==0 for x in M.gauss_jordan_solve(rhs.subs(q,0))[0])
 checks.append({'positive_w2':str(e0),'F_target_Jacobian_nonzero':True,
                'unique_algebraic_F_source':True,
                'F_linear_lift_left_null':str(left[0])})
assert all(z['trace_nonzero'] for z in Etrace.checks)
report={'schema':'marici.nima.nine-point-vertical-label3-cell-fermionic-support.v1','passed':True,
 'F_source':'physical column2 zero; physical column3=(0,w2), physical column4=(0,1); all ordered source minors nonnegative on positive weights',
 'F_is_relabelled_V_cell':True,'F_regular_birational_positive_controls':checks,
 'E_chi3_power4_chi5_power4_minor':'w2*w4; complete E two-sheet trace nonzero at two positive target/external controls',
 'F_chi3_power4_chi5_power4_minor':'identically zero: physical columns3 and5 parallel',
 'A_and_V_chi3_component':'identically zero: physical column3 zero',
 'consequence':'In the explicit FOUR-CELL arbitrary-Y rational span (A,E,V,F), E is the only cell with a generically nonzero chi3^4 chi5^4 coordinate. Thus a bosonic-weighted chi3-independent combination requires E weight zero, absent OTHER cells with that fermionic component. The complete n9 amplitude need not be chi3-independent.',
 'scope':'Source-component support and generic E nonvanishing; no contour weights, exhaustive image coverage or global canonical form.'}
(OUT/'nine-point-vertical-label3-cell-fermionic-support.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'F_positive_birational_controls':len(checks),
 'F_chi3_power4_chi5_power4_identically_zero':True,
 'E_only_four_cell_chi3_power4_chi5_power4':True},indent=2))
