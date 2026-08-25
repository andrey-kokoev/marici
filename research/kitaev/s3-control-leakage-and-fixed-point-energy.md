# Leakage and fixed-point energy of the compiled controls

Owner: `marici.Kitaev`

Status: exact finite fixed-point theorem; perturbations and hardware noise are
outside the claim.

## Bounded question

How much code/gauge-subspace leakage do the three compiled controls create,
and what fixed-point energy penalty follows?

## Vacuum code

On the flat vacuum code, `B^t`, `B^c`, and `K_c` all vanish.  Every compiled
nontrivial-flux unitary therefore acts as the identity and has zero final
vacuum-code leakage.  A useful operation presupposes a prepared endpoint
excitation.

## Gauge-invariant flux excitation

On one gauge orbit, an element projector selects a fraction `1/m` of the
uniform orbit, where `m` is the conjugacy-class size.  After the phase
`exp(-i theta B^g)`, exact projection back to the Haar vertex sector gives

\[
L_m(\theta)=\frac{4(m-1)}{m^2}\sin^2\frac\theta2.
\]

Thus

\[
L_t(\theta)=\frac89\sin^2\frac\theta2,
\qquad
L_c(\theta)=\sin^2\frac\theta2.
\]

At `theta=pi` the respective leakages are `8/9` and `1`.  With unit vertex
penalty, these are also the exact excess expectations of `1-A`.

Clean uncomputation does not generally remove this final physical leakage:
it removes the ancilla, while the element-dependent phase remains.

## Transient ancilla leakage

At the end of holonomy computation but before uncomputation, the ancilla holds
which-element information.  On a Haar-invariant flux excitation the data's
vertex leakage is exactly

\[
\frac23\quad\text{(transposition)},
\qquad
\frac12\quad\text{(three-cycle)}.
\]

This transient is present even when the selected final phase is zero.  It is
coherently repaired by uncomputation, subject to later gate faults.

## `G/H` current

On the six-state gauge orbit of a three-cycle class, `K_c` is the oriented
current on the three `c` states and zero on the three `c^2` states.  Exact
matrix multiplication gives

\[
AK_c=K_cA=0.
\]

It also has support orthogonal to `B^e`.  Hence it commutes with the local
fixed-point Hamiltonian and preserves its energy.  Its nontrivial domain is
the charged `G/H` endpoint subspace in `ker A`; it annihilates the Haar
sector rather than leaking it.

## Verification and falsifiers

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_s3_control_leakage_energy.py
```

The checker proves both symbolic leakage formulas, both transient fractions,
and the exact Haar-current annihilation identities.  Eight aggregate gates
are declared.  Saved result:
`research/kitaev/results/s3-control-leakage-energy.json`.

The result is falsified by a different class fraction, disagreement with a
direct 1,296-state evolution, nonzero `AK_c` or `K_cA`, or a nonunit
fixed-point penalty normalization.  Generic perturbations, finite pulse
bandwidth, and noncommuting hardware terms remain untyped.
