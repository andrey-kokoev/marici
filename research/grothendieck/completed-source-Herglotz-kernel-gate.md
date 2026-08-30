# The source Herglotz kernel is positive only after endpoint--gamma--prime completion

Put `s=1/2+z`. In the honest Euler region `Re(s)>1`, equivalently
`Re(z)>1/2`, the centered completed logarithmic derivative splits as

```
F(z)=F_end(z)+F_gamma(z)+F_prime(z),                    (1)

F_end(z)=1/(z+1/2)+1/(z-1/2),
F_gamma(z)=-(1/2)log pi+(1/2)psi(1/4+z/2),
F_prime(z)=-sum_(n>=2) Lambda(n)n^(-1/2)e^(-z log n).  (2)
```

The canonical two-point kernel correspondingly splits, in this region, as

```
H_Xi=H_end+H_gamma+H_prime,
H_part(z,w)
 =[F_part(z)+conj(F_part(w))]/[z+conj(w)].              (3)
```

## Primewise positivity is impossible

For a single prime-power term with positive coefficient

```
a_n=Lambda(n)n^(-1/2),
```

the diagonal kernel at real `z>1/2` is

```
H_n(z,z)=-a_n e^(-z log n)/z <0.                       (4)
```

Thus neither individual primes nor their convergent sum define a positive
kernel. Positivity, if true, must come from completed coupling to endpoint
and gamma sectors.

## The endpoint transport singularity

At `s=1` (`z=1/2`),

```
1/(s-1)+zeta'(s)/zeta(s)                               (5)
```

is regular: the pole of the endpoint term cancels the pole of the zeta log
derivative. But the Dirichlet series for `zeta'/zeta` diverges there. Hence
the separate kernels in (3) do not extend independently through `z=1/2`.
They must first be combined and analytically transported.

This is stronger than a numerical cancellation warning. A source Gram
construction on the full right half-plane cannot assign positive Hilbert
spaces independently to the raw endpoint and prime terms and then take an
ordinary orthogonal sum; their singular pieces belong to one relative
correspondence.

## Coupled kernel target

The valid construction must produce one completed vector-valued map
`Phi(z)` such that

```
H_Xi(z,w)=<Phi(w),Phi(z)>                               (6)
```

after endpoint--gamma--prime renormalization. The negative prime kernel in
(4) must arise as a cross term or a relative subtraction inside a larger
positive space, not as a positive summand.

This suggests a Krein-to-Hilbert completion pattern: local source sectors may
carry an indefinite bookkeeping form, while the completed quotient or Schur
complement is positive. Any such construction must exhibit the null
subspace and prove the final quotient norm is positive.

## Falsifiers

1. A prime-by-prime positive-kernel claim fails (4).
2. Extending the raw prime series through `s=1` fails its domain.
3. Treating endpoint and prime spaces as an ordinary orthogonal direct sum
   misses their required pole cancellation.

