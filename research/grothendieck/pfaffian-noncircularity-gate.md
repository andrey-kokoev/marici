# The Pfaffian square root is unique but can be tautological

Let `I` be a connected real interval and let `D:I -> R` be real analytic,
nonnegative, and not identically zero. Every real zero of `D` has even order.
Consequently there is a real-analytic function `f` on `I` such that

```
D(T) = f(T)^2.                                           (1)
```

Once the sign of `f` is fixed at one nonzero base point, `f` is unique. Thus
the orientation lost by a positive determinant is only one global sign on
each connected component; analytic continuation fixes all subsequent sign
changes across zeros.

This sharpens the positive-gluing square-root gate. If a source construction
really proves

```
det(I-C(T)*C(T)) = a(T)^2 Xi(T)^2,                       (2)
```

with a known nowhere-zero analytic factor `a`, then a base-point
normalization recovers `a Xi` from the positive determinant. No independent
zero-by-zero Maslov choice is needed.

## Why a Pfaffian alone explains nothing

For every analytic target `f`, the skew family

```
A_f(T) = [ 0     f(T)]
         [-f(T)   0  ]                                  (3)
```

satisfies `Pf(A_f)=f` and `det(A_f)=f^2`. Taking `f=Xi` therefore constructs
the desired Pfaffian only by placing the answer in a matrix entry. The same
trick works for every analytic function and has no arithmetic content.

A noncircular Pfaffian proposal must provide all of the following before the
Xi identity is invoked:

1. a source-defined skew operator or finite truncation;
2. an entrywise construction from archimedean and prime-local data;
3. a source-derived orientation and base-point normalization;
4. a convergence theorem for its Pfaffians or determinant-line sections;
5. an independent identity identifying the limit with completed Xi.

Items 1--4 must not use Xi values, Xi zeros, or a spectral basis indexed by
those zeros. Otherwise item 5 is a relabelling rather than a derivation.

## The actual research target

The next useful object is not an arbitrary Pfaffian. It is a skew lift of the
paired archimedean--prime transfer operator whose square recovers the Krein
graph determinant by a structural identity. In finite rank, this asks for a
source-defined `A_P(T)` with

```
det A_P(T) = det(I-C_P(T)*C_P(T))                       (4)
```

and compatible orientations as the prime cutoff `P` grows. Equation (4)
must follow from the lift, not from choosing a square root after computing
the right-hand side.

## Falsifier

A claimed determinant-line solution fails the explanatory gate if its skew
matrix entries, orientation, basis, or limiting prescription already contain
Xi or its zeros. It also fails if the finite-cutoff Pfaffian signs cannot be
made compatible under cutoff inclusion. Passing the gate would reduce the
orientation problem to a base-point sign and move the real conjectural load
to the source-derived squared determinant and its compatible skew lift.
