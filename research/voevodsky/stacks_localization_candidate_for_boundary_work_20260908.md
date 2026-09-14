# Stacks localization candidate for the RH boundary-work map

Date: 2026-09-08

## Question

Can the missing map from the distinguished theta section to boundary work be constructed as a derived boundary map rather than as a scalar functional fitted to the value of the section?

## Candidate construction

Let the reciprocal determinant carrier be covered by the plus and minus charts `U` and `V`, with overlap `W=U∩V`.  Treat the complete primitive/square/connected/seam/archimedean packet as an object `E` whose local representatives are related by the determinant-three transition on `W`.

Stacks Project, `cohomology.tex`, Lemma `lemma-exact-sequence-j-star`, gives the Mayer--Vietoris distinguished triangle

\[
E\longrightarrow Rj_{U,*}E|_U\oplus Rj_{V,*}E|_V
\longrightarrow Rj_{W,*}E|_W
\longrightarrow E[1].
\]

The third arrow records the overlap mismatch before scalar aggregation.  For a closed boundary locus `Z`, the support-localization triangle in `cohomology.tex` is

\[
R\Gamma_Z(X,E)\longrightarrow R\Gamma(X,E)
\longrightarrow R\Gamma(X\setminus Z,E)
\overset{\partial_Z}{\longrightarrow}R\Gamma_Z(X,E)[1].
\]

The candidate relative boundary operator is the connecting morphism `∂_Z` applied to the overlap packet.  The proposed boundary-work readout is not a map from the scalar value line.  It factors as

\[
\mathcal L_\theta
\longrightarrow
\operatorname{Cone}
\bigl(E_U\oplus E_V\to E_W\bigr)
\overset{\partial_Z}{\longrightarrow}
R\Gamma_Z(X,E)[1]
\overset{\operatorname{Herm}}{\longrightarrow}
\mathsf{Work}.
\]

Because every arrow is defined before zero testing, the zero section maps to zero automatically.  This avoids the scalar-factorization hostile, provided the final Hermitian realization is source-derived.

## Determinant compatibility

Stacks Project, `chow.tex`, Lemma `lemma-additivity-on-perfect`, states that a distinguished triangle of perfect objects gives multiplicative total Chern class and additive Chern character.  The same cone architecture therefore matches the already verified determinant-three anomaly principle: local determinant data compose through the triangle, while the supported cone retains the boundary residual.

The discussion around `chow.tex` remarks `remark-perf-Z-cohomology-K` and `remark-localized-chern-classes-K` identifies perfect complexes supported on `Z` as the correct input for localized characteristic classes.  This suggests that boundary work should be extracted from a supported perfect cone, not from the invertible carrier transition itself.

## Risky consequences

The candidate predicts:

1. the complete local packets agree on the overlap away from the declared boundary locus;
2. their mismatch cone has cohomology supported on that locus;
3. primitive and square anomaly coordinates survive inside the cone rather than being separately continued;
4. the determinant-three transition contributes a unit and hence no supported divisor;
5. the Hermitian image of the connecting class equals the established `D_bw` convention;
6. the zero section maps to the zero supported class by functoriality.

## Strongest immediate falsifier

At finite Euler cutoff, form the actual plus/minus packet comparison on the overlap.  If its cone has a nonzero generic cohomology class away from the seam/polar support, then it is not an object supported on `Z` and the localization construction does not apply.  If it is supported but its Hermitian image differs from

\[
D_{\mathrm{bw}}=J(q_1)-J(q_0)+2R,
\]

then the proposed realization fails even though the localization triangle exists.

## Disposition

This is a source-compatible candidate, not a proved RH bridge.  Stacks supplies the canonical boundary-map architecture and determinant additivity.  It does not identify the RH analytic packets as perfect complexes, prove support of their comparison cone, or construct the Hermitian realization.  The first executable test is generic-support vanishing of the finite-cutoff overlap cone.

## Stacks locators

- `cohomology.tex`, `lemma-exact-sequence-j-star`;
- `cohomology.tex`, support-localization triangle near the definition of `RΓ_Z`;
- `chow.tex`, `lemma-additivity-on-perfect`;
- `chow.tex`, `remark-perf-Z-cohomology-K`;
- `chow.tex`, `remark-localized-chern-classes-K`;
- `perfect.tex`, `lemma-generator-with-support` for Koszul generators of supported derived categories.
