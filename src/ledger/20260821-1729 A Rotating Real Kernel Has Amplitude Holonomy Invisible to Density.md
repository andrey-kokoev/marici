# 1729 — A Rotating Real Kernel Has Amplitude Holonomy Invisible to Density

## Rotating-kernel falsifier

Let a real rank-one kernel rotate around a parameter circle:

\[
k(\phi)=
\begin{pmatrix}
\cos(\phi/2)\\ \sin(\phi/2)
\end{pmatrix},
\qquad 0\le\phi\le2\pi.
\]

The kernel line closes in \(\mathbb{RP}^1\), but its amplitude lift obeys

\[
k(2\pi)=-k(0).
\]

## Amplitude versus density

The amplitude line therefore has holonomy

\[
\boxed{\operatorname{Hol}_{\rm amp}=-1.}
\]

Its Hermitian square is the rank-one projector

\[
P(\phi)=k(\phi)k(\phi)^T,
\]

for which

\[
P(2\pi)=P(0),
\qquad
\boxed{\operatorname{Hol}_{\rm dens}=+1.}
\]

A Čech cycle checker verifies that the amplitude sign product remains \(-1\)
under every vertex gauge, while squaring every transition makes the density
product \(+1\).

## Narrow result

Rotating singular readout can carry genuine Berry/\(\mathbb Z_2\) holonomy in
the amplitude coefficient local system even when the density observable is
globally single-valued.  The Hermitian-square readout erases central phase.

This holonomy requires no new carrier stratum.  It is also not identified with
the cosmological time-root \(\mathbb Z_2\); equality would require a separate
comparison map.

## Durable artifacts

- `research/benincasa/checkers/rotating_kernel_z2_holonomy.rs`
- `research/benincasa/results/rotating-kernel-z2-holonomy.json`
- `research/benincasa/rotating-kernel-z2-holonomy.md`

## Next falsifier

Complexify the kernel line and compute its \(U(1)\) Berry connection.  Test
whether Hermitian-square density transport forgets only central phase or also
loses curvature detectable by supported interference comparisons.
