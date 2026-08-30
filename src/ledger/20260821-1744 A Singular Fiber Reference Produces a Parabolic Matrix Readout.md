# 1744 — A Singular Fiber Reference Produces a Parabolic Matrix Readout

## Singular-reference test

Let the labelled reference frame degenerate as

\[
F_\varepsilon=\operatorname{diag}(1,\varepsilon).
\]

For a fiber holonomy matrix \(H=(h_{ij})\), Entry 1743's readout is

\[
\boxed{
F_\varepsilon^{-1}HF_\varepsilon
=
\begin{pmatrix}
h_{11}&\varepsilon h_{12}\\
\varepsilon^{-1}h_{21}&h_{22}
\end{pmatrix}.
}
\]

## Forced parabolic weights

The two reference columns have source valuations \((0,1)\).  Therefore the
four Hom entries have forced weights

\[
(0,1,-1,0).
\]

The upper off-diagonal entry survives after dividing by its positive Rees
factor \(\varepsilon\).  The lower entry is represented in the negative
parabolic grade by multiplying its pole by \(\varepsilon\).  Both operations
are derived from the source frame valuations, not selected after inspecting
\(H\).

Thus the parabolic packet recovers

\[
(h_{11},h_{12},h_{21},h_{22})
\]

exactly.  In particular, Entry 1741's \(AB\) and \(BA\) remain distinct in the
two shifted off-diagonal grades.

## Narrow result

Ordinary specialization of a singular reference is insufficient: one matrix
entry vanishes and the opposite entry develops a pole.  The source-derived
parabolic/Rees Hom lattice retains the full based holonomy without a post hoc
splitting.

This is coefficient/readout filtration data over the existing carrier; no new
Cut stratum is required.

## Durable artifacts

- `research/benincasa/checkers/singular_reference_parabolic_readout.rs`
- `research/benincasa/results/singular-reference-parabolic-readout.json`
- `research/benincasa/singular-reference-parabolic-readout.md`

## Next falsifier

Let two reference columns vanish at the same order so that the associated
graded frame loses their ordering.  Test whether a labelled flag suffices or a
noncanonical splitting reappears at the repeated-weight locus.
