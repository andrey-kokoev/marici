---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2143 — The All-Deleted Contact Product Has Rank-One Mixed Variation

## Correction

Entries 2137--2138 and 2142 treated the isolated contacts in the all-deleted
graph as additive sectors. This contradicts the frozen source.

Equation (2.14) of Benincasa--Dian, arXiv:2401.05207, sums over edge-deletion
subsets and states explicitly that the unique \(j=n_e\) term is a **product
of contact graphs**. Equation (2.30) displays the same rule for the bubble:
the both-edges-deleted term has the product denominator

\[
y_ay_b(x_1+y_a+y_b)(x_2+y_a+y_b).
\]

Thus the three contacts inside the triangle's all-deleted term multiply.

## Correct two-wall local system

Near \(\nu_i=\nu_j=0\), retain

\[
(1,\tau_i)\otimes(1,\tau_j)
=
(1,\tau_i,\tau_j,\tau_i\tau_j),
\qquad
\tau_k=(2\pi i)^{-1}\log\nu_k.
\]

The variation operators satisfy

\[
V_i(\tau_i\tau_j)=\tau_j,
\qquad
V_j(\tau_i\tau_j)=\tau_i,
\]

and hence

\[
\boxed{
V_iV_j(\tau_i\tau_j)
=V_jV_i(\tau_i\tau_j)
=1.
}
\]

Therefore

\[
\boxed{\operatorname{rank}(V_iV_j)=1.}
\]

## Comparison with the lower square-free packet

The lower Kummer line \(\sqrt{\nu_i\nu_j}\) also has rank-one iterated
variation, although with semisimple characters rather than logarithmic
unipotent monodromy. Equality of ranks does not construct a comparison map,
but the previous rank obstruction is gone.

The source has supplied exactly the operation that Entries 2137--2142
incorrectly declared absent:

\[
\boxed{
\text{disconnected component product}
\longrightarrow
\text{canonical mixed nearby variation}.}
\]

## Corrected classification

- carrier: existing labelled deletion sector and component incidence;
- source operation: product of connected-component contact factors;
- two-normal mixed variation: rank one;
- lower-sector comparison: newly admissible but not yet constructed;
- \(\mathcal Q\): not implicated;
- new carrier datum: none.

## Evidence

- Benincasa--Dian, arXiv:2401.05207, equations (2.14), (2.30), and (4.71);
- Entries 2112, 2135--2142;
- `research/benincasa/checkers/contact_product_mixed_variation.rs`;
- allocator claim `seqclaim-112bb3f891c08a460a090552`.

## Next falsifier

Construct the labelled comparison between the rank-one mixed variation line
of the contact-product tensor system and the lower Kummer line. Preserve
their distinct unipotent and semisimple monodromies. Determine whether a
source-derived associated-grade or Mellin/Leray operation intertwines them;
rank equality alone is insufficient.
