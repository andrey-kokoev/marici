"""Conditional action-and-metric bridge to the EXISTING fixed-Gram tower.

The first four tower probes are explicitly labelled by Bool^2. This is a
chosen interface, not a proof of native source selection. The 137-row matrix
response fixture is a different construction and is not silently identified.
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import io
import json
import runpy
import sys
import sympy as S

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
with redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(HERE / "check_source_rotor_coordinate_trace.py"))
    tower = runpy.run_path(str(HERE / "check_carrier_gram_tower.py"))
    seed = runpy.run_path(str(HERE / "check_seed_endpoint_sections.py"))

Gs, D, A = source["G"], source["D"], source["A"]
G4 = S.Matrix(4, 4, lambda i, j: tower["inner"](
    [int(a == i) for a in range(4)], [int(a == j) for a in range(4)]))
G12 = 10*S.eye(12)+S.ones(12)
SL, SR = S.diag(1, 1, -1, -1), S.diag(1, -1, 1, -1)
L = S.Matrix(4, 4, lambda i, j: int(i == (j ^ 2)))
R = S.Matrix(4, 4, lambda i, j: int(i == (j ^ 1)))
# Ordered joint-character frame: trivial, second-bit odd, first-bit odd,
# both odd. Columns have Euclidean unit norm, NOT Gram unit norm.
W = S.Matrix(4, 4, lambda row, col:
             S.Rational((-1)**(((row & 1) if col in (1, 3) else 0)
                               + ((row >> 1) if col in (2, 3) else 0)), 2))
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def equal(a, b):
    return S.simplify(a-b) == S.zeros(*a.shape)


check("existing-G4", G4 == 10*S.eye(4)+S.ones(4))
check("Walsh-frame", W.T*W == S.eye(4))
check("joint-characters", L*W == W*SL and R*W == W*SR)
check("Gram-in-character-frame", W.T*G4*W == S.diag(14, 10, 10, 10))

# Source inherited Gram is diag(1,2,2,4), so no silent normalization reset.
scales = S.diag(1/S.sqrt(14), 1/S.sqrt(5), 1/S.sqrt(5), S.sqrt(S.Rational(2, 5)))
M = W*scales
Mi = S.simplify(M.inv())
check("metric-isometry", equal(M.T*G4*M, Gs))
check("left-intertwiner", equal(L*M, M*SL))
check("right-intertwiner", equal(R*M, M*SR))
check("inverse", equal(Mi*M, S.eye(4)))

# Solve the full linear intertwiner problem, rather than just exhibiting M.
unknowns = S.symbols("m0:16")
X = S.Matrix(4, 4, unknowns)
solution = next(iter(S.linsolve(list(L*X-X*SL)+list(R*X-X*SR), unknowns)))
N = S.simplify(W.T*S.Matrix(4, 4, solution))
check("all-intertwiners-diagonal-in-character-frame", N == S.diag(*N.diagonal()))
check("four-free-character-scales", len(set().union(*(entry.free_symbols for entry in N))) == 4)
for signs in product((-1, 1), repeat=4):
    candidate = M*S.diag(*signs)
    check(f"isometric-sign-choice/{signs}", equal(candidate.T*G4*candidate, Gs)
          and equal(L*candidate, candidate*SL) and equal(R*candidate, candidate*SR))

# The pre-existing angular generator transports, rather than being inferred
# from the finite involutions or from G4 eigenvalues alone.
D4 = S.simplify(M*D*Mi)
OmegaSource = S.zeros(4)
OmegaSource[1, 2], OmegaSource[2, 1] = 2, -2
Omega4 = S.simplify(Mi.T*OmegaSource*Mi)
Hessian4 = S.simplify(4*Mi.T*S.diag(0, 1, 1, 0)*Mi)
check("transported-angular-generator-is-metric-skew", D4.T*G4+G4*D4 == S.zeros(4))
check("transported-Hamiltonian-identity", D4.T*Omega4 == Hessian4)
check("active-form-rank-two", Omega4.rank() == 2)
check("common-and-third-contrast-stationary", D4*W[:, 0] == S.zeros(4, 1) and D4*W[:, 3] == S.zeros(4, 1))
check("positive-Gram-not-Lorentzian", (W.T*G4*W).diagonal() == S.Matrix([[14, 10, 10, 10]]))

# Reuse the tower's exact direct restriction P_12,4, not coordinate deletion.
P = S.Matrix(4, 12, lambda i, j: int(i == j) if j < 4 else S.Rational(1, 14))
E = S.eye(12)[:, :4]
check("tower-projection-left-inverse", P*E == S.eye(4))
check("tower-metric-adjoint", E.T*G12 == G4*P)
D12 = S.simplify(E*D4*P)
check("chosen-lift-descends-exactly", P*D12 == D4*P)
check("chosen-lift-preserves-ambient-Gram", D12.T*G12+G12*D12 == S.zeros(12))
check("chosen-lift-fixes-discarded-sector", D12*(S.eye(12)-E*P) == S.zeros(12))
# This extension was defined from D4; descent is existence, not selection
# of a native rung12 generator.

x = S.Matrix(S.symbols("x0:4", real=True))
c = Mi*x
q_c, p_c = c[1], 2*c[2]
H = S.simplify((x.T*Hessian4*x)[0]/2)
check("canonical-readout-energy", S.simplify(H-(2*q_c*q_c+p_c*p_c/2)) == 0)
check("canonical-readout-equations", equal(S.Matrix([q_c, p_c]).jacobian(x)*D4*x,
                                           S.Matrix([p_c, -4*q_c])))

# A less arbitrary source clue: the already checked actual six-edge seed
# has a unique cycle cover under its declared simultaneous-section objective.
# Compare its skew part with D4; do NOT identify the whole permutation with
# the continuous rotor (its alternating mode has eigenvalue -1).
vertices, forward = seed["V"], seed["forward"]
cycle = S.Matrix(4, 4, lambda i, j: int(vertices[i] == forward[vertices[j]]))
labels = {"A": 0, "B": 3, "C": 1, "D": 2}
Z = S.Matrix(4, 4, lambda i, j: int(i == labels[vertices[j]]))
cycle4 = Z*cycle*Z.T
check("seed-four-cycle-skew-is-transported-generator", cycle4-cycle4.T == D4)
active_cycle = (S.eye(4)-cycle4**2)/2
minus_cycle = (S.eye(4)-cycle4+cycle4**2-cycle4**3)/4
check("seed-active-plane-projector", active_cycle**2 == active_cycle and active_cycle.rank() == 2)
check("seed-alternating-projector", minus_cycle**2 == minus_cycle and minus_cycle.rank() == 1)
check("generator-squares-to-active-projector", D4**2 == -4*active_cycle)
rotor_quarter = S.eye(4)-active_cycle+D4/2
check("rotor-quarter-matches-cycle-on-active-plane", (rotor_quarter-cycle4)*active_cycle == S.zeros(4))
check("rotor-quarter-misses-only-alternating-sign", rotor_quarter-cycle4 == 2*minus_cycle)
check("whole-cycle-is-not-connected-real-flow", cycle4.det() == -1 and rotor_quarter.det() == 1)

out = {
    "schema": "marici.nima.rotor-rung4-intertwiner.v1", "status": "pass", "checks": checks,
    "target": "fixed stabilizer-probe Gram G4=10I+J, with declared Bool^2 labelling",
    "source": "prior active-sector source coordinates with Gram diag(1,2,2,4)",
    "map": "M=W diag(1/sqrt(14),1/sqrt(5),1/sqrt(5),sqrt(2/5)); W is the ordered orthonormal Walsh frame",
    "all_linear_intertwiners": "W diag(a,b,c,d)",
    "isometric_choices": 16,
    "remaining_freedom": "independent signs of four joint characters; unlabelled probe/frame selection is additional",
    "canonical_readout": {"q_c": str(q_c), "p_c": str(p_c), "H_count": str(H)},
    "D4": [[str(v) for v in D4.row(i)] for i in range(4)],
    "source_form_rank": 2,
    "clock": "external retained phase lift still required; common Gram coordinate is stationary, not the prior angular clock",
    "rung12_lift": "E D4 P exists, preserves Gram and descends; constructed from D4, not independently source-derived",
    "actual_seed_clue": {
        "cover": seed["covers"][0], "vertex_to_probe_labels": labels,
        "identity": "D4=C-C^T for the actual seed's unique cycle-cover permutation in the declared chart",
        "boundary": "Cycle-cover selection objective and skew-part extraction are explicit; this does not select a physical flow",
        "missed_sector": "rank-one alternating sector: the cycle acts by -1 but exp(pi D4/4) by +1; full-cycle determinant is -1",
    },
    "unclosed": ["native selection of Clifford/rotor/phase realization", "actual tower-to-source probe identification",
                 "connection to confirmed 12--9-->6 / 11--8-->5 / 10--7-->4 transport", "connection to 137-row fixture",
                 "clock phase/winding access and physical calibration"],
}
path = HERE.parent / "results" / "rotor-rung4-intertwiner.json"
path.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(f"PASS: {len(checks)} exact/symbolic rung-4 bridge checks")
print("Action-and-metric preserving bridge exists; 16 sign choices remain with labels fixed.")
print("Transported canonical q_c,p_c evolve; common coordinate and third contrast are stationary.")
print("No native generator selection, physical clock, or 137-row identification is claimed.")
