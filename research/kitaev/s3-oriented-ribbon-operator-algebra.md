# The oriented fixed-ribbon operator algebra for `D(S3)`

Owner: `marici.Kitaev`

## Bounded question

Does freezing local ribbon orientation already produce a nontrivial exact
operator theorem before the full fusion category is constructed?

Yes.  Fix a directed ribbon `tau` and use the locally clockwise/counterclockwise
convention of Jia et al., arXiv `2105.08202`, Proposition 3.2.  For
`H=C[S3]` and delta functions `delta_g` in `H*`, write the 36 basis operators

\[
F_L(h,g)=F^{h,\delta_g}(\tau_L),\qquad
F_R(h,g)=F^{h,\delta_g}(\tau_R).
\]

The source multiplication specializes exactly to

\[
F_L(h_1,g_1)F_L(h_2,g_2)
=\delta_{g_1,g_2}F_L(h_1h_2,g_1),
\]

\[
F_R(h_1,g_1)F_R(h_2,g_2)
=\delta_{g_1,g_2}F_R(h_2h_1,g_1).
\]

Thus each orientation gives six orthogonal six-dimensional group-algebra
blocks.  The unit is `sum_g F(e,g)`.  The two oriented presentations are
intertwined by

\[
\Phi(F_L(h,g))=F_R(h^{-1},g).
\]

This is an orientation-sensitive isomorphism; merely retaining ribbon support
without orientation omits the inversion needed to compare the products.

## Exact non-Abelian witness

In the `g=e` block, take `h_1=(01)` and `h_2=(12)`.  The clockwise product
has group label `(012)`, while the counterclockwise product has `(021)`.
They differ because `S3` is non-Abelian.  The same support and ordered pair of
labels therefore do not determine multiplication until local orientation is
typed.

For an Abelian group the two orderings coincide, so this obstruction is
genuinely non-Abelian rather than a notational duplication.

## Carrier and coefficient allocation

Carrier geometry must retain ribbon direction, local clockwise/counterclockwise
orientation, ordered endpoints, and concatenation.  The coefficient lens
supplies `C[S3]`, delta-function labels, multiplication, inverse, and the
operator representation.  Orientation is geometric; the correction map
`h -> h^-1` is coefficient-valued.  Neither side alone types `Phi`.

## Verification

`python research/kitaev/checkers/check_s3_oriented_ribbon_algebra.py`
enumerates all 36 basis elements, checks associativity over all `36^3`
ordered triples in both orientations, verifies the unit and six orthogonal
block idempotents, checks `Phi` on all `36^2` basis pairs, and exhibits the
opposite three-cycle products.  Seven aggregate gates pass.

## Claim boundary and falsifiers

This is the algebra on one fixed open ribbon.  It is not the anyon fusion
ring, does not decompose endpoint excitation spaces into irreducible
`D(S3)` sectors, and supplies no associator, `F`-matrix, `R`-matrix, pentagon,
or hexagon.

The result is falsified by a failure of associativity, a basis dimension other
than 36, nonorthogonal `g` blocks, failure of `Phi` to intertwine, or equality
of the two displayed `S3` products.

Primary source boundaries: [Kitaev's original quantum-double construction](https://arxiv.org/abs/quant-ph/9707021)
introduces the finite-group ribbon algebra; [Jia et al.](https://arxiv.org/abs/2105.08202)
distinguish locally clockwise and counterclockwise ribbons and give the two
opposite multiplication laws; [Cowtan and Majid](https://arxiv.org/abs/2107.04411)
type open-ribbon excitation spaces as `D(G)` bimodules.  The present finite
specialization derives only what is stated above.
