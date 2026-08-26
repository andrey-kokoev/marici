# Finite counterterm authority audit

## Question

Does the finite-time one-loop toy source select a unique finite point in the
rank-three boundary response object, or only a point relative to a bulk
renormalization scheme?

## Frozen primary-source data

The immutable source is Collins--Holman--Vardanyan, arXiv:1408.4801,
`paper.tex` lines 330--355 and 382--428.

The source introduces three local quadratic counterterms. Their contributions
to the late-time basis

\[
(1,p^2\eta^2,p^4\eta^4)
\]

have shape vectors, up to independent nonzero source normalizations,

\[
v_1=(1,-1,0),\qquad
v_2=(-3,-1,0),\qquad
2v_3=(-5,-5,-2).
\]

The source fixes only the infinite parts of their coefficients. It then writes
the renormalized loop in terms of unspecified finite parts
\(I_0^f,I_2^f,I_4^f\). At finite initial time it requires every divergent or
finite oscillatory endpoint term to cancel so that the result matches that
chosen renormalized Bunch--Davies correlator.

The repeated `c_3` label in the third source equation is the source-internal
typo already corrected by Entry 1536: it is the `c_1` coefficient.

## Exact scheme-orbit calculation

After clearing the harmless factor of two, the finite-counterterm response map
is

\[
M_{\rm fin}=
\begin{pmatrix}
2&-6&-5\\
-2&-2&-5\\
0&0&-2
\end{pmatrix}.
\]

Its determinant is

\[
\det M_{\rm fin}=32.
\]

Thus finite local counterterms act transitively on the complete rank-three
linear response space. Quotienting unrestricted finite scheme freedom leaves
no nonzero linear response coordinate.

## Narrow result

The source matching condition canonically fixes the initial boundary
counterterm relative to a chosen bulk-renormalization point. It does not select
that bulk point. Therefore the source defines an affine family of matched
finite-time states, not one absolute finite readout.

This is not a new Carrier defect. The Carrier and coefficient object are
already closed. The missing datum is a renormalization condition selecting a
section of the full finite-scheme orbit. Hadamard admissibility may constrain
such a section, but response-space closure alone cannot.

## Scope

This proves underdetermination only for the abbreviated one-vertex toy model
and only when all three admitted finite local counterterms remain free. It does
not prove that a complete inflationary theory lacks physical normalization
conditions, nor that nonlinear or nonlocal scheme invariants are absent.

## Verification

- `research/benincasa/checkers/finite_counterterm_scheme_orbit.rs`
- `research/benincasa/results/finite-counterterm-scheme-orbit.json`
- exact determinant and rank over the integers
