# A non-normal resolvent family falsifies frozen v8

## Result

Version 8 is falsified. Its zero-limit spectral object controls only the operator at spectral parameter zero. It does not control spectral points born elsewhere under completion.

## Hostile packet

Let (S_N) be the nilpotent shift on (N) coordinates and set

\[
A_N=2I+S_N.
\]

Every finite section has characteristic polynomial

\[
\det(\lambda I-A_N)=(\lambda-2)^N.
\]

Thus every finite spectrum is the singleton (\{2\}). At zero, the operators are uniformly bounded below:

\[
\lVert A_Nx\rVert
\geq 2\lVert x\rVert-\lVert S_Nx\rVert
\geq \lVert x\rVert.
\]

All three v8 zero-point gates are clean: no kernel, no cokernel, closed range, and no zero-limit approximate kernel.

## Off-zero resolvent growth

At spectral parameter (z=5/2), every finite matrix remains invertible. But

\[
(A_N-zI)^{-1}
=
-2\sum_{k=0}^{N-1}(2S_N)^k.
\]

Its corner entry has magnitude (2^N). The finite resolvents therefore have no locally uniform bound at (z=5/2).

## Completed spectral birth

Complete the shifts to the unilateral shift (S) and put (A=2I+S). The vector

\[
y=(1,1/2,1/4,\ldots)
\]

is square-summable and satisfies

\[
(A-\tfrac52 I)^*y=0.
\]

Therefore the range of (A-5I/2) is not dense, so (5/2) belongs to the completed spectrum. It was absent from every finite spectrum.

This is not a zero-range defect of (A). It is non-normal spectral pollution exposed only by the parameterized resolvent.

## Exact defect in v8

v8 declares a zero-limit spectral pro-object but no:

- spectral-parameter domain;
- resolvent family;
- locally uniform resolvent bound;
- pseudospectral or functional-calculus object.

Consequently its finite-section promotion gate can pass at zero while completion creates spectrum elsewhere.

## Required successor

A successor must replace the single zero spectral germ with a parameterized analytic object. It needs:

- a declared spectral domain;
- the resolvent family (R(z)=(A-zI)^{-1}) where defined;
- locally uniform resolvent bounds for finite-section promotion;
- a pseudospectral defect recording blow-up before an actual kernel appears;
- compatibility of the resolvent sheaf with specialization, holonomy, and derived completion.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_v8_nonnormal_resolvent_falsifier.py
```
