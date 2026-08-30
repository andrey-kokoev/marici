# 1949 — The C9 Canonical Contour Freezes the Next Higher-Arity Carrier

## Predeclared test

Entry 1933 leaves a two-stage higher-arity falsifier:

1. derive a nontransverse companion fold from the next source graph;
2. test routing visibility before projecting the positive source-regulator cone.

The first admissible step is therefore to freeze the complete nine-site source carrier.  No fold or coefficient divisor is inferred at this stage.

## Frozen source object

Using Equations (3.8)--(3.11) and (4.1)--(4.3) of arXiv:2305.19686v2, take the cycle graph (C_9) with

\[
Y=(X_1,\ldots,X_9;y_1,\ldots,y_9)
\]

and the source-ordered three cosmological-polytope vertices per edge.  The resulting exact integer vertex matrix has shape

\[
18\times27
\]

and rank (18).  Its physical facets are exactly

\[
72\ \text{proper connected regions}
+9\ \text{spanning }G\setminus e\text{ facets}
+1\ \text{total-energy facet},
\]

for a total of (82).

## Source localization

The first source-ordered pivot basis contains (18) columns and has determinant

\[
\boxed{512}.
\]

It leaves nine unfixed contour variables, as required by the (27-18) dimension count.  Every localized affine denominator, regulator label, ambient orientation, and contour orientation is serialized without changing the source normalization

\[
\frac{1}{17!(2\pi i)^9}.
\]

All facet--vertex pairings are nonnegative.

## Canonical numerator

The exact implicit canonical numerator is

\[
N_{C_9}(Y)
=
\left(\prod_{f=1}^{82}q_f(Y)\right)\Omega_{C_9}(Y),
\]

where (Omega_{C_9}) is the oriented 27-variable contour pushforward fixed by the packet.  Its forced degree is

\[
82-18=64.
\]

No expanded polynomial, triangulation, companion fold, or physical activation is claimed.

## Narrow conclusion

\[
\boxed{
\text{The next higher-arity carrier is now frozen at }C_9.
}
\]

The next finite falsifier is to derive the smallest nontransverse companion fold from this frozen packet and then apply Entry 1933's ordered test:

\[
\text{routing visibility}
\longrightarrow
\text{positive-cone normal projection}.
\]

A fold activated despite failed routing visibility would falsify the carrier rule.  A visible fold with a new regulator chamber structure would enlarge only the sector-specific Betti calculus unless it also forces a new source incidence stratum.

## Verification

- `research/benincasa/checkers/nine_site_canonical_contour_packet.py`
- `research/benincasa/results/nine-site-canonical-contour-packet.json`

The checker was rerun twice with identical SHA-256 output

`82F44A9CE3612A0F1DEF24D728B93592A2EFDE239B0F67DA1B91B08FACB10D2D`.

Allocator claim: `seqclaim-cc38096754933649985f727d`.

Epistemic graph event: `ev-000000002425-23cba57e-62c6-4771-93cc-3b7afc8b688d`.
