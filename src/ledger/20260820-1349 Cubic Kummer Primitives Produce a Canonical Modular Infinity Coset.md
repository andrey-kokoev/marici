# 1349 — Cubic Kummer Primitives Produce a Canonical Modular Infinity Coset

## Status

This is a multi-prime modular theorem candidate, not yet a characteristic-zero theorem.

Entry 1343 established the generic-rank gate and retracted the accidental quadratic closure. The same gate is now applied to cubic Kummer-resolved primitives.

## Cubic ansatz

\[
V_i
=
\sum_{S\subseteq\{1,\ldots,5\}}
P_{i,S}(u)y_S,
\qquad
\deg P_{i,S}\le3.
\]

The affine system has

\[
1+3\cdot32\binom{6}{3}
=
1921
\]

unknowns.

## Multi-prime rank scan

All nine tested fibers are consistent:

\[
\begin{array}{c|ccc}
&z=5&z=7&z=11\\
\hline
p=1019&1056&1152&1024\\
p=1021&1024&992&928\\
p=1031&576&800&768
\end{array}
\]

where entries are coefficient ranks.

Thus cubic consistency survives the maximal observed rank

\[
r_{\max}=1152.
\]

Unlike the quadratic case, no tested full-rank or higher-rank fiber is inconsistent.

## Boundary test at maximal observed rank

At

\[
(p,z)=(1019,7),
\]

append the complete sheet- and order-resolved radial infinity map from the surviving valuation packet.

The ranks are

\[
\operatorname{rank}A=1152,
\]

\[
\operatorname{rank}
\begin{pmatrix}
A\\
B_{\infty,\mathrm{rad}}
\end{pmatrix}
=
1921.
\]

Therefore

\[
\dim\ker A
=
1921-1152
=
769,
\]

and

\[
\operatorname{rank}
\left(
B_{\infty,\mathrm{rad}}|_{\ker A}
\right)
=
1921-1152
=
769.
\]

Hence the boundary map is injective on the entire affine gauge kernel.

The combined inhomogeneous system is inconsistent, so the affine boundary coset does not contain zero.

## Candidate mechanism

At the maximal tested modular rank, the derivative determines a canonical nonzero coset

\[
\boxed{
\beta_z
\in
\mathcal B_{\infty}
/B_{\infty}(\ker A),
\qquad
\beta_z\ne0.
}
\]

Different affine primitives have different boundary representatives, but all represent the same quotient class. This is the correct gauge-invariant object; no preferred primitive is chosen.

## What is established and what is not

Established computationally:

- cubic consistency at nine fibers across three primes;
- survival at maximal observed rank 1152;
- injectivity of the radial boundary map on the 769-dimensional affine kernel at that fiber;
- nonvanishing of the resulting modular boundary coset.

Not established:

- the characteristic-zero cubic affine identity;
- stability of rank 1152 as the generic rank;
- the dimension of the characteristic-zero boundary quotient;
- horizontality or a scalar Picard--Fuchs operator.

## Exact certification gate

A characteristic-zero theorem requires one of:

1. reconstruct a complete cubic primitive and verify all cleared identities exactly; or
2. construct a dual certificate for the quotient class \(\beta_z\) without reconstructing all 1921 coefficients.

The dual route is preferred if it can certify:

\[
\ell A=0,
\qquad
\ell\,\partial_z\Omega\ne0,
\]

with \(\ell\) factoring through the projective radial boundary quotient.

No physical or scalar interpretation is authorized before that gate.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_kummer_resolved_ibp_pilot.rs`
- `research/benincasa/results/five-site-asymmetric-kummer-degree3-census.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_infinity_deck_valuation.rs`
- `research/benincasa/results/five-site-asymmetric-infinity-deck-valuation.json`

Allocator claim: `seqclaim-eb55ad61dd77216cb5e8f19d`.
