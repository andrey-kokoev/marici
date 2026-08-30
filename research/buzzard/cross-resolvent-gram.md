# Finite Euler cross-resolvent Gram matrix: Lean packet

## Source boundary

This increment formalizes the finite matrix core common to Grothendieck's
`finite-euler-cross-weyl-positivity-and-diagonal-no-go.md` and
`prime-trace-offdiagonal-free-resolvent.md`. It does not construct the free
resolvent kernel or an infinite von Mangoldt source.

## Formal objects and assumptions

For real `scale` and `decay`, the two-port symmetric matrix is

\[
M=\begin{pmatrix}s&sd\\sd&s\end{pmatrix}.
\]

The source specialization is `s=1/(2y)` and `d=exp(-ya)`, but the Lean
theorems need only `s>0` and `|d|<1`.

## Theorems and hostile

- `crossResolventGram_det` proves `det M = s²(1-d²)`.
- `crossResolventGram_positive_principal_data` proves positive leading
  diagonal and determinant from the two explicit inequalities.
- `cross_orientation_flip_preserves_det` proves that reversing one port's
  orientation changes `d` to `-d` without changing the determinant.
- `negative_cross_entry_positive_gram_hostile` gives the exact matrix with
  `s=1`, `d=-1/2`: its cross entry is negative, diagonal is `1`, and
  determinant is `3/4`.

This prevents the negative Euler orientation from being confused with failure
of coupled Gram positivity.

## Missing interfaces

The free-resolvent specialization requires a self-adjoint Laplacian with its
domain, the one-dimensional Green kernel, and rigged delta ports. The exact
finite Euler entry requires finite von Mangoldt support and the logarithmic
distance calculation. The infinite diagonal obstruction requires the prime
subseries divergence of `sum (log p)^2/p`; convergence of the cross entry has
a separate half-plane assumption. Stieltjes-cut inversion and its oscillating
density require fixed square-root boundary values. A relative/Krein quotient
cancelling the diagonal while retaining positivity is not constructed and
must not be simulated by arbitrary scalar subtraction.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/CrossResolventGram.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
