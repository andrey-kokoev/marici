# The reciprocal-quartic interval theorem has three independent source gates

## Quotient reduction

Consider a nonnegative palindromic quartic

\[
P(w)=aw^4+bw^3+cw^2+bw+a,
\qquad a>0, b,c\ge0.
\]

With `y=w+w^{-1}`,

\[
P(w)=w^2Q(y),
\qquad
Q(y)=ay^2+by+(c-2a).
\]

The quotient roots lie in the physical interval `[-2,2]` exactly when three
inequalities hold.

## The three gates

### Hyperbolicity

\[
\Delta=b^2-4a(c-2a)\ge0.
\]

This makes both quotient roots real.

### Left-wall midpoint

\[
b\le4a.
\]

The root midpoint is `-b/(2a)`, so this keeps it at or above `-2`.

### Alternating endpoint

\[
Q(-2)=c+2a-2b\ge0.
\]

Equivalently,

\[
P(-1)\ge0.
\]

Together with the midpoint condition, this prevents the lower root from
crossing the left endpoint. The right endpoint needs no additional inequality:
`Q(2)=c+2a+2b>0`, and the nonpositive midpoint prevents both roots from lying
above `2`.

Therefore

\[
\operatorname{Roots}(Q)\subseteq[-2,2]
\]

if and only if all three gates hold.

## Independence

Each condition carries distinct information:

- `(a,b,c)=(1,1,3)` passes both interval-wall gates but has negative
  discriminant;
- `(1,5,8)` is hyperbolic and passes `Q(-2)>=0` but its midpoint lies below
  `-2`;
- `(1,4,0)` is hyperbolic with midpoint exactly `-2` but fails the alternating
  endpoint gate.

Thus none may be inferred from the other two.

## The existing hostile

The four-atom hostile has

\[
(a,b,c)=(1,4,0).
\]

It satisfies

\[
\Delta=24>0,
\qquad b=4a,
\]

but

\[
P(-1)=Q(-2)=-6.
\]

So the first hostile does not fail hyperbolicity. It fails a single
source-readable alternating endpoint inequality.

## Operator form

The quotient roots are the eigenvalues of the symmetric matrix

\[
J_Q=
\begin{pmatrix}
-b/(2a)&\sqrt\Delta/(2a)\\
\sqrt\Delta/(2a)&-b/(2a)
\end{pmatrix}.
\]

The three inequalities are exactly the coefficient form of

\[
-2I\le J_Q\le2I.
\]

This identifies the scalable target. Higher reciprocal degrees should not be
attacked by accumulating coefficient inequalities. They should be represented
by a source-derived Jacobi operator whose spectrum is confined to the physical
interval.

The essential noncircularity requirement remains: the Jacobi recurrence must
come from theta-labelled transport before its zeros are examined. Constructing
`J_Q` afterward from `Q` is only the finite diagnostic.

## Next target

Find the theta operation whose first finite shadow is the alternating endpoint
gate

\[
c+2a\ge2b.
\]

If no source operation supplies it, the Lee–Yang lane closes at degree two. If
it does, derive its higher-rank Jacobi/cone-preservation analogue rather than
testing more isolated quotient polynomials.

