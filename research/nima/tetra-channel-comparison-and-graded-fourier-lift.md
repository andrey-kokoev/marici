# Tetrahedral/channel comparison and the graded Fourier lift

The canonical Tate-torus model matches the semidirect incidence skeleton of the eight-lattice source, but the stable helix relation requires one additional grading step.

## Tetrahedral coordinate embedding

For `4|n`, choose the channel `d_0=(0,2)` and its quarter-rotation orbit

\[
d_i=q^i d_0,\qquad 0\le i<4.
\]

For `n>=8` these are four distinct channels. Define

\[
B_n:\mathbb Z^4\hookrightarrow\mathbb Z^{D_n},
\qquad B_n(e_i)=e_{d_i}.
\]

If `rho` cyclically permutes tetrahedral coordinates and `Q` rotates channel coordinates, then

\[
Q B_n=B_n\rho.
\]

Thus the mixed relation `q u = rho(u) q` is realized on the generator/incidence skeleton. The choice `(0,2)` uses the existing labelled-polygon framing; an unlabelled polygon would retain the expected conjugacy ambiguity.

## Why ordinary Fourier is insufficient

The universal stable source requires

\[
q^4=\Sigma,
\]

whereas Pontryagin Fourier on distributions satisfies

\[
\mathcal F^4=I.
\]

Therefore the ungraded Tate-torus model is not by itself a realization functor from the full stable universal category.

## Graded Fourier lift

Pass to the stable category of graded complexes of lattice distributions and torus functions. Use objects `(h,i,A)` with homological degree `h` and chart phase `i in Z/4`. Define

\[
\widetilde{\mathcal F}(h,i,A)=
\begin{cases}
(h,i+1,\mathcal FA),&i=0,1,2,\\
(h+1,0,\mathcal FA),&i=3.
\end{cases}
\]

Since ordinary Fourier has fourth power identity,

\[
\widetilde{\mathcal F}^{\,4}(h,i,A)
=(h+1,i,A)
=\Sigma(h,i,A).
\]

Hence the graded lift realizes the helix relation exactly rather than forcing suspension to be trivial through periodicization. It also commutes with the channel permutation, so the semidirect relation survives the lift.

## Remaining gate

This establishes comparison on:

- objects and incidence generators;
- tetrahedral/channel rotation;
- the mixed semidirect relation;
- the stable four-step helix relation.

It does not yet assign the designated triangular quotient cells to specific nonzero cofiber triangles or verify the tetrahedral octahedral cells. Those exactness assignments are the remaining data needed for a full exact functor from the universal stable category.

`check_tetra_channel_semidirect_comparison.py` verifies `Q B_n=B_n rho` at `n=8,12,16,20` and explicitly records the need for the graded shift lift.
