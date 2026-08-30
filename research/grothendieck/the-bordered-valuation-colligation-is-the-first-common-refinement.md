# The bordered valuation colligation is the first common refinement

## The apparent missing lift

The prime-two audit found two differently typed readouts:

\[
W_2(c)=\lVert P_{2\nmid n}c\rVert^2
\]

from the input tower, and the scalar Euler cumulants

\[
2q,
\qquad q^2,
\qquad \frac{2}{k}q^k,
\qquad q=2^{-s},
\]

from the boundary determinant tower.

The common refinement is already present in the source construction. It is
not an endomorphism fitted between those readouts.

## One valuation-chain colligation

On a (p)-valuation chain with basis (e_0,e_1,\ldots), let

\[
Se_k=e_{k+1}.
\]

Retain the primitive input port (e_0) and the augmentation output port

\[
\ell(e_k)=1.
\]

The source-local object is the bordered colligation

\[
\mathfrak C_p=(S,e_0,\ell).
\]

All three pieces are independently derived: (S) is prime multiplication,
(e_0) is valuation-zero incidence, and (ell) aggregates the valuation
orbit.

## Input curvature is its defect projection

On the infinite unilateral chain,

\[
S^*S=I,
\qquad
SS^*=I-|e_0\rangle\langle e_0|.
\]

Hence

\[
I-SS^*=|e_0\rangle\langle e_0|.
\]

After decomposing the integer-label module into primitive (p)-valuation
chains, the sum of these vacuum defects is exactly

\[
P_{p\nmid n}.
\]

Thus the prime-exclusion Ward port is the input-defect readout of
(mathfrak C_p).

## Euler data is its transfer readout

The same colligation has boundary transfer function

\[
g_p(q)=\ell(I-qS)^{-1}e_0
=
\sum_{k\ge0}q^k
=
\frac1{1-q}.
\]

Its value--flux jet transport has determinant (g_p(q)^2), and therefore

\[
\log g_p(q)^2
=
2q+q^2+\sum_{k\ge3}\frac{2}{k}q^k.
\]

So the primitive, square, and connected cumulants are the determinant-line
readout of the same source object whose defect readout is prime exclusion.

## The fourth tower's first square

The first common-refinement square is therefore

\[
\begin{array}{ccc}
&\mathfrak C_p&\\
\swarrow&&\searrow\\
P_{p\nmid n}&&g_p(q),\ \log g_p(q)^2.
\end{array}
\]

This resolves the earlier degree mismatch without equating a scalar to a
quadratic form. Both are functorial shadows of one bordered operator system.

## Finite-depth caution

For a chain (e_0,\ldots,e_N), the truncated shift has two defects:

\[
I-SS^*=|e_0\rangle\langle e_0|,
\qquad
I-S^*S=|e_N\rangle\langle e_N|.
\]

The first is the source primitive boundary. The second is a cutoff-terminal
boundary and must be retained in finite naturality checks. It disappears only
under a controlled direct limit; deleting it at finite (N) would fake
conservativity.

The finite transfer function is

\[
g_{p,N}(q)=\sum_{k=0}^{N}q^k.
\]

## What this does not prove

The common carrier and the two readout maps are now explicit, but no
RH-bearing balance has been derived. The next rung must compare the Green
boundary form of the completed direct/dual colligation with its defect
projection while retaining:

- the terminal cutoff defect;
- primitive and square determinant grades;
- the archimedean port;
- reciprocal-sheet incidence.

At (p=2), the next calculation is the exact Green identity of the doubled
bordered colligation, not construction of an arbitrary (K_{2,s}).

## Falsifier

The common-refinement claim fails if the source decomposition does not turn
the sum of chain-vacuum defects into (P_{p\nmid n}), if the transfer readout
does not yield the finite Euler polynomial, or if the two readouts require
different shift, vacuum, or augmentation data.

