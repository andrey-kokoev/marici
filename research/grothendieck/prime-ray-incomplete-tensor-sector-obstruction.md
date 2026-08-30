# The valuation-normalized prime source leaves the vacuum tensor-product sector

For each prime `p`, let the normalized critical source on its exponent ray be
`v_p=(p^(-a/2))_(a>=1)`. Then

```
||v_p||^2=sum_(a>=1)p^(-a)=1/(p-1).                   (1)
```

The normalized coherent vector has vacuum overlap
`exp[-||v_p||^2/2]`. At prime cutoff `P`, the product overlap is

```
O(P)=exp[-(1/2)sum_(p<=P)1/(p-1)].                    (2)
```

Since `sum_p1/(p-1)` diverges like `sum_p1/p`, `O(P)->0`. Equivalently,
`direct_sum_p v_p` is not in the vacuum one-particle Hilbert space. The
global prime coherent source lies in an inequivalent infinite-product sector,
not the product-vacuum incomplete tensor product.

## A positive gamma factor cannot cancel the distance

Tensoring an independent positive gamma Fock space adds norms:

```
||(v_prime,v_gamma)||^2=||v_prime||^2+||v_gamma||^2.   (3)
```

No positive gamma displacement cancels the prime divergence. The earlier
prime--oscillator subtraction is a relative trace difference, not a norm in
a positive direct sum. Prime and gamma sectors must first be compared by a
relative covariance, determinant ratio, or Krein pairing; positivity can be
demanded only after quotienting their common divergent part.

## Surviving analytic types

Three completions remain plausible:

1. relative Fock comparison of quasi-free states with a proved Schatten
   implementability criterion;
2. a nonvacuum Araki--Woods-type representation;
3. a Krein-Fock pre-space with opposite prime/gamma self-contractions and a
   positive null quotient.

Multiplying divergent vacuum partition functions is not a construction. The
shared representation, domains, and cutoff comparison maps must be given.

The obstruction concerns the quadratic norm. The finite linear Euler cross
functional remains meaningful in the honest half-plane and must survive as a
matrix element between distinct source and readout sectors.

## Falsifiers and next target

A proposal fails if it places the global critical source in the product
vacuum sector, claims cancellation by adding a positive gamma norm, or loses
the oriented linear Euler cross entry when changing representations.

The next target is a finite-cutoff Bogoliubov/relative-covariance comparison
between the prime-ray product state and the quarter-shift oscillator state.
Its off-diagonal part must be Hilbert--Schmidt and its diagonal divergences
must match under `K=floor(log P)`.

This is an infinite-product sector no-go, not a construction or RH proof.
