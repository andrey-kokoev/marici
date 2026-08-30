# 3812 — Local Inertia Forbids Ordinary Generic-to-Physical Kummer Contiguity

## Hard claim

The generic counting twist and physical Kummer twist cannot be connected by a
nonzero coefficient-local horizontal morphism near a smooth point of the
Cayley–Menger branch.

## Calculation

For a rank-one Kummer coefficient with exponent `gamma`, local inertia around
the branch is the character

```text
chi_gamma = exp(2 pi i gamma).
```

The two exponents are

```text
gamma_generic  = 5,
gamma_physical = -1/2.
```

Hence

```text
chi_generic  = +1,
chi_physical = -1.
```

The internal Hom from the generic coefficient line to the physical one has
character

```text
chi_Hom = chi_physical / chi_generic = -1.
```

A horizontal local morphism would be an inertia-invariant section of this Hom
line. In characteristic zero, invariance requires `f = -f`, hence `f = 0`.

Equivalently, the exponent difference is

```text
-1/2 - 5 = -11/2,
```

which is not an integer. Multiplication by an integral power of the branch
polynomial therefore cannot provide ordinary Kummer contiguity.

## Relation to Entry 3807

Entry 3807 found that the complete derivative-word kernels differ and that
identity on words does not descend. The inertia calculation explains why this
failure is structural rather than a poor finite basis choice: the two word
systems are representations of coefficient local systems with inequivalent
branch characters.

## Narrow conclusion

The proposed generic-to-physical arrow cannot be an ordinary local
coefficient morphism. Any valid bridge must add independently derived data,
such as a correspondence carrying the sign character, a nearby-cycle or
limiting construction with its own variance, or a source-defined
twist-changing kernel.

No such bridge is needed to define the physical period directly. The clean
frontier is therefore the source-normalized Leray covector constructed inside
the physical `gamma = -1/2` system itself.

This result does not compare abstract cohomology vector spaces and does not
exclude a separately derived nonlocal correspondence.

## Artifacts

- `research/benincasa/checkers/check_rank26_twist_local_inertia_obstruction.py`
- `research/benincasa/results/rank26-twist-local-inertia-obstruction.json`

Allocator claim: `seqclaim-4bd9716c857835ae1acdb0ff`.
