# Fixed-arrangement canonical-form uniqueness in polygon dimension

## Question

Does the five-point numerator-divisibility proof extend to a fixed polygon-channel hyperplane arrangement in dimension `d=n-3`?

## Claim boundary

The theorem assumes positive dimension, a fixed reduced collection of distinct affine hyperplanes, rational top forms with at most simple poles on their projective closures, equal normal-first residues, and no pole along the projective infinity divisor. It proves uniqueness, not existence or source selection.

Let the arrangement have `F` facets and write the difference of two candidate top forms as

\[
\eta=\frac{N(x_1,\ldots,x_d)}{Q(x)}
 dx_1\wedge\cdots\wedge dx_d,
\qquad Q=\prod_{i=1}^{F}a_i.
\]

In a projective infinity chart, affine volume contributes order `z^(-(d+1))`, `Q` contributes `z^(-F)`, and a degree-`m` numerator contributes `z^(-m)`. Absence of an infinity-divisor pole therefore requires

\[
m\le F-d-1.
\]

Equality of facet residues makes the residue of `eta` zero at the generic point of every divisor. With simple poles, this means each distinct irreducible `a_i` divides `N`. Reducedness makes their product divide `N`, so any nonzero `N` has degree at least `F`. Since `F-d-1<F`, no such numerator exists and `eta=0`.

For polygon channels, `F=n(n-3)/2` and `d=n-3`. The exact census for `n=4..7` gives degree bounds `0,2,5,9` versus divisibility lower bounds `2,5,9,14`; the contradiction gap is always `d+1`. These stages check the arithmetic only and do not establish the generic theorem by finite sampling.

The affine volume form is the deliberate rival: it has no facet poles and hence zero facet residues, but its projective infinity pole has order `d+1`. At `n=3`, dimension and facet count are both zero, so residue recursion cannot fix the normalization of the point form; that base value is separate input.

## Disposition

Fixed-arrangement uniqueness holds in every positive dimension under the stated divisor and pole assumptions. This supplies no reverse arrow from the unique form to a source-selected arrangement, supports, residue data, or physical normalization.
