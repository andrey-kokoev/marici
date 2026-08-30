# The joint Schur determinant is the minimum cross-prime comparison object

## Full finite colligation

Let \(A\) be the boundary-history transport, let \(L\) be the diagonal
primitive-loop operator on the prime-labelled space, and let \(B,C\) be the
source incidence and return maps. The finite joint state operator is

\[
M=
\begin{pmatrix}
A&B\\
C&L
\end{pmatrix}.
\]

This is the first object that simultaneously retains:

- the common seam history;
- all primitive prime loops;
- incidence from prime labels into the boundary;
- return from the boundary into every prime label;
- cross-prime paths through the shared boundary.

## Exact Schur reduction

When \(I-A\) is invertible,

\[
\det(I-M)
=
\det(I-A)
\det\left(I-L-C(I-A)^{-1}B\right).
\]

Define the prime-space return matrix

\[
R=C(I-A)^{-1}B.
\]

Its entry \(R_{pq}\) is the complete boundary-mediated path from prime
\(q\) into the shared seam state and back to prime \(p\).

For the acyclic finite boundary transport, \(\det(I-A)=1\). The entire
finite comparison is therefore the joint determinant

\[
\det(I-L-R).
\]

## Why local prime factors are insufficient

The diagonal entries \(R_{pp}\) are the local prime return transfers. The
off-diagonal entries are the cross-prime overlap kernel.

For two primes,

\[
\det(I-L-R)
=
(1-L_p-R_{pp})(1-L_q-R_{qq})-R_{pq}R_{qp}.
\]

Multiplying local diagonal factors discards the closed cross-prime route
\(q\to p\to q\). Since prime seam charts are unitary resegmentations of one
history, there is no source basis for setting this term to zero.

Equal local determinants can therefore coexist with different joint
determinants.

## Joint relative determinant

Factor the bare Euler operator:

\[
I-L-R
=(I-L)
\left(
I-(I-L)^{-1}R
\right).
\]

The comparison with the Euler product is governed by the single operator

\[
K=(I-L)^{-1}R.
\]

If \(K\) belongs to the third Schatten class after paired low-grade boundary
renormalization, the appropriate global object is \(\det_3(I-K)\), together
with its primitive and square boundary data.

This construction packages all cross-prime routes before taking a
determinant. It does not require absolute summation of separately chosen
pairwise anomaly cells. Those cells are expansion shadows of the joint block.

## Categorical meaning

The Euler product is the determinant of the discrete loop object before it is
coupled to the shared boundary. The theta comparison is not a product of
independent local corrections. It is the Schur complement of one
boundary-mediated multicoupling.

The coherencer is consequently matrix-valued before determinant projection.
Scalar primewise multiplication is a quotient that forgets its off-diagonal
routes.

## DPC verdict

Resolved:

- the minimum finite joint Euler–boundary colligation;
- the exact cross-prime return matrix;
- the Schur determinant identity;
- a finite local-equality/global-inequality falsifier;
- the correct candidate for joint third-regularized completion.

Withheld:

- source construction of the complete matrices \(B\) and \(C\);
- third-Schatten control of \((I-L)^{-1}R\);
- reciprocal and archimedean extension of the joint block;
- the zero-state-to-flux bridge.

The smallest falsifier for a product of local comparison factors is a
two-prime block with \(R_{pq}R_{qp}\neq0\).

## Verification

The checker `check_joint_schur_prime_comparison.py` verifies the exact block
determinant identity and exhibits equal diagonal local data with a nonzero
cross-prime determinant correction.
