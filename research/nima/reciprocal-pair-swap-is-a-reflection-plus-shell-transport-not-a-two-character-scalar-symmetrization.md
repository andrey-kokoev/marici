# Reciprocal pair swap is a reflection plus shell transport, not a two-character scalar symmetrization

## Question

Can the ordered-pair and swapped-pair Laplace responses be combined merely by
replacing the ratio character with a symmetric pair such as
\((m/n)^z+(n/m)^z\)?

## Claim boundary

No. Pair swap also changes the object-indexed shell and reflects the correlation
separation. The exact swap requires moving-seam transport before scalar
symmetrization. This identifies another mandatory comparison cell for the
reciprocal/linking response.

## Base reflection identity

For

\[
 K_{[A,B]}(d)
 =\int_A^B\Phi_1(v)\Phi_1(v+d)\,dv,
\]

change variables \(x=v-d\) to obtain

\[
 K_{[A,B]}(-d)
 =K_{[A-d,B-d]}(d).
\]

Thus separation reflection is accompanied by a translation of both shell
endpoints. The kernel is not even at a fixed finite shell.

## Ordered pair

Let

\[
 d=\log\frac mn,
 \qquad
 A_n=a+\log n,
 \qquad
 B_n=b+\log n.
\]

Then

\[
 \rho_{nm}^{[a,b]}(t)
 =(nm)^{-1/2}K_{[A_n,B_n]}(t+d).
\]

The swapped pair is

\[
 \rho_{mn}^{[a,b]}(t)
 =(nm)^{-1/2}K_{[A_m,B_m]}(t-d),
\]

where

\[
 A_m=A_n+d,
 \qquad
 B_m=B_n+d.
\]

Both the separation shift and the shell object change.

## Laplace responses

The first response is

\[
 R_{nm}(z)
 =(nm)^{-1/2}e^{zd}
 \int_d^\infty e^{-zw}K_{[A_n,B_n]}(w)\,dw.
\]

The swapped response is

\[
 R_{mn}(z)
 =(nm)^{-1/2}e^{-zd}
 \int_{-d}^\infty e^{-zw}K_{[A_m,B_m]}(w)\,dw.
\]

These are not two scalar characters multiplying one common transform. Their
lower limits and shell fibres differ.

## Required moving-seam comparison

The repository already supplies object-indexed moving-seam transport

\[
 T_{A_m\leftarrow A_n}
\]

and its endpoint mate. Any reciprocal pairing of \(R_{nm}\) with \(R_{mn}\)
must use this transport to compare the shell fibres before taking an even or
odd combination.

After transport, the reflection identity determines the orientation of the
finite ratio-segment cocycle. Omitting transport is equivalent to identifying
object-indexed Mellin metrics at different shell positions, which is not
source-authorized.

## Diagonal case

When \(n=m\),

\[
 d=0,
 \qquad
 [A_n,B_n]=[A_m,B_m],
\]

and the finite ratio cocycle vanishes. This special case does not authorize the
scalar treatment of off-diagonal pairs.

## Hostile

A proposed response of the form

\[
 (nm)^{-1/2}
 \left[
 \left(\frac mn\right)^z
 +\epsilon
 \left(\frac nm\right)^z
 \right]H(z)
\]

with one shell-independent \(H\) fails unless it separately reconstructs:

1. the translated shell fibres;
2. the lower-limit corrections at \(d\) and \(-d\);
3. the moving-seam metric comparison;
4. the reciprocal orientation sign \(\epsilon\).

Scalar character symmetry alone supplies none of these maps.

## Candidate-one consequence

The reciprocal port cannot be source-normalized solely by the functional
equation's two ratio characters. Its ordered-pair lift must compose
ratio reflection, shell transport, and the oriented finite Laplace cocycle.
This requirement is independent of Xi-zero fitting.

## Disposition

Reciprocal pair swap is now fully typed at the correlation level. The missing
G4 comparison is narrowed to whether its reciprocal/linking block implements
this shell-transported reflection and finite cocycle. No RH conclusion is
authorized.
