# Finite Cauchy observation closes every Euler grade

## Setup

For a finite prime cutoff \(X\), let the raw labelled carrier be diagonal:

\[
A_X(t)e_p=p^{-1/2-it}e_p,
\qquad p\leq X.
\]

Let \(T\) have the centered Cauchy law of scale \(1/2\), whose characteristic
function is

\[
\mathbb E e^{iuT}=e^{-|u|/2}.
\]

Define

\[
D_Xe_p=p^{-1}e_p.
\]

## Exact moment intertwining

For every integer \(k\geq1\),

\[
\mathbb E\,A_X(T)^k=D_X^k.
\]

Indeed, on the \(p\)-labelled coordinate,

\[
\mathbb E\left[p^{-k/2-ikT}\right]
=p^{-k/2}e^{-k\log p/2}
=p^{-k}.
\]

Thus Cauchy observation intertwines every finite Euler grade before scalar
summation.

## Regularized determinant identity

Expanding the finite Euler logarithm grade by grade gives

\[
\mathbb E\log|Z_X(T)|
=\sum_{k\geq1}\frac1k\operatorname{Tr}D_X^k.
\]

Equivalently,

\[
\mathbb E\log|Z_X(T)|
=\operatorname{Tr}D_X-log\det_2(I-D_X).
\]

The three declared scalar grades are therefore:

\[
\operatorname{Tr}D_X,
\qquad
\frac12\operatorname{Tr}D_X^2,
\qquad
\sum_{k\geq3}\frac1k\operatorname{Tr}D_X^k.
\]

This is an exact finite observer--determinant comparison. No zero divisor or
analytic continuation is used.

## Global threshold

As the prime cutoff grows:

- \(\operatorname{Tr}D_X=\sum_{p\leq X}p^{-1}\) diverges;
- \(\operatorname{Tr}D_X^2=\sum_{p\leq X}p^{-2}\) converges;
- every connected grade \(k\geq3\) converges absolutely, and their sum is
  dominated by the already-established trace-class tail.

Hence the scalar observer--completion obstruction is localized exactly to the
primitive grade. The square and connected observed scalar grades are not the
source of the Mertens anomaly.

## Typing boundary

This scalar result does not collapse the filtered carrier:

- raw \(A_X\) is third-Schatten globally, not Hilbert--Schmidt;
- raw \(A_X^2\) is Hilbert--Schmidt but not trace class;
- Cauchy observation improves their scalar moment summability;
- the full boundary-bearing state still retains endpoint, gamma, seam, and
  extension data absent from the traces.

Therefore the result closes finite grade-wise scalar observation but does not
prove state-valued observer--completion interchange.

## Finite falsifier

A proposed anomaly assigned to the observed square or connected scalar grades
must exhibit a divergence there. The prime majorants \(p^{-2}\) and
\(p^{-3}\) forbid such a divergence. Any remaining scalar discrepancy must be
traced to primitive renormalization or to a boundary operation performed
before the scalar readout.

## Verdict

Finite Cauchy observation commutes exactly with every Euler moment. After
observation, all grades from two onward complete absolutely. The live RH cell
is now localized to the primitive Mertens finite part and its coupled
endpoint--gamma boundary completion, while the state-valued filtered carrier
must remain intact until that interchange is resolved.

