---
author: marici.Benincasa
---

# 1475 — The Initial-State Loop Pushforward Closes on a Finite Boundary-Jet Filtration

## Status

Primary-source one-loop test of the integrated initial-state coefficient
sector. The frozen calculation is Collins--Holman,
arXiv:hep-th/0507081v1, Eqs. (6.10)--(6.29).

## Frozen loop

The source's state-dependent one-loop tadpole contains

\[
-\frac{\lambda}{2}
\int_{\eta_0}^{\eta_f}d\eta\,
a^4(\eta)G(\eta_f,\eta)\phi(\eta)
\int\frac{d^3\mathbf k}{(2\pi)^3}
e^{\alpha_k^*}U_k^E(\eta)U_k^E(\eta).
\]

The initial-state coefficient is expanded in labelled frequency moments,

\[
e^{\alpha_k^*}
=
\sum_{n\ge0}d_n
\frac{H^n(\eta_0)}{\Omega_k^n(\eta_0)}
+
\sum_{n\ge1}c_n
\frac{\Omega_k^n(\eta_0)}{a^n(\eta_0)M^n}.
\]

This is an integrated pushforward of the same image coefficient isolated in
Entry 1470, now graded by its ultraviolet moment.

## Boundary localization

For the renormalizable \(d_n\) sector, the source derives the large-momentum
kernel

\[
d_n\int^\infty dk\,k^{1-n}
e^{-2ik(\eta-\eta_0)}+\cdots.
\]

Its exact power count is:

- \(n=0\): quadratic boundary singularity;
- \(n=1\): simple boundary singularity;
- \(n=2\): logarithmic kernel, finite after the remaining time integration;
- \(n>2\): finite.

The divergent pieces are isolated by integrations by parts as derivatives of
the source kernels \(K^{(0)}\) and \(K^{(1)}\). They are cancelled by the two
boundary-local counterterms \(z_0,z_1\), whose beta functions are

\[
\widehat\beta_0
=-\frac{\lambda_Rd_0}{16\pi^2}+\cdots,
\qquad
\widehat\beta_1
=-\frac{\lambda_Rd_1}{24i\pi^2}+\cdots.
\]

## Coefficient architecture

The loop pushforward therefore lands in a filtered boundary coefficient
object:

\[
\boxed{
F_0\mathcal C_\Sigma
\subset
F_1\mathcal C_\Sigma
\subset
F_{\rm finite}\mathcal C_\Sigma,
}
\]

where the first two ultraviolet grades require local counterterms and the
higher renormalizable grades are finite. The nonrenormalizable \(c_n\) sector
extends the boundary operator filtration by higher-dimensional local
operators, suppressed by powers of \(M\), as required by the source EFT.

This is genuine integrated coefficient complexity. It is not exhausted by
the tree-level rank-one line, but it is generated from that line by loop
pushforward, normal jets, and the declared boundary-local operator grading.

## Carrier test

All new ultraviolet support remains at

\[
\Sigma=\{\eta=\eta_0\}.
\]

No new external-energy pole, Cut wall, or incidence generator is produced by
the source one-loop integral. Thus

\[
\boxed{
\text{one-loop initial-state complexity}
=
\text{filtered coefficient data on the existing boundary carrier}.
}
\]

This is a nontrivial one-loop pass for H2.

## Prohibited inference

The result does not prove that every boundary loop or every nonlocal initial
state closes on local boundary operators. It proves closure for the frozen
effective initial states and one-loop tadpole hierarchy calculated by the
source.

## Next falsifier

Audit the leading nonrenormalizable \(c_1\) sector through its explicit
dimension-four boundary counterterms. Determine whether its derivative
structure is exactly the second normal/Rees grade of the background boundary
or requires a separately labelled coefficient jet. Keep this distinct from
the second total-energy normal grade that detects the three-site elliptic
quartic.

## Provenance

- Collins--Holman, arXiv:hep-th/0507081v1, Eqs. (6.10)--(6.29);
- Entries 1468, 1470, 1472, and 1474;
- allocator claim `seqclaim-b73e9590dc5b7a8448b21dcd`.
- epistemic event `ev-000000001586-41be64c8-b8b8-480a-be4a-e4f0460121d7`.
