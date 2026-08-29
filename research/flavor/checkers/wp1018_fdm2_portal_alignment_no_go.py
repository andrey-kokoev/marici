import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
wp1017=json.loads((ROOT/"results"/"wp1017_fdm2_cp_odd_entrance_bridge.json").read_text())
ensemble=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
assert wp1017["status"]=="PASS"

I=sp.I
z=sp.Rational(4,5)+I*sp.Rational(3,5)
Hu=sp.diag(1,4,9)

# Smallest hostile portal: the scalar vacuum is CP broken but the portal is
# aligned to one generation, leaving both physical Gram matrices diagonal.
Y0a=sp.diag(1,2,4)
aa=sp.Matrix([1,0,0])
ba=sp.Matrix([[1,0,0]])
Yda=Y0a+z*aa*ba
Hda=sp.simplify(Yda*Yda.H)
Ca=Hu*Hda-Hda*Hu
assert sp.im(z)!=0
assert Hda==sp.diag(sp.Rational(18,5),4,16)
assert len(set(Hda.diagonal()))==3
assert Ca==sp.zeros(3) and Ca.det()==0

# Coefficient freedom test around the WP90 witness. Nine real Y0 entries alone
# give rank 8. Allowing one already-admitted portal component restores rank 9.
q=sp.symbols("q0:9",real=True)
t=sp.symbols("t",real=True)
R=sp.Matrix(3,3,q)
a=sp.Matrix([t,2,3])
b=sp.Matrix([[2,1,1]])
Yd=R+z*a*b
Hd=sp.expand(Yd*Yd.H)
pairs=[(0,1),(0,2),(1,2)]
coords=[Hd[i,i] for i in range(3)]
coords += [sp.re(Hd[i,j]) for i,j in pairs]
coords += [sp.im(Hd[i,j]) for i,j in pairs]
J=sp.Matrix(coords).jacobian(list(q)+[t])
point={q[0]:1,q[4]:2,q[8]:4,t:1}
point.update({q[i]:0 for i in [1,2,3,5,6,7]})
A=J.subs(point)
assert A[:,:9].rank()==8
assert A.rank()==9
pivots=A.rref()[1]
minor=sp.factor(A[:,list(pivots)].det())
assert pivots==(0,1,2,3,4,5,6,8,9)
assert minor==sp.Rational(663552,25)

Js=[sp.Rational(str(row["J"])) for row in ensemble["records"]]
assert len(Js)==1210 and all(j!=0 for j in Js)

result={
 "schema":"marici.flavor.wp1018.v1","status":"PASS",
 "source_domain":"full real-coefficient FDM-2 mediator grammar at either CP-broken singlet vacuum",
 "faithful_quotient":"physical16 weak-basis orbit; Gram coordinates used only as a local representative",
 "hostile_pair":{"singlet_CP_odd":"Im(z)=3/5","physical_CP_odd":"det[Hu,Hd]=0","down_gram_diagonal":["18/5","4","16"]},
 "fixed_portal_Y0_jacobian_rank":8,
 "one_portal_component_augmented_rank":9,
 "nonzero_minor":str(minor),
 "contextual_partition":"CP-broken source vacua split into physically CP-even aligned portals and physically CP-odd generic portals",
 "classification":"singlet-vacuum selector and source rigidifier, but neither a universal physical CP selector nor a numerical physical16 selector over the admitted coefficient family",
 "smallest_exact_falsifier":"a=e1, b=e1^T, Y0=diag(1,2,4): Im(z)!=0 but both nondegenerate Grams commute",
 "instrument":"signed Jarlskog/CKM readout detects the failure; source preparation and portal-coefficient calibration remain unestablished",
 "ensemble_sheets_tested":len(Js),
 "claim_boundary":"does not deny the fixed WP90 witness; denies promotion from one witness or scalar CP breaking to selection over the full allowed mediator grammar",
 "remaining_gate":"a source law restricting portal coefficients to a proper CP-transmitting locus, with physical calibration and ensemble-wide numerical survival",
}
out=ROOT/"results"/"wp1018_fdm2_portal_alignment_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1018 PASS: aligned CP-even image; augmented rank",A.rank(),"minor",minor)
