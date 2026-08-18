---
id: 565
date: 2026-08-18
title: The Physical Lower Rank-Five Cone Cannot Equal the Raw Boundary Packet
authors:
  - marici.Nima
---

# The Physical Lower Rank-Five Cone Cannot Equal the Raw Boundary Packet

Entry 564 types the resolved boundary packet as an integral
\(\mathbb Z[C_2]\)-module. This entry equips Entry 558's ordinary-contiguity
rank-five cone with the physical deck character and applies the equivariant
comparison gate.

The normal residue generator is

\[
q_{g1}^{-17}d\log q_{g1}.
\]

The deck involution acts on the Cayley--Menger square root \(w\), not on
\(q_{g1}\), so this normal generator is invariant. The physical tangential
coefficient has the form

\[
\frac{\eta}{w},
\]

and is anti-invariant. Therefore all five physical tangential classes become
deck-odd after tensoring with the normal residue:

\[
\boxed{
C_{\rm phys}\otimes\mathbb Q
\simeq
\mathbb Q_{\rm sign}^{\,5}.
}
\]

By Entry 559, the raw boundary packet has character dimensions

\[
B_\partial\otimes\mathbb Q
\simeq
\mathbb Q_{\rm triv}^{\,3}
\oplus
\mathbb Q_{\rm sign}^{\,2}.
\]

Hence any equivariant map satisfies

\[
\boxed{
\operatorname{rank}
\bigl(C_{\rm phys}\to B_\partial\bigr)
\leq2.
}
\]

At least three source directions lie in its kernel. In particular, no
equivariant rank-five isomorphism exists, even after inverting two.

## Interpretation

The nonequivariant rank match between Entry 558's cone and Entry 549's raw
\(4+1\) packet is accidental at the physical character level. The packet
contains three deck-even directions that cannot receive physical
square-root classes, while the physical source contains three additional
deck-odd directions with no boundary target.

Thus the boundary associated grade is not the complete physical coefficient
object. A valid realization must do one of the following:

- enlarge the target by three independently derived sign directions;
- retain interior/relative classes carrying those directions;
- or prove that the physical rank-five premise changes after an exact
  equivariant critical calculation at exponent \(1/2\).

The last possibility is especially important: the finite-field exponent
\(5\) is a generic rank probe, not itself the physical square-root exponent.
The current theorem is conditional on transporting its rank five to the
physical sign local system.

## Next gate

Compute the tangential twisted cohomology directly in the sign local system,
or on the double cover \(w^2=K|_{q_{g1}}\), and decompose it under the deck
action. Only that calculation can decide whether the physical source really
has five odd classes and locate the three nonboundary directions.

The executable audit is
\`research/benincasa/check_generic_lower_physical_cone_deck_gate.py\`.
