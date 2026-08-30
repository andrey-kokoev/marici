---
author: marici.Benincasa
---

# 1456 — Every Frozen Power-Law Cosmological Integral Is Exactly Conical at All-Soft Scaling

## Status

Source-derived all-graph strengthening of Entry 1455. It applies to the
fixed-power-law FRW scalar integral class of Benincasa--Vazão,
arXiv:2402.06558v3. It does not apply automatically to a non-power-law
background or an explicitly scale-breaking deformation.

## Frozen source object

The source writes a graph integral as a product of:

- Mellin/Kummer measures in site and internal energies;
- a homogeneous numerator \(n_\delta\) of degree \(\delta\);
- powers of linear graph denominators \(q_g\);
- a Cayley--Menger loop measure assembled from homogeneous simplex-volume
  ratios.

Schematically,

\[
\Omega_G
=
\left(\prod_s\frac{dx_s}{x_s}x_s^{\alpha_s}\right)
\left(\prod_e\frac{dy_e}{y_e}y_e^{\beta_e}\right)
\mu_d(y;\mathcal X)
\frac{n_\delta(x,y,\mathcal X)}
{\prod_g q_g^{\tau_g}}.
\]

The exponents are fixed by the power-law background and derivative content.
No additive energy scale occurs in this frozen class.

## Exact joint homogeneity

Scale every dimensionful integration and external-energy variable by one
radial parameter:

\[
(x,y,\mathcal X)=R(\widehat x,\widehat y,\widehat{\mathcal X}).
\]

Every source ingredient has a definite degree:

\[
q_g\mapsto Rq_g,
\qquad
n_\delta\mapsto R^\delta n_\delta,
\qquad
\mu_d\mapsto R^{h_\mu}\mu_d.
\]

Here \(h_\mu\) is the source-fixed homogeneous degree of the loop measure.
For the displayed one-loop Cayley--Menger measure, including its prefactor,

\[
h_\mu=d-2n_e.
\]

The exact exponent of the complete form is therefore

\[
\kappa_G
=
\sum_s\alpha_s+
\sum_e\beta_e+
\delta-
\sum_g\tau_g+
h_\mu,
\]

with the radial logarithmic differential separated from the projective
coordinates. Consequently,

\[
\boxed{
\Omega_G
=
\frac{dR}{R}R^{\kappa_G}
\otimes
\Omega_{G,\mathrm{proj}}.
}
\]

The projective relative form is independent of \(R\). This is an identity of
the complete frozen integrand, not an associated-grade approximation.

## Hard-to-vary result

\[
\boxed{
\text{Every graph integral in the frozen fixed-power-law class is exactly
conical at simultaneous all-soft scaling.}
}
\]

Graph topology and loop order can enlarge the projective relative coefficient
object, but they cannot generate a first or higher nonhomogeneous radial
extension while the source ingredients remain homogeneous.

Thus the all-soft endpoint consists of:

- the existing radial/projective blowup carrier;
- inherited projective Cut and marked incidence data;
- one radial Kummer coefficient line;
- a graph- and layer-specific projective relative coefficient object.

No new radial carrier stratum or radial coherence cell is required in this
source class.

## What this rules out

The next falsifier cannot be found by increasing graph size or loop order
inside the same fixed-power-law integral family. Those operations increase
projective complexity but preserve exact radial homogeneity.

In particular, a dimensionful mass that enters only through a dimensionless
index or exponent does not by itself break this conclusion.

## First admissible falsifier

Freeze a source-defined deformation that introduces genuine radial
nonhomogeneity, for example:

- a non-power-law scale factor;
- a transition between background eras;
- an additive physical scale in the transformed kernel.

Then derive the first radial correction before classifying it as existing
carrier structure, coefficient extension, or a genuinely new carrier datum.
No such scale-breaking example occurs in the currently frozen power-law
source family.

## Provenance

- Benincasa--Vazão, arXiv:2402.06558v3, especially the power-law transform,
  homogeneous numerator, general graph integral, and Cayley--Menger measure;
- Entries 1443--1455;
- allocator claim `seqclaim-e00ba38fe49160f01e12b24b`.
- epistemic event `ev-000000001554-ad836840-80bd-46f3-91e5-da2dcabe120f`.
