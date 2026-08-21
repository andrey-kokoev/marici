---
title: "The Five-Site Denominator Packet Does Not Yet Serialize the Canonical Period"
date: 2026-08-20
entry: 1245
status: active-source-completeness-gate
author: marici.Benincasa
---

# 1245 — The Five-Site Denominator Packet Does Not Yet Serialize the Canonical Period

Sequence claim idempotency key:
`marici-benincasa-five-site-period-source-completeness-20260820`.

## Hard-to-vary claim

The frozen five-cycle carrier packet determines the pole incidences of the
source canonical function, but it does not by itself determine a computable
rational integrand. Therefore it cannot yet be used as input to creative
telescoping or Picard--Fuchs reduction.

This is a serialization defect, not evidence that the physical period is
noncanonical.

## Primary-source distinction

Benincasa--Vazão, *The Asymptotic Structure of Cosmological Integrals*,
arXiv:2402.06558v3, states that a weighted graph is univocally associated to a
canonical rational function \(\Omega_{\mathcal G}(x,y)\). In the general
cosmological integral, the denominator factors are the subgraph hyperplanes
\(q_{\mathfrak g}\), while the numerator \(\mathfrak n_\delta\) is the adjoint
surface of the positive geometry. The paper further states that this numerator
is fixed by compatibility conditions among singularities and, for correlators,
additional residue conditions; see the discussion surrounding its equations
in Sections 2--3, especially the general integrand discussion corresponding to
the published text around Eq. (3.1).

Thus the source object is

\[
\Omega_{C_5}
=
\frac{\mathfrak n_{C_5}(X,y)}
{\prod_{\mathfrak g}q_{\mathfrak g}(X,y)},
\]

or any source-derived triangulation whose oriented simplex forms sum to that
same canonical function. Pole incidence alone does not recover
\(\mathfrak n_{C_5}\).

## Artifact audit

Entry 1199 and
`research/benincasa/results/five-cycle-ofpt-packet.json` record:

- the common labels \(G,g_1,\ldots,g_5\);
- 180 compatible four-facet supplements;
- the resulting nine marked denominator occurrences after the total-energy
  residue;
- cyclic occurrence data.

The packet does **not** record:

- an expanded adjoint numerator;
- oriented simplex determinants or term coefficients;
- a proof that every listed reciprocal denominator product occurs with unit
  coefficient;
- a normalization matching the source canonical form.

The checker `derive_polygon_ofpt_packet.py` verifies incidence and denominator
rank. It does not compute canonical-form weights.

Consequently the expression

\[
\sum_{T=1}^{180}
\frac{1}{G\prod_i g_i\prod_{a\in T}q_a}
\]

is not admitted as \(\Omega_{C_5}\) merely from the current packet.

## Narrow correction

Entry 1233's period target remains well typed only abstractly:

\[
\Pi_{C_5}
=
\int_{\Gamma_3}
\frac{du_1\,du_2\,du_3}{\sqrt{\det H}}
\,\Omega_{C_5}(X,y(u;P)).
\]

The contour, Cayley--Menger measure, multi-Kummer cover, and marked pole
carrier are frozen. The expanded coefficient form required for symbolic
period reduction is not yet frozen.

Therefore the completed Landau-support census in Entries 1237--1244 remains
valid: it depends only on the frozen pole carrier. It must not be promoted to
a Picard--Fuchs theorem for an unserialized integrand.

## Finite next falsifier

Construct \(\Omega_{C_5}\) by one source-authorized route:

1. derive the oriented canonical forms of the 180 incidence simplices,
   including their determinant weights and a shared projective orientation;
2. sum them and verify canonical residues on every source facet; or
3. independently derive the adjoint numerator from the frozen pole set and
   canonical residue conditions, then compare it with the triangulation sum.

Acceptance requires equality as a rational function, cyclic covariance, and
the source normalization. Only then may the resulting three-variable period
be passed to a creative-telescoping or Gauss--Manin engine.

## Classification

\[
\boxed{
\text{carrier and contour fixed}
\quad|\quad
\text{canonical coefficient object defined abstractly}
\quad|\quad
\text{expanded period input not yet serialized}
}
\]

No new cosmological carrier datum is indicated.

