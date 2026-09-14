# DAG IndCoh candidate for the relative RH boundary

Date: 2026-09-08

## Search result

The two derived-algebraic-geometry volumes strengthen the Stacks localization candidate in two ways.

### Supported objects are a kernel, not an added boundary coordinate

Volume I, Chapter 4, Section 6.1 defines, for a closed embedding `i:Z→X` with complementary open `j:U→X`,

\[
\operatorname{IndCoh}(X)_Z
=
\ker\bigl(j^*: \operatorname{IndCoh}(X)\to\operatorname{IndCoh}(U)\bigr).
\]

The right adjoint to the inclusion of this supported category sends an object `F` to

\[
\operatorname{fib}\bigl(F\longrightarrow j_*j^*F\bigr),
\]

and is also described as

\[
\operatorname{fib}(\mathcal O_X\to j_*\mathcal O_U)\otimes F.
\]

For the RH analogy, the relative boundary packet should therefore be the fibre of the complete packet's restriction to the generic overlap, not an independently inserted endpoint observable:

\[
B_{\mathrm{rel}}(F)
:=
\operatorname{fib}\bigl(F\to j_*j^*F\bigr).
\]

This construction sends the zero section to zero functorially and retains precisely the part invisible on the generic chart.

### Boundary readback is conservative on the supported category

The same section states that `i!` is conservative on `IndCoh(X)_Z`.  Thus, once the comparison fibre is proved supported on `Z`, vanishing can be checked on the actual boundary pullback.  This is a better match for the desired sequence

\[
\Theta=0
\Longrightarrow B_{\mathrm{rel}}(\Theta)=0
\Longrightarrow D_{\mathrm{bw}}=0
\]

than a scalar functional on the determinant line.  The second implication would be the Hermitian realization of `i!B_rel`.

### Local supported data can glue through a categorical pullback

Volume II, Appendix A, Theorem A.1.2 proves a pullback statement for `IndCoh` on a pushout, and its proof reduces essential surjectivity using localization sequences of DG categories with support.  This suggests a route for the primitive, square, seam, and archimedean boundary pieces: show their local supported objects agree in the supported-category pullback rather than trying to continue their scalar representatives separately.

### A canonical infinitesimal boundary appears as a fibre sequence

Volume II, Section 6.4 gives a canonical fibre sequence for the dualizing object of a square-zero extension.  This suggests modelling first-order seam or anomaly data as an actual square-zero derived thickening.  The boundary term would then be the shifted conormal contribution in the fibre sequence, not a fitted first derivative of the scalar section.

## Candidate RH construction

The combined proposal is:

1. choose a derived base `X` for the reciprocal determinant carrier and a closed seam/polar locus `i:Z→X`;
2. represent the full five-component packet by an object `F` with a defined generic restriction;
3. form the canonical supported fibre
   \[
   B_{\mathrm{rel}}(F)=\operatorname{fib}(F\to j_*j^*F);
   \]
4. use the supported pullback theorem to glue its finite-prime and archimedean local presentations;
5. construct a Hermitian realization
   \[
   \operatorname{Herm}:i^!B_{\mathrm{rel}}(F)\to\mathsf{Work};
   \]
6. compare `Herm` with the already verified covariant graph boundary identity and the normalized `D_bw` formula.

## Falsifiers

The proposal fails at the first applicable item if:

- no derived base and closed locus type the analytic reciprocal charts;
- the comparison fibre has generic support away from the seam/polar locus;
- primitive and square local objects do not agree in the supported pullback;
- the boundary pullback is not in the domain of the Hermitian realization;
- the resulting form differs from `J(q1)-J(q0)+2R`;
- the derived thickening merely encodes a chosen scalar derivative after inspecting `Xi`.

## Scope

This is a speculative architecture.  The cited results prove properties of `IndCoh` on derived schemes; they do not establish that the RH analytic carrier is such a scheme, that its operator packets are ind-coherent objects, or that analytic completion is represented by the stated functors.  The first missing typed object is a source-derived derived base `X` with closed boundary locus `Z` and a realization of the five-component packet as `F∈IndCoh(X)`.

## PDF locators

- `Derived algebraic geometry Vol1.pdf`, Chapter 4, Section 6.1, especially Proposition 6.1.3;
- `Derived algebraic geometry Vol2.pdf`, Appendix A, Theorem A.1.2 and localization reduction A.1.3;
- `Derived algebraic geometry Vol2.pdf`, Section 6.4, Proposition 6.4.2.
