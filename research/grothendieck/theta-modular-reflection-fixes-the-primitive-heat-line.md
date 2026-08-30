# Modular reflection fixes the primitive heat line

## Bounded question

Is the primitive channel `H_1` from packet 115 independent completion data,
or is it fixed by reciprocal modular sewing?

## Differentiated modular identity

Let

\[
 \Theta(t)=\sum_{n\in\mathbb Z}e^{-\pi tn^2}
 =1+2\sum_{n\ge1}e^{-\pi tn^2}.
\]

Then

\[
 \Theta(t)=t^{-1/2}\Theta(1/t)
\]

and

\[
 \Theta'(t)=-2\pi H_1(t).
\]

Differentiating the modular equation gives

\[
 \Theta'(t)
 =-\frac12t^{-3/2}\Theta(1/t)
 -t^{-5/2}\Theta'(1/t).
\]

Therefore

\[
 \boxed{
 H_1(t)+t^{-5/2}H_1(1/t)
 =\frac{t^{-3/2}}{4\pi}\Theta(1/t).}
\]

The two reciprocal representatives of the primitive line do not vary
independently. Their oriented sum is the positive theta-vacuum channel.

## Self-dual seam

At `t=1`, the two representatives coincide, so

\[
 \boxed{
 H_1(1)=\frac{\Theta(1)}{8\pi}.}
\]

Thus the missing primitive datum at the seam is completely determined by the
zeroth theta vacuum.  It is not an adjustable counterterm.

## Corrected closure architecture

Packet 115 found

\[
 \text{completed moment tower}+\text{one primitive line}.
\]

The modular derivative identity upgrades this to

\[
 \boxed{
 \text{two reciprocal completed towers}
 +\text{theta seam value}
 \Longrightarrow
 \text{closed derivative system}.}
\]

This is the precise bilateral repair that the one-sided tail-flow calculation
could not supply.  The primitive norm line is not cancelled by declaration;
its two oriented copies sew to a positive source-fixed boundary value.

## What remains

The identity controls the first primitive channel and, by repeated
differentiation, generates modular relations among all raw heat moments.
However, it does not automatically prove that eliminating the reciprocal
primitive pair yields a positive Schur complement in the complex Mellin
parameter.

The next calculation is finite and sharp: construct the two-chart augmented
matrix for `(Theta,H_1,M_0)` at the seam, derive its canonical bilinear form,
and compute the Schur complement that produces the first generalized
Laguerre/vertical-curvature coefficient.  Its sign must follow without using
zero locations.

The falsifier is a negative Schur complement despite the exact modular sewing
identity. That would prove that closure and positivity of the source packet do
not suffice to orient the analytic continuation.
