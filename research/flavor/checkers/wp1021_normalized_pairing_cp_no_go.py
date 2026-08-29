import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
wp1020=json.loads((ROOT/"results"/"wp1020_scale_free_cp_margin_no_go.json").read_text())
ensemble=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
assert wp1020["status"]=="PASS"

I=sp.I
z=sp.Rational(4,5)+I*sp.Rational(3,5)
Y0=sp.diag(1,2,4)
a=sp.Matrix([1,0,0])
b=sp.Matrix([[0,1,0]])
Hu=sp.diag(1,4,9)

assert (a.T*a)[0]==1
assert (b*b.T)[0]==1
assert (a.T*b.T)[0]==0
Yd=Y0+z*a*b
Hd=sp.simplify(Yd*Yd.H)
expected=sp.Matrix([[2,2*z,0],[2*sp.conjugate(z),4,0],[0,0,16]])
assert Hd==expected
C=Hu*Hd-Hd*Hu
assert C.rank()==2 and C.det()==0

disc_u=sp.discriminant(Hu.charpoly().as_expr(),Hu.charpoly().gen)
disc_d=sp.factor(sp.discriminant(Hd.charpoly().as_expr(),Hd.charpoly().gen))
assert disc_u!=0 and disc_d!=0
assert sp.im(z)!=0

# Deliberate contrasting obstruction: normalized, nonorthogonal WP90 directions
# transmit CP. Normalization alone therefore distinguishes neither class.
aw=sp.Matrix([1,2,3])
bw=sp.Matrix([[2,1,1]])
awn=aw/sp.sqrt((aw.T*aw)[0])
bwn=bw/sp.sqrt((bw*bw.T)[0])
Yw=Y0+z*awn*bwn
Hw=sp.simplify(Yw*Yw.H)
nonzero_obstruction=sp.factor((Hu*Hw-Hw*Hu).det())
assert nonzero_obstruction!=0

Js=[sp.Rational(str(row["J"])) for row in ensemble["records"]]
assert len(Js)==1210 and all(j!=0 for j in Js)

result={
 "schema":"marici.flavor.wp1021.v1","status":"PASS",
 "source_domain":"unit-normalized orthogonal real portal vectors in the one-singlet one-mediator FDM-2 grammar",
 "constraints":{"a_norm_squared":"1","b_norm_squared":"1","a_dot_b":"0","singlet_imaginary_part":"3/5"},
 "hostile_down_gram":str(Hd),
 "up_discriminant":str(disc_u),"down_discriminant":str(disc_d),
 "commutator_rank":C.rank(),"commutator_determinant":"0",
 "contextual_partition":"the same exact norm constraints admit both CP-blind one-edge portals and CP-transmitting portals",
 "classification":"nonconic norm selector and orthogonality rigidifier, but neither physical CP selector nor positive-margin constructor",
 "smallest_exact_falsifier":"a=e1, b=e2^T: unit, orthogonal, complex portal, nondegenerate spectra, but only one mixing edge and J=0",
 "deliberate_failure_nonzero_obstruction":str(nonzero_obstruction),
 "instrument":"signed Jarlskog/CKM readout detects the failure but does not create cyclic support",
 "ensemble_sheets_tested":len(Js),
 "claim_boundary":"tests normalization plus orthogonality, not every possible nonconic source law",
 "remaining_gate":"source-derived three-generation cyclic incidence and oriented transmission margin, not merely norms or pairwise angle",
}
out=ROOT/"results"/"wp1021_normalized_pairing_cp_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1021 PASS: normalized orthogonal portal has rank",C.rank(),"and det 0")
