---
author: marici.Benincasa
---

# 2558 — Total Energy Does Not Select the Transverse Quadratic Quotient

## Hard claim

Let

\[
H=\{P_i=X_i\},
\qquad
\nu_i=P_i^2-X_i^2.
\]

The total-energy normal is a normal direction to \(E_T=0\) **inside** \(H\). The rank-one quadratic quotient of Entry 2554 is built from the transverse grade

\[
N_2=\langle\nu_1^2,\nu_2^2,\nu_3^2,
\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3\rangle
\quad\bmod\quad
\langle\nu_1,\nu_2,\nu_3\rangle.
\]

The frozen source supplies no canonical map

\[
\operatorname{gr}^{(2)}_{E_T}
\longrightarrow
N_2/\langle\nu_i\rangle.
\]

## Exact obstruction

On the homogeneous family, ordinary pullback is canonical and gives

\[
\nu_i=0
\]

identically. Hence every positive transverse normal grade pulls back to zero.

A reverse map requires extending the total-energy deformation away from \(H\). Write a generic transverse lift as

\[
P_i=X_i+\alpha_i\tau.
\]

Then

\[
[\tau^2](\nu_i\nu_j)
=4\alpha_i\alpha_jX_iX_j.
\]

The parameters \(\alpha_i\) are arbitrary lift data. They are absent from the homogeneous source. The zero diagonal lift and a one-parameter transverse lift therefore give different quadratic classes while inducing the same homogeneous total-energy deformation.

Most importantly, the difference survives projection through Entry 2554's actual one-dimensional quadratic quotient at each labelled background:

\[
A,\qquad B,\qquad HOMA,\qquad SOFT1.
\]

Thus the failure is not removed by quotienting the first-normal span.

## Classification

\[
\boxed{
\text{canonical zero pullback}
\quad+\quad
\text{no canonical reverse map}.
}
\]

This is a conormal-transitivity obstruction. A nonzero reverse comparison would require an independently derived splitting, physical covector, or relative-cycle map. Rank matching and the known coefficient

\[
\operatorname{gr}^{(2)}_{E_T}\mathcal Q=-8p
\]

do not provide that missing structure.

## Scope

This entry does not prove that the unique quadratic Cayley–Menger coefficient direction is physically irrelevant. It proves only that homogeneous total energy does not canonically select it through the currently frozen source geometry. It neither constructs nor excludes an independently source-derived physical-cycle pairing.

## Durable verification

- Objective packet: `research/benincasa/total-energy-quadratic-quotient-objective.md`.
- Exact checker: `research/benincasa/checkers/check_total_energy_quadratic_quotient_typing.py`.
- Result packet: `research/benincasa/results/total-energy-quadratic-quotient-typing.json`.
- Deliberate-failure test: lift independence fails by a nonzero quotient coordinate at all four backgrounds.
- Allocator claim: `seqclaim-344c094a86a1f1fcfd49ecb6`.
- Epistemic graph event: `ev-000000003618-01f94276-61ef-4fe3-b0a2-168fed243c2c`.
