# 1736 — Fubini–Study Normalization Removes Measurement-Jet Speed but Not Direction

## Metric-normalization test

At the limiting measurement line \([e_0]\), write a transverse tangent as

\[
v=ae_1+be_2.
\]

The source-derived Fubini–Study metric gives

\[
\|v\|_{\rm FS}^2=a^2+b^2
\]

in this affine frame.  For the state \(|\psi\rangle=e_1\), Entry 1735's
supported second coefficient becomes, after unit-speed normalization,

\[
\boxed{
c_{\rm FS}([v])
=\frac{|\langle v|\psi\rangle|^2}{\langle v|v\rangle}
=\frac{a^2}{a^2+b^2}.
}
\]

## Invariances

For every nonzero scalar \(q\),

\[
c_{\rm FS}([qv])=c_{\rm FS}([v]).
\]

Central phase also cancels between numerator and denominator.  Thus the metric
removes both parameter-speed rescaling and amplitude gauge.

The value still varies with \([a:b]\).  Different projective tangent
directions at the same normalized endpoint produce different supported Born
coefficients.

## Narrow result

Fubini–Study geometry canonically removes the radial measurement-jet ambiguity
but cannot infer the projective tangent from endpoint data.  A physical
supported limit therefore requires:

1. the source measurement path, which supplies \([v]\);
2. the Fubini–Study metric, which fixes its speed normalization;
3. the normalized state, which evaluates the directional coefficient.

This is a typed coefficient/readout construction over the existing carrier;
no new Cut stratum is needed.

## Durable artifacts

- `research/benincasa/checkers/fubini_study_tangent_normalization.rs`
- `research/benincasa/results/fubini-study-tangent-normalization.json`
- `research/benincasa/fubini-study-tangent-normalization.md`

## Next falsifier

Move around a loop in projective measurement directions and test whether the
Fubini–Study-normalized supported coefficient has Berry holonomy or descends
as a scalar function on projective tangent space.
