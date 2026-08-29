import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).parents[1]
wp90 = json.loads((ROOT/"results"/"wp90_renormalizable_fdm2_mediator.json").read_text())
wp92 = json.loads((ROOT/"results"/"wp92_fdm2_perturbative_decoupling.json").read_text())
ensemble = json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
assert all(wp90["gates"].values()) and all(wp92["gates"].values())

x, y, r = sp.symbols("x y r", real=True)
I = sp.I
Y0 = sp.diag(1, 2, 4)
a = sp.Matrix([1, 2, 3])
b = sp.Matrix([[2, 1, 1]])
Hu = sp.diag(1, 4, 9)
Yd = Y0+r*(x+I*y)*(a*b)
Hd = sp.simplify(Yd*Yd.H)
det_general = sp.factor((Hu*Hd-Hd*Hu).det())
det_plus = sp.factor(det_general.subs({x:sp.Rational(4,5), y:sp.Rational(3,5)}))
det_minus = sp.factor(det_general.subs({x:sp.Rational(4,5), y:-sp.Rational(3,5)}))
assert det_plus == 1152*I*r**3 and det_minus == -1152*I*r**3

U = sp.Matrix([[sp.Rational(3,5),sp.Rational(4,5),0],
               [-sp.Rational(4,5),sp.Rational(3,5),0],[0,0,1]])
assert U.T*U == sp.eye(3)
Hu_p, Hd_p = U*Hu*U.T, sp.simplify(U*Hd*U.T)
assert sp.factor((Hu_p*Hd_p-Hd_p*Hu_p).det()-det_general) == 0

# Deliberate failure: delete the imaginary source entrance.
real_slice_obstruction = sp.factor(det_general.subs(y, 0))
assert real_slice_obstruction == 0
assert sp.factor(det_general/(I*r**3*y)) != 0
Js = [sp.Rational(str(row["J"])) for row in ensemble["records"]]
assert len(Js) == 1210 and all(j != 0 for j in Js)

result = {
 "schema":"marici.flavor.wp1017.v1","status":"PASS",
 "source_domain":"proposed FDM-2 complex singlet plus one vectorlike down mediator on its CP-conjugate vacuum union",
 "faithful_quotient":"physical16 weak-basis orbit of the induced Hermitian Gram pair",
 "bridge_identity":str(det_general),
 "selected_vacuum_response":{"plus":str(det_plus),"minus":str(det_minus)},
 "weak_basis_descent":"exact under simultaneous rational orthogonal conjugation; determinant invariant under full unitary weak basis",
 "contextual_partition":"real slice y=0 has J=0; two FDM-2 branches have opposite nonzero J for finite r>0",
 "classification":"qualitative CP selector and source-presentation rigidifier; not a numerical physical16 selector",
 "ensemble_sheets_tested":len(Js),
 "ensemble_statement":"all fitted sheets have J!=0; qualitative union survives but no sheetwise magnitude follows",
 "smallest_exact_falsifier":{"deleted_source_feature":"imaginary entrance y","commutator_determinant":str(real_slice_obstruction)},
 "instrument":"signed Jarlskog/CKM readout conditional on physical singlet/vectorlike-quark preparation and threshold matching",
 "claim_boundary":"existing proposed-source bridge; does not admit FDM-2 as observed, select r or CP-even coordinates, or establish apparatus",
 "remaining_gate":"source-derived finite threshold ratio and complete CP-even coefficient packet with collider-calibrated mediator instrument",
}
out=ROOT/"results"/"wp1017_fdm2_cp_odd_entrance_bridge.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1017 PASS:",det_general)
