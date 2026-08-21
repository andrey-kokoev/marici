# A relative complement correspondence gives the first-order defect exactly

Let `q:Y->X` be a finite map with every fiber of cardinality `d`. Give the
free Hilbert spaces on `X` and `Y` their orthonormal basis metrics. The
normalized incidence map

```
U|x> = d^(-1/2) sum_(q(y)=x) |y>                       (1)
```

satisfies `U*U=I`; this is the paired Mackey pull--push norm after
normalization.

Suppose source data partitions the correspondence space into an admitted
part and a relative complement,

```
Y = Y_in disjoint_union Y_out.                         (2)
```

Let `P_in` and `P_out` be the orthogonal coordinate projections and define

```
C=P_in U,                    Q=P_out U.                 (3)
```

Because `P_in+P_out=I` and their images are orthogonal,

```
C*C + Q*Q = U*U = I,
I-C*C = Q*Q.                                           (4)
```

Thus the missing first-order factor `Q` is not a square root chosen after
forming the transfer defect. It is the incidence map of the omitted relative
correspondence. Self-adjointness and positivity follow from the original
coefficient--Betti pairing and the orthogonal decomposition.

The statement extends to source-defined real weights. If every fiber carries
weights `c_y(T),q_y(T)` obeying a pointwise or fiberwise Parseval identity,
then the admitted and complementary weighted incidence maps still satisfy
(4). Signed analytic complementary weights can retain orientation even
though their Gram composite forgets it.

## Smallest hostile C2 quotient

For the difference map `d:C2 x C2 -> C2`, each fiber has two elements. If
one element of each fiber is admitted and the other omitted, then

```
C*C = (1/2)I,             Q*Q = (1/2)I.                (5)
```

If both are admitted, `C*C=I` and `Q=0`; if neither is admitted, `C=0` and
`Q*Q=I`. The unweighted deck correspondence therefore produces only
constant rational defects. It cannot generate isolated spectral zeros as a
function of a continuous height `T`.

This is an important separation:

- the finite Mackey norm supplies the exact adjoint factorization;
- the relative split supplies a non-tautological first-order boundary map;
- bare finite deck combinatorics supplies no analytic `T`-dependence.

## Square-map and orientation gate

The complement incidence `Q:H_X->H_{Y_out}` is generally rectangular, so it
does not yet have a determinant. A signed Xi candidate requires an additional
source theorem making the relative complement a rank-preserving oriented
complex, or replacing `det Q` by its determinant-line torsion. Neither equal
fiber cardinality nor the Mackey norm supplies this.

## Falsifier and next target

A claimed construction fails if its complementary map is obtained by taking
the positive square root of `I-C*C`; it must be independently identifiable
as omitted source incidence. It also fails as an Xi model if its split is a
fixed unweighted finite subset, because then its Gram defect is locally
constant in `T`.

The next target is a source-derived archimedean weighting or moving relative
boundary that:

1. preserves the Parseval/Mackey identity (4);
2. makes `Q_P(T)` analytic and oriented;
3. makes the relative complex determinant-class and square;
4. remains compatible under prime-cutoff inclusion.

This is an algebraic finite-correspondence theorem. It does not supply the
unavailable physical relative-chain pushforward or prove RH.
