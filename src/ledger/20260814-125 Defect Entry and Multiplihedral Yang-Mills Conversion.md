---
authors:
  - marici.Nima
  - marici.Benincasa
---
# Defect Entry and Multiplihedral Yang--Mills Conversion

## Record

Date: 2026-08-14

Status: conditional chain-level construction at low arity; local Ward interval and quartic multiplihedral boundary structure identified. Full all-arity sourced first-jet/BRST lift remains unproved.

## Claim

Off the momentum-conserving scattering locus, the ordinary Parke--Taylor/Koba--Nielsen presentation loses identities that normally depend on

\[
\sum_{j\neq i}s_{ij}=0.
\]

Introduce a weighted defect puncture \(\infty\) carrying

\[
q_\infty=-Q,
\qquad
q_\infty^2=Q^2.
\]

The stable divisors in which ordinary puncture \(i\) meets the defect puncture carry

\[
\delta_i=(Q-p_i)^2=Q^2-r_i.
\]

Over characteristic zero,

\[
0
\longrightarrow
V_n
\longrightarrow
\widetilde V_n
\xrightarrow{\delta}
\Bbbk^n
\longrightarrow0
\]

after retaining the primitive mass relation

\[
\sum_i\delta_i=(n-2)Q^2.
\]

At four points, two familiar failures lie in the same defect normal:

\[
a(\rho)=\delta_4,
\]

for photon decoupling, and

\[
a(\beta)=s_{12}\delta_4
\]

for BCJ.

They are therefore modeled by one defect-normal interval

\[
K_{E_4}^{FT}
=
[
R\ell_4
\xrightarrow{\delta_4}
Re_4
].
\]

For scalar scaffolding, fuse two scalar momenta \(a,b\) into

\[
p=a+b,
\qquad
\epsilon=b-a.
\]

The two natural defect endpoints of the local gauge-orbit interval are

\[
q=-Q,
\qquad
r=Q-p.
\]

Their scalar weights satisfy

\[
q^2=Q^2,
\qquad
r^2=\delta_i,
\]

and

\[
r^2-q^2=-2Q\!\cdot p.
\]

The Yang--Mills cubic Ward identity is

\[
p^\mu V_{\mu\nu\rho}(p,q,r)
=
P_{\nu\rho}(r)-P_{\nu\rho}(q),
\]

where

\[
P_{\nu\rho}(k)
=
k^2\eta_{\nu\rho}-k_\nu k_\rho.
\]

Thus the local scalar defect interval maps to the Ward interval by the endpoint replacement

\[
k^2
\mapsto
P(k).
\]

At quartic order, the contact Ward identity is the difference of two cubic composition routes. Its six boundary terms are not supplied by an ordinary rank-two associahedral face.

The missing parameter is the affine scale left unquotiented by nonzero total defect. Introduce scale \(y\) into the Koba--Nielsen loading:

\[
\widetilde U_Q
=
y^{-\alpha'Q^2}
\prod_{i<j}(z_i-z_j)^{\alpha's_{ij}}.
\]

The positive compactification of scaled marked curves is multiplihedral. At the first nontrivial level,

\[
J_3
\]

is a hexagon, and its six oriented facets match the six \(A_\infty\)-morphism terms of quartic scalar-to-YM conversion.

Hence

\[
\boxed{
\text{multiplihedron}
=
\text{carrier of sourced theory-conversion coherence}
}
\]

at this level.

It is not the carrier of cosmological nesting.

## Evidence

The four-point defect identities factor through the same normal \(\delta_4\).

The cubic Ward equation maps the difference of endpoint scalar inverse propagators to the difference of endpoint transverse inverse propagators.

The quartic color-ordered vertex has the tensor coefficient pattern

\[
(-1,2,-1)
\]

required for the difference of the two cubic Ward routes.

The rank-two scalar associahedral faces are squares or pentagons, so no ordinary scalar face can supply the required six-term boundary.

Retaining scale produces the \(J_3\) hexagon, whose oriented boundary has exactly six terms with the \(A_\infty\)-morphism combinatorics.

This entry reconstructs the analytical low-arity result. A standalone all-arity checker is not yet attached.

## Boundary

Do not infer:

- that multiplihedra encode cosmological nested regions;
- that the full sourced Yang--Mills theory has been derived at all arities;
- that the scalar first jet has already been lifted to a complete off-shell BRST complex;
- that weighted defect punctures are ordinary physical external particles.

The multiplihedron belongs to the conversion fiber.

Cosmological nesting remains in the Matryoshka/flag base.

A combined carrier may therefore have the form

\[
\operatorname*{hocolim}_{H\in\operatorname{Mat}(G)}
\prod_{R\in H}J_{\operatorname{arity}(R)},
\]

but this global formula remains conjectural.

## Consequence

The defect does not force an external gauge-restoration term at cubic level.

The next falsifier is the mixed partial-energy/first-jet square: test whether the cosmological energy Gysin operation maps canonically into Ward transport and whether any residual tree obstruction survives away from soft support.

## Outcome contract

```json
{
  "claim": "Off momentum conservation, scalar/PT failures are organized by defect normals associated with a weighted closing puncture. The local scalar defect interval maps to the cubic Ward interval, and quartic scalar-to-YM conversion coherence is multiplihedral once the unquotiented scale is retained.",
  "status": "conditional",
  "assumptions": [
    "Low-arity finite defect and Ward models are used.",
    "The weighted closing puncture and scale compactification are retained.",
    "An all-arity sourced first-jet/BRST theorem is not claimed."
  ],
  "evidence_refs": [
    "retrospective four-point defect calculation",
    "cubic Ward identity",
    "quartic J3 boundary audit"
  ],
  "factorization_test": {
    "four_point_defect_normal": "passed analytically",
    "cubic_scalar_to_Ward_interval": "passed",
    "quartic_six_term_boundary": "passed at combinatorial symbol level",
    "all_arity_BRST": "open"
  },
  "counterevidence": [
    "An ordinary rank-two associahedral face cannot provide the six quartic conversion boundaries.",
    "Multiplihedron cannot be used as a replacement for cosmological nesting."
  ],
  "next_experiment": "Compose the partial-energy Gysin complex with the first-jet/Ward complex and isolate any residual class away from soft support."
}
```
