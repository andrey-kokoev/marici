# The completion trace requires half-density-twisted history, not plain Volterra history

## Granularity defect

Plain Volterra history detects the zero-frequency mass

\[
\int_{\mathbb R}g(u)\,du.
\]

But the completion differential

\[
\mathcal C
=
\partial_u^2-\frac14
=
\left(\partial_u-\frac12\right)
\left(\partial_u+\frac12\right)
\]

has relative trace ports at the two half-density characters:

\[
M_-(g)=\int e^{-u/2}g(u)\,du,
\qquad
M_+(g)=\int e^{u/2}g(u)\,du.
\]

Therefore the previously constructed plain endpoint jump is faithful on its own two-endpoint system but is not yet the Wronskian completion trace. Linking it directly to the Euler/Wronskian odd port would compare different spectral locations.

## Twisted causal resolvents

The source-matched histories are the conjugated Volterra operators

\[
(H_-g)(u)
=
e^{u/2}
\int_{-\infty}^{u}
e^{-v/2}g(v)\,dv,
\]

and

\[
(H_+g)(u)
=
e^{-u/2}
\int_{-\infty}^{u}
e^{v/2}g(v)\,dv.
\]

They satisfy

\[
\left(\partial_u-\frac12\right)H_-g=g,
\]

\[
\left(\partial_u+\frac12\right)H_+g=g.
\]

Their renormalized outgoing traces are exactly

\[
\lim_{u\to\infty}e^{-u/2}H_-g(u)
=
M_-(g),
\]

\[
\lim_{u\to\infty}e^{u/2}H_+g(u)
=
M_+(g).
\]

Thus the two weighted Wronskian moments are endpoint jumps of the correctly twisted histories.

## Reciprocal reflection

Reflection exchanges the two first-order factors:

\[
R
\left(\partial_u-\frac12\right)
R
=
-
\left(\partial_u+\frac12\right).
\]

After matching causal and anti-causal orientations, it exchanges the two twisted history channels. The even and odd pushforward ports are therefore

\[
w_{1/2}
=
\frac{M_-+M_+}{\sqrt2},
\qquad
j_{1/2}
=
\frac{M_+-M_-}{\sqrt2}.
\]

These are the actual completion wall and reciprocal-jump coordinates.

## Repair of the earlier incidence calculation

The plain Volterra identity

\[
\langle\Phi',T\Phi\rangle
=
-\|\Phi\|_2^2
\]

remains a valid zero-frequency causal square law. It does not by itself normalize the half-density odd port \(j_{1/2}\). The twisted incidence coefficients must be recomputed using \(H_-\) and \(H_+\).

This is a repair, not a rejection of the relative-history architecture:

- the label tensor factor remains valid;
- the wall-extended graph-space method remains valid after exponential conjugation;
- endpoint Hadamard faithfulness remains valid;
- only the history generator and trace weights change.

## Correct next theorem

Construct the pair of exponentially twisted relative Sobolev spaces on which \(H_-\) and \(H_+\) are closed, prove reciprocal reflection exchanges them, and compute their theta incidences. Only then can the jump port be linked to the Euler ratio or Wronskian current with exact normalization.
