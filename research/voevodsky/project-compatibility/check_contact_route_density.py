"""Component/dash-factor restoration without identifying it with a period-grade inverse."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'contact-route-density-restoration.md',ROOT/'temp/triangle-measure-primary-2401.05207-source/GeomCosmoCorr.tex',ROOT/'src/ledger/20260824-2136 Component-Resolved Deletion Poles Reproduce the Labelled Normal Module.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();y12,y23,y31,l1,l2,l3,q=s.symbols('y12 y23 y31 l1 l2 l3 q',positive=True)
H=1/(l2*y12*y23*y31);P=y31/(q*l1*l3);D=1/(y12*y23*y31*l1*l2*l3)
assert s.simplify(H*P-1/(y12*y23*q*l1*l2*l3))==0
assert s.simplify(H/(l1*l3)-D)==0
A=H*4*P*(2*q/y31);B=-8*H/(l1*l3)
assert s.simplify(A-8*D)==0 and s.simplify(A+B)==0
g12,g23,g31=s.symbols('g12 g23 g31');base={g12:1,g23:1,g31:1}
F=A*g12*g23+B*g12*g23*g31
assert s.simplify((g31*s.diff(F,g31)).subs(base)+8*D)==0
wrong=(A+B)*g12*g23*g31
assert s.simplify(g31*s.diff(wrong,g31))==0
r=s.symbols('r',positive=True)
# p1=(1,0,0), p2=(0,1,0), p3=(-1,-1,0), l=(0,0,r).
a=r;b=s.sqrt(r*r+1);c=b
physical={y12:a,y23:b,y31:c,l1:1+a+c,l2:1+a+b,l3:s.sqrt(2)+b+c,q:1+s.sqrt(2)+a+b}
assert s.limit(r**6*D.subs(physical),r,s.oo)==s.Rational(1,8)
assert s.limit(r**4*H.subs(physical),r,s.oo)==s.Rational(1,2)
assert s.limit(r**2*(-8/(l2*l3)).subs(physical),r,s.oo)==-2
assert s.integrate(r**(-4),(r,1,s.oo))==s.Rational(1,3)
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'restored_density':'1/(y12 y23 y31 ell1 ell2 ell3)','correct_final_edge_response':'-8 D','wrong_shared_mask_response':0,'restored_uv_degree':-6,'reduced_contact_uv_degree':-2,'cartesian_radial_tail_power':-4,'scope':'Canonical universal factor convention and selected signed kernel packet. No claim that restoration is an inverse normal-grade map or a proof for all graph sectors.'}
(HERE/'contact-route-density-restoration.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
