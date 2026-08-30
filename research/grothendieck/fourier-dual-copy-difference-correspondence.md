# Fourier duality turns spectral copying into a source difference correspondence

Let `G` be a finite abelian group of order `n`, with character group
`G_hat`. On the spectral side define the conjugation-twisted copy map

```
C_J |chi> = |chi> tensor |conj chi>.                   (1)
```

Let `F:l^2(G)->l^2(G_hat)` be the unitary Fourier transform. Transporting
(1) to the source side gives

```
C_diff = (F* tensor F*) C_J F.                         (2)
```

Character orthogonality yields the explicit formula

```
C_diff |x>
 = n^(-1/2) sum_(a-b=x) |a> tensor |b>.                (3)
```

Thus conjugation matching in spectral variables is Fourier dual to the
difference correspondence

```
d:G x G -> G,
d(a,b)=a-b.                                            (4)
```

Every fiber has cardinality `n`. If `I_diff` is the unnormalized incidence
map

```
I_diff |x> = sum_(a-b=x)|a,b>,                          (5)
```

then

```
I_diff* I_diff = n I = |ker d| I,                      (6)
C_diff = n^(-1/2) I_diff,
C_diff* C_diff=I.                                      (7)
```

This derives the `|ker q|` norm from a genuine pull--push composite rather
than inserting it as a convention.

## Small hostile C2 branch quotient

For `G=C_2`, subtraction equals addition and each output has two preimages:

```
d^(-1)(0)={(0,0),(1,1)},
d^(-1)(1)={(0,1),(1,0)}.
```

Hence `I_diff*I_diff=2I`. The normalized incidence is exactly the Fourier
transport of the two-dimensional conjugation graph copy map.

## Arithmetic interpretation and limit

The theorem supplies a precise model for the proposed paired
coefficient--Betti system:

```
spectral conjugation graph  <--Fourier-->  source difference fibers.
```

It suggests that a prime-side realization should be sought as a convolution
or difference correspondence, not as finitely many scalar explicit-formula
tests. However, the Xi transform is not presently an admitted unitary
Fourier equivalence between an arithmetic chain space and the zero-divisor
space. Equations (1)--(7) are a finite abelian theorem, not a construction of
the unavailable physical relative-chain pushforward.

The next falsifier is normalization: any proposed finite model must produce
the fiber cardinality before normalization and an isometry afterward.

