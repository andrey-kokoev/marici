import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
wp1018=json.loads((ROOT/"results"/"wp1018_fdm2_portal_alignment_no_go.json").read_text())
assert wp1018["status"]=="PASS"

I=sp.I
u1,u2,u3=sp.symbols("u1 u2 u3",real=True)
p12,p23,p31,q12,q23,q31,y=sp.symbols(
    "p12 p23 p31 q12 q23 q31 y",real=True)
h12=p12+I*y*q12
h23=p23+I*y*q23
h31=p31+I*y*q31
H=sp.Matrix([[0,h12,sp.conjugate(h31)],
             [sp.conjugate(h12),0,h23],
             [h31,sp.conjugate(h23),0]])
Hu=sp.diag(u1,u2,u3)
C=Hu*H-H*Hu
delta=(u1-u2)*(u2-u3)*(u3-u1)
T=sp.factor(sp.im(h12*h23*h31))
expected_T=sp.factor(y*(q12*p23*p31+p12*q23*p31+p12*p23*q31)
                     -y**3*q12*q23*q31)
assert sp.factor(T-expected_T)==0
assert sp.simplify(sp.expand(C.det()-2*I*delta*T))==0

# Reconstruct the WP90 transmitting witness.
z=sp.Rational(4,5)+I*sp.Rational(3,5)
Y0=sp.diag(1,2,4)
a=sp.Matrix([1,2,3])
b=sp.Matrix([[2,1,1]])
Yd=Y0+z*a*b
Hd=sp.simplify(Yd*Yd.H)
prod=sp.factor(sp.im(Hd[0,1]*Hd[1,2]*Hd[2,0]))
det_wp90=sp.factor((sp.diag(1,4,9)*Hd-Hd*sp.diag(1,4,9)).det())
assert prod==sp.Rational(24,5)
assert det_wp90==1152*I

# Deliberate failure: a and c=Y0*b^T collinear makes their wedge vanish.
aa=sp.Matrix([1,0,0])
ba=sp.Matrix([[1,0,0]])
ca=Y0*ba.T
Q=aa*ca.T-ca*aa.T
assert Q==sp.zeros(3)
nonzero_obstruction=prod
assert nonzero_obstruction!=0

result={
 "schema":"marici.flavor.wp1019.v1","status":"PASS",
 "source_domain":"real-coefficient rank-one FDM-2 mediator grammar at a CP-broken singlet vacuum",
 "faithful_discriminant":"det[Hu,Hd]=2*i*Delta_u*T in the nondegenerate up-mass representative",
 "transmission_polynomial":str(expected_T),
 "portal_geometry":"q_ij are components of a wedge c with c=Y0*b^T; a wedge c=0 is a sufficient exact blind locus",
 "contextual_partition":"T=0 physically CP-even portal class; T>0 and T<0 opposite signed physical CP classes",
 "wp90_witness":{"T":str(prod),"det_commutator":str(det_wp90)},
 "classification":"weak-basis-invariant discriminator and instrument readout, not a source selector; T!=0 is an open genericity condition unless dynamics supplies a margin",
 "smallest_exact_falsifier":"a parallel to Y0*b^T makes every q_ij zero while the singlet remains complex",
 "deliberate_failure_nonzero_obstruction":str(nonzero_obstruction),
 "instrument":"signed Jarlskog/CKM measurement realizes the discriminator but cannot prepare or enforce T!=0",
 "claim_boundary":"formula assumes nondegenerate up spectrum for equivalence with J; no portal coefficient law, normalization, or apparatus is inferred",
 "remaining_gate":"source-derived weak-basis-covariant law and positive margin excluding T=0 before fitting",
}
out=ROOT/"results"/"wp1019_fdm2_cp_transmission_discriminant.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1019 PASS: T =",expected_T,"WP90 T =",prod)
