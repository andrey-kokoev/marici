---
authors:
  - marici.Nima
date: 2026-08-18
---
# 648 — The Physical Shared-Wall Boundary Is a Closed Cech Cocycle

## Hard-to-vary claim

The source-unsplit physical \(q_{G_{12}}\)-residue determines a canonical
closed class in the shared-wall localization complex. Its three nonzero
wall components satisfy the pair-incidence compatibility relations, and its
mixed occurrence component is zero.

## Physical wall vector

On the frozen residue surface, write

\[
\Omega_{\rm phys}
=
\frac{da\wedge db}{w\,q_{g_1}q_{g_2}q_{g_3}}
\left(\frac1{q_{g_{23}}}+\frac1{q_{g_{31}}}\right),
\qquad w^2=K_E.
\]

Entries 593--594 prove that its residues on the three shared walls are
generically nonzero conductor classes. Denote them by

\[
(\rho_1,\rho_2,\rho_3)
\in
\bigoplus_{i=1}^3H^1(W_i^\nu\setminus C_i)(-1).
\]

## Pair-incidence differential

For two transverse affine-linear walls \(q_i,q_j\), the two orders of
iterated residue differ by the oriented Jacobian:

\[
\operatorname{Res}_{q_j}\operatorname{Res}_{q_i}\Omega
=
\frac{F(p_{ij})}{\det d(q_i,q_j)},
\qquad
\operatorname{Res}_{q_i}\operatorname{Res}_{q_j}\Omega
=
-\frac{F(p_{ij})}{\det d(q_i,q_j)}.
\]

The exact gate evaluates all three shared-wall pairs at three generic
kinematic points. The remaining shared denominator, both occurrence
denominators, and \(K_E\) are nonzero at every tested intersection. Hence
the cancellation is legal rather than a hidden \(0/0\):

\[
\boxed{d_{\rm Cech}(\rho_1,\rho_2,\rho_3)=0.}
\]

## Mixed occurrence component

At

\[
u=q_{g_{31}}=0,
\qquad
v=q_{g_{23}}=0,
\]

the source occurrence factor is

\[
\frac1u+\frac1v=\frac{u+v}{uv}.
\]

Its double-residue numerator vanishes at \(u=v=0\). Therefore the physical
cocycle has no component in the extra rank-one mixed class of Entry 645.

## Resulting typed object

The source now determines the boundary class

\[
\boxed{
\rho_{\rm phys}=(\rho_1,\rho_2,\rho_3;0)
\in\ker d_{\rm Cech}.
}
\]

This is stronger than the separate nonvanishing statements of Entry 594:
the three residues assemble into one legal localization cocycle. It is also
narrower than an absolute pushforward. No basis or projector identifies
\(\rho_{\rm phys}\) with coordinates in \(\mathcal T_7\).

## Consequence for the frontier

Entries 644 and 646 exclude both elliptic support and a wall boundary of
the physical real chain. Entry 645's mixed ambient direction is unoccupied.
The remaining admissible operation is therefore the supported Gysin image
of this specific closed three-wall vector:

\[
i_{W!}(\rho_{\rm phys})\longrightarrow\mathcal T_7.
\]

The next falsifier is to construct that map from the normalization sequence
and determine the flat saturation of its image, without choosing
\(\mathcal T_7\) coordinates after seeing the answer.

## Evidence

- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`;
- `research/benincasa/physical_g12_shared_wall_residues.py`;
- `research/benincasa/check_unsplit_occurrence_pair.rs`;
- Entries 593--595 and 644--646.

## Outcome contract

~~~json
{
  "claim": "The source-unsplit physical shared-wall residues fail the pair-incidence compatibility relation or require the mixed occurrence generator.",
  "status": "falsified",
  "shared_wall_components": 3,
  "shared_pair_cech_differential": 0,
  "mixed_occurrence_component": 0,
  "physical_boundary_class": "closed three-wall localization cocycle",
  "T7_coordinates": "unselected",
  "next_experiment": "Construct its normalization-derived supported Gysin image and flat saturation inside T7."
}
~~~
