# An exceptional-point monodromy falsifies frozen v9

## Result

Version 9 is falsified as a mode-resolved network signature. A total resolvent sheaf can be globally single-valued while its eigenchannel sheets have nontrivial monodromy over an external parameter loop.

## Hostile packet

Consider the matrix family

\[
A(t)=\begin{pmatrix}0&1\\t&0\end{pmatrix}.
\]

Its characteristic equation is

\[
\lambda^2=t.
\]

Away from (t=0), the two eigenvalues are (+\sqrt t) and (-\sqrt t). One circuit around the origin changes the sign of the square root, so the two eigenvalue sheets exchange.

## Why the v9 resolvent remains clean

The total resolvent is

\[
(A(t)-zI)^{-1}
=
\frac{1}{t-z^2}
\begin{pmatrix}z&1\\t&z\end{pmatrix}.
\]

It is rational and single-valued in (t). On any compact set avoiding (t=z^2), it is holomorphic and bounded. It satisfies the resolvent identity exactly.

Thus every local requirement of the v9 resolvent sheaf can pass.

## Hidden mode exchange

On the double cover (t=s^2), the spectral projectors are

\[
P_\pm=\frac12\left(I\pm\frac{A(s^2)}{s}\right).
\]

They are idempotent, resolve the identity, and select eigenvalues (\pm s). Under the deck transformation (s\mapsto-s),

\[
P_+\longleftrightarrow P_-.
\]

The total resolvent is invariant under the same deck turn. Therefore it cannot, by itself, distinguish trivial global mode labels from exchanged mode labels.

This is the optical exceptional-point phenomenon in exact algebraic form: the aggregate transfer function returns after one loop, while the mode channels do not.

## Exact defect in v9

v9 declares only the complex spectral parameter (z). It does not declare:

- the external control-parameter base (t);
- the joint parameter–spectral incidence variety;
- its branch locus and normalization;
- the eigenprojector local system;
- deck transport or mode-permutation monodromy.

The ordinary resolvent sheaf therefore forgets precisely the channel topology the network signature is meant to retain.

## Required successor

A successor must work over the joint spectral cover

\[
\Sigma=\{(t,z):\det(A(t)-zI)=0\}.
\]

It must retain the normalization of that cover, branch strata, Riesz-projector transport, deck permutations, and their compatibility with the total resolvent, specialization, and completed sewing.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v9_exceptional_point_monodromy_falsifier.py
```
