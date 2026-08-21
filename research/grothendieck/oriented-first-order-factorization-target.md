# An oriented first-order boundary map is the minimal surviving square root

The positive transfer Gram operator should not be asked to manufacture its
own sign. The minimal non-tautological architecture begins one level earlier.
Let

```
Q(T): E_P -> F_P                                        (1)
```

be a source-defined real or complex square boundary map between equally
ranked oriented spaces, and define

```
B(T)=Q(T)* Q(T).                                        (2)
```

Then

```
det B(T)=|det Q(T)|^2.                                  (3)
```

In the real oriented case this is `(det Q(T))^2`, while `det Q(T)` itself is
signed and analytic. If one singular direction of `Q(T)` crosses zero
linearly, `det Q` has a simple zero and changes sign, whereas `det B` has the
required double zero. This matches the local multiplicity pattern of Xi and
Xi squared without Kramers over-doubling.

The associated chiral operator

```
H_Q(T) = [ 0     Q(T)* ]
         [ Q(T)    0   ]                                (4)
```

is self-adjoint by construction. Its kernel is the sum of the kernels of
`Q(T)` and `Q(T)*`, so the loss of invertibility of the oriented boundary map
is visible as a zero mode of a self-adjoint first-order system.

## Why the direction of construction matters

Starting with a positive `B(T)` and choosing `Q(T)=sqrt(B(T))` or a Cholesky
factor is circular. It imports the desired square root, generally loses
analyticity at a simple signed-root crossing, and supplies no arithmetic
explanation. The admissible direction is

```
source boundary map Q  ->  adjoint pairing  ->  B=Q*Q.  (5)
```

Both the entries of `Q` and the orientations of its domain and codomain must
be fixed before computing `B` or comparing its determinant with Xi.

This also explains the scalar hostile cases. The positive family `B=t^2`
has the oriented first-order source `Q=t`, so its determinant square root is
analytic and signed. The positive family `B=1-x^2` on `|x|<1` has no
polynomial `Q` over `R[x]`; writing `Q=sqrt(1-x^2)` merely adjoins the answer.

## Relation to the transfer Gram operator

The useful conjecture is no longer merely

```
B_P(T)=I-C_P(T)*C_P(T) >= 0.                            (6)
```

It is the stronger source factorization

```
I-C_P(T)*C_P(T) = Q_P(T)*Q_P(T),                        (7)
```

where `Q_P` is a relative boundary differential or torsion map defined
independently of the transfer matrix. Equation (7) simultaneously explains
contractivity, even Gram multiplicity, and the oriented square root. It is
strictly stronger than positivity and is false for a generic contraction.

## Falsifier

A proposal fails if `Q_P` is introduced only after diagonalizing or taking a
square root of `I-C_P*C_P`, if its orientation is chosen from Xi signs, or if
its finite-cutoff entries use Xi zeros. The smallest algebraic falsifier is
the scalar generic contraction `C=[x]`, because `1-x^2` has no polynomial
first-order factor over `R[x]`.

## Next construction problem

Search the paired coefficient--Betti correspondence for a genuine
first-order relative boundary map whose adjoint composite is the transfer
defect. This makes self-adjointness an adjoint-complex theorem rather than an
assumption. Until such a map is supplied, the result is a precise target—not
a construction of Xi, a Hilbert--Polya operator, or a proof of RH.
