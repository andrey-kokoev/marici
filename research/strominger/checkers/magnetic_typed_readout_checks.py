"""Exact checks for typed forgetting versus unauthorized codiagonal readout."""
import json
import os
import sympy as sp


checks = []


def record(cid, statement, condition, detail):
    status = "pass" if condition else "FAIL"
    checks.append({"id": cid, "statement": statement, "status": status,
                   "detail": str(detail)})
    print(f"[{status:>4}] {cid}: {statement} ({detail})", flush=True)


# Two independently typed one-dimensional outputs.  Forgetting the labels
# leaves their direct sum and preserves rank.  Applying a codiagonal is an
# additional quotient and creates the anti-diagonal kernel.
typed_transport = sp.eye(2)
codiagonal = sp.Matrix([[1, 1]])
record("FORGET.rank", "ordinary type forgetting preserves the direct-sum rank",
       typed_transport.rank() == 2, "underlying map is still the 2x2 identity")
record("QUOTIENT.kernel", "the codiagonal quotient creates an anti-diagonal kernel",
       (codiagonal * typed_transport).nullspace() ==
       [sp.Matrix([-1, 1])], "ker[1 1]=span(-1,1)")
record("QUOTIENT.not_forgetful", "type erasure plus codiagonal is not a conservative forgetful functor",
       typed_transport.rank() != (codiagonal * typed_transport).rank(),
       "rank 2 becomes rank 1")


# Reflected branches on an N-fold cover align exactly when 2q is integral.
def aligned_on_cover(q, degree):
    return sp.Mod(2 * degree * q, degree) == 0


integer_failures = [(q, degree) for q in range(1, 31)
                    for degree in range(1, 13)
                    if not aligned_on_cover(sp.Rational(q), degree)]
record("PAIRING.integer", "every integral reflection component admits the common readout pairing",
       not integer_failures, f"q=1..30,N=1..12; failures={integer_failures[:1]}")

rational_components = [sp.Rational(35, 3), sp.Rational(55, 3)]
rational_failures = [(q, degree) for q in rational_components
                     for degree in range(3, 61, 3)
                     if aligned_on_cover(q, degree)]
record("PAIRING.fractional", "no thirds-clearing cover authorizes the rational branch pairing",
       not rational_failures,
       f"q=35/3,55/3; N=3,6,...,60; false alignments={rational_failures[:1]}")


# A typed determinant is a blockwise rank certificate, not the scalar sum of
# coordinates from different target types.
x, y = sp.symbols("x y")
typed_matrix = sp.diag(x, y)
typed_maximal = sp.factor(typed_matrix.det())
collapsed_matrix = codiagonal * typed_matrix
record("DETERMINANT.blockwise", "the typed maximal minor retains both sector factors",
       typed_maximal == x * y and collapsed_matrix == sp.Matrix([[x, y]]),
       "typed determinant=xy; collapsed readout=[x y]")

# Equivariant descent keeps the invariant character sector; it does not apply
# a codiagonal to nontrivial characters.  Schur's condition for a homogeneous
# map of charge c from chi to psi is psi=chi+c mod N.
candidate_charges = [2, 1, 1]
record("DESCENT.invariants", "none of the fractional candidates has an ordinary descended scalar",
       all(charge != 0 for charge in candidate_charges), candidate_charges)


def homogeneous_map_exists(source_charge, target_charge, map_charge, degree=3):
    return (source_charge + map_charge - target_charge) % degree == 0


record("DESCENT.schur", "no charge-zero morphism sends either candidate sector to scalars",
       all(not homogeneous_map_exists(charge, 0, 0)
           for charge in set(candidate_charges)),
       "Hom_Z3(V_chi,V_0)=0 for chi=1,2")
record("DESCENT.charged", "a nontrivial readout requires an explicitly charged morphism",
       homogeneous_map_exists(1, 0, 2) and
       homogeneous_map_exists(2, 0, 1),
       "charges 2 and 1 respectively absorb the source deck charge")
record("DESCENT.uniform_twist", "a uniform twist cannot repair relative charge mismatch",
       all(((candidate_charges[0] + twist) -
            (candidate_charges[1] + twist)) % 3 == 1
           for twist in range(3)),
       "relative charge remains 1 mod 3")

# Sector-specific charged adapters have independent normalizations.  Charge
# conservation alone does not select their relative readout weight.
alpha, beta, amplitude = sp.symbols("alpha beta A", nonzero=True)
opposite_packet = sp.Matrix([amplitude, -amplitude])
weighted_readout = sp.Matrix([[alpha, beta]]) * opposite_packet
record("COHERENCE.weights", "the anti-diagonal packet cancels only after choosing equal adapter weights",
       sp.factor(weighted_readout[0]) == amplitude * (alpha - beta),
       weighted_readout[0])
record("COHERENCE.not_canonical", "an allowed independent adapter rescaling destroys unit-weight cancellation",
       weighted_readout[0].subs({alpha: 1, beta: 1}) == 0 and
       weighted_readout[0].subs({alpha: 1, beta: 2}) != 0,
       "deck charge fixes admissibility, not the relative normalization")

# Adding reflection enlarges Z3 to D3.  The conjugate charge sectors form its
# real two-dimensional standard representation.  It has no invariant linear
# covector, but x^2+y^2 is an invariant quadratic readout.
sqrt3 = sp.sqrt(3)
rotation = sp.Matrix([[-sp.Rational(1, 2), -sqrt3 / 2],
                      [sqrt3 / 2, -sp.Rational(1, 2)]])
reflection = sp.diag(1, -1)
u, v = sp.symbols("u v")
linear_equations = list((sp.Matrix([[u, v]]) * rotation -
                         sp.Matrix([[u, v]])))
linear_equations += list((sp.Matrix([[u, v]]) * reflection -
                          sp.Matrix([[u, v]])))
linear_solution = sp.solve(linear_equations, (u, v), dict=True)
record("DIHEDRAL.no_linear", "the reflected charge doublet has no invariant linear readout",
       linear_solution == [{u: 0, v: 0}], linear_solution)

x0, y0 = sp.symbols("x0 y0")
vector = sp.Matrix([x0, y0])
norm = sp.expand((vector.T * vector)[0])
rotated_norm = sp.simplify(((rotation * vector).T *
                            (rotation * vector))[0])
reflected_norm = sp.simplify(((reflection * vector).T *
                              (reflection * vector))[0])
record("DIHEDRAL.quadratic", "the first lawful invariant is the quadratic norm",
       sp.simplify(rotated_norm - norm) == 0 and
       sp.simplify(reflected_norm - norm) == 0,
       norm)
record("DIHEDRAL.visible", "a nonzero anti-diagonal packet is visible to the invariant norm",
       sp.expand(norm.subs({x0: amplitude, y0: -amplitude})) ==
       2 * amplitude**2,
       "||(A,-A)||^2=2*A^2")

# Hermitian/real positivity is essential: the holomorphic quadratic x^2+y^2
# has complex isotropic vectors, while the star-compatible norm does not.
ar, ai, br, bi = sp.symbols("ar ai br bi", real=True)
hermitian_energy = ar**2 + ai**2 + br**2 + bi**2
anti_energy = sp.expand(hermitian_energy.subs({br: -ar, bi: -ai}))
record("POSITIVE.hermitian", "the star-compatible anti-diagonal energy is a positive sum of squares",
       anti_energy == 2 * (ar**2 + ai**2), anti_energy)
record("POSITIVE.loss", "the zero route-loss packet has zero invariant energy",
       hermitian_energy.subs({ar: 0, ai: 0, br: 0, bi: 0}) == 0,
       "packet=(0,0)")
record("POSITIVE.complex_caveat", "a holomorphic quadratic alone has nonzero complex isotropic vectors",
       (x0**2 + y0**2).subs({x0: 1, y0: sp.I}) == 0,
       "(1,i) shows why the star/real structure is required")

failed = [check for check in checks if check["status"] != "pass"]
output = {
    "schema": "marici.checker_results.v1",
    "checker": "magnetic_typed_readout_checks.py",
    "author": "marici.Strominger",
    "scope": {"strength": "exact typed-readout mechanism checks"},
    "checks": checks,
    "n_pass": len(checks) - len(failed),
    "n_fail": len(failed),
    "verdict": "Forgetting labels while retaining the direct-sum target preserves rank; a codiagonal can create spurious kernels. Equivariant descent forbids scalar readouts from the candidate sectors. With reflection, conjugate charges form the D3 standard doublet: it has no invariant linear functional, while its star-compatible Hermitian norm sees every nonzero anti-diagonal packet. The star structure is essential because a holomorphic quadratic has complex isotropic vectors. Charged linear adapters require new normalization data.",
}
outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "magnetic_typed_readout.json"), "w",
          encoding="ascii") as handle:
    json.dump(output, handle, indent=2)
print(f"\n{len(checks) - len(failed)} passed, {len(failed)} failed", flush=True)
raise SystemExit(1 if failed else 0)
