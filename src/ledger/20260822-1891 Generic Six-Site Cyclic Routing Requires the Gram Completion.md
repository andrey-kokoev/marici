# Entry 1891 — Generic Six-Site Cyclic Routing Requires the Gram Completion

## Frozen question

Does the full-rank opposite-pairing deformation used in Entries 1886–1888
support the three-chart cyclic descent required by Entry 1889 before taking
the homogeneous Gram limit?

No additional carrier cells or fitted transition maps are admitted.

## Generic labelled cover

Let the four routing vectors be

\[
r_i=p_1+\cdots+p_i,\qquad i=1,\ldots,4,
\]

and let

\[
q_5=p_1+\cdots+p_5.
\]

For the cyclic pairing deformation with opposite pairing (k), the routing
Gram determinant is

\[
\det H(k)=-\frac14 k(6+7k).
\]

Thus the routing chart is full rank away from (k=0,-6/7).  Retaining the
four routing coordinates \(\alpha_i\), the six source-labelled quadratic
cover equations were exported before imposing the triple wall.  Their
wall pullback reproduces the two generic equations in
\((x,v,w,z,k)\) used by the earlier critical calculation.

## Failed unrestricted chart transport

The sixth vertex is not generically contained in the routing four-plane.
Its exact normal square is

\[
q_5^2-b^T H^{-1}b
=
-\frac{4k(k-3)(2k+3)}{6+7k}.
\]

Consequently, changing the routing origin by two sites changes the ambient
four-plane unless this expression vanishes.  A direct attempt to transport
all six cover equations without imposing this condition fails.  Therefore
the three chartwise Cartier components from Entry 1889 do **not** form a
generic cyclic routing atlas over the unrestricted one-parameter family.

This is a geometric obstruction, not a coordinate-normalization defect.

## Gram-completed atlas

Set the sixth-vertex normal square to zero before chart transport.  Equivalently,
replace the sixth vertex by its canonical (H(k))-projection while retaining
all four source pairings (b_i=r_i\mathbin\cdot q_5).  On this four-dimensional
Gram-completion locus, the three charts based at vertices (1,3,5) have
source-derived affine transitions

\[
\alpha=o_s+T_s\beta.
\]

All three transition determinants are nonzero on their stated generic loci.
Direct substitution verifies all six labelled squared-distance equations in
each chart:

\[
3\text{ charts}\times6\text{ equations}=18
\]

exact zero identities over \(\mathbb Q(k)\).

Hence

\[
\boxed{
\text{the cyclic routing atlas exists on the Gram completion, but not on
the unrestricted generic normal family.}
}
\]

## Interpretation

Entry 1889's length-six descended Cartier object is naturally attached to
the Gram-completed coefficient geometry.  Its cyclic descent cannot yet be
promoted to a generic off-Gram coefficient family.  This updates the prior
toward a Gram-supported Cartier excess, but does not settle the question:
a generic divisor may still exist chartwise and specialize to that excess.

## Next falsifier

Compute the full chartwise critical ideal of the unspecialized wall equations,
saturate by

\[
k(6+7k),\quad xvwz,
\]

and the source wall-multiplier factors, and eliminate (x,v,w).  Only after
that chartwise elimination should its components be compared on the
Gram-completion locus.

## Durable verification

- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_symmetric_landau.rs`
- `research/benincasa/marici-gm/src/bin/six_site_disjoint_pair_triple_labelled_atlas.rs`
- `research/benincasa/results/six-site-disjoint-pair-triple-symmetric-landau.json`
- `research/benincasa/results/six-site-disjoint-pair-triple-labelled-atlas.json`
- allocator claim: `seqclaim-d85f4e013985f1f4c93a9b96`
- epistemic event: `ev-000000002253-21697771-c0cc-4e32-8dac-84077f35b94e`
