# Flavor Krylov Frame Gives Cyclicity, Not Physical Orientation

## Result

Three typed Flavor ports need not come from three unrelated fields. One
triplet-valued seed \(x\) and one source-derived evolution \(A\) generate the
Krylov frame

\[
x,
\qquad
Ax,
\qquad
A^2x.
\]

Its alternating carrier is

\[
\Omega_A(x)=\det[x,Ax,A^2x].
\]

This is the finite controllability determinant of the pair \((A,x)\). It is an
alternating carrier on vector representatives, but it is not a physical
orientation observable when the seed is only a ray.

## Exact positive witness

Take

\[
A=\operatorname{diag}(1,2,3),
\qquad
x=(1,1,1)^T.
\]

Then

\[
\Omega_A(x)=2.
\]

The three ports are therefore independent even though they arise from one
seed. Their typing comes from iteration depth under the source operation \(A\),
not from copying the same field three times.

## Orientation covariance

Under a change of frame \(S\), transform both source objects:

\[
A\longmapsto SAS^{-1},
\qquad
x\longmapsto Sx.
\]

The Krylov matrix transforms by left multiplication with \(S\), so

\[
\Omega_{SAS^{-1}}(Sx)
=
\det(S)\Omega_A(x).
\]

Orientation-preserving cyclic relabellings preserve the carrier. Reflections
reverse its sign. Thus the Krylov determinant realizes exactly the alternating
local system required by the stabilizer theorem.

## WP612 correction: the sign does not descend

Flavor's common-left weak-basis group is \(U(3)\), and the physical seed is a
ray. Rephasing the representative by \(\zeta\) gives

\[
x\longmapsto \zeta x,
\qquad
\Omega_A(x)\longmapsto \zeta^3\Omega_A(x).
\]

For

\[
\zeta=e^{i\pi/3},
\]

the seed projector is unchanged while \(\zeta^3=-1\). The signed determinant
therefore flips between two representatives of the same physical seed ray.

What descends is

\[
|\Omega_A(x)|^2.
\]

For a simple-spectrum Hermitian \(A\), this is the squared spectral
Vandermonde times the product of the seed probabilities in the three
eigendirections. It is a positive cyclicity test, not an alternating Flavor
selector.

## Two exact degeneracies

The candidate vanishes if \(A\) has insufficient spectral distinction. For
example, repeating an eigenvalue makes the three iterates dependent.

It also vanishes when \(x\) misses an eigendirection, even if \(A\) has three
distinct eigenvalues. These are independent failure modes:

- the evolution does not generate three distinct responses;
- the seed does not reach the full response space.

In control language, \(x\) must be a cyclic vector for \(A\).

## Why exactly three ports

For a three-dimensional carrier, Cayley–Hamilton expresses every later iterate
as a combination of the first three. In the exact witness,

\[
A^3-6A^2+11A-6I=0.
\]

So the construction has an intrinsic three-port closure. It does not require
an indefinitely enlarged tower.

## WP610 boundary

Figueiredo's WP610 result prohibits an attractive shortcut. The existing
charged-current overlap

\[
W_{ij}=\operatorname{Tr}(P_i^uP_j^d)
\]

cannot be reinterpreted as this Krylov source. Permutation-valued \(W\) forces
the two Yukawa operators to commute and makes the Jarlskog invariant vanish,
whereas the physical Fourier hostile has uniform overlap and nonzero Jarlskog
invariant.

Accordingly, \(A\) and \(x\) must be new source operations acting on or beside
the admitted spectral ports while preserving the observed overlap data. They
cannot be fitted from the desired orientation or read backward from \(W\).

## Finite falsifiers

A proposed Krylov mediator is rejected if any of the following occurs:

1. \(\det[x,Ax,A^2x]=0\);
2. its sign does not reverse under a reflected common frame;
3. \(A\) or \(x\) is chosen from the target vacuum rather than derived from the
   source;
4. introducing the operation changes the already admitted charged-current
   overlap instead of supplying a compatible additional port.

The checker verifies the first two algebraically, together with cyclic
invariance and exact Cayley–Hamilton closure.

## Status

The Krylov mechanism remains the smallest algebraic construction of the three
typed Flavor incidences. WP612 closes its use as a physical signed selector.
It leaves a narrower control question:

Which admitted microscopic evolution \(A\) and seed port \(x\) form a cyclic
pair while leaving the physical spectral-overlap sector unchanged?

Without a separately source-derived phase or volume-reference port, even such a
pair supplies only positive cyclicity. It does not supply Flavor orientation or
a numerical prediction.
