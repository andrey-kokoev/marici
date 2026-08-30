# 1863 — The Third-Rees Endpoint Test Is One Angular Integral

## Local expansion

Near an active-soft endpoint, write the source-normalized radial integrand as

\[
\frac{r^2\bigl(A_0+A_1r+A_\delta\delta+\cdots\bigr)}
{\delta+cr+dr^2+\cdots}\,dr\,d\Omega.
\]

On either coefficient-zero ray of Entries 1860--1862, \(A_0=0\). The exact
division identities are

\[
\frac{r^3}{\delta+cr}=\frac{r^2}{c}-\frac{\delta r}{c^2}
+\frac{\delta^2}{c^3}-\frac{\delta^3}{c^3(\delta+cr)},
\]

\[
\frac{r^2}{\delta+cr}=\frac{r}{c}-\frac{\delta}{c^2}
+\frac{\delta^2}{c^2(\delta+cr)}.
\]

## Third logarithmic coefficient

After radial integration, the coefficient of \(\delta^3\log\delta\) has
angular density

\[
\boxed{\frac{A_1}{c^4}-\frac{A_\delta}{c^3}}.
\]

Therefore the finite acceptance test is

\[
\boxed{\mathcal C_3=\int d\Omega\left(\frac{A_1}{c^4}-\frac{A_\delta}{c^3}\right)}.
\]

The third Rees logarithmic term is present if and only if the source-normalized
integral \(\mathcal C_3\) is nonzero.

## Missing source data

Computing \(\mathcal C_3\) requires:

1. the source-fixed normal deformation defining \(A_\delta\);
2. the radial derivative \(A_1\) of the complete residual coefficient;
3. the physical angular domain, orientation, and boundary prescription.

Tangential simplicity from Entry 1862 supplies none of these automatically.

## Narrow result

The question has been reduced to one typed angular integral. No carrier change
is required, and no third-Rees class has yet been asserted.

## Next falsifier

Derive \(A_1\), \(A_\delta\), and the angular current directly from the frozen
Bunch--Davies endpoint prescription. Evaluate \(\mathcal C_3\) without choosing
an angular regulator or normal deformation post hoc.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_active_soft_third_rees_gate.py`
- `research/benincasa/results/five-site-region-pair-active-soft-third-rees-gate.json`
- Entries 1836 and 1860--1862
- allocator claim: `seqclaim-6a85baf8c9ff616c842ad043`
