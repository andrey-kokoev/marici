# 2857 — Complete Source Normalization Removes the Soft Endpoint Weight Mismatch

## Normalization defect

Entries 2844 and 2847 compared two differently normalized objects:

- the negative endpoint retained the marked rational source coefficient;
- the positive endpoint was replaced by the pure Cayley–Menger period.

At \(\xi=+1\), the factor

\[
\xi+1=2
\]

is a unit, but the rest of the source coefficient

\[
\frac{a+p}{2p(a-p)^2(a+3p)(\xi+1)}
\]

does not disappear. It must be evaluated on the positive endpoint.

## Complete positive-germ entries

Set

\[
r^2=5-4\kappa,
\qquad
s^2=5+4\kappa.
\]

After the \(q_{g1}\) residue, the marked negative endpoint gives

\[
c_-^{\rm full}
=
\frac{\pi i(r+1)}
{2p^4r(r-1)^2(r+3)}.
\]

At the positive endpoint, retaining the unit value \(\xi+1=2\) and all other marked factors gives

\[
c_+^{\rm full}
=
\frac{\pi i(s+1)}
{4p^4s(s-1)^2(s+3)}.
\]

Therefore

\[
\deg_p(c_-^{\rm full})
=
\deg_p(c_+^{\rm full})
=-4.
\]

The weight difference is zero.

## Correction

The weight-three obstruction of Entry 2844 is retracted. The \(p^3\) factor required in Entry 2847 was an artifact of stripping the positive endpoint coefficient. Entry 2847's broader warning about square-root and occurrence typing remains relevant only after replacing its displayed comparison by the complete-source ratio.

## Surviving obstruction

The two endpoints still have different relative variance:

\[
\operatorname{Res}_{q_{g1}}\phi_{\rm CM}
\]

at \(\xi=-1\), versus an ordinary coefficient-valued Cayley–Menger boundary specialization at \(\xi=+1\).

Thus the remaining comparison problem is not homogeneous weight. It is the relative Stokes/Gysin differential between two degrees, together with the occurrence covectors derived in Entries 2851–2855.

The next finite test is to construct the complete relative-chain boundary identity. If it contains both endpoint terms, its coefficient is now dimensionless and must be derived from source orientation and the unit value \(\xi+1=2\).

## Durable artifacts

- research/benincasa/check_soft_endpoint_complete_source_weights.py
- research/benincasa/soft-endpoint-complete-source-weights.json

