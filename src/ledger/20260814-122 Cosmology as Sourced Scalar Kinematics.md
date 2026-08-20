---
authors:
  - marici.Nima
  - marici.Benincasa
---
# Cosmology as Sourced Scalar Kinematics

## Record

Date: 2026-08-14

Status: conditional structural identification in finite kinematic space.

Scope: unconserved massless external momenta with a distinguished total momentum defect. This entry does not derive a cosmological state, vacuum prescription, FLRW dynamics, or integrated wavefunction.

## Claim

Let

\[
\widetilde V_n
=
\{s_{ij}=s_{ji},\ s_{ii}=0\}
\]

be symmetric Mandelstam space before imposing momentum conservation, and define the signless incidence map

\[
\partial_+:\widetilde V_n\to \Bbbk^n,
\qquad
r_i=\sum_{j\neq i}s_{ij}.
\]

Ordinary scattering kinematics is the kernel

\[
V_n=\ker\partial_+.
\]

For momenta \(p_i\) with

\[
s_{ij}=2p_i\!\cdot p_j
\]

and total momentum

\[
Q=\sum_i p_i,
\]

the row sums are

\[
r_i=2p_i\!\cdot Q.
\]

Thus the failure of the scattering constraints is exactly the momentum defect:

\[
\boxed{
Q\neq0
\quad\Longleftrightarrow\quad
\partial_+(s)\neq0
}
\]

within the momentum realization.

Moreover,

\[
Q^2
=
\sum_{i<j}s_{ij}
=
\frac12\sum_i r_i.
\]

A canonical conserved extension is obtained by adjoining a closing leg

\[
q_\infty=-Q.
\]

The enlarged system satisfies

\[
\sum_i p_i+q_\infty=0,
\]

but \(q_\infty\) is generically weighted or massive:

\[
q_\infty^2=Q^2.
\]

Define defect coordinates

\[
\delta_i=(Q-p_i)^2.
\]

For massless \(p_i\),

\[
\delta_i=Q^2-r_i.
\]

Hence the cosmological deformation away from scattering can be represented by the source data

\[
(r_i,Q^2)
\]

or equivalently

\[
(\delta_i,Q^2),
\]

subject to

\[
\sum_i\delta_i=(n-2)Q^2.
\]

The scattering locus is the source-free boundary

\[
Q\to0,
\qquad
r_i\to0.
\]

This gives the working sector relation

\[
\boxed{
\text{scattering}
=
\text{zero-defect locus of sourced kinematics}.
}
\]

## Evidence

The identification follows directly from

\[
r_i=\sum_{j\neq i}2p_i\!\cdot p_j
=2p_i\!\cdot(Q-p_i)
=2p_i\!\cdot Q
\]

for \(p_i^2=0\), and

\[
Q^2
=
\left(\sum_i p_i\right)^2
=
2\sum_{i<j}p_i\!\cdot p_j
=
\sum_{i<j}s_{ij}.
\]

The closing-leg construction is the tautological conserved completion \(q_\infty=-Q\).

This is a retrospective ledger reconstruction from the cosmology investigation. No standalone repository checker has yet been attached to this entry.

## Boundary

The following stronger statements are not established:

- \(Q\) is a new primitive of the scalar master;
- sourced kinematics alone determines a cosmological wavefunction;
- the closing leg is an ordinary additional massless particle;
- the zero-defect limit by itself determines a scattering/cosmology nearby-cycle functor;
- a choice of cosmological vacuum follows from \(Q\neq0\).

The investigation instead demoted \(Q\) from an independent primitive: it is reconstructed from failure of the ordinary scattering constraints.

Integral bookkeeping requires retaining the primitive mass line \(Q^2\). Eliminating it prematurely can introduce artificial torsion in the defect quotient.

## Consequence

Cosmology can be tested as a derived sector of the same scalar kinematic carrier before introducing a second master geometry.

The next question is whether cosmological partial-energy boundaries are intrinsic valuations of the resolved Cut carrier or require additional sector-specific combinatorics.

## Outcome contract

```json
{
  "claim": "Cosmological kinematics can be represented as the sourced complement of the ordinary scattering kernel: r_i = 2 p_i·Q, with scattering recovered at Q=0. The closing leg q_infinity=-Q gives a canonical conserved completion.",
  "status": "conditional",
  "assumptions": [
    "External p_i are massless in the finite kinematic model.",
    "The statement concerns kinematic carrier structure, not a full cosmological wavefunction.",
    "No standalone checker has yet been attached."
  ],
  "evidence_refs": [
    "retrospective cosmology derivation",
    "scalar-master kinematic framework"
  ],
  "factorization_test": {
    "source_map_identity": "analytic pass",
    "closing_leg_conservation": "analytic pass",
    "scattering_zero_defect_limit": "analytic pass",
    "wavefunction_factorization": "not tested"
  },
  "counterevidence": [
    "Sourced kinematics alone does not determine vacuum or period data.",
    "The closing leg is generically massive or weighted."
  ],
  "next_experiment": "Construct partial-energy divisors on the occurrence-resolved Cut carrier and test Cut compatibility without adding a new nesting primitive."
}
```
