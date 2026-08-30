# 2902 — The Additive Marked Route Cocycle Is Globally Nonexact

## Exactness question

Entry 2897 proved that the two marked route corrections commute.  The next
question is whether one source-normalized, single-valued meromorphic affine
primitive can remove both corrections globally.

## Route one-forms

For the \(x=1\) occurrence, let

\[
B=\frac{3-\kappa}{(1-\kappa)^2}.
\]

Entry 2892 gives the simple-pole residues

\[
\operatorname{Res}_{\xi=-\kappa}(R_1\,d\xi)
=\frac{B}{64p^4},
\qquad
\operatorname{Res}_{\xi=-1}(R_1\,d\xi)
=-\frac{B}{64p^4}.
\]

For the \(x=-3\) occurrence,

\[
R_{-3}
=
-\frac{1}{64p^4(\xi+1)(\kappa-\xi)},
\]

so

\[
\operatorname{Res}_{\xi=\kappa}(R_{-3}\,d\xi)
=\frac{1}{64p^4(1+\kappa)},
\qquad
\operatorname{Res}_{\xi=-1}(R_{-3}\,d\xi)
=-\frac{1}{64p^4(1+\kappa)}.
\]

## Obstruction

The derivative of a single-valued rational or meromorphic affine gauge has
zero residue at every pole.  Both labelled route directions instead have
nonzero generic residues.  Their local primitives necessarily contain
logarithms.

For generic \(\kappa\), the marked supports \(\xi=-\kappa\) and
\(\xi=+\kappa\) are distinct.  Consequently the two labelled Kummer classes
cannot cancel each other under one scalar gauge.

## Result

The additive marked route cocycle is globally nonexact in the admitted
single-valued meromorphic category.  Local logarithmic primitives exist, but
no global source-normalized affine splitting removes both translations.

Thus the route packet is not presentation data.  It is intrinsic relative
readout information:

- its compact elliptic projection is zero;
- its source occurrence readout is nonzero;
- its composition is abelian;
- its global Kummer cohomology class is nonzero.

No new carrier divisor is required.  The obstruction lives in the coefficient
and readout layer over existing marked support.

## Next falsifier

Compute the source-selected monodromy representation of this rank-two Kummer
class and test whether the physical soft observable depends only on its
cohomology class or also on the chosen pointed normalization.

## Durable artifacts

- `research/benincasa/check_soft_marked_route_cocycle_nonexact.py`
- `research/benincasa/soft-marked-route-cocycle-nonexact.json`
