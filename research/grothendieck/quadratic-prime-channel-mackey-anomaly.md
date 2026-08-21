# The quadratic prime channel is the first Mackey-forbidden Adams operation

The two low-order channels omitted by the third prime determinant are

```
C_1(s)=Tr(P_s),
C_2(s)=(1/2)Tr(P_s^2)=(1/2)Tr(P_(2s)).                 (1)
```

Thus the quadratic channel is not an unrelated second scalar. It is the
second power/Adams operation applied to the prime propagation operator, with
the cyclic coefficient `1/2` forced by the logarithm.

For a finite abelian quotient `q:G->G/K`, the power--Mackey theorem says that
the `n`th power square commutes with fiber transfer exactly when

```
gcd(n,exp K)=1.                                        (2)
```

Therefore every exponent-two branch kernel admits the linear operation but
rejects the quadratic operation. The first analytically nonsummable
Hermitian channel is simultaneously the first algebraically
Mackey-incompatible repetition.

## Smallest hostile C2 calculation

Let `G=C2={0,1}`, `q:C2->1`, and let `delta_0` be the selected coefficient
function. The second power map sends both points to zero, so

```
q_! [2]^* delta_0 = 2,
[2]^* q_! delta_0 = 1.                                (3)
```

The Mackey square fails by the fiber multiplicity two. Dividing transfer by
two repairs the scalar on one side only by sending the frozen selected vector
to one half; it violates the original integral normalization. The analytic
coefficient `1/2` in `C_2` is therefore compatible with cyclic-logarithm
bookkeeping but does not turn the second power into an ordinary normalized
Mackey morphism.

## Interpretation

This is a structural coincidence with a precise conditional consequence. If
the prime repetition channels are to be realized through the same
coefficient--Betti power correspondence, then the quadratic channel must be
represented as a descent defect, derived correction, or boundary of a
larger relative complex. It cannot be inserted as a strictly functorial
second Adams channel across exponent-two fibers.

The canonical norm relation offers the appropriate algebraic type. For a
degree-two norm `N`,

```
N^2=2N,                  N(2-N)=0=(2-N)N,              (4)
```

giving a two-periodic complex with alternating maps `N` and `2-N`. A
candidate anomaly complex could place the quadratic repetition in this
two-periodic defect rather than demand strict descent. This is only a type
match: no source theorem currently identifies its torsion with `C_2`, gamma
completion, or Xi.

## Falsifiers

A proposed two-channel construction fails if it:

1. treats `C_2` as independent of the second power of the linear prime
   operator;
2. asserts strict second-Adams Mackey compatibility across a `C2` kernel;
3. uses the factor `1/2` to average without auditing the selected-vector
   normalization;
4. identifies the norm two-periodic complex with the analytic counterterm
   without a finite-cutoff trace or torsion identity.

## Next target

At finite prime cutoff, construct a graded two-channel complex combining the
linear prime map with the norm-defect pair `(N,2-N)`, and test whether its
logarithmic torsion reproduces the forced `Tr(P_s^2)/2` term while preserving
the archimedean pairing. Failure already in the `C2` fiber kills this route.

This establishes an algebraic anomaly gate, not the required analytic
complex, physical relative-chain pushforward, or RH.
