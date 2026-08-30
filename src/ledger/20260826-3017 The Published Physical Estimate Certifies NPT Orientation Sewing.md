# 3017 — The Published Physical Estimate Certifies NPT Orientation Sewing

**Status:** source-derived physical certificate  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-925f61f6015122ab9e7f4dea`

## Scope

Entry 3015 incorrectly reported that the numerical maximum-likelihood density matrix for the published sixteen-count run was unavailable. James et al. give it explicitly in equation (4.11). This entry repairs that defect and applies the predeclared NPT handedness test to the source-fixed physical estimator.

## Frozen estimator

The source defines

\[
\rho_p(t)=\frac{T^\dagger(t)T(t)}{\operatorname{Tr}(T^\dagger(t)T(t))}
\]

and minimizes its stated Gaussian count likelihood over the sixteen real triangular parameters of \(T\). For the exact count packet used in Entry 3015, equation (4.11) publishes the fitted matrix. The source reports its eigenvalues as

\[
0.986022,
\quad
0.0139777,
\quad
0,
\quad
0.
\]

Thus this is the source-authorized positive estimator, not a fitted repair introduced by Marici.

## Independent NPT audit

Using the matrix entries printed in equation (4.11), the checker obtains

\[
XX=0.9712,
\qquad
YY=-0.9620,
\qquad
ZZ=0.9815.
\]

Aspect’s direct handedness witness is

\[
W_{\rm ML}
=
\frac{1-XX+YY-ZZ}{4}
=
-0.478675.
\]

The partial-transpose spectrum computed from the printed matrix is approximately

\[
(-0.4801606,
0.4178035,
0.4929626,
0.5694944).
\]

The negative eigenvalue is separated from zero by nearly one half. Therefore the source’s physical estimate is decisively NPT and synchronizes the relative complex orientation of the two optical ports.

## Rounding audit

The four-decimal printed matrix has a smallest ordinary eigenvalue near

\[
-3.8\times10^{-5}.
\]

This is a publication-rounding artifact: the source reports the fitted estimator’s two smallest eigenvalues as zero. It is five orders of magnitude smaller than the NPT margin and cannot account for the negative partial-transpose eigenvalue.

## Narrow conclusion

For this historical source run, all three layers are now source-authorized and explicit:

1. the circular local analyzers;
2. the entangled two-port source;
3. the positive maximum-likelihood readout.

Their composition produces a physical NPT certificate. Relative complex handedness is therefore not merely algebraically available or ideally predicted; it is selected by the source’s actual composite optical readout.

This remains a sector-specific reconstruction. It does not imply that positivity synchronizes orientation in sectors lacking an NPT composite.

## Next falsifier

Test the same orientation-sewing criterion on a positive-partial-transpose or separable source packet. The prediction is that local analyzer records remain complete after calibration, but positivity no longer selects the relative \(C_2\) orientation. This control is necessary to show that the synchronization is caused by entanglement support rather than by the reconstruction algorithm.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-925f61f6015122ab9e7f4dea`, value 3017.
- Primary estimator: arXiv:quant-ph/0103121, equations (4.4)–(4.11).
- Checker: `research/benincasa/checkers/check_published_two_photon_npt.rs`.
- Physical witness: \(W_{\rm ML}=-0.478675\).
- Partial-transpose minimum: approximately \(-0.4801606\).
- Entry 3015 certification boundary explicitly withdrawn.
- Epistemic-graph admission: `ev-000000005808-e0435dff-c13a-4f9d-8684-688c94b2096a`.
