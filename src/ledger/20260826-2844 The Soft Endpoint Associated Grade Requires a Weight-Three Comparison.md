# 2844 — The Soft Endpoint Associated Grade Requires a Weight-Three Comparison

> **Retracted by the complete-source normalization audit.** At \(\xi=+1\),
> the factor \(\xi+1\) is a unit, but the remaining marked rational
> coefficient must still be evaluated on the endpoint. Doing so gives the
> positive endpoint the same \(p\)-weight \(-4\) as the negative residue.
> The weight-three mismatch below resulted from comparing a marked negative
> endpoint with a pure, coefficient-stripped positive period.

## Frozen endpoint types

Entry 2843 places the two soft endpoints in different relative degrees:

\[
E_+=\phi_{\rm CM}|_{\xi=+1},
\qquad
E_-=\operatorname{Res}_{q_{g1}}\phi_{\rm CM}|_{\xi=-1}.
\]

Their associated graded has one line in each of degrees zero and one. This statement does not construct the differential between them.

## Source-normalized local entries

Set

\[
r=\sqrt{5-4\kappa}.
\]

On the positive (a)-sheet, the unmarked positive-endpoint vanishing period is

\[
c_+=\frac{\pi i}{p\sqrt{5+4\kappa}}.
\]

At the negative endpoint, the source residue factor is

\[
\frac{a+p}{2p(a-p)^2(a+3p)}
=
\frac{r+1}{2p^3(r-1)^2(r+3)}.
\]

Multiplying it by the pure Cayley–Menger local period gives

\[
c_-=
\frac{\pi i(r+1)}
{2p^4r(r-1)^2(r+3)}.
\]

## Weight audit

The homogeneous (p)-weights are

\[
\deg_p(c_+)=-1,
\qquad
\deg_p(c_-)=-4.
\]

Therefore the two entries cannot be added as components of one scalar covector without a source-derived comparison carrying (p)-weight (+3), in addition to the already known relative-degree shift.

This is a typing obstruction, not yet a construction of that comparison. In particular, the calculation does not prove that an existing Gysin normalization supplies the required weight.

## Narrow result

The soft endpoint object currently exists only as an associated-graded pair

\[
\operatorname{gr}E=E_+\oplus E_-.
\]

An ordinary two-entry Kummer covector remains undefined. The next finite falsifier is to derive the comparison map from the full marked-relative de Rham reduction and test whether its source normalization carries the required (p)-weight (+3). If no such map exists, the two endpoint periods do not define a scalar readout.

## Durable artifacts

- `research/benincasa/check_soft_endpoint_relative_cone_grade.py`
- `research/benincasa/soft-endpoint-relative-cone-grade.json`
