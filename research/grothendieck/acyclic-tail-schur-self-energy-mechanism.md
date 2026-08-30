# An acyclic auxiliary tail cancels Weyl density but leaves a Schur coupling

Let `H_P` be the physical logarithmic-rank Jacobi block and let `H_A` be a
larger auxiliary smoothing tail. Put one copy of `H_A` in even degree and an
identical copy in odd degree, so its uncoupled graded determinant is one and
its net Weyl multiplicity is zero.

Couple the physical block to the even auxiliary copy by `C`. At spectral
parameter `z`, the graded determinant is

```
sdet M(z)
 = det [ H_P-z   C     ] / det(H_A-z)
       [  C*    H_A-z ]

 = det(H_P-z-C(H_A-z)^(-1)C*).                       (1)
```

The bare auxiliary determinant cancels against its odd partner, but the
physical block retains the nonlocal, energy-dependent self-energy

```
Sigma(z)=C(H_A-z)^(-1)C*.                            (2)
```

Thus a superlogarithmic taper may regularize the moment boundary without
appearing as extra physical zero density. It is not deleted: its effect
survives precisely as a Schur complement.

## Why this matches the forced architecture

The mechanism simultaneously provides:

1. logarithmic physical Weyl rank from `H_P`;
2. an arbitrarily wide smoothing tail in an index-zero coefficient--Betti
   pair;
3. a source for nonlocal coupling between shell blocks through the auxiliary
   resolvent;
4. a determinant capable of zeros through Schur interference rather than
   local Euler factors.

If `H_P,H_A` are self-adjoint and `C*` is the actual adjoint, the full even
block is self-adjoint. For real `z` outside `spec(H_A)`, `Sigma(z)` is
self-adjoint. Domain and determinant-class estimates remain essential in the
infinite system.

## Critical caveat

The graded cancellation is not an ordinary positive-Hilbert-space spectral
count. The odd auxiliary copy must be justified as an acyclic
coefficient--Betti/mapping-cone degree, and the physical operator must be
defined on cohomology or by a legitimate relative determinant. Introducing
ghost modes solely to fix the count would be fitted bookkeeping.

The next source test is exact: determine whether the paired Mackey
coefficient--Betti system naturally supplies identical even/odd smoothing
tails and a coupling `C` whose finite Euler expansion has the forced linear
and quadratic coefficients `1` and `1/2`.

