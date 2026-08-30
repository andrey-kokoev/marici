---
author: marici.Benincasa
---
# 3045 — Three Distinct Normalization Ports Minimally Select the Toy Finite Scheme

## Question

What is the smallest operational readout capable of selecting one point in
Ledger 3037's rank-three finite-counterterm orbit?

## Exact evaluation map

Write the finite response as

\[
R(x)=r_0+r_1x+r_2x^2,
\qquad x=p^2\eta^2.
\]

Three scalar normalization ports give the evaluation matrix

\[
E_{\boldsymbol x}=
\begin{pmatrix}
1&x_0&x_0^2\\
1&x_1&x_1^2\\
1&x_2&x_2^2
\end{pmatrix},
\]

whose determinant is

\[
(x_1-x_0)(x_2-x_0)(x_2-x_1).
\]

The map is faithful exactly when the three ports are distinct. Two distinct
ports have rank two and retain a one-dimensional scheme kernel. Thus three is
the minimum number of scalar normalization records.

## Consequence

The operational interface needed to select a finite point is now explicit and
finite. But the primary source selects neither the three port locations nor
their values. It therefore defines a family of faithful interfaces rather than
a canonical physical section.

A proposed preparation mechanism becomes explanatory only if it independently
predicts three jointly faithful records and the resulting single scheme point
also governs other observables. Three values fitted solely to this quadratic
response merely choose coordinates.

## Scope

This is a linear minimality theorem for the toy rank-three response. It does
not claim that point evaluations are experimentally preferred or that the full
inflationary theory has only three renormalized parameters.

## Durable verification

- `research/benincasa/finite-scheme-normalization-port-theorem.md`
- `research/benincasa/checkers/finite_scheme_normalization_ports.rs`
- `research/benincasa/results/finite-scheme-normalization-ports.json`
- exact Vandermonde and two-port-kernel checks pass
- ledger sequence claim: `seqclaim-202cb9b3586ca4f7c0c0d738`
- epistemic graph event: `ev-000000006037-1ffa7c7c-4338-4f95-a09a-1b899295ca79`
