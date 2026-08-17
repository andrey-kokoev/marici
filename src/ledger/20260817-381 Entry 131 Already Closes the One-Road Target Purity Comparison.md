# Entry 131 Already Closes the One-Road Target Purity Comparison

## Correction

Entry 380 correctly identifies the coefficientwise three-face target, but
its stated remaining purity comparison is not open.  Entry 131 already
constructs that comparison in the definitionally scoped absolute \(D03\)
road-face PC model.

Its theorem is

\[
\boxed{
\operatorname{pur}_{x_3,\partial}^{\rm PC}:
E_{3,\rm src}\otimes\operatorname{or}(x_3)[-1]
\xrightarrow{\sim}
i_{x_3}^{!}P_3,
}
\]

where the source is independently assembled as

\[
E_{3,\rm src}
=B\langle g_3\rangle[1]
\oplus
[B\langle h_3\rangle\xrightarrow{u_3}B\langle p_3\rangle]
\]

from Entry 129's occurrence Thom line and Entry 100's original/Borel--Moore
can--var packet.  The target \(i_{x_3}^{!}P_3\) is the actual Cartier
costalk of the Entry-105 closed-star packet, not a formal coefficient label.

Thus the arrow denoted \(\operatorname{pur}^{\rm PC}_{i3}\) in Entry 380 is
already obtained by endpoint transitivity from this one edge map.

## Endpoint transitivity

For \(i=0,1\), Entry 131 uses the canonical adjunction

\[
R\!\operatorname{Hom}_B
\left(B/(x_i),R\!\operatorname{Hom}_A(B,P_3)\right)
\simeq
R\!\operatorname{Hom}_A\left(A/(x_3,x_i),P_3\right).
\]

After the complete occurrence and normal Koszul--Cech comparisons, this
produces the two restrictions

\[
+\frac{[dX_{03}]}{x_0x_3u_0u_1u_3u_5},
\qquad
+\frac{[dX_{03}]}{x_1x_3u_0u_1u_3u_5}.
\]

These are exactly the two coefficient cells rerun for Entry 380.  Every
lower Cech term is retained.  The graph Bockstein forces the purity map to
be scalar identity on both the radial/Tor-zero and normal/Tor-one lines;
positive coorientation fixes that scalar to \(+1\).

Entry 377 independently confirms that Entry 176's relative normal cap
tensors with this same purity map and introduces no additional target-side
choice.

## What remains

The one-road target purity, its two endpoints, and its finite cap are closed.
The missing datum is instead a single source-to-target realization

\[
\boxed{
\mathfrak R_{03}:
\mathcal K_{03}^{\rm pre}
\longrightarrow
\mathcal E_{03}^{\rm PC,\check C}
}
\]

in a common mixed-variance category, whose faces simultaneously satisfy:

\[
q_J\longmapsto x_3q_{03}^{Q},
\qquad
\operatorname{gr}_{x_3}^{1}(\mathfrak R_{03})
=\operatorname{pur}_{x_3,\partial}^{\rm PC},
\]

and whose lower/endpoint boundary is the image of

\[
d(H_{\rm Morse}p-\widetilde\xi h_3)
=q_Jp-d\widetilde\xi\,h_3.
\]

Entries 378--380 determine every face of this prospective realization.
They do not construct \(\mathfrak R_{03}\) itself.  That is now the exact
one-road frontier.

## Meta-level consequence

No additional target costalk, endpoint residue, or local purity theorem
should be built.  The remaining work is a naturality/realization problem:
show that the normalization-sheet pre-quotient correspondence of Entry 356
maps into the already existing road-face PC object so that its generic,
Cartier, lower-Cech, and endpoint faces are restrictions of one morphism.

This also changes the right falsifier.  A failure now cannot be blamed on a
missing target shape or normalization.  It must appear as a nonzero
naturality obstruction in the common mapping complex, or as failure to
retain the generic \(Q\)-leg.

## Evidence boundary

This correction is a dependency synthesis, not a new purity proof.  Its
inputs are Entry 131's explicit finite Cartier theorem, Entry 377's cap lift,
Entry 378's Rees coefficient bridge, Entry 379's indivisible lower/endpoint
gate, and the freshly rerun Entry-129/130 endpoint checker recorded in Entry
380.  The mixed-variance realization \(\mathfrak R_{03}\), full primal trace,
and global \(D_3\) assembly remain unconstructed.
