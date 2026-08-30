# 1735 — A Degenerating Measurement Requires Its Projective Tangent Jet

## Degenerate-readout falsifier

Fix \(|\psi\rangle=e_1\) and a normalized measurement family

\[
|m_\varepsilon\rangle
=\frac{e_0+\varepsilon(ae_1+be_2)}
{\sqrt{1+\varepsilon^2(a^2+b^2)}}.
\]

At \(\varepsilon=0\), the limiting measurement line is normalized and
orthogonal to the state:

\[
\langle m_0|\psi\rangle=0.
\]

## Supported probability

The exact Born probability is

\[
\boxed{
p_\varepsilon
=\frac{\varepsilon^2a^2}
{1+\varepsilon^2(a^2+b^2)}.
}
\]

Therefore

\[
\operatorname{gr}^{(1)}_\varepsilon p=0,
\qquad
\operatorname{gr}^{(2)}_\varepsilon p
=a^2=|\langle v|\psi\rangle|^2,
\]

where \(v=ae_1+be_2\) is the measurement tangent.

Different projective tangents \([a:b]\) have the same normalized endpoint but
different supported readouts.  Reparameterization
\(\varepsilon\mapsto q\varepsilon\) also rescales the second coefficient by
\(q^2\).  Endpoint Born normalization fixes neither datum.

## Narrow result

Joint normalization of the limiting state and measurement does not determine
the supported zero-overlap limit.  A canonical scalar requires the source to
specify the projective measurement tangent and its parameter normalization,
equivalently the second probability jet.

The exceptional datum belongs to the readout coefficient family over the
existing measurement incidence.  No new Cut carrier stratum is required.

## Durable artifacts

- `research/benincasa/checkers/degenerate_measurement_second_jet.rs`
- `research/benincasa/results/degenerate-measurement-second-jet.json`
- `research/benincasa/degenerate-measurement-second-jet.md`

## Next falsifier

Equip projective measurement space with its source-derived Fubini–Study metric
and normalize the tangent to unit speed.  Test whether this removes the radial
jet ambiguity while preserving a direction-dependent, gauge-invariant
supported Born coefficient.
