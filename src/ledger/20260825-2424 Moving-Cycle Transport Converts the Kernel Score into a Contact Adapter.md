---
author: marici.Benincasa
date: 2026-08-25
---

# 2424 — Moving-Cycle Transport Converts the Kernel Score into a Contact Adapter

## Question

Entry 2421 proves that the literal \(K^{-1/2}\) normal jets recover the
rank-seven interaction module before integration. The main
Cayley--Menger boundary nevertheless moves when the momentum magnitudes
\(P_i^2=X_i^2+\nu_i\) vary at fixed site energies. The bare derivative
\(\partial_{\nu_i}K^{-1/2}\) is therefore not yet covariant under this
main-boundary transport.

## Source-normalized local lift

Use the generic rank-thirty-four lower family with the four frozen walls

\[
q_{g_1}=c+b+X_1,
\quad q_{g_2}=c+a+X_2,
\quad q_{g_3}=a+b+X_3,
\quad q_{g_{23}}=c+b+X_2+X_3.
\]

On a local chart where \(\partial_pK\ne0\), define

\[
V_i=-\frac{\partial_{\nu_i}K}{\partial_pK}\,\partial_p.
\]

Then

\[
\boxed{\partial_{\nu_i}K+V_i(K)=0.}
\]

Thus \(D_i=\partial_{\nu_i}+V_i\) transports the moving
Cayley--Menger boundary. Different nonvanishing pivots are local
presentations of the same Gauss--Manin operation; a single pivot zero is not
intrinsic support.

## Exact cancellation

For the source top form

\[
\omega=K^\gamma\prod_q q^{-1}\,dc\wedge da\wedge db,
\qquad \gamma=-\frac12,
\]

the covariant derivative is

\[
(\partial_{\nu_i}+\mathcal L_{V_i})\omega
=
\left[
\gamma\frac{\partial_{\nu_i}K+V_i(K)}K
+\operatorname{div}V_i
-\sum_q\frac{V_i(q)}q
\right]\omega.
\]

The first term vanishes identically. Therefore

\[
\boxed{
\nabla_{\nu_i}^{K\text{-bdry}}\omega
=
\left(
\operatorname{div}V_i-
\sum_q\frac{V_i(q)}q
\right)\omega.
}
\]

The interaction has not disappeared. It has moved from a bare kernel score
into the velocity field \(V_i\), whose action produces a divergence term and
source-labelled contact weights on the marked walls.

## Exact chart certificates

Using cyclicly matched pivots \((a,b,c)\) for \((\nu_1,\nu_2,\nu_3)\), the
three local representatives clear respectively against

\[
(\partial_aK)^2q_{g_2}q_{g_3},
\]

\[
(\partial_bK)^2q_{g_1}q_{g_3}q_{g_{23}},
\]

and

\[
(\partial_cK)^2q_{g_1}q_{g_2}q_{g_{23}}.
\]

Their cleared numerators are exact polynomials. No factor \(K^{-1}\)
remains.

## Support classification

- marked-wall poles are existing source support;
- a zero of one chosen \(\partial_pK\) is a lift-chart boundary;
- simultaneous failure of all fiber-gradient pivots on \(K=0\) is the
  existing Cayley--Menger/Landau discriminant;
- no new Carrier divisor is produced by main-boundary normal transport.

This gives a source-derived contact-weighted scalar transfer operation for
the main Cayley--Menger hypersurface, but not yet the complete physical-cycle
transfer or its period rank.

## Scope

The calculation is a chain-level local Gauss--Manin identity for \(K=0\).
The source semialgebraic cycle is also bounded by a labelled family of signed
Cayley--Menger minors. Tangency to those boundaries has not been checked, so
this entry must not yet be called a complete physical-cycle lift. It also
does not prove that the resulting period covectors jointly recover all seven
classes or supply the independently missing finite-momentum tensor vertex.

## Durable evidence

- `research/benincasa/check_physical_normal_gauss_manin_lift.py`;
- `research/benincasa/physical-normal-gauss-manin-lift.json`;
- sequence claim `seqclaim-7008bec9aca424b1e9442a72`.

## Next falsifier

Reduce the three contact-weighted covariant responses in the same rank-34
twisted quotient used by Entry 2413. Then close their orbit under the
admissible site-energy and marked-residue ports and compute the resulting
rank on the source interaction quotient. Any surviving kernel is now a
genuine physical-readout candidate rather than a moving-boundary artifact.
