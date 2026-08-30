# 2295 — The Full Contact-Weighted Finite-\(q\) Observer Matrix Has Only the Existing Gram Rank Loss

## Restore the frozen contact coefficients

Entries 2216 and 2230 derive the contact-normal Gaussian response

\[
-8\operatorname{diag}(C_{12},C_{23},C_{31}).
\]

Entries 2272–2281 derive the finite-\(q\) scalar-plus-tensor adapter \(T(q)\)
for the spectral Gaussian source.  The complete contact-packet observer map is
therefore

\[
\boxed{
R_{\rm ct}(q)
=-8\operatorname{diag}(C_{12},C_{23},C_{31})T(q).
}
\]

This is source multiplication in the labelled occurrence basis; no row
projector or post-hoc normalization is chosen.

## Full determinant

\[
\det R_{\rm ct}(q)
=(-8)^3C_{12}C_{23}C_{31}\det T(q).
\]

Each contact coefficient is a reciprocal shifted-energy product.  Entries
2177 and 2223 prove that it has no finite affine zero.  Hence contact weighting
does not add a finite rank-loss locus.

Combining with Entry 2281 gives

\[
\boxed{
\operatorname{rank}R_{\rm ct}(q)<3
\iff
q\cdot(p_1\times p_2)=0
}
\]

on the finite positive-energy source chamber.

## Support classification

- \(C_e\) poles are the existing shifted contact-energy divisors;
- \(C_e\to0\) occurs only at contact infinity and is recovered on the score
  Cartier grade by Entries 2224–2225;
- the only finite rank loss is the existing Gram/projection wall;
- no independent Landau or new Carrier factor occurs in the determinant.

Thus the angular transfer theorem applies to the actual contact packet, not
only to an abstract three-dimensional adapter.

## Verification

`research/benincasa/checkers/contact_weighted_finite_q_observer.rs` verifies
the determinant identity on 8,000 exact nonzero contact/weight packets.
