---
author: marici.Benincasa
---

# 2023 — A Complete Thermal Gaussian Source Selects a Ray Rather Than a Unique Readout

## Purpose

Entry 2022 closed an incomplete loop-matching source. As a control, test the same intrinsic readout map on a Gaussian source whose state is fully specified.

## Frozen source

Collins, *Initial state propagators*, arXiv:1309.2656, derives the quadratic initial action and gives the thermal specialization

\[
\alpha_k=0,
\qquad
\beta_k=-\frac{2\omega_k n_k^2}{2n_k+1},
\qquad
B_k=\frac{2\omega_k n_k(n_k+1)}{2n_k+1},
\]

with Bose occupation

\[
n_k=\frac1{e^{\beta\omega_k}-1}\ge0.
\]

In intrinsic covariance coordinates this is simply

\[
\nu_k=n_k,
\qquad
\kappa_k=0.
\]

## Projection to the readout quotient

Entry 2018 uses

\[
P=\text{one quadrature of }\kappa,
\qquad
S=\nu+\text{the orthogonal quadrature of }\kappa.
\]

Therefore the complete thermal source maps canonically to

\[
\boxed{(P,S)=(0,n_k)}.
\]

It lies in the positive domain

\[
S>-\frac12
\]

for every finite temperature, including the vacuum endpoint \(n_k=0\). No counterterm representative or phase convention affects this conclusion because \(\kappa=0\).

## Result

The readout calculus does produce a physical section when the source supplies a complete state prescription. But the state **class** alone selects only the ray

\[
\boxed{P=0,\quad S\ge0}.
\]

A particular temperature profile \(\beta(k)\) selects a point or trajectory on that ray. Thus completeness of the coefficient object and uniqueness of the physical readout remain distinct claims.

## Architectural lesson

This control separates three layers:

\[
\text{positivity}\to\{S>-\tfrac12\},
\]

\[
\text{thermal source class}\to\{P=0,S\ge0\},
\]

\[
\text{temperature profile}\to(P(k),S(k))=(0,n_k).
\]

Carrier/coherence specifies the legal domain; a source family specifies a subspace; source parameters specify the physical section. The failure in Entry 2019 is therefore not a defect of the readout map but absence of the final source datum.

## Next falsifier

Apply the quotient to a complete squeezed Gaussian source with \(\kappa\ne0\). Test whether its source phase and squeezing amplitude map injectively to \((P,S)\), or whether the late-time quotient forgets a state direction. This distinguishes a faithful physical readout from another finite-to-one projection.

## Provenance

- Collins, arXiv:1309.2656, thermal-state specialization;
- Entries 2018, 2019, and 2022;
- allocator claim `seqclaim-6eb1412d19b0e6f01788e0bf`.

Epistemic graph event: `ev-000000002755-15b9e94a-dd22-485f-8035-35a6dcc095e3`.
