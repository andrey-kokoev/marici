# A sublogarithmic shell rank restores compact-height summability

The fixed-rank no-go leaves a constructive alternative. Center the shell
coordinate as `x=r-1/4`, so `|x|<=1/2`; the removed scalar phase is harmless.
On a compact height set `|T|<=A`, projection onto polynomials through degree
`m-1` is no worse than Taylor truncation, whose remainder obeys

```
delta_m(T) <= exp(A) (A/2)^(2m)/(m!)^2.             (1)
```

Choose a shell-dependent rank

```
m_k = ceil(c log(log k)/log(log(log k)))             (2)
```

for all sufficiently large `k`. Stirling's formula gives, uniformly on the
chosen compact height set,

```
delta_(m_k)(T) <= (log k)^(-2c+o(1)).                (3)
```

Therefore

```
sum_k delta_(m_k)(T)/k < infinity                    (4)

```

whenever `c>1/2`, locally uniformly in `T`. The same argument survives any
fixed number of `T` derivatives: differentiating only contributes fixed
powers of the bounded coordinate and polynomial factors in `m`, which are
absorbed by the strict margin `2c>1`.

This is an upper bound, not an optimality theorem. It establishes that the
height obstruction does not force a full infinite fiber in every finite
shell. A finite but growing moment fiber—with remarkably slow growth—can
make the discarded prime phase Hilbert--Schmidt on every compact height set.

## Scope correction: source vector, not full operator

The estimate above controls the distinguished Euler phase vector in each
shell. It does not control `(1-P_m)M_xP_m` on the entire moment space. The top
Jacobi coefficient tends to `1/4`, so the full generator leakage remains
nonsummable for every hard rank schedule. Accordingly, “Hilbert--Schmidt” in
this packet applies only to the assembled distinguished-source leakage, not
to an operator intertwiner or analytic Fredholm family. See
`growing-moment-generator-boundary-no-go.md`.

## New architectural target

Use the quarter-shifted constant channel for the gamma covariance and attach
`m_k-1` centered moment channels to shell `k`. The remaining tasks are:

1. define compatible weighted Mackey pull--push maps between these varying
   fibers;
2. prove that the compressed height family and its derivatives have the
   required Schatten-class bounds;
3. identify a determinant renormalization whose constant channel retains the
   gamma factor while the moment channels reproduce the Euler phases;
4. test whether the required growing multiplicity corrupts compact resolvent
   or zero multiplicity.

The falsifier is now quantitative: any proposed ranks `m_k` must make the
weighted projection-error series converge locally uniformly in height.
