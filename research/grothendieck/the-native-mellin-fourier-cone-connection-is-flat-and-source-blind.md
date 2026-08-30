# The native Mellin--Fourier cone connection is flat and source-blind

## Transported-cone candidate

The fixed-cone no-gos leave a cone field transported by the direct--dual
Mellin action. On one labelled pair at logarithmic coordinate `q`, write

\[
M_t=
\begin{pmatrix}
e^{itq}&0\\
0&e^{-itq}
\end{pmatrix},
\qquad
F=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

The cone field is `C_t=M_t C_0`. Fourier--Tate reflection swaps the sheets.

## Exact closing relation

Direct calculation gives

\[
FM_tF=M_{-t}.
\]

Therefore the natural direct--reflection--dual--reflection loop has holonomy

\[
FM_tFM_t=I.
\]

This closes for every `q`, every `t`, every initial cone, and every source
amplitude. It is the defining dihedral relation between translation and
reflection, not an arithmetic theorem.

The infinitesimal connection says the same thing. Its generator is

\[
A_q=iq
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\]

and reflection reverses it:

\[
FA_qF=-A_q.
\]

Thus the native transported cone bundle is flat along the only loop supplied
by Mellin motion and sheet reflection.

## Why this adds no RH force

Transporting `C_0` by `M_t` guarantees membership by definition. Closing it
with `F` adds no source constraint because the holonomy is identically the
identity before theta amplitudes, prime labels, boundary currents, or scalar
readout enter.

The positive two-atom hostile therefore admits exactly the same flat control
geometry. Nothing in this connection distinguishes its off-seam zeros from
the completed theta source.

## Required sixth datum

A non-tautological cone-field route needs an additional source-dependent leg
whose loop is not forced by the dihedral transport law. Candidates include:

- the moving endpoint/seam incidence;
- primitive and prime-square boundary currents;
- an archimedean trace map that is not determined by `M_t` and `F`;
- a transverse operator observer;
- a controlled localization with independently known kernel.

Its curvature or anomaly must be computed before scalar evaluation. The
relevant loop is then a comparison between two genuinely different paths,
not `FM_tFM_t`, whose equality is formal.

## Multi-tower reading

The input and output towers plus the transport control tower generate a flat
action groupoid. The missing wall is another comparison channel connecting
the source preparation to the boundary observer. In this sense the suspected
extra tower is real: not a higher coherence among the same arrows, but an
additional functor whose Beck--Chevalley residual can carry source content.

## Disposition

The source-independent transported-cone branch is closed. The next attack
should add the moving seam incidence to the loop and compute whether its
naturality residual is zero, source-typed, or already known to be a
constructor syzygy.

