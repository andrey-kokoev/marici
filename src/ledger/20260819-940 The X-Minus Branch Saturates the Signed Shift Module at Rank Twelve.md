# 940 — The X-Minus Branch Saturates the Signed Shift Module at Rank Twelve

## Frozen branch comparison

Entry 939 left two opposite-target copies unconstructed.  The test is made on
the same (A_4/Y/Q) Rees chart, now on the signed sheet

\[
A_4=1,\qquad X=-1,\qquad Y=1,\qquad Q=1.
\]

Because (Q=XYZ), this sheet forces (Z=-1).  The diagonal branch is
therefore regularized by (Z+1), while the independently derived
off-diagonal branch retains its source-derived (U) regularization.

## Exact result

The diagonal branch has twelve nonzero entries and target character

\[
(1,1).
\]

The off-diagonal branch has six nonzero entries and target direction

\[
(0,1).
\]

Their six-component source rows are projectively equal: every source
(2\times2) minor vanishes.  Their target minor is nonzero.  Thus the same
new (X=-1) source line occurs in two independent target directions.

Applying the two pair-shift characters from Entry 931 supplies the
opposite-target copy of each of Entry 939's two new source directions.  Hence

\[
\boxed{
\operatorname{rank}R_{\rm source}^{\rm signed}=6,
\qquad
\operatorname{rank}M_{\rm signed}=2\cdot6=12.
}
\]

The former alternatives rank ten and rank eleven are rejected for this
resolved branch system.

## Narrow interpretation

The rank-twelve result is not an imposed tensor completion.  It is generated
by the diagonal and off-diagonal source branches on both (X)-sheets.  The
growth remains coefficient data over the already frozen root divisor

\[
A_4^2=X^2=Q^2=1.
\]

No new carrier stratum is indicated.

## Next falsifier

Determine whether the rank-twelve signed module carries a canonical
reflection-compatible integral lattice, or only the rational source basis
currently computed.  Derive the lattice from residue orientations and source
normalizations; do not choose it by clearing denominators after the fact.

## Durable verification

- checker:
  `research/benincasa/marici-gm/src/bin/string_six_point_three_normal.rs`;
- packet:
  `research/benincasa/string-six-point-xminus-branches.json`;
- verified command:
  `cargo run --quiet --bin string_six_point_three_normal`;
- allocator claim:
  `seqclaim-b893f071ba059aa0bcc2427b`.
- epistemic event:
  `ev-000000000557-8ac98fe0-0183-4804-8b4f-c8c3d0312d50`.
