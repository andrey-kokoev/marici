# 1997 — The C9 Scalar Logarithmic Seam Defect Is Canonically de Rham Exact

## Source-derived coefficient gate

Entry 1994 closes the generic first-order companion-fold lane for all 480 maximal \(C_9\) source orbits.  Nima's oriented endpoint seam is a five-circuit relation/coherence cell with role order

\[
(L_i,R_i,g_{i+1},G,r_i).
\]

Before introducing a higher-rank coefficient object, test the smallest coefficient system already supplied by the frozen rational contour: its scalar logarithmic de Rham system.

Write

\[
\alpha_j=d_z\log L_j,
\qquad
h_{j\mu}=\partial_\mu\log L_j.
\]

Then

\[
\partial_\mu\alpha_j=d_z h_{j\mu}.
\]

## Exact five-circuit identity

Let \(C\) be the ordered five-circuit and \(\partial_{\rm OS}\) its Orlik--Solomon boundary.  Define the standard logarithmic transgression

\[
T_\mu(\alpha_C)
=
\sum_{k=1}^{5}(-1)^{k-1}h_{k\mu}
\alpha_{C\setminus k}.
\]

The exact exterior-algebra audit gives

\[
\boxed{
\partial_\mu\partial_{\rm OS}(\alpha_C)
=
-d_z\partial_{\rm OS}T_\mu(\alpha_C).
}
\]

The minus sign is forced because the de Rham differential and the degree-minus-one Orlik--Solomon boundary anticommute in the total complex.

The identity contains twenty nonzero labelled terms.  The defect is therefore not strictly zero on chosen representatives, but it is canonically de Rham exact.

## Consequence for physical activation

For a closed contour \(\Gamma\), Stokes gives

\[
\int_\Gamma
\partial_\mu\partial_{\rm OS}(\alpha_C)=0.
\]

For a relative physical chain,

\[
\int_\Gamma d_zH_\mu
=
\int_{\partial\Gamma}H_\mu,
\qquad
H_\mu=-\partial_{\rm OS}T_\mu(\alpha_C).
\]

Thus the first admissible seam activation is neither an ordinary carrier class nor an absolute scalar-coefficient class.  It is a supported boundary pairing between the source-derived relative chain and the canonical seam homotopy.

## Narrow result

\[
\boxed{
\text{The scalar logarithmic }C_9\text{ coefficient system has no
absolute seam obstruction, but it has a canonical relative-boundary
transgression.}
}
\]

This does not prove that the physical contour activates the transgression.  The next finite falsifier is to derive the actual \(C_9\) relative boundary from the frozen contour packet and pair it with \(H_\mu\), retaining cyclic occurrence labels and orientations.  If that pairing vanishes, scalar coefficients close the seam lane.  If it survives, its support and cyclic character must be computed before physical interpretation.

## Verification

- `research/benincasa/checkers/c9_seam_logarithmic_homotopy.py`
- `research/benincasa/results/c9-seam-logarithmic-homotopy.json`

Result SHA-256:

`1ca09189316b2cc845569c6197b8a060e5d42b8cb421185a75799e903f6e3516`

Allocator claim: `seqclaim-f6748552b3f0dbb52631b489`.

Epistemic graph event: `ev-000000002708-2e158f95-98f3-4015-a67d-381bff9fb09f`.
