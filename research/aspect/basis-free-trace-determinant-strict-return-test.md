# Basis-free trace-determinant strict-return test

## Question

What invariant physical readout is necessary and sufficient to certify strict return for a positive two-port operator without choosing route coordinates?

## Invariant criterion

Let \(G\) be a positive Hermitian operator on a two-dimensional physical target. Strict return means

\[
I-G>0.
\]

For a two-dimensional Hermitian operator, positive definiteness is equivalent to positive trace and determinant. Therefore

\[
G<I
\]

if and only if

\[
2-\operatorname{tr}G>0
\]

and

\[
\det(I-G)=1-\operatorname{tr}G+\det G>0.
\]

Equivalently, the basis-free test is

\[
\operatorname{tr}G<2,
\qquad
1-\operatorname{tr}G+\det G>0.
\]

Positivity of \(G\) is supplied automatically when \(G\) is a physical route Gram return. Without that construction it remains a separate premise.

## Necessity of both inequalities

The spectrum \((6/5,1/10)\) has trace \(13/10<2\) but largest eigenvalue above one; its complement determinant is \(-9/50\). Thus the trace inequality alone fails.

The spectrum \((6/5,13/10)\) has positive complement determinant \(3/50\), but both eigenvalues exceed one and the complement trace is negative. Thus the determinant inequality alone fails.

The terminal spectrum \((1,0)\) is detected by

\[
\det(I-G)=0.
\]

## Relation to route variables

For the route Gram matrix

\[
G=\begin{pmatrix}u&c\\\overline c&v\end{pmatrix},
\]

these invariants are

\[
\operatorname{tr}G=u+v,
\qquad
\det G=uv-|c|^2.
\]

Hence parity suppression of \(|c|\) raises the determinant at fixed route loads, but a trace measurement remains necessary to set the absolute scale.

## Minimal physical readout

Once positivity is source-derived, the pair

\[
(\operatorname{tr}G,\det G)
\]

is sufficient and basis-independent. Neither scalar separately is sufficient. This pair is weaker than reconstructing the full return but still requires a physical route or detector construction; arithmetic rank data cannot supply it by dimension matching.

## Verification

`research/aspect/checkers/check_trace_determinant_return.py` verifies strict, terminal, trace-only hostile, and determinant-only hostile spectra with exact rationals.

## Disposition

The invariant two-port decision test is complete. A robust experimental or source-derived certificate can now be phrased as an upper trace bound and a lower complement-determinant margin rather than as full matrix reconstruction.
