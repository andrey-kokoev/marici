---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Physical G12 Residue Must Pass a Localization-Descent Gate

## Degree correction

Entries 589--591 correctly identify the missing physical denominators and
their literal substitutions, but their proposed direct target in the
rank-34 lower module is type-wrong.

The original integrand is a three-form in ((c,a,b)).  Poincare residue along

\[
q_{G_{12}}=c+E=0
\]

is a two-form on the residue surface

\[
S_E:\quad w^2=K_E(a,b).
\]

It therefore cannot directly land in the ordinary three-variable
deletion-closed rank-34 lower module.  Entry 590's exact denominator formulas
and unit Jacobian remain valid, but the displayed target arrow is superseded
by the supported residue object below.

## Correct localization object

Let (W) be the union on (S_E) of the four residual walls in either
labelled summand.  The physical residue class lives in

\[
H^2(S_E\setminus W).
\]

The relevant localization sequence is

\[
\boxed{
H^2(S_E)
\longrightarrow
H^2(S_E\setminus W)
\xrightarrow{\partial_W}
H^1(W)(-1)
\longrightarrow
H^3(S_E).
}
\]

This is the same degree gate already established for the mixed-face classes
in `elliptic-mixed-face-geometry.json`.

The q-only nine-master module belongs to (H^2(S_E)).  Hence there is no
canonical map backwards from the physical open-wall residue to the
nine-master module.  Such a class descends only if

\[
\boxed{\partial_W[\operatorname{Res}_{G_{12}}\Omega_{m phys}]=0.}
\]

Only after a lift to (H^2(S_E)) exists may the infinity-Gysin projection to
the rank-two elliptic quotient be applied.

## What Entry 591 establishes

Entry 591 proves one component of this descent test: the source-unsplit
combination has zero simple residue on the occurrence exceptional divisor.
It does not evaluate the localization boundaries on the three shared walls

\[
q_{g_1},\qquad q_{g_2},\qquad q_{g_3}.
\]

Accordingly, the proposed next step “map the common core into the
nine-master module” is also superseded.  The next admissible calculation is
to compute these three wall residues, including their normalization-sheet
and intersection compatibility.  A nonzero boundary means the physical
class is intrinsically relative; a zero total boundary produces a canonical
q-only lift whose infinity-Gysin image can then be tested.

## Consequence for the rank-34 census

The rank-34 lower module remains the correct deletion-closed ambient
coefficient census and controls the denominator filtration before residue.
It is not the codomain of the Poincare residue.  Relating the two requires a
morphism of localization triangles, not an identification of their rank
shadows.

## Evidence

- `research/benincasa/physical-g12-residue-localization-typing.json`;
- `research/benincasa/elliptic-mixed-face-geometry.json`;
- Entries 545 and 589--591.

## Outcome contract

~~~json
{
  "claim": "The physical q_G12 Poincare residue directly defines a class in the rank-34 lower module or in the q-only nine-master module.",
  "status": "falsified",
  "residue_degree": 2,
  "physical_residue_home": "H^2(S_E minus W)",
  "q_only_home": "H^2(S_E)",
  "descent_boundary_target": "H^1(W)(-1)",
  "occurrence_exceptional_boundary_zero": true,
  "shared_wall_boundaries_computed": false,
  "next_experiment": "Compute the q_g1, q_g2, and q_g3 localization residues of the source-unsplit physical class and test their Cech compatibility."
}
~~~
