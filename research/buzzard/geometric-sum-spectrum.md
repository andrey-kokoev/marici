# Geometric-sum Adams spectrum: Lean packet

## Source boundary

This increment formalizes the scalar eigenvalue mechanism shared by
Grothendieck's `coprime-cyclic-monodromy-adams-spectrum.md`,
`modular-cyclic-monodromy-adams-spectrum.md`, and
`finite-monodromy-exponent-adams-spectrum.md`. It does not claim the full
matrix/group theorem from the scalar calculation alone.

## Formal objects and coefficient types

`scalarGeometricSum x n` is the finite sum from exponent `0` through `n-1`.
The multiplication identity and zero-to-root implication hold over an
arbitrary commutative ring. The complete two-mechanism classification is
stated over an arbitrary field.

## Theorems and hostiles

- `scalarGeometricSum_mul_sub_one` proves
  `S_n(x)(x-1)=x^n-1`.
- `scalarGeometricSum_at_one` identifies the identity eigenvalue with the
  scalar image of `n`.
- `scalarGeometricSum_zero_implies_pow_eq_one` proves every vanishing
  eigenvalue is an `n`-th root of unity.
- `nontrivial_rootOfUnity_geometricSum_zero` proves the converse away from
  eigenvalue one.
- `scalarGeometricSum_zero_iff_characteristic_or_root` separates exactly the
  characteristic mechanism from the nontrivial root-of-unity mechanism.
- `characteristic_and_rootOfUnity_hostiles` exhibits both mechanisms over
  `ZMod 2` and `ZMod 5`.

## Missing interfaces

The full monodromy theorems require elementary-abelian kernels, faithful
finite-group representations, fiberwise twisted norm matrices, determinant
reduction to eigenvalues over an algebraic closure, control of Jordan
corrections, Cauchy's theorem, and the exponent criterion. Cyclic and
nonabelian quotients must remain distinct. Basis-level group-algebra
operations are not automatically ring Adams endomorphisms, and no physical
chain transfer is constructed.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/GeometricSumSpectrum.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
