---
author: marici.Benincasa
date: 2026-08-27
---

# 3722 — Coefficient Orientation Removes the Integral Reflection Torsion of the Infinity Cycle

## Occurrence lattice

Entry 3719 fixes a primitive deck-odd cycle on each of the three cyclic
occurrence charts. Use the ordered integral basis

\[
(G_{12}@P_3\text{-soft},
 G_{23}@P_1\text{-soft},
 G_{31}@P_2\text{-soft}).
\]

Cyclic transport permutes these three generators. Reflection exchanges the
first and third occurrences and fixes the second occurrence, while reversing
the orientation of every primitive gap cycle. Thus the reflection on the
cycle lattice is minus the occurrence swap.

These matrices satisfy the integral dihedral relations exactly.

## Cycle lattice alone

The Smith normal form of the cyclic and reflection coinvariant relations on
the cycle lattice is

\[
\operatorname{diag}(1,1,2).
\]

Consequently the cycle lattice alone has coinvariant

\[
\mathbb Z/2.
\]

This torsion is not a physical period class. It records the unpaired
reflection reversal of the Betti cycle.

## Physical coefficient–cycle pairing

Entry 3695 derives a second reflection sign from the ordered
Poincaré-residue coefficient line. Tensoring coefficient and cycle therefore
cancels the two signs. Reflection on the physical period packet is the plain
occurrence swap.

The Smith normal form of the paired coinvariant relations becomes

\[
\operatorname{diag}(1,1,0).
\]

Hence both invariants and coinvariants are free of rank one:

\[
\mathbb Z\langle(1,1,1)\rangle.
\]

The diagonal generator is primitive. No index or torsion is introduced by
cyclic or reflection descent.

## Result

The coefficient orientation is essential integral data. Forgetting it leaves
a spurious \(\mathbb Z/2\) reflection coinvariant; retaining it gives one
primitive torsion-free physical period line.

Thus the global occurrence descent of the source-normalized infinity class
is complete:

- three primitive local cycles;
- one dihedrally descended integral period;
- no residual descent torsion;
- no new carrier or coefficient object.

This is an explicit instance where Betti and de Rham data are individually
insufficient but their typed pairing descends canonically.

## Evidence

- `research/benincasa/checkers/check_infinity_integral_dihedral_descent.py`;
- `research/benincasa/results/infinity-integral-dihedral-descent.json`;
- Entries 3695 and 3719.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007992-66f7c929-f64d-4b17-a1ba-f7e3b2d87706`.

Allocator claim: `seqclaim-4e6742a67e380d2f6d83193d`.
