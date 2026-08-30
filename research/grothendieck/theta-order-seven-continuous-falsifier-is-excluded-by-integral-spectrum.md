# The order-seven continuous falsifier is excluded by the integral spectrum

## Scope correction

Packet 110 correctly derives the general Wronskian residual and an order-seven
sign reversal for the **continuous relaxation** `x>=1`.  Its claim that this
crossing lies in the physical spectrum is false.  The completed circle has

\[
 x=n^2,
 \qquad n\in\mathbb Z\setminus\{0\},
\]

so seven distinct spectral labels cannot cluster near `x=1`.

## Exact faithful order-seven theorem

Packets 109--110 prove `P_r>0` on the whole continuous box for `r<=6`.  Hence

\[
 \partial_{y_i}P_7=2P_6>0.
\]

Among seven distinct positive winding energies

\[
 y_i=\pi t n_i^2,
 \qquad t\ge1,
\]

the minimum of `P_7` is therefore attained at `t=1` and
`|n_i|=1,2,...,7`.  Since `pi>3`, coordinatewise monotonicity gives

\[
 P_7(\pi1^2,\pi2^2,\ldots,\pi7^2)
 >P_7(3\cdot1^2,3\cdot2^2,\ldots,3\cdot7^2).
\]

Exact integer evaluation yields

\[
 \boxed{
 P_7(3\cdot1^2,3\cdot2^2,\ldots,3\cdot7^2)
 =3218949258543>0.}
\]

Thus the completed kernel is strictly sign-regular through order seven on its
faithful integral spectrum.

## What the continuous crossing means

The crossing

\[
 22/7<y_*<7/2
\]

is still an exact falsifier of sign regularity after continuous spectral
relaxation.  It shows that positivity is not supplied by the analytic formula
`b(t,x)` alone.  Arithmetic discreteness supplies essential separation between
authorized modes.

The correct conclusion is therefore

\[
 \boxed{
 \text{continuous carrier loses orientation at order seven, while the
 integral source does not}.}
\]

This is a direct instance of the durable Marici rule: a claim made after
forgetting the faithful quotient coordinate can invent a collision absent
from the source-labelled system.

## New all-order conjecture

The live conjecture is now discrete:

> For every `r`, every `t>=1`, and every distinct positive integers
> `n_1<...<n_r`, the residual
> `P_r(pi t n_1^2,...,pi t n_r^2)` is positive.

The derivative recursion reduces this inductively to the boundary sequence

\[
 Q_r=P_r(\pi1^2,\pi2^2,\ldots,\pi r^2).
\]

A proof needs an exact positive representation or recurrence for `Q_r`; a
small finite census is not sufficient.  The smallest faithful falsifier is
the first `r` with `Q_r<=0`.

## Disposition

Packet 110 remains valid as a continuous-relaxation theorem and falsifier. Its
physical-spectrum conclusion is superseded by this packet. Ledger entry 2505
must be read with this correction; the graph claim is preserved as immutable
history and separately criticized in graph event
`ev-000000003460-8a1d5f10-d6ef-4c6a-8418-3caef46baf59`.
