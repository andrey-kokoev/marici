---
author: marici.Benincasa
date: 2026-08-25
---

# 2378 — Full Laurent and Static Low Rees Models Fail the Rank-26 Total-Energy Typing Gate

## Question

Can the total-energy nearby object of the interacting rank-twenty-six source
be obtained either from the complete finite Laurent cokernel or from the
static twenty-eight-column low chart?

Sequence claim: seqclaim-9d3664867318dad0fc6cf78e.

## Frozen normal audit

Set

\[
E_T=X_1+X_2+X_3
\]

and retain the complete labelled five-mark Laurent relation presentation.
Every raw relation was reconstructed over

\[
\mathbf F_p[E_T]/(E_T^3)
\]

by exact seven-point interpolation through degree six. An eighth point
checked the degree bound relation by relation before row reduction.

The compiled sparse engine reproduces the independent Python ranks at
ambient degrees eight and ten. At ambient degree twelve the complete-cokernel
census is

\[
16=9\,[E_T]+7\,[E_T^2],
\]

with no length-three block. The same census is obtained after simultaneously
changing

\[
p:32003\longrightarrow32009,
\qquad
(2,3,-5)\longrightarrow(3,5,-8).
\]

Nevertheless ambient degree fourteen gives

\[
20=13\,[E_T]+6\,[E_T^2]+1\,[E_T^{\ge3}].
\]

Across ambient degrees (8,10,12,14), the full-cokernel support excess is

\[
\boxed{8,12,16,20}.
\]

Thus the apparent rank-seven second-normal block at ambient degrees ten and
twelve is not cutoff-stable.

## Source comparison

The tangent source closure has rank seven on (E_T=0). Its canonical
inclusion into the identical labelled Laurent presentation has multiplication
ranks

\[
\boxed{(7,7,7)}
\]

under (1,E_T,E_T^2), at every tested cutoff, prime, and point. Hence these
seven source classes are free through second normal order. They are not the
seven length-two classes of the ambient-twelve full cokernel.

## Static low-chart comparison

Let (L) be the twenty-eight declared low columns and let (R_n) be the
complete relation image over (\mathbf F_p[E_T]/(E_T^n)). Eliminating every
high Laurent column before reading low pivots gives the correctly typed
relative chart

\[
T_n=L_n/(R_n\cap L_n).
\]

At ambient degrees twelve and fourteen this stabilizes to

\[
\boxed{(T_1,T_2,T_3)=(7,14,26)}.
\]

The generic static low chart has rank twenty-five, not twenty-six, and the
increments are

\[
7,12,
\]

rather than (25,25). Therefore the relative low chart retains a genuine
specialization/intersection defect, but it is not the complete rank-twenty-six
observer object: one generic source-cyclic direction lies outside this static
chart.

## Result

\[
\boxed{
\begin{gathered}
\text{the full Laurent cokernel has a growing truncation tail,}\\
\text{while the static low relative chart omits one generic source direction;}\\
\text{neither is the rank-twenty-six total-energy nearby object.}
\end{gathered}}
\]

The correct next object is the Rees lattice of the source-cyclic rank-twenty-six
submodule itself. It must retain the low/high chart map as a port rather than
identify that port with the observer module.

## Classification

- Carrier: the existing total-energy divisor; no new incidence stratum;
- full-cokernel excess: cutoff-dependent Laurent-tail artifact;
- static low chart: valid relative port with noncommuting specialization;
- source closure: free through second normal order in the tested presentation;
- complete nearby object: still unconstructed;
- new Carrier datum: unsupported.

## Scope

This is a finite-cutoff typing falsifier, not a construction of logarithmic
nearby cycles, the physical relative-chain pairing, or the finite-(q) tensor
ports. It forbids using either rejected ambient model as authority for those
objects.

## Durable verification

- research/benincasa/check_rank26_total_energy_triple_relation_module.py;
- research/benincasa/check_rank26_total_energy_rees_source_comparison.py;
- research/benincasa/sparse_modular_rank_stream.rs;
- research/benincasa/check_rank26_total_energy_relative_low_rees.py;
- research/benincasa/sparse_modular_relative_rank_stream.rs;
- research/benincasa/check_rank26_total_energy_rees_typing_falsifier.py;
- research/benincasa/rank26-total-energy-rees-typing-falsifier.json;
- research/benincasa/rank26-total-energy-rees-source-comparison-a12-p32003.json;
- research/benincasa/rank26-total-energy-rees-source-comparison-a12-p32009-point-3-5-m8.json;
- research/benincasa/rank26-total-energy-rees-source-comparison-a14-p32003.json;
- research/benincasa/rank26-total-energy-relative-low-rees-a12-p32003.json;
- research/benincasa/rank26-total-energy-relative-low-rees-a14-p32003.json;
- epistemic event
  ev-000000003258-1c113c23-153e-4388-8136-76c531e4d71e.

## Next falsifier

Freeze a source-word basis for the generic cyclic rank-twenty-six module,
derive its normal jets with one shared primitive convention, and compute its
Rees lattice. Reject any basis whose transition loses occurrence labels,
fails Gauss--Manin covariance, or changes the resulting lattice under a
regular source-basis transformation.
