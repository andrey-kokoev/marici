---
authors:
  - marici.Nima
  - marici.Benincasa
---
# Three-Site Elliptic Coefficient System and Nearby-Cycle Degeneration

## Record

Date: 2026-08-14

Status: conditional structural identification of the homogeneous rank-two elliptic block; first-order cosmological first-jet completeness falsified as a sufficient loop test.

## Claim

For the homogeneous one-loop three-site cosmological wavefunction, the rank-two elliptic Picard--Fuchs subsystem is not an arbitrary elliptic coefficient system.

It is canonically identified as

\[
\boxed{
\mathbb V_{\triangle,\mathrm{ell}}
\simeq
\mathcal K_{B^{-1/2}}
\otimes
m^*\mathbb H_{\mathrm{Leg}},
}
\]

where

- \(\mathbb H_{\mathrm{Leg}}\) is the universal Legendre Gauss--Manin variation;
- \(m=A/B\) is the signed-energy cross-ratio;
- \(\mathcal K_{B^{-1/2}}\) is a rank-one Kummer twist.

Entry 148 uses the reciprocal Legendre coordinate \(m_{148}=B/A=m^{-1}\).
The two conventions describe the same Legendre variation after the standard
permutation of branch points; formulas comparing the entries must apply this
reciprocal change of coordinate.

In homogeneous energy variables,

\[
A=\ell_1\ell_2,
\qquad
B=\ell_3\ell_4,
\]

where the \(\ell_i\) are the four signed-energy hyperplanes.

Thus the elliptic subsystem is generated entirely from the existing signed-energy divisor arrangement.

Its singular support satisfies

\[
\operatorname{Sing}
(\mathbb V_{\triangle,\mathrm{ell}})
\subseteq
\mathcal A_{\mathrm{energy}}.
\]

No additional carrier divisor is introduced by the pure elliptic block.

The scattering boundary is

\[
E_T=\ell_4=0.
\]

At this boundary the elliptic curve degenerates to a nodal rational curve and the elliptic variation degenerates through nearby cycles into Tate/Kummer data.

At the physical \(B=0\) degeneration, the \(-1\) from Legendre continuation
is cancelled by the \(-1\) Kummer monodromy of \(B^{-1/2}\). The total
twisted system therefore has unipotent monodromy

\[
T=\exp N,
\qquad
\operatorname{rank}N=1,
\qquad
N^2=0.
\]

Hence

\[
\boxed{
\psi_{E_T=0}
(
\mathbb V_{\triangle,\mathrm{ell}}
)
=
\text{Tate/Kummer variation}.
}
\]

The algebraic-letter quartic

\[
\mathcal Q
\]

is constant to first order in the total-energy parameter,

\[
\mathcal Q
=
-16X_1^2X_2^2
+
O(E_T^2).
\]

Therefore the first genuinely elliptic deformation appears only at second normal order.

A first ordinary normal jet cannot detect it.

## Evidence

Direct substitution transforms the published second-order Picard--Fuchs operator into the Legendre hypergeometric equation.

Homogenization identifies the modulus

\[
m
=
\frac{\ell_1\ell_2}
{\ell_3\ell_4}.
\]

The elliptic discriminant becomes

\[
\Delta_E
=
16AB(A-B)^4,
\]

whose support is exactly the signed-energy arrangement together with the ordinary site-energy hyperplanes.

The published scattering degeneration corresponds to

\[
E_T=0,
\]

where the elliptic curve becomes nodal.

The algebraic quartic expands as

\[
\mathcal Q
=
-16X_1^2X_2^2
+O(E_T^2).
\]

Consequently the first nontrivial algebraic deformation is invisible to first-order normal analysis.

## Boundary

This entry identifies only the homogeneous rank-two elliptic block.

It does not prove:

- the complete marked relative coefficient system;
- the full Gauss--Manin extension including additional denominator sections;
- the complete nearby-cycle filtration;
- the full Picard--Fuchs system.

The stronger identification

\[
\mathbb V_{\triangle}
=
R^1\pi_*
(E_X\setminus D_X)
\]

remains conjectural.

## Consequence

The first-order cosmological first-jet program is insufficient for integrated loop cosmology.

The correct discriminating object becomes the nearby-cycle and second-Rees filtration of the elliptic coefficient system.

This substantially strengthens the intermediate Marici hypothesis:

\[
\boxed{
\text{shared carrier}
+
\text{shared derived/six-functor calculus}
+
\text{sector-specific coefficient systems}.
}
\]

It weakens the hypothesis that a universal first-jet construction alone controls loop cosmology.

## Outcome contract

```json
{
  "claim": "The homogeneous three-site elliptic subsystem is a Kummer-twisted pullback of the universal Legendre variation over the existing signed-energy arrangement. Its scattering degeneration is a nearby-cycle degeneration to Tate/Kummer data, and the first algebraic elliptic deformation appears only at second normal order.",
  "status": "conditional",
  "assumptions": [
    "Published homogeneous three-site Picard-Fuchs system.",
    "Homogeneous energy variables.",
    "Only the rank-two elliptic block is identified."
  ],
  "factorization_test": {
    "Legendre_identification": "passed",
    "existing_divisor_support": "passed",
    "scattering_nearby_cycle": "passed",
    "first_jet_sufficiency": "falsified",
    "full_relative_extension": "open"
  },
  "next_experiment": "Construct the complete marked Gauss-Manin coefficient object, compute second-Rees nearby cycles, and determine whether the algebraic quartic is entirely coefficient-theoretic or forces a new carrier stratum."
}
```
