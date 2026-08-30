# 1746 — A Rotating Second Jet Defines a Parabolic Local System

## Source-derived flag

At the rank-deficient locus of Entry 1745, labelled occurrence subtraction
produces a line and quotient

\[
L_1\subset V,
\qquad L_2=V/L_1.
\]

On overlaps, every transition preserving this source flag has the form

\[
P=\begin{pmatrix}\sigma_1&a\\0&\sigma_2\end{pmatrix},
\qquad \sigma_i\in\{\pm1\}.
\]

The shear (a) depends on the local lift of (L_2). It vanishes from the
associated-grade transition:

\[
\operatorname{gr}P=\operatorname{diag}(\sigma_1,\sigma_2).
\]

Consequently the endomorphism grades have characters

\[
\boxed{(1,\sigma_1\sigma_2,\sigma_1\sigma_2,1).}
\]

The off-diagonal grades retain exactly the relative line holonomy. A common
sign ((\sigma_1,\sigma_2)=(-1,-1)) is central and therefore invisible on
endomorphisms, while opposite signs produce nontrivial off-diagonal
monodromy.

## Narrow result

The complete labelled second jet canonically defines a parabolic local
system. It does not canonically define one globally fixed scalar matrix:
local matrices glue by parabolic conjugation unless an independent frame
trivialization is supplied.

No local Smith basis is chosen. The flag comes from the labelled source
occurrences, and the associated-grade monodromy is independent of the
lift-dependent shear.

This is again coefficient/readout structure over the existing carrier, not a
new Cut incidence stratum.

## Durable artifacts

- `research/benincasa/checkers/rotating_second_jet_flag.rs`
- `research/benincasa/results/rotating-second-jet-flag.json`
- `research/benincasa/rotating-second-jet-flag.md`

## Next falsifier

Replace the split sign transport by a genuinely unipotent parabolic loop.
Test whether its shear is an intrinsic extension class of the filtered
reference local system or can be removed by a globally regular change of
lift.
