# A vacuum state alone does not authorize feedback attenuation

## Question

What is the minimal categorical and operator signature required to turn a
distinguished Fock vacuum into an authorized attenuation family?

## Pointedness is insufficient

A vacuum state is a distinguished arrow

\[
\eta:\mathbf 1\longrightarrow E
\]

from the tensor unit into an environment object. It fixes a reference state.
By itself it supplies no operation mixing the visible boundary port \(P\)
with \(E\).

Therefore:

- a tensor unit can fix a canonical frame;
- a vacuum vector can initialize an auxiliary system;
- neither constructs a beam splitter or feedback attenuator.

The missing datum is an interaction.

## Minimal linear dilation signature

For amplitude-level attenuation of a port \(P\), the smallest dilation uses
an environment port of the same linear type and a unitary

\[
U_\tau:P\oplus E\longrightarrow P\oplus E,
\qquad 0\le\tau\le1.
\]

After choosing an authorized identification \(E\simeq P\), the canonical
matrix is

\[
U_\tau=
\begin{pmatrix}
\sqrt{\tau}I&\sqrt{1-\tau}I\\
-\sqrt{1-\tau}I&\sqrt{\tau}I
\end{pmatrix}.
\]

The visible compression is

\[
\pi_PU_\tau\iota_P=\sqrt{\tau}I_P.
\]

If both the outgoing and returning incidence legs pass through this
compression, the round-trip feedback receives the factor \(\tau\).

This construction requires all of:

1. a dagger or inner-product structure;
2. a biproduct or two-port sum \(P\oplus E\);
3. source-authorized scalar amplitudes and square roots;
4. an identification of the environment with the port type;
5. vacuum initialization;
6. visible and environment output projections;
7. a rule for retaining or terminating the environment.

Pointed monoidal structure supplies only part of item five.

## Full dilation versus visible channel

The unitary \(U_\tau\) preserves total norm. The visible compression is a
contraction because amplitude escapes into the environment.

These are different systems:

- the full dilation has both output ports;
- the visible channel discards or terminates one port;
- the feedback Schur complement depends on which environment paths can
  return.

To obtain exactly

\[
S_\tau=D-\tau CA^{-1}B,
\]

the environment output must not re-enter the visible loop, and the direct
block \(D\) must remain uncoupled from it. Otherwise extra vacuum-mediated
terms appear.

## Minimal dilation uniqueness

For the scalar contraction \(\sqrt{\tau}I_P\), every minimal unitary dilation
has the same visible compression and is unique up to a unitary change of
environment frame.

Thus:

- the visible attenuation law is canonical once \(\tau\) and the port metric
  are fixed;
- the dilation frame is a gauge torsor;
- physical claims involving the environment output require a chosen frame or
  frame-invariant formulation.

This is the same architecture as the sheet-origin torsor: a canonical
quotient behavior need not select a unique implementation frame.

## Composition requires fresh vacuum

Visible attenuation satisfies

\[
\sqrt{\tau}\sqrt{\sigma}=\sqrt{\tau\sigma}.
\]

But composing two dilations with the same coherent environment generally
does not realize the visible channel at \(\tau\sigma\). The environment
retains memory and can return amplitude.

The semigroup law

\[
\mathcal A_\tau\mathcal A_\sigma=\mathcal A_{\tau\sigma}
\]

requires either:

1. a fresh vacuum environment for each attenuation;
2. an environment reset or trace operation;
3. a Fock factorization providing independent vacuum increments.

This is the dilation cocycle required under composition. Without it,
cutoffwise attenuation can accumulate hidden common-mode memory.

## Constructor-equivalence criterion

Two attenuation implementations are constructor-equivalent only if they
agree on:

- the visible channel;
- the environment-output relation;
- the fresh-vacuum or memory rule;
- the sheet action;
- the cutoff composition law.

Agreement only on the scalar visible factor is scalar equivalence. It does
not identify the full dilation.

## Theta/Tate application

To authorize the feedback homotopy, the theta/Tate source must derive:

1. a boundary port object \(P_s\);
2. a vacuum port \(E_s\) of compatible type;
3. a coherent rotation \(U_{\tau,s}\);
4. covariance under Fourier–Tate sheet exchange;
5. compatibility with primitive, square, seam, and archimedean rows;
6. a fresh-vacuum factorization under cutoff or parameter composition;
7. a theorem identifying the visible compression with the desired scaled
   Schur term.

The distinguished Fock vacuum is a candidate for item two. None of the other
items follows from its existence.

## Hostile fixtures

### Vacuum without interaction

Take a visible port and a distinguished environment vector but no mixing
unitary. No attenuation channel is defined.

### One-leg attenuation

Scaling \(B\) by \(\sqrt{\tau}\) while leaving \(C\) unchanged produces a
round-trip factor \(\sqrt{\tau}\), not \(\tau\).

### Discarded environment geometry

Two minimal dilations can have the same visible scalar channel but different
environment frames and seam actions. They are not constructor-equivalent if
the environment remains observable.

### Environment reuse

Two rotations through the same environment produce interference and memory
terms. The visible composition need not equal attenuation by the product
parameter.

### Full-system substitution

Invertibility of the full unitary dilation does not imply invertibility of
the compressed visible Schur complement.

## Relation to Aspect's corrected instrument

Aspect's two-port fixture realizes the exact signature. Visible and vacuum
amplitudes \(3/5\) and \(4/5\) form a full unitary port. Passing both
incidence legs through the visible compression yields the round-trip factor
\(9/25\), not \(3/5\). Retaining vacuum outcomes distinguishes the full
dilation from its visible compression.

This is an operational model of the theorem, not source authority for the
theta/Tate port.

## Disposition

The minimal attenuation constructor is now classified. It is a
vacuum-initialized two-port unitary dilation plus a termination and
fresh-vacuum composition law. A vacuum or tensor unit alone is insufficient.

The theta/Tate feedback homotopy remains conditional until these arrows are
derived or the physical Schur index is computed directly without
attenuation.

## Claim boundary

This packet proves a finite linear dilation classification. It does not
derive a theta environment port, Fock factorization, seam-compatible mixing,
or compressed-index theorem.
