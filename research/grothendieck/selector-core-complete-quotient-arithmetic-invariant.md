# The selector normal core is a complete quotient-arithmetic invariant

## Classification theorem

For a finite group `G` and selector `c`, define

`K_c=Core_G(Stab_R(c))`.

A normal subgroup `K` is selector-admissible for `c` exactly when

`K subset K_c`.

The forward direction uses normality: if `K subset Stab_R(c)`, then `K` lies
in every conjugate of the stabilizer and hence in its core. The reverse
direction is immediate.

Consequently two selectors `c,d` have identical admissible normal-kernel
down-sets if and only if `K_c=K_d`. Since the resonance decoration `R(K)`
depends only on `G` and `K`, equal cores also give identical decorated
quotient lattices and identical terminal arithmetic spectra.

The core is therefore a complete invariant of quotient--arithmetic behavior,
but not a complete invariant of selectors themselves.

## Exact S3 separator

On `S3`, compare:

- the fully labelled selector, whose stabilizer is trivial;
- the right-coset selector for a nonnormal transposition subgroup, whose
  stabilizer has order two.

The selectors and their raw stabilizers differ, but both normal cores are
trivial. Exact subgroup enumeration confirms that both admit only the trivial
normal kernel and therefore carry the same quotient--arithmetic behavior.

## Scope

This equivalence forgets all selector information not visible to normal deck
quotients. It neither identifies the physical observables nor supplies a
Betti relative-chain pushforward.
