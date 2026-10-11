"""LIMITATION: numerical checks in a fixed 4x4 matrix model only.

This does not consume Agda Tick terms or establish a faithful interpretation
of them. It demonstrates non-uniqueness of interpolations for the chosen
matrix-level corner constraints.
"""
from fractions import Fraction as F
from pathlib import Path
import cmath
import json
import math

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
EPS = 1e-9


def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def add(a, b):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(a, b))


def scale(c, a):
    return tuple(tuple(c * x for x in r) for r in a)


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(4))
                       for j in range(4)) for i in range(4))


def mv(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(4)) for i in range(4))


def norm(v):
    return math.sqrt(sum(abs(x) ** 2 for x in v))


def dist(a, b):
    return norm(tuple(x - y for x, y in zip(a, b)))


def mat_dist(a, b):
    return math.sqrt(sum(abs(a[i][j] - b[i][j]) ** 2
                         for i in range(4) for j in range(4)))


# Basis order |00>, |01>, |10>, |11>. L/R flip the first/second bit.
I = eye(4)
L = tuple(tuple(F(i == (j ^ 2)) for j in range(4)) for i in range(4))
R = tuple(tuple(F(i == (j ^ 1)) for j in range(4)) for i in range(4))
PL = scale(F(1, 2), add(I, scale(-1, L)))
PR = scale(F(1, 2), add(I, scale(-1, R)))
Q = mm(PL, PR)
P00 = add(add(I, scale(-1, PL)), add(scale(-1, PR), Q))
P10 = add(PL, scale(-1, Q))
P01 = add(PR, scale(-1, Q))
P11 = Q

# H_c(alpha,beta) = alpha*PL + beta*PR + c*(alpha+beta)*PL*PR.
# It is the sum of commuting axis generators
# (PL+cQ) and (PR+cQ), with c=0 or c=2.
def evolution(c, alpha, beta):
    phases = (1, cmath.exp(-1j * alpha), cmath.exp(-1j * beta),
              cmath.exp(-1j * (alpha + beta + c * (alpha + beta))))
    pieces = (P00, P10, P01, P11)
    out = tuple(tuple(0j for _ in range(4)) for _ in range(4))
    for phase, projector in zip(phases, pieces):
        out = add(out, scale(phase, projector))
    return out


source = tuple(complex(i == 0) for i in range(4))
left = tuple(complex(i == 2) for i in range(4))
right = tuple(complex(i == 1) for i in range(4))
target = tuple(complex(i == 3) for i in range(4))

passed = 0
checks = []


def check(label, ok, detail=""):
    global passed
    checks.append({"property": label, "status": "PASS" if ok else "FAIL", "detail": detail})
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))
    passed += bool(ok)


print("Tick continuous ambiguity — fixed matrix model only")
print("Generator pair: H0=PL+PR; H2=PL+PR+4*PL*PR (not scalar multiples).")
print("Each axis leg uses PL+2cQ or PR+2cQ with c in {0,2}.")

# Both generators produce the same four corner states and route endpoints.
for c, label in ((0, "H0"), (2, "H2")):
    at_source = mv(evolution(c, 0, 0), source)
    at_left = mv(evolution(c, math.pi, 0), source)
    at_right = mv(evolution(c, 0, math.pi), source)
    at_target = mv(evolution(c, math.pi, math.pi), source)
    check(f"{label}: source corner", dist(at_source, source) < EPS)
    check(f"{label}: left intermediate", dist(at_left, left) < EPS)
    check(f"{label}: right intermediate", dist(at_right, right) < EPS)
    check(f"{label}: target corner", dist(at_target, target) < EPS)
    # The two commuting leg operations compose in either schedule.
    check(f"{label}: leftFirst endpoint",
          dist(mv(evolution(c, 0, math.pi), at_left), target) < EPS)
    check(f"{label}: rightFirst endpoint",
          dist(mv(evolution(c, math.pi, 0), at_right), target) < EPS)
    # Applying the same two pi legs in reverse restores the source.
    returned = mv(evolution(c, math.pi, 0), mv(evolution(c, 0, math.pi), target))
    check(f"{label}: return endpoint", dist(returned, source) < EPS)

# H2 is not a scalar multiple of H0 (so this is not merely a speed rescaling).
H0 = add(PL, PR)
H2 = add(add(PL, PR), scale(4, Q))
inner = sum(float(H0[i][j] * H2[i][j]) for i in range(4) for j in range(4))
norm0_sq = sum(float(H0[i][j] ** 2) for i in range(4) for j in range(4))
best_scale = inner / norm0_sq
proportional_residual = mat_dist(H2, scale(best_scale, H0))
check("generators are not scalar multiples", proportional_residual > EPS,
      f"best-fit scale={best_scale:.6g}; residual={proportional_residual:.6g}")

# At a fixed parameter value, the two generators act differently on the same
# source state; compare a point strictly between the constrained corners.
alpha = beta = 0.37
mid0 = mv(evolution(0, alpha, beta), source)
mid2 = mv(evolution(2, alpha, beta), source)
generator_difference = dist(mid0, mid2)
check("non-proportional generators differ at an intermediate point",
      generator_difference > 1e-5, f"state distance={generator_difference:.6g}")

# Same generator, two paths from source to target: at t=1/2 compare diagonal
# with the L-then-R boundary route (both are continuous parameter paths).
t = 0.5
diagonal = mv(evolution(0, math.pi*t, math.pi*t), source)
l_then_r = mv(evolution(0, math.pi, 0), source)  # boundary path's midpoint
path_difference = dist(diagonal, l_then_r)
check("same generator, different path gives different intermediate state",
      path_difference > 1e-5, f"state distance={path_difference:.6g}")

print(f"\nChecks: {passed}/{len(checks)}")
result = {
    "schema": "marici.nima.tick-continuous-ambiguity.v2",
    "status": "pass" if passed == len(checks) else "fail",
    "caveat": "Fixed 4x4 matrix model; no Agda Tick terms consumed.",
    "generator_pair": ["H0=PL+PR", "H2=PL+PR+4*PL*PR"],
    "generator_pair_nonproportional": True,
    "intermediate_state_distance": generator_difference,
    "same_generator_path_state_distance": path_difference,
    "checks": checks,
    "finding": "Within this model, the same discrete corner and schedule-endpoint constraints admit non-proportional generators and distinct interpolating paths.",
    "scope": "Matrix-model demonstration only; does not prove a faithful Agda Tick interpretation."
}
(RESULTS / "tick-continuous-ambiguity.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
