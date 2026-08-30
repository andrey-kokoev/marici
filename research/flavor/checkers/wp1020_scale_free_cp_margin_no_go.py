import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
wp1019=json.loads((ROOT/"results"/"wp1019_fdm2_cp_transmission_discriminant.json").read_text())
ensemble=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
assert wp1019["status"]=="PASS"

I=sp.I
lam=sp.symbols("lam",real=True,positive=True)
z=sp.Rational(4,5)+I*sp.Rational(3,5)
Y0=sp.diag(1,2,4)
a=sp.Matrix([1,2,3])
b=sp.Matrix([[2,1,1]])
Hu=sp.diag(1,4,9)
Yd=Y0+lam*z*a*b
Hd=sp.simplify(Yd*Yd.H)
C=sp.simplify(Hu*Hd-Hd*Hu)
detC=sp.factor(C.det())
assert detC==1152*I*lam**3

disc_u=sp.discriminant(Hu.charpoly().as_expr(),Hu.charpoly().gen)
disc_d=sp.factor(sp.discriminant(Hd.charpoly().as_expr(),Hd.charpoly().gen))
assert disc_u==14400
assert disc_d.subs(lam,0)==291600
J2=sp.factor(-detC**2/(4*disc_u*disc_d))
assert sp.limit(J2,lam,0,dir="+")==0
leading=sp.factor(sp.limit(J2/lam**6,lam,0,dir="+"))
assert leading>0

# Every positive lambda preserves field content, charges, support pattern and
# the nonzero portal orbit, while its invariant margin approaches zero.
for n in [1,2,5,10]:
    assert detC.subs(lam,sp.Rational(1,n))!=0

Js=[abs(sp.Rational(str(row["J"]))) for row in ensemble["records"]]
assert len(Js)==1210 and min(Js)>0

result={
 "schema":"marici.flavor.wp1020.v1","status":"PASS",
 "source_domain":"positive rescaling ray of the WP90 portal coupling inside the same one-singlet one-mediator grammar",
 "preserved_structure":["field representations","gauge charges","CP action","portal support","rank-one topology","nonzero portal orbit for every lambda>0"],
 "exact_commutator_response":str(detC),
 "normalized_J_squared_limit":"0 as lambda approaches 0 from above",
 "normalized_J_squared_leading_coefficient":str(leading),
 "contextual_partition":"all finite lambda>0 are CP transmitting, but no uniform positive invariant margin exists on the scale-free ray",
 "classification":"exact scale-free no-go for a symmetry-only CP margin; normalization is a logically independent source resource",
 "smallest_exact_falsifier":"lambda=1/n preserves all qualitative symmetry data while det[Hu,Hd]=1152*i/n^3 approaches zero",
 "instrument":"signed CKM/Jarlskog readout measures the collapse but does not set the portal norm",
 "ensemble_sheets_tested":len(Js),
 "claim_boundary":"applies to source constraints invariant under positive portal rescaling; a nonhomogeneous independently derived normalization can evade it",
 "remaining_gate":"derive a nonconic source normalization or quantized portal magnitude, prove radiative closure, and calibrate it physically",
}
out=ROOT/"results"/"wp1020_scale_free_cp_margin_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1020 PASS:",detC,"J2/lambda^6 ->",leading)
