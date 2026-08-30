# The Mertens finite part is cutoff-covariant, not absolute

## The hostile clock change

Let

\[
M(Y)=\sum_{p\le Y}-\log(1-p^{-1}).
\]

Mertens' theorem gives

\[
M(Y)=\log\log Y+\gamma+o(1).
\]

Now present the same cutoff family through the external clock

\[
Y=X^\alpha,
\qquad \alpha>0.
\]

If one subtracts the counterterm belonging to `X` rather than to the actual
cutoff `Y`, then

\[
M(X^\alpha)-\log\log X-\gamma
\longrightarrow
\log\alpha.
\]

The apparent finite anomaly can therefore be manufactured solely by changing
the cutoff parameterization.

## Covariant normalization

The source-bearing cutoff object must retain its actual arithmetic norm `Y`.
Its counterterm is

\[
C(Y)=\log\log Y+\gamma.
\]

Then every power-clock presentation gives

\[
M(X^\alpha)-C(X^\alpha)\longrightarrow0.
\]

Thus the Mertens finite part is not an absolute scalar attached to an
unlabelled directed limit. It is a covariant relative scalar attached to the
pair consisting of a finite Euler boundary and its source scale.

## Consequence for the completion square

The left side of the Mertens--completion square must be typed as

```text
(finite labelled Euler boundary, actual norm scale)
    -> relative Cauchy finite part.
```

Forgetting the scale coordinate introduces a one-dimensional additive
counterterm torsor. The completed BSY value may be compared with the source
finite part only after both are normalized at the same endpoint anchor.

This does not remove the BSY anomaly. It removes false anomalies caused by
regulator reparameterization. After covariant normalization, the remaining
difference is still

\[
\sum_{\Re\rho>1/2}
m_\rho\log\left|\frac\rho{1-\rho}\right|.
\]

## Relation to the low-current filtration

The scale coordinate belongs to the primitive logarithmic current. It cannot
be reconstructed from the trace-class tail after completion. This explains
why the `k=1` boundary channel must remain explicit in any Schatten-three or
relative-determinant realization of the square. Removing it first leaves the
finite counterterm origin undetermined.

The prime-square channel remains a separate issue: fixing the primitive scale
does not prove compatibility of the Hilbert but non-trace-class contribution
with completion.

## Falsifier

Given any proposed completion theorem, replace `X` by `X^alpha` while keeping
the finite Euler boundary fixed as an arithmetic set. If its claimed anomaly
changes by `log alpha`, the theorem depends on an external clock and is not
source-covariant. If it transports the actual norm scale and remains
unchanged, this regulator gate passes but RH orientation remains open.

## Scope

This packet proves cutoff-clock covariance and identifies the primitive
current as the carrier of the counterterm origin. It does not prove
Mertens--completion commutativity, control the square current, or prove RH.
