# Squarefree prime-cube positivity is a Walsh-spectrum condition

Let `d` distinct primes index the vertices of the squarefree cube
`G=(C2)^d`. Assume the normalized cross correlation is translation compatible
on this cube:

```
K(x,y)=f(x+y),                         x,y in G.       (1)
```

The Gram operator is convolution by `f`. Walsh characters
`chi_eta(x)=(-1)^(eta dot x)` diagonalize it, with eigenvalues

```
lambda_eta=sum_(x in G) f(x)(-1)^(eta dot x).         (2)
```

Therefore

```
K>=0  iff  lambda_eta>=0 for every eta in G.          (3)
```

This turns all squarefree mixed-prime cycle constraints into a finite Fourier
positivity test. The two-prime even/odd rectangle inequalities are its first
nontrivial instance when opposite routes agree.

## Exact tensor/Mackey case

If coprime interchange gives

```
f(x)=product_j r_j^(x_j),                              (4)
```

then

```
lambda_eta=product_j [1+(-1)^(eta_j)r_j].             (5)
```

Every eigenvalue is nonnegative whenever `|r_j|<=1`. Thus exact Mackey
interchange plus the individual prime-edge contractions closes every finite
squarefree cube at once.

## Holonomy and failure of translation compatibility

If two routes to the same squarefree vertex give different correlations, the
kernel is not of the convolution form (1). That failure must first be recorded
as a route-holonomy matrix; the Walsh test cannot average it away. The earlier
`c-d` rectangle channel is the first such obstruction.

If route independence holds but (4) fails, the Walsh eigenvalues in (2)
measure higher mixed-prime interaction defects directly. A negative character
is an explicit finite negative Weil square.

## Research consequence

The global local-to-positive program now has two sharply separated tasks:

1. **descent/coherence:** prove that completed Weil cross maps are independent
   of the ordered Mackey route, producing a convolution kernel on each
   squarefree cube;
2. **Fourier positivity:** prove all Walsh coefficients of that kernel are
   nonnegative, ideally by deriving the tensor factorization (4) or a positive
   dilation.

Neither follows from Euler multiplicativity alone because the archimedean and
endpoint pieces are shared across all prime directions.

