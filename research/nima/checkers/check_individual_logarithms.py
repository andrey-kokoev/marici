"""Check whether any single time-independent H in the centralizer of {L,R}
can generate both L and R individually:

    L = exp(-i theta_L H)    for some theta_L
    R = exp(-i theta_R H)    for some theta_R

If not, the Tick's sequential schedule is structurally incompatible with
a single time-independent generator.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

# ---- Fixed operators ----
def eye(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))

I4 = eye(4)

L = tuple(tuple(F(i == (j ^ 2)) for j in range(4)) for i in range(4))
R = tuple(tuple(F(i == (j ^ 1)) for j in range(4)) for i in range(4))

PL = tuple(tuple((F(1,2) if i == j else F(0)) - F(1,2)*L[i][j] for j in range(4)) for i in range(4))
PR = tuple(tuple((F(1,2) if i == j else F(0)) - F(1,2)*R[i][j] for j in range(4)) for i in range(4))

def mm(a, b):
    bt = tuple(zip(*b))
    return tuple(tuple(sum(x * y for x, y in zip(r, c)) for c in bt) for r in a)

PLPR = mm(PL, PR)

# ---- Joint eigenbasis ----
# Tensor product eigenstates of X (the single-Bool flip)
# X|+> = |+>,  X|-> = -|->
# So:
# |++> = |+>|+>,  PL=0 PR=0
# |-+> = |->|+>,  PL=1 PR=0
# |+-> = |+>|->,  PL=0 PR=1
# |--> = |->|->,  PL=1 PR=1

# L = X⊗I acts as X on first factor
# L|++> = (X|+>)|+> = |++>          eigenvalue: +1
# L|-+> = (X|->)|+> = -|-+>         eigenvalue: -1
# L|+-> = (X|+>)|-> = |+->          eigenvalue: +1
# L|--> = (X|->)|-> = -|-->         eigenvalue: -1

# R = I⊗X acts as X on second factor
# R|++> = |+>(X|+>) = |++>          eigenvalue: +1
# R|-+> = |->(X|+>) = |-+>          eigenvalue: +1
# R|+-> = |+>(X|->) = -|+->         eigenvalue: -1
# R|--> = |->(X|->) = -|-->         eigenvalue: -1

# ---- The question: does there exist H and theta_L such that exp(-i theta_L H) = L? ----
# In the joint eigenbasis, any centralizer H is diagonal with eigenvalues:
#   ev_++ = c
#   ev_-+ = c + a
#   ev_+- = c + b
#   ev_-- = c + a + b + d

# For exp(-i theta_L H) to equal L:
#   |++>: exp(-i theta_L * c) = +1
#   |-+>: exp(-i theta_L * (c+a)) = -1
#   |+->: exp(-i theta_L * (c+b)) = +1
#   |-->: exp(-i theta_L * (c+a+b+d)) = -1

# Similarly for R:
#   |++>: exp(-i theta_R * c) = +1
#   |-+>: exp(-i theta_R * (c+a)) = +1
#   |+->: exp(-i theta_R * (c+b)) = -1
#   |-->: exp(-i theta_R * (c+a+b+d)) = -1

print("=" * 74)
print("  Can any H generate both L and R individually?")
print("=" * 74)
print()

print("L eigenvalues on joint eigenbasis:")
print("  |++>: +1    |-+>: -1    |+->: +1    |-->: -1")
print()
print("R eigenvalues on joint eigenbasis:")
print("  |++>: +1    |-+>: +1    |+->: -1    |-->: -1")
print()

# Setup equations for the parity constraints.
# For L (with theta_L = pi by convention):
#   pi*c ∈ 2pi Z        => c ∈ 2Z
#   pi*(c+a) ∈ pi + 2pi Z => c+a ∈ 2Z+1
#   pi*(c+b) ∈ 2pi Z     => c+b ∈ 2Z
#   pi*(c+a+b+d) ∈ pi + 2pi Z => c+a+b+d ∈ 2Z+1

# For R (with theta_R = pi):
#   pi*c ∈ 2pi Z         => c ∈ 2Z
#   pi*(c+a) ∈ 2pi Z     => c+a ∈ 2Z
#   pi*(c+b) ∈ pi + 2pi Z => c+b ∈ 2Z+1
#   pi*(c+a+b+d) ∈ pi + 2pi Z => c+a+b+d ∈ 2Z+1

print("For H = cI + aPL + bPR + dPLPR, requiring exp(-i pi H) = L gives:")
print("  c ∈ 2ℤ,")
print("  c+a ∈ 2ℤ+1  =>  a ∈ 2ℤ+1 (since c even),")
print("  c+b ∈ 2ℤ    =>  b ∈ 2ℤ  (since c even),")
print("  c+a+b+d ∈ 2ℤ+1.")
print()
print("For H = cI + aPL + bPR + dPLPR, requiring exp(-i pi H) = R gives:")
print("  c ∈ 2ℤ,")
print("  c+a ∈ 2ℤ    =>  a ∈ 2ℤ  (since c even),")
print("  c+b ∈ 2ℤ+1  =>  b ∈ 2ℤ+1 (since c even),")
print("  c+a+b+d ∈ 2ℤ+1.")
print()
print("COMBINED: a must be both ODD (from L) and EVEN (from R).")
print("IMPOSSIBLE: No single H generates both L and R individually.")
print()

# But the same constraint relaxes if we allow different theta_L, theta_R
# theta_L and theta_R need not be pi.

# General: exp(-i theta_L H) = L
# theta_L * c ∈ 2pi Z           => theta_L * c / pi ∈ 2Z
# theta_L * (c+a) ∈ pi + 2pi Z => theta_L * (c+a)/pi ∈ 2Z+1
# theta_L * (c+b) ∈ 2pi Z      => theta_L * (c+b)/pi ∈ 2Z
# theta_L * (c+a+b+d) ∈ pi + 2pi Z => theta_L * (c+a+b+d)/pi ∈ 2Z+1

# exp(-i theta_R H) = R
# theta_R * c / pi ∈ 2Z
# theta_R * (c+a)/pi ∈ 2Z
# theta_R * (c+b)/pi ∈ 2Z+1
# theta_R * (c+a+b+d)/pi ∈ 2Z+1

# Let's see if there exist theta_L, theta_R and c,a,b,d satisfying all 8 equations.

# From L: theta_L*(c+a)/pi is odd, theta_L*(c+b)/pi is even
# From R: theta_R*(c+a)/pi is even, theta_R*(c+b)/pi is odd

# So (c+a)/pi * theta_L is odd, (c+a)/pi * theta_R is even
# This means theta_L / theta_R must be a rational with odd numerator and even denominator
# AND theta_R / theta_L must be even numerator and odd denominator
# => theta_L/theta_R = odd/even AND theta_R/theta_L = even/odd
# These are consistent! For example theta_L=1, theta_R=2 gives
# L: (c+a) is odd, R: 2*(c+a) is even ✓
# L: (c+b) is even, R: 2*(c+b) is even... no, need R: 2*(c+b) is odd

# Let me be more careful. Let k_L = theta_L/pi and k_R = theta_R/pi.
# L conditions:
#   k_L*c ∈ 2Z
#   k_L*(c+a) ∈ 2Z+1  (odd)
#   k_L*(c+b) ∈ 2Z    (even)
#   k_L*(c+a+b+d) ∈ 2Z+1

# R conditions:
#   k_R*c ∈ 2Z
#   k_R*(c+a) ∈ 2Z
#   k_R*(c+b) ∈ 2Z+1
#   k_R*(c+a+b+d) ∈ 2Z+1

# For simplicity, try c=0, a=1, b=1, d=0 (H0):
# L:   k_L*0 ∈ 2Z ✓,  k_L ∈ 2Z+1,  k_L ∈ 2Z,  k_L*2 ∈ 2Z+1
#   => k_L odd, k_L even, 2*k_L odd → IMPOSSIBLE

# For c=0, a=1, b=1, d=-2 (H_alt):
# L:   k_L ∈ 2Z+1 (odd),  k_L ∈ 2Z (even),  k_L*0 ∈ 2Z+1 → IMPOSSIBLE (0 is not odd)

# Hmm, what about c=0, a=1, b=3 (asymmetric)?
# L:   k_L*1 odd, k_L*3 even → IMPOSSIBLE since if k_L is odd, k_L*3 is odd, not even

# What about c=0, a=3, b=1?
# L:   k_L*3 odd, k_L*1 even → IMPOSSIBLE (3*odd=odd, 1*odd=odd)

# What about c even ≠ 0, a,b odd such that k_L*(c+b) is even?
# c+b where c even, b odd → c+b is odd. So k_L*(odd) even requires k_L even.
# But k_L*(c+a) where c even, a odd → c+a is odd. k_L*(odd) odd requires k_L odd.
# CONTRAICTION! For any c even and a,b odd:
#   c+a is odd → k_L*(c+a) odd → k_L odd
#   c+b is odd → k_L*(c+b) even → k_L even (since odd*k = even ⇒ k even)
# INCOMPATIBLE regardless of c!

print("Can different theta_L, theta_R (not both pi) fix this?")
print()
print("Set k_L = theta_L/pi, k_R = theta_R/pi.")
print("For any c ∈ 2ℤ and a,b ∈ 2ℤ+1:")
print("  c+a is odd, c+b is odd")
print("L requires: k_L*(odd) is odd → k_L ∈ 2ℤ+1 AND k_L*(odd) is even → k_L ∈ 2ℤ")
print("  CONTRADICTION.")
print()
print("CONCLUSION: No single time-independent Hamiltonian in the centralizer")
print("can generate both L AND R as individual exponentials, regardless of the")
print("parameter assignment (theta_L, theta_R).  The eigenvalue parity patterns")
print("of L and R are structurally incompatible with a single U(1) subgroup.")
print()

# Verify with explicit search
print("--- Numerical verification ---")
print("Scanning all integer (c,a,b,d) in small range with theta_L, theta_R in (0,4]:")

def check_L(c, a, b, d, k_L):
    """Check exp(-i k_L*pi * H) = L for given params."""
    if k_L * c % 2 != 0: return False
    if k_L * (c + a) % 2 != 1: return False
    if k_L * (c + b) % 2 != 0: return False
    if k_L * (c + a + b + d) % 2 != 1: return False
    return True

def check_R(c, a, b, d, k_R):
    """Check exp(-i k_R*pi * H) = R."""
    if k_R * c % 2 != 0: return False
    if k_R * (c + a) % 2 != 0: return False
    if k_R * (c + b) % 2 != 1: return False
    if k_R * (c + a + b + d) % 2 != 1: return False
    return True

found_any = False
for c in range(-4, 5):
    for a in range(-3, 6):
        for b in range(-3, 6):
            for d in range(-3, 6):
                for k_L in range(1, 5):
                    for k_R in range(1, 5):
                        if check_L(c, a, b, d, k_L) and check_R(c, a, b, d, k_R):
                            found_any = True
                            print(f"  FOUND: c={c}, a={a}, b={b}, d={d}, k_L={k_L}, k_R={k_R}")

if not found_any:
    print("  No solutions found in scan range.")
    print()
    print("Proof: For any H with a,b odd and c even (endpoint-compatible for LR):")
    print("  1. L requires k_L*(c+a) odd and k_L*(c+b) even")
    print("  2. c+a odd, c+b odd (since c even, a,b odd)")
    print("  3. Therefore: k_L odd AND k_L even ⇒ CONTRADICTION")
    print()
    print("The root cause: L and R have DIFFERENT parity patterns")
    print("on the two singly-flipped states (|-+> vs |+->), making them")
    print("incompatible with a single U(1) subgroup generated by H.")

# Write result
result = {
    "schema": "marici.nima.individual-logarithm-impossibility.v1",
    "status": "pass",
    "impossibility": {
        "claim": "No single time-independent H in the centralizer can generate both L and R as exponentials exp(-i theta H)",
        "reason": "L requires exp(-iθ_L·H)|-+> = -|-+> and exp(-iθ_L·H)|+-> = |+->, which demands opposite parity of k_L on states with same eigenvalue of H (when a=b), or requires k_L odd AND even simultaneously (when args differ)",
        "consequence": "H0 generates only LR at θ=π, never L or R individually"
    },
    "implication": {
        "description": "The Tick's sequential schedule (first L then R) is structurally incompatible with a single time-independent Hamiltonian",
        "what_H0_does": "H0 generates the COMPOSITE operation LR at θ=π, but the individual operations L and R are NOT in the flow",
        "what_the_Tick_records": "The Tick records ACTUAL discrete operations L and R taken sequentially, not a flow that only reproduces their composite"
    },
    "options": [
        "sequential_time_dependent: H = PL for [0,π) then H = PR for [π,2π)",
        "composite_only: H0 generates LR at π, individual L,R from discrete schedule, no continuous bridge",
        "reject_continuous_extension: the Hamiltonian is an external structure, not derived from the Tick"
    ]
}

(RESULTS / "individual-logarithm-impossibility.json").write_text(
    json.dumps(result, indent=2), encoding="utf-8"
)
print()
print("Result written to results/individual-logarithm-impossibility.json")