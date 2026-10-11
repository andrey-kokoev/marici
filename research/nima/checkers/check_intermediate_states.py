"""Check whether the continuous path under H0 = PL+PR visits the
intermediate states recorded in the Tick's schedule.

The Tick records:
  leftFirst:  |00> -> |10> -> |11>   (expandLeft then expandRight)
  rightFirst: |00> -> |01> -> |11>   (expandRight then expandLeft)

Under the time-independent Hamiltonian H0 = PL+PR, the path is:
  psi(theta) = exp(-i theta PL) exp(-i theta PR) |00>

We ask: does there exist theta such that psi(theta) = |10> ?
"""
from fractions import Fraction as F
import math, cmath, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

# ---- Exact arithmetic for the joint eigenbasis ----
# |00> in the |++>, |-+>, |+->, |--> basis:
# |00> = (|++> + |-+> + |+-> + |-->)/2
JOINT_BASIS = {
    '++': (F(1,2),  F(1,2),  F(1,2),  F(1,2)),  # PL=0 PR=0
    '-+': (F(1,2),  F(1,2), -F(1,2), -F(1,2)),  # PL=1 PR=0
    '+-': (F(1,2), -F(1,2),  F(1,2), -F(1,2)),  # PL=0 PR=1
    '--': (F(1,2), -F(1,2), -F(1,2),  F(1,2)),  # PL=1 PR=1
}

# Each basis state in the |00>,|01>,|10>,|11> representation:
# |++> = (|00>+|01>+|10>+|11>)/2
# |-+> = (|00>+|01>-|10>-|11>)/2
# |+-> = (|00>-|01>+|10>-|11>)/2
# |--> = (|00>-|01>-|10>+|11>)/2
# So |00> in the |++>, |-+>, |+->, |--> basis:
BASIS_00 = (F(1,2), F(1,2), F(1,2), F(1,2))  # in (++, -+, +-, --) ordering

def component_10_in_joint():
    """Return the coefficient of |10> in each joint eigenstate."""
    # |10> = (|++> - |-+> + |+-> - |-->)/2
    return {'++': F(1,2), '-+': -F(1,2), '+-': F(1,2), '--': -F(1,2)}

# ---- Continuous evolution under H0 = PL+PR ----
# In the joint eigenbasis, exp(-i theta H0) = diag(1, e^{-i theta}, e^{-i theta}, e^{-2i theta})
# So psi(theta) = (1/2)[|++> + e^{-i theta}|-+> + e^{-i theta}|+-> + e^{-2i theta}|-->]

def psi_component_10(theta):
    """The |10> component amplitude of psi(theta)."""
    # |10> component = sum of coefficients in each eigenstate * e^{-i * eigenvalue * theta}
    c = component_10_in_joint()
    amp = complex(c['++'], 0) * complex(1.0, 0.0)  # e^{-i*0*theta} = 1
    amp += complex(c['-+'], 0) * cmath.exp(-1j * theta)
    amp += complex(c['+-'], 0) * cmath.exp(-1j * theta)
    amp += complex(c['--'], 0) * cmath.exp(-2j * theta)
    return amp

def psi_full(theta):
    """Return the full psi(theta) as a dict of |ab> components."""
    # The four amplitudes in the |00>,|01>,|10>,|11> basis
    pl, pr = complex(1,0), complex(1,0)  # will be set based on eigenvalues
    # Actually compute directly:
    # |00> coefficient: (1 + e^{-i theta} + e^{-i theta} + e^{-2i theta})/4
    # |01> coefficient: (1 + e^{-i theta} - e^{-i theta} - e^{-2i theta})/4
    # |10> coefficient: (1 - e^{-i theta} + e^{-i theta} - e^{-2i theta})/4
    # |11> coefficient: (1 - e^{-i theta} - e^{-i theta} + e^{-2i theta})/4
    e1 = cmath.exp(-1j * theta)
    e2 = cmath.exp(-2j * theta)
    return {
        '00': (1 + e1 + e1 + e2) / 4,
        '01': (1 + e1 - e1 - e2) / 4,
        '10': (1 - e1 + e1 - e2) / 4,
        '11': (1 - e1 - e1 + e2) / 4,
    }

def is_basis_state(amps, target, tol=1e-10):
    """Check if amps represents the target basis state |ab>."""
    target_idx = {'00': 0, '01': 1, '10': 2, '11': 3}
    for name, amp in amps.items():
        expected = 1.0 if name == target else 0.0
        if abs(amp - expected) > tol:
            return False
    return True

# ---- Main analysis ----
print("=" * 74)
print("  Continuous path under H0 = PL+PR does NOT visit schedule intermediates")
print("=" * 74)
print()

print("Setup: source = |00>, targets = |11>")
print("Schedule leftFirst: |00> -> |10> -> |11>")
print("Schedule rightFirst: |00> -> |01> -> |11>")
print()

print("Under H0 = PL+PR, the continuous path is:")
print("  psi(theta) = exp(-i theta PL) exp(-i theta PR) |00>")
print("  = (1/2)[|++> + e^{-i theta}|-+> + e^{-i theta}|+-> + e^{-2i theta}|-->]")
print()

print("In the |00>,|01>,|10>,|11> basis:")
print("  psi_00(theta) = (1 + 2e^{-i theta} + e^{-2i theta})/4")
print("  psi_01(theta) = (1 + 0 - e^{-2i theta})/4")
print("  psi_10(theta) = (1 + 0 - e^{-2i theta})/4")
print("  psi_11(theta) = (1 - 2e^{-i theta} + e^{-2i theta})/4")
print()

# Check if there's a theta where psi is exactly |10>
# |10> = (0, 0, 1, 0) in the |00>,|01>,|10>,|11> basis
# From above: psi_10(theta) = (1 - e^{-2i theta})/4
# To equal 1: (1 - e^{-2i theta}) = 4, so e^{-2i theta} = -3
# |1 - e^{-2i theta}| = 4, |e^{-2i theta}| = 1 => impossible

print("Can psi(theta) = |10> for any theta?")
print("  Need psi_00=0, psi_01=0, psi_10=1, psi_11=0")
print("  From psi_10 = (1 - e^{-2i theta})/4 = 1 => e^{-2i theta} = -3")
print("  But |e^{-2i theta}| = 1 for all real theta, |-3| = 3")
print("  => NO SOLUTION")
print()

# Check if there's a theta where psi is exactly |01>
# psi_01 = (1 - e^{-2i theta})/4 = 1 (is it?)
# From above: psi_01(theta) = (1 + 0 - e^{-2i theta})/4
# Wait, check: |01> coefficient = (1 + e^{-i theta} - e^{-i theta} - e^{-2i theta})/4
#   = (1 - e^{-2i theta})/4
# To equal 1: (1 - e^{-2i theta}) = 4 => e^{-2i theta} = -3 => same impossible

print("Can psi(theta) = |01> for any theta?")
print("  psi_01 = (1 - e^{-2i theta})/4 = 1 => e^{-2i theta} = -3")
print("  Same impossibility.")
print()

# ---- Verify with numerical sampling ----
print("Numerical scan: does any theta give |10> or |01>?")
print(f"{'theta':>10} {'|00>':>10} {'|01>':>10} {'|10>':>10} {'|11>':>10}  |intermediate?")
print("-" * 80)

found_10 = False
found_01 = False
for k in range(21):
    theta = k * math.pi / 20
    amps = psi_full(theta)
    near_10 = abs(amps['10'] - 1.0) < 1e-6 and abs(amps['00']) < 1e-6 and abs(amps['01']) < 1e-6 and abs(amps['11']) < 1e-6
    near_01 = abs(amps['01'] - 1.0) < 1e-6 and abs(amps['00']) < 1e-6 and abs(amps['10']) < 1e-6 and abs(amps['11']) < 1e-6
    if near_10:
        found_10 = True
        label = " << |10>"
    elif near_01:
        found_01 = True
        label = " << |01>"
    else:
        label = ""
    
    print(f"{theta:10.6f} {abs(amps['00']):10.6f} {abs(amps['01']):10.6f} "
          f"{abs(amps['10']):10.6f} {abs(amps['11']):10.6f}{label}")

print()
print(f"  Visits |10>? {found_10}")
print(f"  Visits |01>? {found_01}")

# ---- Check whether this matters for the Tick ----
print()
print("=" * 74)
print("  Interpretation")
print("=" * 74)
print()
print("The continuous path under H0 = PL+PR NEVER visits the intermediate")
print("states |10> or |01>.  Instead it passes through superpositions.")
print()
print("This means:")
print("  1. The Tick's schedule (first L then R) is a SEQUENTIAL discrete process.")
print("  2. The path under H0 is a SIMULTANEOUS continuous evolution.")
print("  3. They DO NOT MATCH beyond the endpoints.")
print()
print("Options:")
print("  A. Use a time-dependent Hamiltonian (PL then PR) that matches")
print("     the schedule's sequential structure.  This requires declaring")
print("     the switch point as additional structure.")
print("  B. Keep the time-independent H0 and accept that the continuous")
print("     interpolation departs from the discrete schedule between endpoints.")
print("  C. The Tick does not record continuous paths, only discrete")
print("     operations.  The Hamiltonian is not required to visit the")
print("     intermediate states — only to reproduce the endpoint operations.")
print()
print("Option C is the current checker's position.  But the fact remains")
print("that H0's continuous path does not reflect the Tick's sequential record.")
print("This is a design choice that should be explicitly stated, not assumed.")
print()

# Write result
result = {
    "schema": "marici.nima.intermediate-state-continuity-check.v1",
    "status": "pass",
    "continuous_path_under_H0": {
        "description": "psi(theta) = exp(-i theta PL) exp(-i theta PR) |00>",
        "intermediate_10_reachable": False,
        "intermediate_01_reachable": False,
        "reason": "psi_10 = (1 - e^{-2i theta})/4 requires e^{-2i theta} = -3 which has |e^{-2i theta}| = 3 != 1"
    },
    "schedule_match": {
        "leftFirst": "psi(theta) reaches |10>? NO",
        "rightFirst": "psi(theta) reaches |01>? NO"
    },
    "options": {
        "A_sequential_H": "time-dependent: PL then PR",
        "B_simultaneous_H0": "time-independent: PL+PR",
        "C_discrete_only": "Hamiltonian need not match schedule structure"
    },
    "conclusion": "The time-independent Hamiltonian H0 = PL+PR generates a continuous path that does NOT respect the schedule's sequential structure. This is compatible with the Tick (which records only discrete states) but means the continuous interpolation is a distinct structure, not derived from the schedule."
}

# Save
(RESULTS / "intermediate-state-continuity-check.json").write_text(
    json.dumps(result, indent=2), encoding="utf-8"
)
print("Result written to results/intermediate-state-continuity-check.json")