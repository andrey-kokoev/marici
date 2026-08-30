# Weighted endpoint incidence reproduces the exact order-three boundary filtration

Author: `marici.Nima`

Date: 2026-08-26

Status: exact asymptotic typing theorem and renormalized-unitarity correction

## Arithmetic endpoint incidence

For a displacement (q_{p,k}=k\log p), arithmetic translation moves the
endpoint by

\[
\Delta_{p,k}G
=
G(k\log p)-G(0).
\]

Weight it by the source coefficient

\[
w_{p,k}=\frac1k p^{-k/2}.
\]

The grade-$k$ endpoint current at cutoff $X$ is

\[
J_{k,X}(G)
=
\frac1k
\sum_{p\le X}
p^{-k/2}
\left(
G(k\log p)-G(0)
\right).
\]

This is the scalar boundary shadow of the weighted interval-incidence map.

## Large-prime behavior

Assume the retained tail decays so that

\[
G(q)\longrightarrow0
\]

as (q\to\infty), with (G(0)\ne0). Then

\[
G(k\log p)-G(0)
\longrightarrow
-G(0).
\]

Therefore convergence is governed by

\[
\sum_p p^{-k/2}.
\]

The three regimes are exact:

- $k=1$: the primitive endpoint current diverges with the prime
  (p^{-1/2}) mass;
- $k=2$: the square endpoint current diverges logarithmically with the prime
  harmonic mass;
- $k\ge3$: the endpoint current converges absolutely.

This is the endpoint-incidence form of the previously established Schatten
three filtration.

## Concrete decaying source

For

\[
G(q)=e^{-q},
\]

the endpoint increment is

\[
\Delta_{p,k}G=p^{-k}-1.
\]

Hence

\[
J_{k,X}
=
\frac1k
\sum_{p\le X}
\left(
p^{-3k/2}-p^{-k/2}
\right).
\]

The negative baseline term displays the primitive and square divergences
without any zero data or analytic continuation.

## Consequence for sewing

The raw weighted boundary packet does not define an ordinary Hilbert port at
infinite cutoff. Therefore the earlier abstract requirement

\[
J^*J=I
\]

cannot be imposed on the unrenormalized primitive and square scalar ports.

The correct object is the typed third-order boundary vessel:

```text
primitive endpoint current
+ square endpoint current
+ convergent connected tail
+ seam carrier
+ archimedean countercurrent
```

Losslessness must be proved as a relative or renormalized unitary law on this
complete packet. Every finite cutoff must still reproduce the ordinary
source norm exactly.

## Relation to the determinant vessel

The same first two grades removed from the scalar (det_3) tail reappear here
as nonconvergent endpoint incidences. This is not a numerical coincidence:
both arise from the first two terms of relative transport before the
trace-class connected tail begins.

Thus the determinant coherencer and the passive-boundary coherencer are two
readouts of one typed low-order current packet.

## Revised zero-confinement gate

The two-sector passive theorem remains valid only after constructing a
renormalized cross-sewing map that:

1. retains the primitive and square currents as boundary data;
2. includes the seam and archimedean countercurrent;
3. is exactly lossless at every finite cutoff;
4. descends to the third-order completion;
5. has no completion-null port direction.

Calling the raw local Tate factors unitary off seam would ignore precisely
the divergent channels that must repair their gain.

## Finite falsifiers

At increasing prime cutoffs, compute each grade separately. The construction
fails if:

- the first two grades are silently discarded;
- the connected grade begins before order three;
- the finite sum of all declared boundary currents differs from the endpoint
  incidence;
- renormalized sewing changes any finite-cutoff readout;
- a claimed raw infinite-port norm assigns finite mass to the primitive
  current without an exponential rigging or counterterm.

