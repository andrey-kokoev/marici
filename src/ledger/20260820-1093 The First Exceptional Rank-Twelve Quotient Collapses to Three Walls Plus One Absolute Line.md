# 1093 — The First Exceptional Rank-Twelve Quotient Collapses to Three Walls Plus One Absolute Line

## Record

Entries 1090--1091 derived the joint Rees geometry at ((u,v)=(0,2)) and
closed its first marked-incidence test.  Applying the same source-normalized
Laurent reduction to the exceptional (p\neq0) chart now gives a stable
finite-field quotient.

Sequence claim: `seqclaim-fe8bccd177d7d0c9d0ecca7f`.

## Frozen exceptional reduction

Use

\[
s=\frac qp,
\qquad
K_E=\operatorname{in}_J(K)(1,s,A,B),
\]

with the strict-transform walls

\[
L_{1,E}=B-1,
\qquad
L_{2,E}=A+\frac{s-1}{2}.
\]

The twelve source classes and all four exact sectors retain the ordering and
primitive-degree-eight convention of the generic four-stratum reducer.

## Stable quotient rank

At generic (s=2,3,5), the exact ranks are

\[
\operatorname{rank}(d_E)=107,
\qquad
\operatorname{rank}(d_E+M_{12})=111.
\]

Therefore

\[
\boxed{
\dim M_{E}=111-107=4.
}
\]

The labelled rank increments are

\[
(1,1,1,0,0,0,1,0,0,0,0,0),
\]

so a source-ordered quotient basis is

\[
\boxed{
(\Omega_{111},\Omega_{101},\Omega_{110},e_4).
}
\]

The classes (e_1,e_2,e_3) vanish.  The six classes (e_4,\ldots,e_9)
span one absolute line; no individual absolute coordinate other than the
chosen source-ordered (e_4) representative is primitive-independent in the
unsaturated twelve-coordinate presentation.

## Reconstructed absolute line

Relative to ([e_4]), two independent 61-bit primes give identical rational
reconstructions:

\[
[e_5]
=
-\frac{24}{(s+3)(s^2+3)}[e_4],
\]

\[
[e_6]
=
\frac{12(s+1)^2}{(s-1)(s+3)(s^2+3)}[e_4],
\]

\[
[e_7]
=
-\frac{6(s+1)^2}{(s-1)(s^2+3)}[e_4],
\]

\[
[e_8]
=
-\frac{(s+1)^2(s+3)^2}
{2(s-1)(s^2+3)}[e_4],
\]

and

\[
[e_9]
=
-\frac{
s^6-2s^5+7s^4+24s^3+83s^2-6s+21
}{
5(s-1)(s+1)^2(s^2+3)
}[e_4].
\]

Each reconstruction used eighteen discovery directions and passed nine
unused directions at each prime.

## Deutsch--Popperian verdict

The conjecture that Rees normalization restores a generic rank-twelve
exceptional fiber is falsified in the tested finite models.  The normalized
associated grade is instead

\[
\boxed{
W_3\oplus L_{\rm abs},
}
\]

with three marked-wall classes and one absolute line.

This is not a new carrier rank.  It is a degeneration of the coefficient
object on the existing joint resolution.  The reconstructed pole set is

\[
(s-1)(s+1)(s+3)(s^2+3)=0,
\]

but no carrier interpretation is assigned until these factors are derived
from the exceptional branch/marked discriminant.

## Epistemic status

- quotient ranks: established in the two tested exact finite fields;
- rational formulas: replicated modular reconstruction with unused-point
  verification;
- characteristic-zero polynomial witness: not yet constructed;
- intrinsic pole support: not yet established;
- new carrier datum: unsupported.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- `research/benincasa/rank12-u0-v2-exceptional-line.json`;
- identical reconstruction over the primary and replication primes.

Epistemic graph admission:
`ev-000000000791-aaf2c965-6c36-41cb-836a-664cdca9a8e8`.

## Next falsifier

Derive the exceptional discriminant and marked collision resultants directly
from (K_E,L_{1,E},L_{2,E}).  Test whether every candidate pole factor

\[
s-1,\quad s+1,\quad s+3,\quad s^2+3
\]

belongs to existing branch or marked support.  A residual factor absent from
that frozen geometry would reject this absolute line as a complete
coefficient description; only a source-derived incidence factor could reopen
the carrier hypothesis.
