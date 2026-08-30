# 1733 — Matched Holonomy Trivializes the Comparison Line but Not Its Generator

## Matched-reference test

Suppose the signal and reference amplitude lines satisfy

\[
T_L=T_R.
\]

Then Entry 1732's relative nearby monodromy is trivial:

\[
T_LT_R^{-1}=1.
\]

The nearby invariant space is therefore rank one.

## Remaining ambiguity

Topological triviality does not choose a nonzero flat generator.  If \(v\) is
one generator, then

\[
v\longmapsto qv,
\qquad q\in\mathbb C^\times,
\]

is another.  Thus the generator space is a \(\mathbb C^\times\)-torsor.

A fixed-coordinate functional \(\gamma\) gives

\[
\gamma(qv)=q\gamma(v),

\]

so it does not define a gauge-invariant scalar.  A genuine dual cycle must
transform as

\[
\gamma\longmapsto q^{-1}\gamma,
\]

after which

\[
\boxed{\langle q^{-1}\gamma,qv\rangle=\langle\gamma,v\rangle.}
\]

## Narrow result

Matched holonomy is necessary but not sufficient for a canonically normalized
physical pairing.  The source must additionally provide a covariant normalized
dual cycle, a Hermitian metric plus basepoint phase, or an integral/polarized
lattice.

This is the same normalization obstruction encountered for the cosmological
exceptional projective line.  No new carrier stratum is implicated.

## Durable artifacts

- `research/benincasa/checkers/matched_holonomy_normalization.rs`
- `research/benincasa/results/matched-holonomy-normalization.json`
- `research/benincasa/matched-holonomy-normalization.md`

## Next falsifier

Use normalized quantum states and a source-specified rank-one measurement
operator to derive the dual pairing.  Determine whether Born normalization
removes the \(\mathbb R_{>0}\) scale while leaving a relative \(U(1)\) phase
that must be calibrated by an interferometric basepoint.
