---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 702 — The Generic Five-Pole Euler Rank Is Sixty

## Hard-to-vary claim

Before homogeneous specialization, the generic five-pole family of Entry
700 has Euler/deletion--restriction rank

\[
\boxed{60}.
\]

This is a rank theorem for the two corners of the derived base-change
problem. It is not a construction of the comparison map
\(\beta_{\rm GM}\), its cone, or its support.

## Generic restricted geometry

On the fifth-pole divisor

\[
q_{\mathcal G_{12}}=X_1+X_2+X_3+c=0,
\]

set \(c=-(X_1+X_2+X_3)\). The four retained marked lines become

\[
L_1:b=X_2+X_3,
\qquad
L_2:a=X_1+X_3,
\]

\[
L_3:a+b=-X_3,
\qquad
L_{23}:b=X_1.
\]

The restrictions of the generic Cayley--Menger branch polynomial to every
one of these lines are quartics in the residual coordinate. Exact
square-free tests at the three rational generic points

\[
(X;P)=(2,3,5;7,11,13),
\]

\[
(X;P)=(3,5,7;11,13,17),
\]

and

\[
(X;P)=(5,7,11;13,17,19)
\]

give degree four, square-free degree four, and nonzero discriminant for all
four lines. A single such witness proves that each symbolic discriminant is
not identically zero; the repeated witnesses guard against accidental
specialization. Hence every line has four distinct branch punctures on the
generic locus.

## Deletion census

In source order \((L_1,L_2,L_3,L_{23})\), the numbers of new finite line
intersections are

\[
(0,1,2,2).
\]

The last count is two because \(L_1\) and \(L_{23}\) are parallel. A line
with four branch punctures and \(m\) new finite intersections contributes
\(4+m-1\). Therefore the increments are

\[
\boxed{(3,4,5,5)}.
\]

Starting from the rank-nine absolute \(q_{\mathcal G_{12}}\)-residue
surface gives

\[
\boxed{
\operatorname{rank}M^{\rm gen}_{4|G}
=9+3+4+5+5=26.
}
\]

The generic lower deletion has source rank 34, so

\[
\boxed{
\operatorname{rank}M^{\rm gen}_5=34+26=60.
}
\]

## Homogeneous comparison

Entry 596 proved

\[
\operatorname{rank}M^{\rm hom}_5=15+20=35.
\]

Thus the two cohomological corner ranks differ by

\[
\boxed{60-35=25}.
\]

Geometrically, homogeneous specialization simultaneously rationalizes the
generic lower algebraic sector and turns three of the restricted quartics
into forced-square branch configurations.

## Derived-base-change discipline

The number 25 is not yet

\[
\dim H^\bullet(\operatorname{Cone}\beta_{\rm GM}).
\]

Ranks do not construct \(\beta_{\rm GM}\), determine cancellations between
cohomological degrees, or locate higher Tor and vanishing-cycle support.
Entry 701's acceptance contract therefore remains active.

The legitimate conclusion is only:

\[
\boxed{
\text{any finite model of }\beta_{\rm GM}\text{ must account for a
generic-to-homogeneous Euler-rank change of }25.
}
\]

This rules out a degreewise free rank-preserving model, but it does not by
itself classify the derived comparison as obstructed.

## Consequence for \(\mathcal Q\)

No \(\mathcal Q\)-valuation is admissible yet. The rank change occurs along
the entire homogeneous normal locus \(I=0\), while \(\mathcal Q=0\) is a
further divisor inside that locus. Only an explicitly constructed cone can
separate its universal homogeneous contribution from residual
\(\mathcal Q\)-supported cohomology.

## Evidence

- `research/benincasa/check_generic_five_pole_base_change_rank.py`;
- `research/benincasa/generic-five-pole-base-change-rank.json`;
- Entries 185, 596, 700, and 701;
- allocator claim `seqclaim-77cd7b3d1f86521251c7ebd7`.

## Next falsifier

Construct a finite labelled twisted de Rham model over
\(A/I^3\) whose generic and homogeneous Euler characteristics reproduce 60
and 35. Then construct the canonical derived base-change map on that model
and compute its cone separately on
\([\nu_1\nu_2]\), \([\nu_1\nu_3]\), and \([\nu_2\nu_3]\). Reject any model
that obtains 25 only by an untyped quotient or fitted cancellation.
