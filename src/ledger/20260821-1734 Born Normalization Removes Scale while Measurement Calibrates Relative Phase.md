# 1734 — Born Normalization Removes Scale while Measurement Calibrates Relative Phase

## Normalized-pairing test

Use the normalized two-path state and rank-one measurement

\[
|\psi_\theta\rangle
=\frac{|0\rangle+e^{i\theta}|1\rangle}{\sqrt2},
\qquad
|m_\phi\rangle
=\frac{|0\rangle+e^{i\phi}|1\rangle}{\sqrt2}.
\]

Both are source-normalized unit vectors.

## Born scalar

Their measurement probability is

\[
\boxed{
p_{\theta,\phi}
=|\langle m_\phi|\psi_\theta\rangle|^2
=\frac{1+\cos(\theta-\phi)}2.
}
\]

Independent global phase changes of \(|\psi\rangle\) and \(|m\rangle\) multiply
the overlap by a unit phase and leave \(p\) invariant.  The checker verifies
this exactly on \(\mathbb Z_4\subset U(1)\).

## What is fixed

Born normalization removes the positive radial rescaling from Entry 1733's
\(\mathbb C^\times\)-torsor.  The observable still depends on the relative
phase \(\theta-\phi\), but the source-specified measurement operator supplies
the calibration \(\phi\).  Neither \(\theta\) nor \(\phi\) is an absolute
observable separately.

## Narrow result

A normalized state plus a normalized labelled measurement operator produces a
canonical Born scalar.  The remaining phase is relational and calibrated by
the physical readout.  This realizes the paired-runtime principle explicitly:
the amplitude coefficient obtains operational meaning only together with its
typed measurement.

No new Cut carrier stratum is required.

## Durable artifacts

- `research/benincasa/checkers/born_normalized_interference.rs`
- `research/benincasa/results/born-normalized-interference.json`
- `research/benincasa/born-normalized-interference.md`

## Next falsifier

Let the measurement projector itself degenerate so its calibrated overlap
vanishes.  Test whether joint state–measurement normalization produces a
canonical supported limit or again leaves a projective relative direction.
