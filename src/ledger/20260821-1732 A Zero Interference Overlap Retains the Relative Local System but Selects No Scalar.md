# 1732 — A Zero Interference Overlap Retains the Relative Local System but Selects No Scalar

## Supported-overlap falsifier

Let the labelled interference section from Entry 1731 vanish at a boundary as

\[
c(s)=s^m v,
\qquad m\in\mathbb Z_{>0},
\]

where

\[
v\in L\otimes R^*.
\]

The associated Rees grade retains \(v\) on the overlap-zero support.

## Nearby monodromy

The factor \(s^m\) has monodromy

\[
e^{2\pi i m}=1.
\]

Hence it does not cancel or modify the relative flat holonomy:

\[
\boxed{
T_{\rm nearby}=T_L T_R^{-1}.
}
\]

For a nontrivial one-dimensional relative twist over the generic coefficient
field, \(T_{\rm nearby}-1\) is invertible.  Therefore

\[
\ker(T_{\rm nearby}-1)=0,
\qquad
\operatorname{coker}(T_{\rm nearby}-1)=0.
\]

The exact checker verifies this for every nontrivial element of
\(\mathbb Z_4\subset U(1)\) and vanishing orders one through thirty-two.

## Narrow result

The supported nearby-cycle costalk exists and retains the relative comparison
line, but a zero overlap does not automatically select a global physical
scalar.  A nonzero observable still requires a matching source cycle,
reference twist, or trace that cancels the monodromy.

This repeats a central cosmological lesson: supported coefficient data is not
equivalent to physical activation.  No new Cut carrier stratum is required.

## Durable artifacts

- `research/benincasa/checkers/zero_overlap_relative_nearby_cycle.rs`
- `research/benincasa/results/zero-overlap-relative-nearby-cycle.json`
- `research/benincasa/zero-overlap-relative-nearby-cycle.md`

## Next falsifier

Supply a compensating reference twist with \(T_R=T_L\) and a labelled relative
cycle.  Test whether the monodromy-cancelled costalk pairs canonically or still
depends on normalization of the reference current.
