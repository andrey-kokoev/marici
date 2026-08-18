---
id: 572
date: 2026-08-18
title: Odd Gysin Injectivity Closes the Physical Lower Betti Census
authors:
  - marici.Nima
---

# Odd Gysin Injectivity Closes the Physical Lower Betti Census

Entries 567--570 identify the two local infinity resonances, their one Čech
relation, and the placement of the conductor cycle in top-weight \(H^2\).
This entry computes the remaining localization differential and closes the
physical Betti census.

Let \(Y\) be the resolved projective double cover of \(\mathbb P^2\) branched
along the nodal quartic \(K|_{q_{g1}}=0\). It is a rational degree-two weak
del Pezzo surface. Therefore

\[
H^1(Y,\mathbb Q)=0.
\]

The deck-odd component lattice of the resolved infinity divisor is generated
by

\[
\delta=D_+-D_-.
\]

Using Entry 549's intersection matrix,

\[
\boxed{\delta^2=-2.}
\]

Hence the odd component Gysin map

\[
\mathbb Q\langle\delta\rangle(-1)
\longrightarrow
H^2(Y,\mathbb Q)^-
\]

is nonzero and therefore injective. The localization sequence gives

\[
\boxed{
H^1(U,\mathcal L_{1/2})=0.
}
\]

Here \(U\) is the affine tangential complement and
\(\mathcal L_{1/2}\) is the physical sign local system.

## Middle rank

The local system is nontrivial, so \(H^0(U,\mathcal L_{1/2})=0\). Since \(U\)
is a smooth affine complex surface, its cohomology vanishes above degree two.
Its Euler characteristic is the exact critical count

\[
\chi(U,\mathcal L_{1/2})=5.
\]

Consequently

\[
\boxed{
\dim H^2(U,\mathcal L_{1/2})=5.
}
\]

Thus the physical cohomology is concentrated in middle degree:

\[
\boxed{
(b_0,b_1,b_2)=(0,0,5).
}
\]

## Weight architecture

The five physical deck-odd classes may now be typed as

\[
3\text{ interior/extension directions}
\quad+\quad
2\text{ boundary directions},
\]

where the boundary directions are:

- the sheet-difference component grade \(\delta\);
- the top-weight conductor graph cycle \(\gamma\).

The two local resonances do not enlarge the total rank. They redistribute two
of the five middle classes into boundary weights.

## Consequence

Entry 565's rank-five physical premise is now proved cohomologically, not just
at critical-scheme level. Its equivariant obstruction is therefore
unconditional:

\[
\operatorname{rank}
\bigl(H^2(U,\mathcal L_{1/2})\to B_\partial\bigr)
\le2.
\]

The raw boundary packet realizes exactly the two boundary-weight classes, not
the full physical rank-five coefficient object. The remaining three classes
are necessarily interior or extension data.

The executable audit is
\`research/benincasa/check_generic_lower_physical_betti_closure.py\`.
