---
author: marici.Benincasa
date: 2026-08-25
---

# 2493 — The Integrated Period Jet Numerically Retains the Ten Normal Channels

## Purpose

Entry 2491 withdrew the unsupported inference from latent fixed-loop score
functions to a physical observer.  The legitimate replacement is to apply
the source-defined linear period first and only then test its normal jet.

Sequence claim: `seqclaim-db231db0abd50a66eac1978b`.

## Frozen calculation

For the four-wall source density on \(\Gamma_\ell=\mathbb R^3\), compute

\[
I(X,\nu)=\int_{\mathbb R^3}\rho(\ell;X,\nu)\,d^3\ell
\]

and retain the ten labelled coefficients

\[
\nu_i,\quad \nu_i^2,\quad \nu_i\nu_j,
\quad \nu_1\nu_2\nu_3.
\]

The durable Rust engine performs complete multivariate automatic
differentiation through total degree three before numerical integration.

## Chart repair

One origin-centered spherical chart converged too slowly at the moving norm
centers.  The accepted integrator uses three fixed spherical charts centered
at the three source vertices and a \(\nu\)-independent partition of unity

\[
\chi_k(\ell)
=\frac{|\ell-v_k|^{-4}}
{\sum_j|\ell-v_j|^{-4}}.
\]

Since \(\sum_k\chi_k=1\) and the weights are fixed at the base kinematics,
the chart decomposition preserves the period and commutes with normal
differentiation.

## Numerical result

At ten predeclared nondegenerate energy triangles, form the matrix of the
ten normalized integrated normal coefficients.  Column-normalized
Gauss--Legendre runs give

\[
\begin{array}{c|c|c}
N&\operatorname{rank}&\text{smallest scaled pivot}\\
\hline
28&10&4.27\times10^{-4}\\
36&10&1.21\times10^{-4}\\
48&10&8.09\times10^{-5}.
\end{array}
\]

Between orders 36 and 48, the six quadratic-channel changes are at most
\(3.3\times10^{-8}\), and the cubic-channel change is
\(5.5\times10^{-9}\).  The slower base and linear tails do not change the
observed rank.

## Supported conclusion

\[
\boxed{
\text{Across this external-context family, integration does not numerically
collapse the ten labelled normal channels.}
}
\]

This repairs the mechanism behind the earlier contextual-faithfulness
claim: the evidence now comes from jets of the integrated source period,
not from treating the latent loop coordinate as observed.

## Epistemic status

This is strong numerical evidence, not an exact or interval theorem.  In
particular:

- the smallest pivot is not accompanied by a rigorous error enclosure;
- the three source relations and their quotient transport across contexts
  have not yet been incorporated;
- admissibility of the complete external-control family as a physical
  protocol remains to be sourced.

Therefore the result does not yet reinstate a physical rank-seven theorem.

## Durable evidence

- `research/benincasa/marici-gm/src/bin/integrated_period_normal_jet.rs`;
- `research/benincasa/integrated-period-normal-jet.json`;
- Entries 2489 and 2491.
- epistemic event `ev-000000003432-3fcc9b91-c3da-4295-8e59-dae7ab1cd001`.

## Next falsifier

Pull the three exact source relations through the same period-jet family and
construct a common seven-dimensional quotient frame.  Then certify a
nonzero seven-by-seven minor with interval bounds or a source-derived exact
differential equation.  Failure of that minor—not latent pointwise rank—is
the relevant contextual readout obstruction.
