# 2855 — The Physical Soft Chamber Selects an Occurrence, Not a Deck Character

## Source chamber

The residue-surface coordinate is

\[
a=y_{23}.
\]

The frozen physical integration chamber requires

\[
y_{23}\ge0.
\]

For generic \(-1<\kappa<1\), both endpoint collision squares

\[
A_-=(5-4\kappa)p^2,
\qquad
A_+=(5+4\kappa)p^2
\]

are strictly positive. Each algebraic endpoint therefore has two collision germs

\[
a=+\sqrt{A_\pm},
\qquad
a=-\sqrt{A_\pm},
\]

but only the positive germ lies in the closure of the physical chamber.

## Physical occurrence covector

In the ordered basis

\[
\bigl(e_{+\sqrt A},e_{-\sqrt A}\bigr),
\]

the physical chain covector is

\[
V_{\rm phys}=(1,0).
\]

This selection is source-derived from positivity; it is not a fitted character projection.

Under the deck swap

\[
T=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\]

one has

\[
V_{\rm phys}T=(0,1).
\]

Thus the physical chamber covector is not monodromy invariant. It selects an occurrence, not the invariant or anti-invariant character of the complete algebraic packet.

## Consequence

The physical evaluations of the marked and unmarked endpoint packets are well-defined on the positive chamber and reproduce their positive-germ entries. However, this does not construct a comparison between them: they retain different relative degrees and differ by \(p\)-weight three.

Accordingly:

- the full occurrence modules are the correct global coefficient objects;
- the positive chamber supplies a source-authorized local readout;
- analytic continuation transports that readout to another occurrence;
- no global scalar endpoint sum follows from the chamber selection alone.

The remaining test is the relative-chain boundary map between the marked and unmarked endpoint degrees. It must be derived before their two chamberwise values can be combined.

## Durable artifacts

- research/benincasa/check_soft_endpoint_physical_occurrence_covector.py
- research/benincasa/soft-endpoint-physical-occurrence-covector.json

