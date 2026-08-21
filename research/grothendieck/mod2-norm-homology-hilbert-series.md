# The residual mod-two norm homology has a closed Hilbert series

Epistemic-graph event: 1361.

## Graded theorem

Write the five-site group algebra as

`A=F_2[epsilon_1,...,epsilon_5]/(epsilon_i^2)`

with augmentation degree one for every `epsilon_i`.  For a collapsed branch
set `B` of size `k`, the norm differential is multiplication by

`epsilon_B=product_(i in B) epsilon_i`.

Factor `A=A_B tensor A_(B^c)`.  On `A_B`, multiplication by `epsilon_B` is
nonzero only on the unit: its image is the top monomial, while its kernel is
the span of all nonunit monomials.  Consequently

`H(A,N_B)=(ker N_B/im N_B)`

has basis

`epsilon_I epsilon_J`

with `empty != I proper_subset B` and arbitrary `J subset B^c`.

Its Hilbert series is

`H_k(t)=(1+t)^(5-k) ((1+t)^k-1-t^k)`.

Evaluation at `t=1` gives

`2^(5-k)(2^k-2)`,

recovering Ledger 1340's total dimensions.

## Controls

- `k=1`: `H_1(t)=0`.
- `k=2`: `H_2(t)=2t(1+t)^3`, with graded dimensions `2,6,6,2`.
- `k=5`: `H_5(t)=5t+10t^2+10t^3+5t^4`.

The full-collapse homology therefore reproduces the proper nonempty Boolean
subsets of the five branch directions; the empty and full subsets are
removed respectively by the kernel condition and norm image.

## Scope

This identifies exactly where the formal bad-prime information lives in the
augmentation filtration.  It is not relative-chain homology and does not
assert physical support for the corresponding simultaneous branch strata.
Any physical comparison must first construct the missing specialization and
then compare its filtration with this formal deck module.
