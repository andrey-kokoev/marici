# Selector stabilizer and maximal coefficient quotient

## Theorem

Let a finite group `G` act on itself by right translation and let
`c:G->R` be a frozen coefficient selector.  Define

`Stab_R(c)={k in G : c(gk)=c(g) for every g in G}`.

For a normal subgroup `K`, the selector descends through `G->G/K` if and
only if

`K subset Stab_R(c)`.

Thus `Stab_R(c)` is the largest kernel through which the coefficient selector
can descend whenever it is normal; in general the admissible normal kernels
are exactly the normal subgroups contained in the stabilizer.

The power--Mackey spectrum is a second gate applied only after this kernel
admission.  Algebraic compatibility cannot enlarge the selector stabilizer.

## Five-site selectors

For `G=(C2)^5`:

- the frozen identity selector `delta_0` has trivial stabilizer, so only the
  identity quotient is coefficient-admissible;
- the constant orbit trace has full stabilizer, so every quotient descends,
  but this is a different observable;
- a nontrivial character or coordinate selector has a codimension-one
  stabilizer and admits exactly kernels contained in that hyperplane.

## Scope

This classifies coefficient-side descent.  It does not construct a Betti
relative-chain pushforward, prove boundary compatibility, or identify a
physical observable after changing the selector.  It sharpens why the unit
sieve of Ledger 1282 cannot repair Ledger 1283's frozen-selector failure.

