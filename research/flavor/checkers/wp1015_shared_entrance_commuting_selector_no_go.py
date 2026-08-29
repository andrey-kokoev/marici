import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).parents[1]
wp500 = json.loads((ROOT/"results"/"wp500_tree_loop_port_split.json").read_text())
ensemble = json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())

assert wp500["passed"]
assert wp500["two_sector_tree_matching"]["port_rank"] == 1
assert wp500["checks"]["shared_up_down_tree_ports_are_collinear"]

t = sp.Rational(6, 5)
X = sp.diag(-1, 0, 1)
Y = sp.Matrix([[0, 1, -sp.I*t], [1, 0, 1], [sp.I*t, 1, 0]])
p = sp.symbols("p", real=True)
L = X+p*Y
Au, Bu, Cu, Ad, Bd, Cd = sp.symbols(
    "A_u B_u C_u A_d B_d C_d", real=True
)
Hu = Au*sp.eye(3)+Bu*L+Cu*L**2
Hd = Ad*sp.eye(3)+Bd*L+Cd*L**2
commutator = sp.simplify(Hu*Hd-Hd*Hu)
assert commutator == sp.zeros(3)
assert commutator.det() == 0

# The Gram form follows for a Yukawa matrix aI+bL with Hermitian L:
# |a|^2 I + (a conjugate(b)+conjugate(a)b)L + |b|^2 L^2.
# Positivity restricts the real polynomial coefficients but does not alter
# simultaneous diagonalizability.
lam = sp.symbols("lambda")
charpoly_L = sp.factor(L.charpoly(lam).as_expr())
disc_L = sp.factor(sp.discriminant(charpoly_L, lam))
assert disc_L == 4*(86*p**2+25)**3/sp.Integer(15625)
assert disc_L > 0

Js = [sp.Rational(str(record["J"])) for record in ensemble["records"]]
assert len(Js) == 1210
assert all(value != 0 for value in Js)
assert min(abs(value) for value in Js) > 0

# Deliberate-failure test: a second independently labelled Hermitian entrance
# replaces the common word by X in one sector and Y in the other. The exact
# CP-odd commutator obstruction immediately becomes nonzero.
independent_commutator = X*Y-Y*X
independent_obstruction = sp.factor(independent_commutator.det())
assert independent_obstruction == 24*sp.I/5
assert independent_obstruction != 0

result = {
    "schema": "marici.flavor.wp1015.v1",
    "status": "PASS",
    "source_domain": wp500["domain"],
    "source_operation": "shared coherent tree entrance with collinear up/down linear-word coefficient vectors",
    "gram_family": "Hu=A_u I+B_u L+C_u L^2; Hd=A_d I+B_d L+C_d L^2",
    "weak_basis_descent": "L and both Gram polynomials transform by simultaneous conjugation",
    "proper_image": "commuting positive nondegenerate Gram pairs; J=0",
    "ensemble_sheets_surviving": sum(value == 0 for value in Js),
    "ensemble_sheets_tested": len(Js),
    "contextual_partition": "one source-selected commuting class versus 1210 fitted noncommuting sheets",
    "classification": "source-derived selector and shared-frame rigidifier, but experimentally falsified; no viable physical selector",
    "smallest_exact_falsifier": {
        "added_resource": "second independently labelled Hermitian entrance",
        "witness_pair": "X,Y",
        "commutator_determinant": str(independent_obstruction),
    },
    "instrument": "signed Jarlskog/CKM readout already typed; no connector loop instrument is inferred",
    "claim_boundary": "conditional on the exact WP500 shared-frame, shared-entrance, identity-mass grammar and Hermitian linear word; it does not apply after adding independent entrances",
    "remaining_gate": "derive at least two noncollinear entrance directions and a source law relating their coefficients without fitting physical16",
}

out = ROOT/"results"/"wp1015_shared_entrance_commuting_selector_no_go.json"
out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print("WP1015 PASS: the source-authorized shared entrance selects J=0 and misses all fitted sheets")
