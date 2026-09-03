# Coercive finite-reduction Schur gate

## Question

What exact operator inequality is needed for logarithmic high-mode coercivity to reduce RH positivity to a certified finite block?

## Claim boundary

A block-operator theorem identifies the missing condition. High-mode coercivity and positivity of the uncorrected low block are not sufficient: the low--high coupling must enter through a Schur complement. No quantitative Weil-form constants are supplied here.

## Block decomposition

Let the Hilbert space split as

\[
\mathcal H
=
\mathcal H_{\leq N}
\oplus
\mathcal H_{>N}.
\]

Write the self-adjoint Weil operator as

\[
W
=
\begin{pmatrix}
A&B^*\\
B&C
\end{pmatrix}.
\]

Here \(A\) is finite dimensional, \(C\) is the high-mode block, and \(B\) contains boundary and commutator coupling.

Suppose a quantitative Gårding estimate gives

\[
C\geq cI
\]

for an explicit \(c>0\). Then \(C\) is invertible and

\[
W\geq0
\]

is equivalent to

\[
A-B^*C^{-1}B\geq0.
\]

This is the finite Schur complement that must be certified.

## Norm-bound certificate

If the exact inverse is unavailable, the coercive bound gives

\[
C^{-1}\leq c^{-1}I.
\]

Therefore the sufficient finite-dimensional condition is

\[
A-c^{-1}B^*B\geq0.
\]

A still coarser sufficient condition is

\[
\lambda_{\min}(A)
\geq
\frac{\lVert B\rVert^2}{c}.
\]

Every constant must be source-computable and interval-certified.

## Deliberate failure

The matrix

\[
\begin{pmatrix}
1&2\\
2&1
\end{pmatrix}
\]

has positive low and high diagonal blocks, but determinant \(-3\) and eigenvalue \(-1\). Thus neither separate block positivity nor high-mode coercivity closes the proof without cross-block control.

## Application to the proposed route

The proposed log-elliptic programme needs five objects:

1. an explicit interval projection \(P_{\leq N}\);
2. a proved high-mode constant \(c(L,N)>0\) for the archimedean-minus-prime block;
3. an explicit bound or enclosure for
   \[
   B=P_{>N}WP_{\leq N};
   \]
4. a rigorous finite matrix enclosure for \(A=P_{\leq N}WP_{\leq N}\);
5. a positive lower bound for the corrected matrix
   \[
   A-B^*C^{-1}B,
   \]
   or for its conservative replacement \(A-c^{-1}B^*B\);
6. uniform control of these bounds as the support interval grows;
7. convergence of compact-support truncations to the Gaussian heat-polynomial probes in the Weil-form norm.

The endpoint contribution is finite rank but is not automatically harmless: it enters \(A\), \(B\), or both according to the chosen projection. Fixed-support coercivity alone applies only to a local test class because inverse Fourier transforms of Gaussian heat-polynomial probes have unbounded support.

## Falsification condition

The coercive route fails at a declared \((L,N)\) if any of the following occurs:

- the computed \(c(L,N)\) is nonpositive;
- the cross-bound \(\lVert B\rVert^2/c\) exceeds the certified low-block margin;
- boundary commutators do not decay with \(N\);
- the finite corrected block has a certified negative eigenvalue.

Failure at one cutoff does not refute RH, but it refutes that finite-reduction certificate at the declared parameters.

## Disposition

At fixed support, the route is mathematically viable only as a Schur-complement argument. “High modes are positive; check the low modes” omits a necessary proof edge. For the endpoint-free heat cone it remains diagnostic unless the constants are uniform under support exhaustion and the truncations converge in the Weil-form norm. The next executable local test is to extract explicit \(c\), \(B\), and \(A\) bounds; promotion to an RH proof additionally requires the two exhaustion conditions.

## Verification

- `research/voevodsky/checkers/check_coercive_finite_reduction_schur_gate.py`
- `research/voevodsky/results/coercive_finite_reduction_schur_gate.json`
