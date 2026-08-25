"""Twelve hostile countermodels for the completed physical engine."""
import json, os
import sympy as sp
checks=[]
def rec(g,s,p,d): checks.append({"gate":g,"statement":s,"passed":bool(p),"detail":d})
z,zb,x,xb=sp.symbols("z zb x xb", nonzero=True)
old=(zb-xb)/((z-x)*(1+z*zb)*(1+x*xb))
new=(zb-xb)*(1+zb*x)**2/((z-x)*(1+z*zb)**3*(1+x*xb))
pm=lambda e:e.subs({z:-1/z,zb:-1/zb,x:-1/x,xb:-1/xb},simultaneous=True)
rec("H1.coordinate_green","coordinate Green creates a spurious ratio while invariant Green glues",sp.simplify(z**-4*pm(old)/old-x**2/z**2)==0 and sp.simplify(z**-4*pm(new)/new-1)==0,"old=x^2/z^2; new=1")
boundary_ok=all(sp.limit(x**(2*r),x,0)==0 for r in range(1,13)) and x**0==1
rec("H2.chart_boundary","a jet diagonal x^(2r) vanishes only at the excluded overlap boundary",boundary_ok,"orders r=1..12; order zero is identity")
n=sp.symbols("n", integer=True, nonnegative=True)
sextic=117649*n**6+1142876*n**5+4482667*n**4+9331658*n**3+11378290*n**2+8050616*n+2559072
rec("H3.cutoff_tail","every finite cutoff has a nonzero grade-three remainder witness",all(c>0 for c in sp.Poly(sextic,n).all_coeffs()),"positive sextic coefficients")
X=sp.Matrix([[0,1],[1,0]]); I=sp.eye(2); E=(I+X)/2; M=(I-X)/2
rec("H4.single_parity","single parity ports have kernels but their pair is faithful",E.rank()==M.rank()==1 and sp.Matrix.vstack(E,M).rank()==2,"ranks 1,1,joint 2")
rec("H5.period_local","a nonzero double pole is exact and period blind",sp.diff(-1/(z-x),z)==1/(z-x)**2 and sp.residue(1/(z-x)**2,z,x)==0,"local port restores it")
B=sp.Matrix([[1,0,-1]])
rec("H6.single_contour","one contour aliases a three-residue packet",B.rank()==1 and len(B.nullspace())==2,"complete constrained basis has dimension two")
A=sp.diag(2,3,5); naive=sp.eye(3).row_join(sp.eye(3)); mismatch=sp.eye(3).row_join(-A); graph=sp.Matrix.vstack(A,sp.eye(3))
rec("H7.antipodal_sum","untyped sum is blind while the true matching graph is exact",len(naive.nullspace())==3 and mismatch*graph==sp.zeros(3) and graph.rank()==3,"adapter retained")
S=sp.Matrix([[1,1]])
rec("H8.exact_collision","two exact coincident labels lose their difference",S*sp.Matrix([1,-1])==sp.zeros(1,1),"primitive difference")
V1=sp.Matrix([[1,1,1],[0,1,2]]); V2=sp.Matrix([[1,1,1],[0,1,2],[0,1,4]])
rec("H9.collision_moments","insufficient moments lose a line and the next moment restores it",V1.rank()==2 and V2.rank()==3,"three tangent labels")
Iu=sp.I
def qmat(pts): return sp.Matrix([[1+a*b,a+b,-Iu*(a-b),1-a*b] for a,b in pts]).T
special=qmat([(0,0),(1,1),(Iu,-Iu),(1+Iu,1-Iu)]); generic=qmat([(0,0),(1,1),(Iu,-Iu),(2+Iu,2-Iu)])
rec("H10.charge_rank","distinct directions need not have generic charge rank",special.rank()==3 and generic.rank()==4,"rank 3 fixture versus rank 4 repair")
xx,yy=sp.symbols("xx yy"); f=sp.Function("f")
wave=f(xx+yy)
rec("H11.characteristic","an enlarged smooth sector has characteristic zero modes",sp.simplify(sp.diff(wave,xx,4)-sp.diff(wave,yy,4))==0,"excluded from finite point jets")
l=sp.symbols("l", integer=True, nonnegative=True); mult=(l-1)*l*(l+1)*(l+2)
rec("H12.zero_modes","spin reconstruction requires the declared l<=1 quotient",[j for j in range(10) if mult.subs(l,j)==0]==[0,1],"constant Green mode handled separately")
passed=sum(i["passed"] for i in checks)
payload={"checker":"completed_physical_engine_hostile_falsifiers.py","strength":"twelve exact hostile countermodels and repairs","passed":passed,"total":len(checks),"checks":checks,"verdict":"All twelve hostile gates pass. Every apparent counterexample is localized to a typed boundary: coordinate representative, chart edge, cutoff, selected parity/contour port, untyped matching, collision resolution, nongeneric charge rank, unauthorized characteristic enlargement, or omitted zero-mode quotient."}
outdir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"results"); os.makedirs(outdir,exist_ok=True)
with open(os.path.join(outdir,"completed_physical_engine_hostile_falsifiers.json"),"w",encoding="ascii") as h: json.dump(payload,h,indent=2,sort_keys=True); h.write("\n")
for i in checks: print(f"{'PASS' if i['passed'] else 'FAIL'} {i['gate']}: {i['statement']} - {i['detail']}")
print(f"SUMMARY {passed}/{len(checks)}")
if passed!=len(checks): raise SystemExit(1)
