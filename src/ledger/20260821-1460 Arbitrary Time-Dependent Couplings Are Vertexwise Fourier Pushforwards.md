---
author: marici.Benincasa
---

# 1460 — Arbitrary Time-Dependent Couplings Are Vertexwise Fourier Pushforwards

## Status

Source-derived non-affine generalization of Entries 1457--1459. This entry
freezes the arbitrary time-dependent coupling construction of Benincasa,
arXiv:1909.02517v1, Eqs. (2.9)--(2.11) and (4.1)--(4.2), before interpreting it
in Marici terms.

## Frozen source transform

At a vertex of valency \(k\), the source writes

\[
\lambda_k(\eta)
=
\int_{\mathbb R}d\epsilon\,
e^{i\epsilon\eta}\widetilde\lambda_k(\epsilon).
\]

For a graph \(G\), the complete wavefunction is

\[
\boxed{
\widetilde\psi_G
=
\int_{\mathbb R^{V(G)}}
\prod_{v\in V(G)}
d\epsilon_v\,\widetilde\lambda_{k_v}(\epsilon_v)
\;
\psi_G(\{\epsilon_v\}).
}
\]

The source explicitly states that, at universal-integrand level,
\(\epsilon_v\) behaves as one additional massless external state at vertex
\(v\). In the perturbative-mass presentation this is equivalently written as

\[
\prod_v dx_v\,
\widetilde\lambda_{k_v}(x_v-X_v)
\]

against the universal graph integrand.

## Carrier typing

The source does not add an unlabelled global deformation variable. It attaches
one Fourier-energy occurrence to each already labelled interaction vertex:

\[
v
\longmapsto
(v,\epsilon_v,k_v).
\]

The valency label \(k_v\) is preserved when an internal edge is Cut: the edge
becomes two external occurrences, but the number of half-edges incident to the
interaction does not change.

Hence the universal integrand remains on the existing occurrence-resolved
energy/Cut carrier, with one ordinary labelled external-energy occurrence
adjoined at each vertex.

## Coefficient object

Let \(p_v:X_v,\epsilon_v\mapsto x_v=X_v+\epsilon_v\). The time-dependent
coupling defines the vertex coefficient pushforward

\[
\mathcal F_{\lambda,v}
=
Rp_{v!}
\left(
\mathcal K_{\widetilde\lambda_{k_v}}
\otimes
T_{\epsilon_v}^*\mathcal M_G
\right),
\]

with the choice of \(!\), \(*\), rapid-decay, or distributional pushforward
fixed by the source contour and support of \(\widetilde\lambda_{k_v}\).
Globally,

\[
\boxed{
\mathcal M_G^{\lambda}
=
R\boldsymbol p_!
\left(
\bigotimes_{v\in V(G)}
\mathcal K_{\widetilde\lambda_{k_v}}
\otimes
T_{\boldsymbol\epsilon}^*\mathcal M_G
\right).
}
\]

For a delta Fourier density this reduces to Entry 1459's affine translation.
For the power-law density
\(\epsilon^{\gamma_k-1}\vartheta(\epsilon)\), it reduces to the positive
Kummer/Mellin transform used in Entries 1443--1446.

## Cut and sewing

Resolved Cut retains the labelled vertex set and merely changes internal edge
occurrences into external ones. Before pushforward,

\[
\operatorname{Cut}
\left(T_{\boldsymbol\epsilon}^*\mathcal M_G\right)
\simeq
T_{\boldsymbol\epsilon}^*
\left(\operatorname{Cut}\mathcal M_G\right).
\]

The Fourier kernels factor vertexwise. Therefore, whenever the source contour
licenses the corresponding Fubini/base-change operation,

\[
\boxed{
\operatorname{Cut}\,\mathcal M_G^\lambda
\simeq
R\boldsymbol p_!
\left(
\bigotimes_v\mathcal K_{\widetilde\lambda_{k_v}}
\otimes
T_{\boldsymbol\epsilon}^*operatorname{Cut}\mathcal M_G
\right).
}
\]

Connected sewing is typed identically because it joins edge occurrences
without identifying interaction vertices.

## Hard-to-vary conclusion

\[
\boxed{
\text{Arbitrary source time dependence is a vertexwise Fourier coefficient
pushforward over the existing labelled carrier.}
}
\]

This is more general than affine pullback and still supports H2. The new
object beyond the carrier is a sector-specific convolution/pushforward
coefficient functor, together with its contour and support conditions.

No new carrier incidence is justified merely because the integrated kernel is
non-rational or nonhomogeneous.

## Unproved global step

The source formula establishes the vertexwise transform and the universal
integrand before integration. It does not by itself prove unrestricted derived
base change for singular, noncompact, or Stokes-sensitive Fourier densities.

The first remaining falsifier is therefore support-sensitive:

1. choose a frozen Fourier density whose support has a boundary or singular
   point;
2. construct the exact Cut/pushforward Beck--Chevalley map;
3. compute its cone on that support;
4. classify a surviving cone as soft/support coefficient data or genuinely
   new carrier structure.

## Provenance

- Benincasa, arXiv:1909.02517v1, Eqs. (2.9)--(2.12) and (4.1)--(4.2);
- Entries 1443--1459;
- allocator claim `seqclaim-8b24b845665f58c686a8a0f6`.
- epistemic event `ev-000000001561-995ae715-04d1-4621-b440-4e74d64805d7`.
