# 3816 — The Rank-26 Marked Geometry Has Boolean Profile Nine Plus Nine Plus Eight

## Question

After ordinary generic-to-physical contiguity is excluded, what is the
smallest support-sensitive structure on which the physical half-twist Leray
covector must be constructed?

## Frozen geometry

On the `q_G12` residue surface, the unmarked affine quartic complement has
Euler rank nine. The five marked lines meet the quartic in respectively

```text
(2, 2, 2, 4, 4)
```

distinct points. Among the ten line pairs, precisely two are parallel:

```text
(g1,g23), (g2,g31).
```

The other eight pairs meet at distinct affine crossings, and no crossing lies
on the quartic at the frozen generic point.

## Boolean rank function

For a subset `S` of marked lines, deletion gives

```text
r(S) = 9 + sum over i in S of (number(K intersect Li)-1)
          + number of nonparallel pairs contained in S.
```

Möbius inversion on the full five-mark Boolean lattice has grade totals

```text
absolute grade          9
single-mark grade       9
pair-crossing grade     8
triple-and-higher grade 0
```

Their sum is the established rank 26.

The singleton contributions are `(1,1,1,3,3)`. Every nonparallel pair has
coefficient one; the two parallel pairs have coefficient zero. Every subset
of size at least three has zero Möbius coefficient.

## Consequence for the Leray frontier

At the generic marked locus, the support-sensitive associated grade of the
physical readout requires only three kinds of input:

1. the rank-nine unmarked period packet;
2. five source-labelled wall packets of total rank nine;
3. eight source-labelled pair-corner packets.

No independent generic triple-mark period generator is predicted by the
deletion profile. Higher Čech terms may still supply relations and coherence,
but not a new Euler-rank contribution.

This turns the direct physical-half-twist construction into a finite
wall-and-corner problem. The next calculation is to derive the residue and
orientation maps from the canonical physical Leray germ to these five wall
and eight corner packets, then test Čech compatibility. The maps must be
source-derived; the rank profile does not select their values.

## Scope

This is an Euler/Möbius statement about the deletion filtration. It does not
assert that the rank-26 coefficient object splits canonically as a direct sum
of ranks `9`, `9`, and `8`, nor that every associated-grade class is selected
by the physical chain.

## Artifacts

- `research/benincasa/checkers/check_rank26_boolean_deletion_mobius_profile.py`
- `research/benincasa/results/rank26-boolean-deletion-mobius-profile.json`

Allocator claim: `seqclaim-5a11527ae9bd71ab2e01598d`.
