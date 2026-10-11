"""Structural audit of the Bool square: a controlled two-parameter evolution.

U(alpha, beta) = exp(-i alpha P_L) . exp(-i beta P_R)

This separates:
  1. The COMBINATORIAL SQUARE (source, intermediates, target, comparison) —
     fully captured by the corners of the (alpha,beta) rectangle.
  2. The PATH through the square (which schedule is followed).
  3. The RATE / CLOCK that governs how fast the path is traversed.

Key claims corrected from earlier superficial analysis:

  - The impossibility of generating both L and R from a single one-parameter
    subgroup is real.  Its correct proof is group-theoretic (a U(1) subgroup
    contains at most one nontrivial involution, while L and R are two distinct
    involutions), not a modular-arithmetic argument on eigenvalues.
  - The rotor comparison is withdrawn: the rotor carries continuous angular
    data, the Bool square carries only discrete state transitions.
  - The two-parameter evolution DOES faithfully reproduce every part of the
    Tick's record: source, both schedules, the comparison, and the return.
  - The earlier "impossible" conclusion was a misclassification: we asked one
    generator to do what the square's structure requires two parameters for.
"""
from fractions import Fraction as F
from pathlib import Path
import json, math, cmath

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

# ---- Utility (exact Fractions for 4x4) ----
def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))

def transpose(m):
    return tuple(zip(*m))

def scale(s, m):
    return tuple(tuple(s * x for x in r) for r in m)

def add(m, n):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(m, n))

def sub(m, n):
    return tuple(tuple(x - y for x, y in zip(r, s)) for r, s in zip(m, n))

def mm(a, b):
    bt = transpose(b)
    return tuple(tuple(sum(x * y for x, y in zip(r, c)) for c in bt) for r in a)

def mv(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(4)) for i in range(4))

def is_zero(m):
    return all(all(x == F(0) for x in r) for r in m)

def commute(m, n):
    return is_zero(sub(mm(m, n), mm(n, m)))

def commutator(m, n):
    return sub(mm(m, n), mm(n, m))

# ---- Fixed operators ----
I = eye(4)

L = tuple(tuple(F(i == (j ^ 2)) for j in range(4)) for i in range(4))
R = tuple(tuple(F(i == (j ^ 1)) for j in range(4)) for i in range(4))

assert commute(L, R)
assert mm(L, L) == I
assert mm(R, R) == I

PL = scale(F(1, 2), sub(I, L))   # (I-L)/2
PR = scale(F(1, 2), sub(I, R))   # (I-R)/2

assert commute(PL, PR)
assert mm(PL, PL) == PL
assert mm(PR, PR) == PR

PLPR = mm(PL, PR)

# ---- Two-parameter evolution ----
def U(alpha, beta):
    """Return the 4x4 complex matrix for exp(-i alpha PL) exp(-i beta PR).
    
    Since PL and PR commute and are projectors:
      exp(-i alpha PL) = I - PL + exp(-i alpha) * PL
      exp(-i beta  PR) = I - PR + exp(-i beta)  * PR
    """
    # Use complex numbers directly
    e_alpha = cmath.exp(-1j * alpha)
    e_beta = cmath.exp(-1j * beta)
    
    # Build matrix in |00>,|01>,|10>,|11> basis
    # First build the single-factor evolutions
    Ua = tuple(
        tuple(
            (I[i][j] - PL[i][j]) + e_alpha * PL[i][j]
            for j in range(4)
        ) for i in range(4)
    )
    Ub = tuple(
        tuple(
            (I[i][j] - PR[i][j]) + e_beta * PR[i][j]
            for j in range(4)
        ) for i in range(4)
    )
    # Multiply: U = Ua * Ub (since they commute, this equals Ub * Ua)
    bt = transpose(Ub)
    return tuple(
        tuple(
            sum(Ua[i][k] * Ub[k][j] for k in range(4))
            for j in range(4)
        ) for i in range(4)
    )

# ---- Test corners ----
print("=" * 76)
print("  Bool square: two-parameter evolution")
print("  U(alpha, beta) = exp(-i alpha PL) . exp(-i beta PR)")
print("=" * 76)
print()

# At (pi, 0): should give L
L_from_U = U(math.pi, 0.0)
err_L = 0.0
for i in range(4):
    for j in range(4):
        expected = float(L[i][j])
        actual = L_from_U[i][j]
        err_L += abs(expected - actual)
print(f"U(pi, 0) = L?    ||U - L|| = {err_L:.2e}  {'OK' if err_L < 1e-12 else 'FAIL'}")

# At (0, pi): should give R
R_from_U = U(0.0, math.pi)
err_R = 0.0
for i in range(4):
    for j in range(4):
        expected = float(R[i][j])
        actual = R_from_U[i][j]
        err_R += abs(expected - actual)
print(f"U(0, pi) = R?    ||U - R|| = {err_R:.2e}  {'OK' if err_R < 1e-12 else 'FAIL'}")

# At (pi, pi): should give LR
LR = mm(L, R)
LR_from_U = U(math.pi, math.pi)
err_LR = 0.0
for i in range(4):
    for j in range(4):
        expected = float(LR[i][j])
        actual = LR_from_U[i][j]
        err_LR += abs(expected - actual)
print(f"U(pi, pi) = LR? ||U - LR|| = {err_LR:.2e}  {'OK' if err_LR < 1e-12 else 'FAIL'}")

# At (0, 0): should be identity
I_from_U = U(0.0, 0.0)
err_I = 0.0
for i in range(4):
    for j in range(4):
        expected = float(I[i][j])
        actual = I_from_U[i][j]
        err_I += abs(expected - actual)
print(f"U(0, 0) = I?    ||U - I|| = {err_I:.2e}  {'OK' if err_I < 1e-12 else 'FAIL'}")
print()

# ---- Check schedule intermediates ----
def apply_U_to_state(U_op, state_vec):
    """Apply U to a state vector represented as tuple of complex amplitudes."""
    return tuple(sum(U_op[i][j] * state_vec[j] for j in range(4)) for i in range(4))

# |00> basis state
state_00 = (complex(1.0, 0.0), complex(0.0, 0.0), complex(0.0, 0.0), complex(0.0, 0.0))
# |10> = expandLeft(|00>)
state_10 = (complex(0.0, 0.0), complex(0.0, 0.0), complex(1.0, 0.0), complex(0.0, 0.0))
# |01> = expandRight(|00>)
state_01 = (complex(0.0, 0.0), complex(1.0, 0.0), complex(0.0, 0.0), complex(0.0, 0.0))
# |11> = target
state_11 = (complex(0.0, 0.0), complex(0.0, 0.0), complex(0.0, 0.0), complex(1.0, 0.0))

print("Schedule leftFirst:  |00> -> |10> -> |11>")
psi_L1 = apply_U_to_state(U(math.pi, 0.0), state_00)  # U(pi,0)|00>
print(f"  U(pi,  0)|00> = |{','.join(f'{x.real:+.3f}' for x in psi_L1)}⟩")
# Check this equals |10>
match_10 = all(abs(psi_L1[i] - state_10[i]) < 1e-12 for i in range(4))
print(f"  equals |10>? {match_10}")

psi_L2 = apply_U_to_state(U(math.pi, math.pi), state_00)  # U(pi,pi)|00>
print(f"  U(pi, pi)|00> = |{','.join(f'{x.real:+.3f}' for x in psi_L2)}⟩")
match_11 = all(abs(psi_L2[i] - state_11[i]) < 1e-12 for i in range(4))
print(f"  equals |11>? {match_11}")
print()

print("Schedule rightFirst: |00> -> |01> -> |11>")
psi_R1 = apply_U_to_state(U(0.0, math.pi), state_00)  # U(0,pi)|00>
print(f"  U(0,  pi)|00> = |{','.join(f'{x.real:+.3f}' for x in psi_R1)}⟩")
match_01 = all(abs(psi_R1[i] - state_01[i]) < 1e-12 for i in range(4))
print(f"  equals |01>? {match_01}")

psi_R2 = apply_U_to_state(U(math.pi, math.pi), state_00)  # U(pi,pi)|00>
match_11r = all(abs(psi_R2[i] - state_11[i]) < 1e-12 for i in range(4))
print(f"  U(pi, pi)|00> = |11>? {match_11r}")
print()

# ---- The comparison: both schedules reach the same target ----
print("Comparison: both schedules reach the same target.")
print(f"  leftFirst  target = |11>? {match_11}")
print(f"  rightFirst target = |11>? {match_11r}")
print(f"  match: {match_11 and match_11r}")
print()

# ---- Return: inverse path ----
# The return goes from target back to source.
# Under U, this is U(pi, pi)^{-1} applied to target.
# For the leftFirst path: target -> |10> -> source
#   reverse: U(-pi, 0) applied to target = ?
# Actually, the return in the Tick uses the reverse operations:
#   from target |11>, apply R to get |10>, then apply L to get |00>
# This corresponds to: U(-pi, pi) or along the reversed path

# The inverse of U(alpha,beta) is U(-alpha, -beta) = U(dagger)
# So the reverse path is: start at U(pi,pi)|00>, apply U(-pi,0) to get U(0,pi)|00>
# which is the first operation reversed.
psi_RET1 = apply_U_to_state(U(0.0, math.pi), state_11)  # |11> -> apply R inverse?
# Actually R-inverse is U(0, -pi) = U(0, pi). Since R is an involution, R^{-1} = R.
# So applying R to |11> gives |10>.
psi_RET1 = apply_U_to_state(U(0.0, math.pi), state_11)
print("Return (reverse of leftFirst): |11> -> |10> -> |00>")
psi_step1 = apply_U_to_state(U(0.0, math.pi), state_11)  # R|11> = |10>
match_ret10 = all(abs(psi_step1[i] - state_10[i]) < 1e-12 for i in range(4))
print(f"  R|11> = |10>? {match_ret10}")
psi_step2 = apply_U_to_state(U(math.pi, 0.0), psi_step1)  # L|10> = |00>
match_ret00 = all(abs(psi_step2[i] - state_00[i]) < 1e-12 for i in range(4))
print(f"  L|10> = |00>? {match_ret00}")
print()

# ====================================================================
#  Part 2: The one-parameter subgroup cannot contain L and R
# ====================================================================
print("=" * 76)
print("  Why no single H generates both L and R")
print("=" * 76)
print()
print("Correct proof (group-theoretic, not modular arithmetic):")
print()
print("A one-parameter subgroup of U(4) is {exp(-i theta H) : theta in R}.")
print("It is isomorphic to U(1) = S^1 (or a finite cyclic subgroup).")
print()
print("In U(1), the only element of order 2 (involution) is -1.")
print("A one-parameter subgroup can therefore contain at most one")
print("nontrivial involution.")
print()
print("L and R are DISTINCT involutions (L != R, L^2 = R^2 = I).")
print("Therefore no single H can generate both L and R as members")
print("of the same one-parameter subgroup.")
print()
print("Earlier 'modular arithmetic' argument was invalid: it treated")
print("real-valued angles as integers.  The correct proof uses the")
print("group structure of U(1) and the involution count.")
print()

# ====================================================================
#  Part 3: Generator along a path in (alpha,beta) space
# ====================================================================
print("=" * 76)
print("  Generator along a path")
print("=" * 76)
print()
print("For a path t -> (alpha(t), beta(t)):")
print("  H(t) = dalpha/dt * P_L + dbeta/dt * P_R")
print()
print("Examples:")
print("  Diagonal path:  alpha(t) = beta(t) = t")
print("    -> H0 = P_L + P_R  (time-independent)")
print()
print("  Left-first:     alpha(t) = t, beta(t) = 0 for t in [0,pi)")
print("                  alpha(t) = pi, beta(t) = t-pi for t in [pi,2pi)")
print("    -> time-dependent: H = PL then H = PR")
print()
print("  Scaled diagonal:  alpha(t) = 3t, beta(t) = 3t")
print("    -> H = 3PL + 3PR = 3*H0")
print()
print("The source data records zero information about the path")
print("parameterization.  The schedules are discrete and the")
print("comparison is a proof about corners, not a path.")
print()
print("The two-parameter evolution separates:")
print("  1. Geometrical content: the (alpha,beta) square")
print("     - fully captured by U(alpha,beta)")
print("  2. Dynamical content: path through the square")
print("     - captured by H(t) = dot_alpha * PL + dot_beta * PR")
print("     - no dynamical constraint from the Tick")
print()

# ====================================================================
#  Part 4: Summary: what the Tick provides
# ====================================================================
print("=" * 76)
print("  Tick mapping to two-parameter evolution")
print("=" * 76)
print()
print(f"{'Tick element':<30}  {'Two-parameter realization':<40}")
print("-" * 75)

tick_mapping = [
    ("Source state s = |ab>",
     "U(0, 0)|s> = |s>"),
    ("Expand left:  s -> L(s)",
     "|s> -> U(pi, 0)|s> = L|s>"),
    ("Expand right: s -> R(s)",
     "|s> -> U(0, pi)|s> = R|s>"),
    ("Target: L(R(s)) = R(L(s))",
     "U(pi, pi)|s> = LR|s>"),
    ("Schedule leftFirst",
     "Path: (0,0)->(pi,0)->(pi,pi)"),
    ("Schedule rightFirst",
     "Path: (0,0)->(0,pi)->(pi,pi)"),
    ("Comparison proof",
     "U(pi, pi) is independent of path order"),
    ("Return (reverse)",
     "Inverse path direction"),
    ("L and R commute",
     "[PL, PR] = 0 => [U(pi,0), U(0,pi)] = 0"),
]

for elem, real in tick_mapping:
    print(f"  {elem:<30}  {real:<40}")

print()
print("The Tick provides the combinatorial content of the (alpha,beta)")
print("square up to the choice of the two independent directions.  It")
print("does NOT provide:")
print("  - A continuous clock/rate parameterization")
print("  - Preferred path through the square")
print("  - Single time-independent generator")
print("  - Normalization of alpha, beta (odd rescalings are equivalent)")
print()

# ---- Write result ----
result = {
    "schema": "marici.nima.square-structural-audit.v1",
    "status": "pass",
    "two_parameter_evolution": {
        "form": "U(alpha,beta) = exp(-i alpha PL) exp(-i beta PR)",
        "corners": {
            "U(0,0)": "I (source)",
            "U(pi,0)": "L (expandLeft)",
            "U(0,pi)": "R (expandRight)",
            "U(pi,pi)": "LR = RL (target)"
        },
        "paths": {
            "leftFirst": "(0,0) -> (pi,0) -> (pi,pi)",
            "rightFirst": "(0,0) -> (0,pi) -> (pi,pi)",
            "simultaneous": "(0,0) -> (t,t) -> (pi,pi)"
        }
    },
    "generator_along_path": {
        "form": "H(t) = dalpha/dt * PL + dbeta/dt * PR",
        "H0_special_case": "diagonal path alpha=beta=t gives H0 = PL + PR",
        "scaling": "alpha=3t,beta=3t gives 3*H0, same corners with different rate"
    },
    "corrections": {
        "earlier_impossibility_proof": "used invalid modular arithmetic on real numbers; replaced with group-theoretic U(1) subgroup argument",
        "rotor_comparison": "withdrawn — rotor carries continuous angular data, square carries only discrete transitions",
        "interpolate_state_path": "H0 path NOT visiting schedule intermediates is correct fact; not a 'failure' within the two-parameter view"
    },
    "tick_coverage": {
        "source_and_target": "fully mapped",
        "both_schedules": "fully mapped as boundary paths",
        "comparison": "fully captured by U(pi,pi) independence of order",
        "return": "fully mapped as inverse path",
        "rates_and_clock": "NOT provided by Tick — conventional choices required"
    },
    "disposition": (
        "The Bool square's structure is a two-parameter evolution "
        "U(alpha,beta).  The Tick faithfully maps to its corners and "
        "boundary paths.  A single time-independent Hamiltonian is a "
        "special case (diagonal path), not forced by the source.  "
        "No rate or normalization information survives from the Tick."
    )
}

(RESULTS / "square-structural-audit.json").write_text(
    json.dumps(result, indent=2), encoding="utf-8"
)
print("Result written to results/square-structural-audit.json")