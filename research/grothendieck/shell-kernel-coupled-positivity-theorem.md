# The shell-kernel leakage has a universal positive determinant

The prime-to-shell map fits an orthogonal decomposition

```
H_prime = V_shell + K_shell,
```

where `V_shell` contains the retained moment channels and `K_shell` is the
discarded within-shell sector. Height multiplication does not preserve this
splitting. Its off-diagonal leakage is an operator

```
B(T): V_shell -> K_shell.
```

For the distinguished Euler source vector, the growing-rank schedule gives a
square-summable assembled defect bounded by the weighted projection-error
series

```
||B(T)||_2^2 <= sum_k delta_(V_k)(T)/k < infinity
```

locally uniformly in height. This does not establish that the full operator
leakage `(1-P)M_xP` is Hilbert--Schmidt; the top Jacobi boundary makes that
stronger statement false. The theorem below applies if an independently
source-derived Hilbert--Schmidt operator `B` is supplied.

## Universal coupled-positivity theorem

For any Hilbert--Schmidt operator `B:V->K`, form the skew-adjoint doubled
operator

```
J_B = [ 0   -B* ]
      [ B    0  ].
```

Then `J_B` is Hilbert--Schmidt, `J_B^2` is trace class, and

```
det_2(I+J_B) = det(I+B*B) = product_j (1+s_j(B)^2) > 0.   (1)
```

Here `det_2` is the second regularized Fredholm determinant. The identity
follows by pairing the eigenvalues `+i s_j` and `-i s_j`; their linear
regularization factors cancel. Equivalently it is the Schur determinant of

```
[ I  -B* ]
[ B   I  ].
```

This is the first genuinely universal coupled positivity available in the
shell model: positivity is not imposed on a prime determinant and does not
come from deleting `K_shell`. It is forced by the oriented off-diagonal pair
`B,-B*`.

## What it does and does not solve

The theorem gives the correct Schatten consequence once `B` is
Hilbert--Schmidt. The slowly growing schedule supplies this only for the
distinguished-source defect, not for full moment-bundle height evolution.
For the latter, hard truncation remains non-Hilbert--Schmidt and the positive
determinant is unavailable without a further soft-cutoff or cancellation.

It does **not** prove that this determinant is the gamma factor, the Euler
product, `Xi`, or one. Nor does it provide an unavailable physical
relative-chain pushforward. Equality with the completed zeta determinant
would require a source-derived identification of the compressed diagonal
block and this Schur correction. Declaring the correction trivial would be
the fitted cancellation warned against by Nima.

The next falsifier is finite and hostile: construct the compressed height
matrix for several shifted shells and compare its exact block determinant
with the product of the retained determinant and `det(I+B*B)`. Any remaining
diagonal `K_shell` factor or non-Schur term must be retained explicitly.
