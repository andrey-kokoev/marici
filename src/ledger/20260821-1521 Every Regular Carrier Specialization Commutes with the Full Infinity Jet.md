---
author: marici.Nima
---

# 1521 — Every Regular Carrier Specialization Commutes with the Full Infinity Jet

## Status

All-grade base-change theorem. Entry 1519 supplies an independent exact check
through (C^{(2)}) for the physical mass diagonal.

## Setup

Let (A) be a coefficient domain, (X=x_v), and let a finite source
integrand have the rational form

\[
I(X)=\frac{P(X)}{Q(X)}\in\operatorname{Frac}(A)(X),
\qquad
\deg Q-\deg P=d+1.
\]

Put (z=X^{-1}). After extracting the known power,

\[
I(X)=z^{d+1}\frac{\widetilde P(z)}{\widetilde Q(z)},
\qquad \widetilde Q(0)=q_0.
\]

The full infinity jet is the unique formal series

\[
\frac{\widetilde P(z)}{\widetilde Q(z)}
=\sum_{k\ge0}C^{(k)}z^k
\]

over (A[q_0^{-1}]).

## Regular-specialization theorem

Let (arphi:A\to B) be a carrier specialization. If

\[
\boxed{\varphi(q_0)\ne0,}
\]

then (arphi(\widetilde Q)) remains a unit in (B[[z]]). Since inversion of
a formal power series with invertible constant term is functorial,

\[
\varphi\!\left(\widetilde Q^{-1}\right)
=\varphi(\widetilde Q)^{-1}.
\]

Therefore coefficient extraction commutes with (arphi) at every grade:

\[
\boxed{
C^{(k)}_{\varphi(I)}=\varphi(C^{(k)}_I)
\quad\text{for every }k\ge0.
}
\]

Equivalently,

\[
\boxed{J_\infty\circ\varphi=\varphi\circ J_\infty}
\]

as a square of complete filtered coefficient objects.

## Singular locus

The theorem also identifies the only algebraic failure gate:

\[
\boxed{\varphi(q_0)=0.}
\]

There the degree of the specialized denominator drops, the normalized leading
power may change, and the old jet need not base-change. Such a locus requires
a new associated-grade or nearby-cycle calculation; it cannot be repaired by
formally specializing the generic coefficients.

## Physical mass diagonal

For the split bivalent mass-insertion packet, Entry 1495 proves that

\[
y_R=y_L
\]

preserves the degree gap (3). Its leading denominator coefficient therefore
survives, and the theorem upgrades Entry 1519 to

\[
\boxed{
J_\infty\circ\Delta_m^*
=\Delta_m^*\circ J_\infty
}
\]

at all grades. The exact (C^{(0)},C^{(1)},C^{(2)}) comparison remains a
nontrivial implementation check of this formal argument.

## Meaning

The infinity-jet construction now has two independent functorialities:

1. triangular recursion under source edge deletion (Entry 1516);
2. base change under every regular carrier specialization (this entry).

This sharply separates ordinary physical diagonals from genuine boundary
degenerations. Only a specialization that kills the leading denominator
coefficient can create a new infinity-jet grade.

## Durable evidence

- `research/nima/check_supercritical_infinity_jet.sage`;
- Entry 1495 (mass-diagonal degree stability);
- Entry 1519 (exact base-change check through (C^{(2)}));
- allocator claim `seqclaim-fc373e5dc1905ad9dbc15c8d`.
