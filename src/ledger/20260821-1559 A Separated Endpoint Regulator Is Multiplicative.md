# 1559 — A Separated Endpoint Regulator Is Multiplicative

## Hard-to-vary claim

Separate the two endpoint occurrences with smooth one-sided mollifiers before
taking their coincidence limit. The two time-ordering chambers contribute

\[
\frac12,qquad\frac12,
\]

and their sum equals the product of the one-occurrence masses:

\[
\boxed{I_{12}+I_{21}=I_1I_2=1.}
\]

Thus the regulated endpoint limit is multiplicative and does not generate
the factor-two enhancement required by Eq. (19).

## Regulated calculation

Use the one-sided exponential mollifier

\[
\rho_\varepsilon(x)
=\varepsilon^{-1}e^{-x/\varepsilon},
\qquad x\ge0.
\]

Scaling removes \(\varepsilon\). Direct quadrature gives

\[
\int\rho=0.999999999362246,
\]

\[
I_{12}=0.500000000562245,
\qquad
I_{21}=0.499999998799926.
\]

For the printed local coefficient
\(H_0=-\tfrac12\delta S_0\) and the formal endpoint delta mass two required
by Entry 1539, the regulated weights are

\[
\int H_0=-S_0,
\qquad
-\frac12\iint H_0H_0=-\frac12S_0^2,
\]

exactly matching direct expansion of \(e^{iS_0}\).

## Artifacts

- `research/benincasa/checkers/regulated_endpoint_occurrence_limit.rs`
- `research/benincasa/results/regulated-endpoint-occurrence-limit.json`

## Narrow conclusion

A standard separated contour regulator closes the endpoint limit without an
excess class. A diagonal contact term could modify the two-boundary sector,
but it cannot also double the one-boundary mixed sector. Therefore the single
diagonal-cell escape proposed after Entry 1558 is insufficient.

Within the frozen toy source, the surviving alternatives are narrower:

1. an omitted one-boundary contribution not represented in Eq. (18)'s direct
   exponent expansion;
2. a genuinely nonfactorizing contour prescription with independent primary
   derivation;
3. or a normalization error in Eq. (19).

No new carrier incidence is indicated.

## Next falsifier

Re-derive Eq. (19)'s mixed and boundary--boundary coefficients directly from
the primary source's Eq. (17) exponent, without introducing \(H_0\) as a
delta insertion. Compare that direct expansion term-by-term with the printed
Eq. (18) representation. The first differing coefficient identifies whether
the defect lies in the exponent-to-Hamiltonian conversion or in Eq. (19)'s
final contraction.
