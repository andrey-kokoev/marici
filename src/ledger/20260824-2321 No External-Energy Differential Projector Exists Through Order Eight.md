---
authors:
  - marici.Benincasa
date: 2026-08-24
---

# 2321 — No External-Energy Differential Projector Exists Through Order Eight

## Question

Is Entry 2320's failure of external route projection merely a second-order
artifact?

## Complete source factors

For every one of the six simplex terms in arXiv:2408.16386, equation (4.15),
retain the complete rational factor

\[
\frac1{
q_{\mathcal G}
q_{\mathfrak g_1}q_{\mathfrak g_2}q_{\mathfrak g_3}
q_{\mathcal G_{ij}}q_{\mathfrak g_{kl}}}.
\]

The Cayley--Menger twist \(K^\gamma\) is common to all six routes and is
independent of the external site energies \(X_i\).  For
\(d=3,n_s=3,L=1\), the source exponent is

\[
\gamma=-\frac12.
\]

Thus it does not alter the external-energy jet calculation.

## Bounded high-order census

At fixed generic \(X=(2,3,5)\), construct every multivariate Taylor
coefficient in \((X_1,X_2,X_3)\) through total order \(d\).  For each order,
use more independent exact loop-fiber samples than are required to determine
all jet coefficients.  Test whether one loop-independent row can select any
of the six routes simultaneously at all samples.

The results are

\[
\begin{array}{c|rrrrrrrrr}
d&0&1&2&3&4&5&6&7&8\\
\hline
N_d&1&4&10&20&35&56&84&120&165\\
\operatorname{rank}M_d&1&4&10&20&35&56&84&120&165\\
\operatorname{rank}[M_d|e_k]&2&5&11&21&36&57&85&121&166
\end{array}
\]

for every \(k=1,\ldots,6\), where

\[
N_d=\binom{d+3}{3}.
\]

## Result

\[
\boxed{
\text{No complete simplex route has a loop-variable-independent
external-energy projector through total order eight.}
}
\]

The source score tower keeps acquiring independent coefficient functions,
but the desired route selector remains one rank outside their image at every
tested depth.

This is a finite hostile census, not an all-order theorem.  It nevertheless
rules out the possibility that one or two omitted external score grades were
responsible for Entry 2320's failure.

## Interpretation

Interaction has changed the observer architecture:

- pointwise loop-context scores are faithful;
- marked iterated residues are faithful;
- finite external-energy differentiation is not a route projector through
  substantial depth.

The surviving information is therefore present in the coefficient object but
does not descend through this external readout.  This is a sector-specific
coefficient/readout obstruction, not new Carrier support.

## Next falsifier

Use the source Gauss--Manin reduction rather than raw differentiation.  Test
whether integration and IBP reduce the six orbit routes to a finite module on
which the induced connection admits a faithful external quotient.  The
marked-residue basis and physical relative cycle must remain explicit.

## Durable verification

- `research/benincasa/checkers/interacting_scalar_external_jet_depth.rs`;
- `research/benincasa/interacting-scalar-external-jet-depth.json`;
- allocator claim `seqclaim-287ed87256505d7ab3819535`.

