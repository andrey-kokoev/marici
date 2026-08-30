# Provenance-carrying exact lifts for the Cayley--Menger packet

## Missing datum

The previous reducer returned only a normal-form remainder. It discarded how
that remainder was obtained from the four original exact generators:

1. the logarithmic-gradient relation in \(a\);
2. the logarithmic-gradient relation in \(b\);
3. the logarithmic-gradient relation in the auxiliary fiber coordinate;
4. the localization relation \(zK-1\).

Consequently, independently reduced fibers had no shared primitive packet that
could be differentiated coherently.

## Constructor

Each Gröbner basis element now carries a four-component polynomial provenance
vector. Every Buchberger operation—monic normalization, S-polynomial
formation, and reduction—updates the polynomial and provenance together.

For a class representative \(f\), exact reduction returns

\[
f=r+\sum_{i=1}^4 q_i g_i,
\]

where \(r\) is the canonical remainder, \(g_i\) are the original exact
generators, and the \(q_i\) are retained primitive coefficients.

The implementation verifies this identity coefficientwise for every derived
basis element and every class reduction.

## Finite verification

For the complete sixteen-class normal-plus-cyclic packet:

- the source exact-generator count is four;
- the tracked and untracked Gröbner bases agree termwise and have 36 elements;
- all sixteen tracked remainders equal the previous remainders;
- all sixteen source representatives reconstruct exactly from remainder plus
  trace;
- the packet retains fiberwise rank four.

At A, B, and HOMA, with independent-prime replication at A, the primitive
packet has 64 nonzero components and 3514 or 3515 polynomial terms.

## Scope

This constructs the previously missing exact-lift provenance. It does not yet
construct a flat connection. The next step is to differentiate the primitive
coefficients and the four source exact generators as one typed packet. Mixed
flatness remains the acceptance gate.

## Artifacts

- `research/benincasa/checkers/check_cm_exact_lift_provenance.py`
- `research/benincasa/results/cm-exact-lift-provenance.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

