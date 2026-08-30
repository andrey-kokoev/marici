# Endpoint Anchor Plus Path Derivative Energy Proves the Unit Gap

Let \(u:[0,L]\to\mathbb C\) be absolutely continuous with the source-fixed
endpoint normalization

\[
u(0)=1.
\]

Define the path derivative energy

\[
E=\int_0^L|u'(x)|^2\,dx.
\]

Cauchy–Schwarz gives, for every \(x\in[0,L]\),

\[
|u(x)-1|
\le
\sqrt{x}\left(\int_0^x|u'(t)|^2dt\right)^{1/2}
\le\sqrt{LE}.
\]

Therefore the strict energy condition

\[
LE\le q^2<1
\]

implies

\[
|u(x)|\ge1-q,
\qquad
\|u^{-1}\|_\infty\le(1-q)^{-1}.
\]

By the preceding small-norm compiler, it also supplies a canonical logarithm,
zero winding, and every finite root frame.

## Sharpness

On \([0,1]\), the affine family

\[
u_a(x)=1-ax
\]

has derivative energy \(E=a^2\) and saturates the estimate at \(x=1\):

\[
|u_a(1)-1|=a=\sqrt E.
\]

At \(a=1\), the endpoint value vanishes. For

\[
a_N=1-N^{-1},
\]

every finite stage satisfies \(E_N<1\), but the inverse norm equals \(N\) and
the gap collapses. A cutoff-independent strict energy margin is mandatory.

## Path coverage is a constructor

For a larger domain, the theorem applies if every admissible point is joined
to the vacuum anchor by a source-authorized path of length at most \(L\), with
the derivative energy along each such path bounded by \(E\). Without path
coverage, endpoint anchoring controls only its connected component. On two
disconnected components, a function can equal one on the anchored component
and zero on the other while having zero derivative energy on both.

Likewise, a bulk \(L^2\) derivative energy does not automatically bound every
path restriction. A trace, Sobolev, or foliation theorem is required to pass
from the bulk Clark/Green channel to the path energy used here.

## Theta/Tate consequence

This gives Grothendieck a direct route from the Clark derivative and endpoint
channels to normalization closure. The finite target is:

1. identify the scalar normalization ratio \(u_X\) and its vacuum endpoint;
2. derive a source-native family of paths covering the off-seam domain;
3. prove a uniform path length \(L_K\);
4. dominate the path derivative energy by \(E_K\) with
   \(L_KE_K<1\).

If the available Green identity controls only bulk energy, the missing step is
now exactly the bulk-to-path trace estimate. The seam channel may be essential
for that step, but its authority must come from the source geometry.

## Falsifiers

- The energy margin approaches the threshold one.
- A bulk derivative norm is substituted for path energy without a trace
  theorem.
- Some admissible component has no path to the vacuum anchor.
- Path lengths grow with cutoff.
- Endpoint normalization is imposed after solving rather than derived from the
  source vacuum.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to compile Clark derivative energy and endpoint data into
the uniform unit estimate.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The sharp energy threshold is exact, and the sole geometric typing gap
is isolated as source-authorized path coverage plus bulk-to-path control.
