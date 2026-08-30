# 2843 — The Two Soft Endpoints Belong to Different Relative Variances

## Marked source factor

The exceptional source form contains

\[
R(a,\xi)=
\frac{a+p}
{2p(a-p)^2(a+3p)(\xi+1)}.
\]

This factor must be retained when promoting Entry 2841's pure Cayley–Menger periods to the marked-relative coefficient system.

## Negative endpoint

At \(\xi=-1\), two structures coincide:

1. the Cayley–Menger branch collision;
2. the divided marked wall \(q_{g1}/X_1=\xi+1\).

The source has logarithmic normal order \(-1\). The correctly typed object is therefore an iterated specialization

\[
\operatorname{Res}_{q_{g1}}
\phi_{\rm CM},
\]

with its Gysin/degree shift.

## Positive endpoint

At \(\xi=+1\), the Cayley–Menger branch collision remains, but

\[
\xi+1=2

\]

is a unit. This endpoint carries the unmarked specialization

\[
\phi_{\rm CM}
\]

at normal order zero.

## Genericity audit

The pure collision roots obey

\[
A_--p^2=4(1-\kappa)p^2,
\qquad
A_+-p^2=4(1+\kappa)p^2.
\]

Hence the marked \(a=p\) collision occurs only at the deeper base endpoints \(\kappa=+1\) and \(\kappa=-1\), not for generic \(-1<\kappa<1\).

## Consequence

The two \(\xi\)-endpoint occurrences are not two entries of one ordinary rank-two covector. They are objects of different relative variance and normal degree. The required comparison is a relative de Rham/Gysin cone combining

\[
\operatorname{Res}_{q_{g1}}\phi_{\rm CM}
\]

with

\[
\phi_{\rm CM}.
\]

Only after constructing its degree shift and comparison map can one define a total endpoint readout or test contragredient transport. A direct \(VU-I\) calculation on the pair from Entry 2841 would be mistyped.

## Durable artifacts

- `research/benincasa/check_soft_endpoint_relative_variance.py`
- `research/benincasa/soft-endpoint-relative-variance.json`
