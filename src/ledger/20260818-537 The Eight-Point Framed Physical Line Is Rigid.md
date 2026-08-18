---
id: 537
date: 2026-08-18
title: The Eight-Point Framed Physical Line Is Rigid
---

# The Eight-Point Framed Physical Line Is Rigid

Entry 536 separated the ambient derived (mathbb Z^5) from the uniqueness
question for the distinguished physical section.  This entry computes the
correct relative deformation diagram with all physical boundary values held
fixed.

On each of the eight Cut charts, the local object is the unique six-point
framed connector of Entries 388 and 421 tensored with the primitive
four-point unit.  Its fixed data are the generic (Q)-roof, Cartier residue,
endpoint swap, Tor orientation, and primitive coefficient (+1).  The local
relative deformation and automorphism groups are both zero.

On each of the twelve compatible pair overlaps, the object is the tensor of
three primitive four-point units from Entry 442.  Both ordered restrictions
and their Koszul sign are fixed.  A relative endomorphism must kill the tensor
unit and is therefore zero; the overlap has no residual gauge automorphism.

Consequently the Čech diagram of relative endomorphism complexes has ranks

\[
\boxed{C^0_{m rel}=0,qquad C^1_{m rel}=0}.
\]

Its degree-zero homology and its higher automorphism groups vanish.  Entry
533 supplies an existing global primitive section, so the framed section
space is nonempty and has exactly one component:

\[
\boxed{\text{the eight-point framed physical line exists and is rigid}.}
\]

The ambient free (mathbb Z^5) of Entry 536 does not act on this section.
Its representatives are derived edge cochains of the unfixed loaded object;
they do not preserve the predeclared primitive boundary values and hence are
absent from the relative endomorphism diagram.

This is a rigidity theorem in the same cellular fs/Kato sector as Entries
435--446 and 533.  It does not promote the construction to a raw global
scheme-level correspondence, nor does it establish higher-arity
factorization beyond the first octagon.

The next nonvacuous direction is no longer eight-point Cut coherence.  It is
either:

1. construct the raw algebraic/log six-functor comparison beyond the Kato
   sector; or
2. formulate the (n=10) physical Cut nerve and test whether the native Thom
   local system again cancels its Koszul holonomy before attempting a full
   cellular lift.

The executable audit is
`research/voevodsky/check_n8_framed_physical_line_rigidity.py`.
