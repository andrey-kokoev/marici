# The det3 multiplicative anomaly is the mixed relationship coherencer

Author: `marici.Nima`

Date: 2026-08-26

Status: exact finite anomaly formula and coherence law

## Relative composition

Let

\[
(I+A)(I+B)=I+C,
\qquad
C=A+B+AB.
\]

For the third-order determinant, ordinary determinants multiply, but the
regularizing exponential contributes a residual. Define

\[
\rho(X)=-\operatorname{tr}X+rac12\operatorname{tr}(X^2).
\]

Then

\[
\log\det_3(I+C)
-\log\det_3(I+A)
-\log\det_3(I+B)
=
\rho(C)-\rho(A)-\rho(B).
\]

Expanding and using cyclicity of trace gives the exact anomaly

\[
\alpha_3(A,B)
=
\operatorname{tr}
\left(
A^2B+AB^2+\frac12ABAB
\right).
\]

It begins at cubic order. The primitive and square counterterms have removed
the separate linear and quadratic pieces, but their interaction under
composition leaves this mixed relationship term.

## Why it is a coherencer

For three relative operations, define the product law

\[
A\star B=A+B+AB.
\]

Associativity of operator multiplication gives

\[
(A\star B)\star C=A\star(B\star C).
\]

The anomaly satisfies the cocycle identity

\[
\alpha_3(A,B)
+\alpha_3(A\star B,C)
=
\alpha_3(B,C)
+\alpha_3(A,B\star C).
\]

Thus local determinant increments depend on factorization, while the complete
packet has path-independent endpoint transport. Dropping the anomaly breaks
coherence even when the final ordinary determinant agrees.

## Relationship energy

The anomaly is neither an individual contribution from (A) nor one from
(B). It consists entirely of mixed words. It is therefore an exact algebraic
model of relationship energy:

- it exists only when operations interact;
- it depends on their typed order inside the word;
- trace cyclicity makes the two-factor scalar anomaly symmetric;
- higher staging requires the cocycle law rather than pairwise equality;
- it disappears under a bookkeeping scheme that retains only isolated
  channel traces.

This is the determinant-vessel counterpart of the Schur mixed term and the
control-theory interaction residual.

## RH limitation

The anomaly restores composability of regularized determinant transport. It
does not have a fixed sign for general operators. Exact examples realize
positive, negative, and zero values while satisfying the cocycle identity.

Therefore it is a coherencer, not an orientation law. An RH-bearing theorem
would have to derive a source restriction on the actual theta operators that
controls the completed anomaly together with the seam and archimedean
currents.

## Finite falsifiers

Any proposed third-order determinant compiler fails if:

- it treats (det_3) as freely multiplicative;
- it omits mixed cubic or quartic words;
- its staged anomalies violate the cocycle identity;
- it assumes the anomaly is positive without a source restriction.

The checker verifies the exact trace formula and the three-stage cocycle on
rational noncommuting matrices.

