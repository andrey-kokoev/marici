# Fock space is a candidate common domain, not yet a form core

## Question

Is there a natural analytic Hilbert space in which endpoint evaluation is bounded, Gaussian translates are total, and prime translations remain controlled?

## Segal--Bargmann candidate

Transport the real-line Gaussian observer system through a Segal--Bargmann transform

\[
\mathcal B:L^2(\mathbb R)\longrightarrow\mathcal F_\alpha,
\]

where `F_alpha` is a Bargmann--Fock space of entire functions with Gaussian area weight.

This simultaneously supplies:

- bounded evaluation at every fixed complex point, including the endpoint arguments;
- coherent-state vectors corresponding to Gaussian translates/modulations;
- totality of the coherent-state family;
- unitary Weyl displacement operators implementing the Heisenberg translation action;
- a number operator controlling polynomial spectral moments and heat derivatives.

These properties address the topology mismatch left by ordinary `L^2`.

## Sector transport

### Endpoint

Complex evaluation is represented by a reproducing kernel vector. The two endpoint evaluations therefore become bounded finite-rank channels and retain their one-positive/one-negative Krein decomposition.

### Prime terms

Each paired prime displacement becomes a bounded Weyl adjacency. Labelwise positive/negative functional-calculus splitting remains available, and the log-Gaussian coefficients control the direct-sum row.

### Gamma term

The real-line multiplier

\[
w_\Gamma(u)
=
\operatorname{Re}\psi(1/4+iu/2)-\text{normalization}
\]

grows logarithmically. Its Segal--Bargmann conjugate is unbounded. It must be defined through the closed multiplication form on the real side and transported unitarily; it is not a bounded Fock multiplier.

## Candidate graph domain

Let `A` and `B` be the source-derived positive and negative row operators after transport. The natural candidate domain is

\[
\mathcal D_W
=
\operatorname{Dom}(A)\cap\operatorname{Dom}(B)
\]

with norm

\[
\|F\|_{\mathcal D_W}^2
=
\|F\|_{\mathcal F_\alpha}^2
+
\|AF\|^2+
\|BF\|^2.
\]

The required theorem is that the coherent-state span is a core for both rows, hence dense in this intersection graph norm.

## Exact tests

A valid Fock realization must prove:

1. the selected Bargmann normalization sends the actual Gaussian translate probes to the claimed coherent states;
2. endpoint evaluations match the explicit-formula normalization;
3. the transported gamma form is closed and has the coherent span as a core;
4. the infinite labelled prime row is closed or bounded on the same domain;
5. heat and Weyl actions preserve the common core and satisfy the declared generator cell;
6. no observer-dependent change of Fock weight is used.

## Strongest obstruction

Totality of coherent states in the Fock norm does not imply graph-core density for the unbounded gamma row. That is the first unresolved analytic theorem. Failure would invalidate promotion from finite Gram positivity to the full completed form even though every endpoint and prime operation is individually well behaved.

## Disposition

Adopt Bargmann--Fock space as the leading common-domain candidate, not as an established solution. Its decisive acceptance test is simultaneous graph-core density for the transported gamma and prime feature rows with the fixed source normalization.
