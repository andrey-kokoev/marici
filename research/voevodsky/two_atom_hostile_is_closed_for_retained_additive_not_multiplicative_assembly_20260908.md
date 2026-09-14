# Two-atom hostile is closed for retained additive, not multiplicative, assembly

Date: 2026-09-08

## Retained additive assembly

For distinct primes, the selected G1 source assembly is the labelled direct sum

\[
e_p\oplus e_q.
\]

Its support is the disjoint union of the `p` and `q` prime-power fibres.  It
contains no `pq`-labelled primitive coordinate.  Hence

\[
\pi_{\rm prim,pq}(e_p\oplus e_q)=0
\]

by source typing, before applying any observer.

Every retained G1 component commutes with prime idempotents.  The direct-sum
Green form therefore satisfies

\[
G(P_px,P_qy)=0\qquad(p\ne q).
\]

Thus the invisible-feature hostile from the generic two-atom audit cannot
occur inside the selected additive assembly: an extra cross-prime vector would
leave the declared source support, and an extra mixed Green block would violate
the proved idempotent relation.

A finite audit over distinct pairs from the first six primes checked both
support absence and zero mixed blocks in 60 assertions.

## Same-prime qualification

This does not force grade diagonality.  Primitive and square vectors in one
prime fibre have an authorized nonzero Gram overlap, and later fibrewise
Wronskian codiagonalization may combine grades.  Those terms remain provenance-
tracked inside `G_p`.

## G2 consequence

The generic phrase “two-atom assembly” must distinguish two operations:

1. labelled additive/direct-sum assembly, whose mixed-prime coherence is closed;
2. multiplicative or star assembly with a genuine `pq` target, which is not
   constructed by the retained G1 carrier and remains open if G2 requires it.

Scalar Euler multiplication cannot be used to promote the first operation to
the second.  The next G2 specification must say whether multiplicative assembly
is actually admitted.  If it is, its `pq` interface and mixed Green cell need a
new source rule.  If it is not, the cross-prime two-atom hostile is already
resolved by G1.4.

## Evidence

- `check_marici_rh_two_atom_retained_additive_assembly_20260908.py`
- `marici_rh_two_atom_retained_additive_assembly_certificate_20260908.json`
- `research/nima/rh-g1-4-prime-diagonality-is-exact-on-the-retained-labelled-carrier.md`
