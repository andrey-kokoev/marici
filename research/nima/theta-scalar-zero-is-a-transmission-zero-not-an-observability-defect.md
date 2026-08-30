# Theta scalar zero is a transmission zero, not an observability defect

## Status

Exact control-theoretic typing correction. A zero of a distinguished
source-to-readout channel is an invariant transmission-zero question. It is
not resolved by proving that the internal state is observable, controllable,
energetic, or recoverable from a larger output family.

This identifies the correct finite compiler for any proposed theta control
realization and explains why the optical dark-port and arithmetic-erasure
constructions improve state resolution without implying RH.

## State-space gate

For a finite realization

\[
x_{k+1}=Ax_k+Bu_k,
\qquad
y_k=Cx_k+Du_k,
\]

the Rosenbrock system matrix is

\[
\mathcal P(\lambda)=
\begin{pmatrix}
\lambda I-A&-B\\
C&D
\end{pmatrix}.
\]

An invariant transmission zero is a value \(\lambda\) for which there are
\(x\) and \(u\), not both zero, satisfying

\[
(\lambda I-A)x-Bu=0,
\qquad
Cx+Du=0.
\]

Equivalently, \(\mathcal P(\lambda)\) loses rank. The state and input form a
nontrivial internal trajectory whose distinguished output is dark.

## Observability is a different question

Observability tests whether

\[
Cx=CAx=\cdots=CA^{n-1}x=0
\]

forces \(x=0\) when the input is absent. Transmission-zero analysis permits a
nonzero input to sustain the dark trajectory. Consequently, a minimal system
can be both controllable and observable while retaining transmission zeros.

Adding enough output rows may make the full state visible without removing a
zero of one distinguished output row.

## Smallest optical witness

A balanced two-path interferometer is unitary and its resolved route state has
positive norm. At destructive phase, one detector port is dark while the
orthogonal port is bright. Resolving both ports reconstructs the state, but it
does not make the original dark-port amplitude nonzero.

This is simultaneously:

- a faithful full-output realization;
- a lossless energy balance;
- a transmission zero of the selected scalar channel.

Therefore neither observability nor losslessness is a zero-exclusion law.

## Arithmetic character witness

For the two-label packet

\[
a=(1,-1),
\]

the trivial aggregation port vanishes and the complementary character port is
nonzero. The complete character family is faithful, yet the distinguished
trivial port remains dark.

This is the static Rosenbrock analogue: enlarging the output family removes
state ambiguity while preserving the selected-channel zero.

## Correct RH compiler target

Any source-derived theta realization must distinguish three questions:

1. whether the labelled internal packet is nonzero;
2. whether a declared output family is faithful on that packet;
3. whether the distinguished completed scalar channel has invariant zeros off
   the critical seam.

Only the third question carries RH force.

The required finite falsifier for a proposed realization is a nontrivial
kernel vector of its Rosenbrock matrix at an off-seam spectral parameter. A
positive state Gramian, complete tomography, or nonzero complementary output
does not repair that rank loss.

## What kind of law could exclude the zero

A viable source law would need to place the distinguished transfer channel in
a zero-free class before its scalar divisor is inspected. Candidate forms
include a source-derived strict positive-real law, an outer or minimum-phase
factorization, or a collocated passive realization whose strictness survives
completion.

Each candidate has a hard circularity gate. It is rejected if its strictness,
outerness, inverse bound, or collocation is obtained by dividing by the
completed scalar section or by assuming its nonvanishing.

Passivity without source-derived port collocation is insufficient. A passive
multiport can have a dark selected channel while total energy is conserved.

## Consequence

The control lane should stop asking whether a zero-state is observable. The
sharper question is whether the actual theta source supplies a realization in
which the distinguished scalar port is source-locally minimum phase in each
open half-plane.

If no such realization is constructed before scalar completion, control
theory supplies an exact taxonomy of the obstruction but no RH proof.
