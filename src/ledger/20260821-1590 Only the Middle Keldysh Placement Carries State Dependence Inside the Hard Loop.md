# 1590 — Only the Middle Keldysh Placement Carries State Dependence Inside the Hard Loop

## Type refinement of Entry 1589

The three statistical placements

\[
F_LA_MA_R,qquad R_LF_MA_R,qquad R_LR_MF_R
\]

do not have the same momentum variance in the source one-loop graph.

The left and right factors are external Dyson legs at observed momentum
(p).  The middle factor is the self-energy containing loop momenta

\[
q,qquad k=|p-q|.
\]

Hence only (F_M) places state dependence inside the hard loop.  The outer
placements multiply the ordinary Bunch--Davies self-energy by an external
state variation and belong to vacuum renormalization acting on that leg.

## Internal occurrence resolution

The middle statistical variation has two labelled internal occurrences,

\[
q\quad\text{and}\quad k.
\]

They may be identified only after deriving the source
(q\leftrightarrow k) symmetry and preserving the integration orientation.

## Raw ultraviolet grade

For simultaneous (q\sim k\sim Q), the source data give

\[
d^3q:\ +2,
\qquad
(p^2+q^2+k^2)^2:\ +4,
\qquad
G_qG_k:\ -2.
\]

Therefore the raw radial integrand has degree

\[
\boxed{4.}
\]

The source Hadamard condition (eta_Q=o(Q^{-2})) lowers the middle
state-dependent grade strictly below (2).

No convergence claim follows yet: time primitives, endpoint terms,
subtractions, and counterterms remain to be included.

## Consequence

The next Hadamard audit is one middle-self-energy calculation with two
internal occurrence labels, not three symmetric Dyson-placement audits.

This is a coefficient-filtration question over the existing contour carrier.

## Artifacts

- `research/benincasa/keldysh-uv-responsibility-split.md`
- `research/benincasa/checkers/keldysh_uv_responsibility_split.rs`
- `research/benincasa/results/keldysh-uv-responsibility-split.json`

Ledger sequence claim: `seqclaim-de80afe4fc079a4cc0441afc`.
