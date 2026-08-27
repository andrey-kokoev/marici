# The scalar dagger lift of the backward equalizer is rank one and cannot recover the prime-exclusion Ward form

## Canonical dagger lift

The linear prime-scale equalizer on a zero-state is

\[
(1+q)R_p=q(A_1+qB_2).
\]

Tensoring with its conjugate gives the exact positive identity

\[
|1+q|^2|R_p|^2
=|q|^2|A_1+qB_2|^2.
\]

This lift is source-derived and preserves the primitive-square interference
term. It is the canonical sesquilinear shadow of the linear mate.

## Rank obstruction

Let `C_X` be a finite labelled coefficient module and write the scalar
primitive transform as a covector

\[
R_p(c)=\rho_p c.
\]

Then its dagger square is the quadratic form

\[
|R_p(c)|^2
=c^*\rho_p^*\rho_p c.
\]

The matrix `rho_p^* rho_p` has rank at most one, independently of the seam
coefficients multiplying it.

By contrast, the native prime-exclusion Ward form is

\[
W_p(c)=\lVert P_{p\nmid n}c\rVert^2.
\]

Its rank is the number of independently retained `p`-free labels. At the
smallest prime-two module with labels `(1,2,3)`,

\[
P_{2\nmid n}
=\operatorname{diag}(1,0,1),
\]

which has rank two. Therefore no scalar backward covector, after any dagger
square or nonzero scalar weighting, can reproduce the ambient Ward form.

## Consequence for `3+2+1`

The linear backward equalizer is valid but already scalarized. Its canonical
dagger lift controls one coherent combination of the exclusion labels, not
the complete exclusion packet.

The order of operations must be reversed:

```text
failed order:
  aggregate labels -> scalar backward mate -> dagger square

required order:
  retain labelwise backward mates -> form vector/pro-valued packet
  -> dagger or exterior square -> compare with Ward projection
```

Thus the backward witness tower needs a label-separating rung before its
sesquilinear rung. This is the same complete-first, compress-last rule found
in the other sectors.

## Minimal observer count

On an unrestricted cutoff module, any family of `m` scalar backward covectors
produces a Gram form of rank at most `m`. To recover the exclusion Ward form,
one needs at least

\[
m\ge\operatorname{rank}P_{p\nmid n}.
\]

That rank grows with the cutoff. Therefore no fixed finite family of scalar
backward observers can recover the completed Ward tower on unrestricted
label packets. The natural target is a labelwise or pro-valued backward
correspondence.

## Scope

A smaller source-dynamical null pullback could have lower effective rank. But
that restriction must be independently derived; it cannot be chosen to make
the scalar form sufficient. On the ambient labelled module, the rank
obstruction is exact.

## Durable verification

- Checker: `checkers/check_scalar_dagger_ward_rank_obstruction.py`
- The checker verifies the exact prime-two ranks and a representative
  rank-one dagger form.
