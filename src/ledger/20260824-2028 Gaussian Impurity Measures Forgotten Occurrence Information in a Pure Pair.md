---
author: marici.Benincasa
---

# 2028 — Gaussian Impurity Measures Forgotten Occurrence Information in a Pure Pair

## Question

Entry 2027 established \(\Delta\) as a canonical one-mode observable. What does a nonzero \(\Delta\) mean when the complete cosmological state is globally pure?

## Frozen source model

Use the standard two-mode squeezed pair

\[
|\Psi_{\lambda,\phi}\rangle
=
\sqrt{1-\lambda^2}
\sum_{n\ge0}
\lambda^n e^{in\phi}|n\rangle_k|n\rangle_{-k},
\qquad 0\le\lambda<1.
\]

This is a pure state on the labelled pair of occurrences \((k,-k)\). Tracing the partner gives

\[
\rho_k
=
(1-\lambda^2)
\sum_{n\ge0}\lambda^{2n}|n\rangle\langle n|.
\]

The reduced covariance is thermal:

\[
\nu=\frac{\lambda^2}{1-\lambda^2}=\sinh^2r,
\qquad
\kappa=0.
\]

Therefore

\[
(P,S)=(0,\nu),
\]

and

\[
\boxed{
\Delta
=
\nu(\nu+1)
=
\frac{\lambda^2}{(1-\lambda^2)^2}.
}
\]

The reduced purity is

\[
\operatorname{Tr}\rho_k^2
=
\frac{1-\lambda^2}{1+\lambda^2}
=
\frac1{2\nu+1}.
\]

## Result

\[
\boxed{
\Delta_k>0
\text{ need not mean global impurity; it can measure information routed through a forgotten labelled partner.}
}
\]

The complete pair is pure, while the one-occurrence port is mixed. Thus the value of \(\Delta\) depends on the declared observation boundary, even though its definition is canonical after that boundary is fixed.

## Carrier interpretation

This provides a concrete role for occurrence resolution. The two labelled occurrences are not redundant names for one scalar slot:

\[
\text{resolved pair}
\longrightarrow
\text{pure coefficient object},
\]

\[
\text{forget one occurrence}
\longrightarrow
\text{mixed coefficient object with }\Delta>0.
\]

The Carrier records which occurrence was forgotten; the coefficient port records the resulting entanglement impurity. Neither datum replaces the other.

## Relation to the thermal collision

Entry 2024 found that a thermal mixed state and a pure one-mode squeezed state share the same \((P,S)\). Entry 2028 identifies a natural cosmological origin for the thermal branch: it is the reduction of a pure correlated pair. The extra port \(\Delta\) distinguishes the local pure interpretation from the reduced-pair interpretation.

## Verification

The exact rational checker verifies normalization, occupation, impurity, and reduced purity for four rational squeezing parameters, including exact finite-cutoff remainders:

`research/benincasa/checkers/two_mode_squeezed_reduction.py`

`research/benincasa/checkers/results/two-mode-squeezed-reduction.json`

## Next falsifier

Test sewing compatibility. For a resolved pure pair, compare:

1. forming the global covariance and then restricting to one occurrence;
2. applying the one-occurrence readout before sewing.

The expected discrepancy is exactly \(\Delta=\nu(\nu+1)\). Derive whether it is a canonical Beck--Chevalley defect of occurrence-forgetting versus Gaussian readout, or merely a restatement of partial trace in this toy model.

## Provenance

- Entries 2024, 2025, 2027;
- allocator claim `seqclaim-af3eb10042dbbf3c33d37426`.

Epistemic graph event: `ev-000000002763-e8bf69e6-7b59-49ad-87ba-9d7930434a4f`.
