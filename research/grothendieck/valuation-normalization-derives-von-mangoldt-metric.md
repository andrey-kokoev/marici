# Valuation coordinates derive the reciprocal von Mangoldt metric prime by prime

Fix a prime `p`. Its prime-power ray is the exponent chain

```
1,p,p^2,...,p^K  <->  a=0,1,...,K.                    (1)
```

The logarithmic potential is

```
log(p^a)=a log p,                                      (2)
```

and its first divisor difference is

```
log(p^a)-log(p^(a-1))=log p=Lambda(p^a).               (3)
```

The intrinsic dimensionless coordinate on this chain is the valuation

```
v_p(p^a)=a=log(p^a)/log p.                             (4)
```

Passing from logarithmic coefficients to valuation coefficients therefore
applies

```
S_p: c_a -> c_a/(log p).                               (5)
```

Pulling the standard Euclidean metric on valuation coefficients back through
`S_p` gives

```
||c||_p^2=sum_(a>=1)|c_a|^2/(log p)^2.                (6)
```

Thus the reciprocal-square von Mangoldt metric is not merely selected by
divergence matching. It is the canonical metric obtained by measuring the
primitive divisor coefficient in valuation units rather than logarithmic
length units.

For the von Mangoldt vector itself, (3)--(6) give one unit per prime-power
site:

```
||Lambda(p^a)e_(p,a)||_p^2=1.                          (7)
```

After the critical factor `p^(-a/2)`, its quadratic contribution becomes
`p^(-a)`. Summing over exponents gives

```
sum_(a>=1)p^(-a)=1/(p-1),                              (8)
```

whose prime sum has the required `log log P` divergence; higher powers change
only the finite part relative to `sum_p1/p`.

## Colored Mackey compatibility

The weight `1/(log p)^2` is constant along a fixed `p`-ray. Any finite
surjection or incidence fiber entirely inside that ray is therefore balanced,
so the ordinary cardinality pull--push norm survives.

If a fiber mixes prime colors `p` and `q`, its weights differ unless `p=q`.
The hostile two-point criterion then shows that frozen-selector normalization
and ordinary degree cannot both survive. Therefore the canonical object is a
prime-colored family of exponent correspondences, not a single quotient that
forgets prime labels.

This fits the Euler tensor-product structure of the divisor zeta transform:
each prime exponent chain carries its own valuation normalization, and the
full finite Euler box is assembled from these colored factors. The existing
Dirichlet metric `D_p*D_p` on logarithmic potentials remains non-diagonal in
exponent sites; (6) concerns the primitive coefficient leg before divisor
pushforward, so the two metrics are complementary rather than competing.

## Pairing and Euler cross term

Let the coefficient basis use valuation-normalized vectors
`e_(p,a)/(log p)` and the Betti dual basis use `(log p)e_(p,a)^vee`. Their
evaluation remains one. Expressing the physical source in the unnormalized
coefficient coordinate restores the linear factor `Lambda(p^a)=log p` in the
cross-resolvent, while its Hilbert norm is computed in valuation units and
has the harmonic size (8).

This supplies an exact finite weighted coefficient--Betti adjunction on each
prime-colored ray. It does not supply a color-forgetting Mackey quotient or
the infinite tensor-product completion.

## Falsifiers and next target

A proposal fails if it:

1. treats `1/(log p)^2` as an arbitrary diagonal weight rather than the
   valuation-coordinate pullback;
2. mixes distinct prime colors in a fiber while retaining ordinary degree;
3. applies the reciprocal weight at integers outside prime-power support;
4. forgets the dual Betti rescaling and thereby loses evaluation adjunction;
5. identifies the colorwise finite construction with the completed infinite
   relative determinant.

The next target is the incomplete tensor product of these normalized prime
rays with the even oscillator reference. Its vacuum/reference vector must
make the relative covariance trace finite while retaining the colored Euler
cross functional.
