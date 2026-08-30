# 1623 — The Source Cubic Momentum Channel Lands on the Statistical Axis of the Second-Rees Cone

## Frozen source component

For an observed momentum occurrence \(p\), retain the two ordered internal occurrences \((q,k)\), momentum conservation, and the finite-EFT domain.  Entry 1616 fixes the source production amplitude channelwise as

\[
A_{p;qk}=-i\bigl(H_{p;qk}-S_{p;qk}\bigr).
\]

The first-order state component is

\[
\int_{\mathcal D_\Lambda}d\Pi_{qk}\,
A_{p;qk}|1_p,1_q,1_k\rangle.
\]

## Reduced covariance map

Trace the two labelled internal occurrences.  Distinct momentum labels are orthogonal, so cross-channel interference vanishes.  Endpoint interference remains inside each channel.  Consequently,

\[
x_1(p)=0,
\qquad
y_1(p)=0,
\]

and

\[
\boxed{
n_2(p)
=
\int_{\mathcal D_\Lambda}d\Pi_{qk}\,
\left|H_{p;qk}-S_{p;qk}\right|^2.
}
\]

The anomalous first jet vanishes because its operator changes observed particle number by two, whereas the vacuum and cubic production component differ by three total quanta.

The ordered \((q,k)/(k,q)\) occurrence factor cancels the identical-pair \(1/2!\) channelwise, as in Entry 1617.  Entry 1618 supplies the positive symmetric finite-EFT measure.

## Result

The source cubic production channel lands on the statistical axis of the Gaussian second-Rees cone:

\[
\boxed{
n_2(p)-|\beta_1(p)|^2
=n_2(p)
\geq0.
}
\]

Saturation occurs exactly when

\[
H_{p;qk}=S_{p;qk}
\]

for almost every admitted internal channel.

Thus no interference term survives outside the positive labelled pairing.  The only destructive interference is the source-derived bulk/surface cancellation already contained in \(|H-S|^2\).

## Qualifications

The finite checker audits complex endpoint amplitudes and occurrence normalization.  It does not numerically integrate a model-specific continuum kernel.  Coincident internal labels form special strata and remain occurrence-resolved before physical trace.

## Architectural consequence

For this actual cubic source channel, the abstract coefficient mechanism of Entry 1622 is realized without a new carrier cell:

\[
\text{source endpoint difference}
\to
\text{labelled momentum Cut norm}
\to
\text{statistical second-Rees covariance grade}.
\]

## Durable artifacts

- `research/benincasa/checkers/cubic_momentum_second_rees_map.rs`
- `research/benincasa/results/cubic-momentum-second-rees-map.json`
- `research/benincasa/cubic-momentum-second-rees-map.md`

## Next falsifier

Add a nonzero Gaussian first jet \(\beta_p\) to the source state and compute the mixed cubic–Gaussian second grade.  Test whether all terms linear in the cubic channel are Hamiltonian/coherent tangents while the genuinely statistical remainder is still a positive labelled Cut norm.  Preserve the \(p,q,k\) occurrence labels and do not infer the answer from the vacuum channel.
