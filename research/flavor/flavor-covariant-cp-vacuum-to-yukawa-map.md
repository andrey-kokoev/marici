# The FDM-2 vacua map to explicit CP-conjugate Yukawa orbits (WP89)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Missing map audited

WP88 repaired stochastic totality, but a symbolic declaration `J=s j(q)` did
not yet exhibit the promised vacuum-to-Yukawa map. `FDM-2` is completed here
without choosing a texture chart.

Let the CP-even base `q` contain ordered positive up/down spectra, three mixing
angles, and an unsigned phase magnitude `delta0 in (0,pi)`. In the standard
CKM representative define

\[
H_u=\operatorname{diag}(u_1,u_2,u_3),\qquad
H_d(s)=V(s\delta_0)\operatorname{diag}(d_1,d_2,d_3)V(s\delta_0)^\dagger.
\]

The physical map is the weak-basis orbit

\[
f(s,q)=[H_u,H_d(s)].
\]

Changing representative by simultaneous conjugation leaves this orbit fixed.
At the two vacua,

\[
H_d(-1)=H_d(+1)^*,\qquad J(-1)=-J(+1),
\]

while all masses, CKM moduli, and CP-even Gram words agree. Thus the uniform
orientation coin prepares an exact CP-conjugate pair over the same CP-even
base. At `s=0`, `V` is real and `J=0`, so the stochastic task genuinely moves
the hostile symmetric input into the proper CP-broken union.

## Exact certificate

The checker uses rational Pythagorean mixing data and an exact algebraic phase,
constructs both Gram pairs, and verifies unitarity, equal spectra/moduli and
mixed traces, complex-conjugate Grams, and opposite nonzero Jarlskog
invariants. No sparse texture phase or reference port appears.

## Scope

This proves the quotient map required by the proposed `FDM-2` package. It does
not derive the map from a renormalizable flavon representation or establish a
laboratory realization of the orientation coin; those remain UV engineering
and empirical gates.

Verification: `uv run --with sympy python
research/flavor/checkers/wp89_covariant_cp_vacuum_yukawa_map.py`.
