# Minimal Phase Ports Are Cycle Holonomies

Let a finite labelled graph (G=(V,E)) support nonzero Hermitian couplings
(z_{uv}=\overline{z_{vu}}). A change of phase frame at each channel,

\[
g=(g_v)_{v\in V}\in U(1)^V,
\]

acts by

\[
z_{uv}\longmapsto g_u z_{uv}\overline{g_v}.
\]

The individual edge phases are therefore gauge coordinates, not independent
readout data. Choose a spanning forest (T\). Vertex phases can make every
coupling on (T) positive real. Each chord (e\in E\setminus T) then closes
one fundamental cycle, whose oriented holonomy

\[
h_e=\prod_{(u,v)\in C_e}\frac{z_{uv}}{|z_{uv}|}
\]

is unchanged by all vertex rephasings.

For a graph with (c) connected components, the phase quotient is

\[
U(1)^E/U(1)^{V-c}\simeq H^1(G;U(1))
\simeq U(1)^{\beta_1},
\qquad
\beta_1=|E|-|V|+c.
\]

Consequently, edge magnitudes together with one holonomy per independent
cycle reconstruct the Hermitian coupling packet up to channel rephasing.
This number is minimal: changing any one chord phase changes its fundamental
holonomy without changing any edge magnitude or tree-fixed coordinate.

## Tree and real-locus consequences

On a forest, \(\beta_1=0\). Every nonzero complex coupling can be made
positive real, so no gauge-invariant phase port exists. Asking for one would
retain a basis convention rather than an abstract distinction.

If source structure restricts all couplings to a real locus, the same
classification becomes

\[
H^1(G;C_2)\simeq C_2^{\beta_1}.
\]

Thus the earlier one-bit statement is correct for a single independent real
cycle, but it is neither the generic complex answer nor a per-edge rule.

## Triangle witness and spectral blindness

Consider the positive Hermitian matrices

\[
M_+=\begin{pmatrix}
2&1/2&-i/2\\
1/2&2&1/2\\
i/2&1/2&2
\end{pmatrix},
\qquad
M_-=\overline{M_+}.
\]

Strict diagonal dominance makes both positive definite. Every diagonal and
edge magnitude agrees. Their oriented triangle holonomies are (+i) and
(-i). Complex conjugation preserves the characteristic polynomial, so even
the complete unordered spectrum cannot choose between these two labelled
cycle orientations.

For a triangle, the determinant contains the coupling phases only through

\[
2\Re(z_{12}z_{23}\overline{z_{13}}).
\]

It therefore sees the cosine of the holonomy but loses its orientation under
(h\mapsto\overline h\). A determinant port is not a coherent holonomy port.

## Compiler boundary

The minimal phase interface depends on the authorized incidence graph:

- first derive which channels and nonzero couplings exist;
- quotient by authorized channel rephasings;
- retain one (U(1)) coordinate for each independent complex cycle;
- reduce it to (C_2) only when a real structure is source-derived;
- retain no phase coordinate on a forest unless an external frame is itself
  operative.

This is shared Carrier geometry. Choosing (U(1)), a real form, or a smaller
coefficient group belongs to the coefficient lens. No theta-specific graph or
phase group is inferred here; that application remains frozen.

## Falsifiers

- Counting one physical phase port for every nonzero edge.
- Removing a nontrivial cycle holonomy by vertex gauge.
- Treating equal spectra as equality of labelled Hermitian packets.
- Using a determinant to recover the orientation of a complex holonomy.
- Claiming a (C_2) cycle code without a source-derived real locus.
- Importing a graph topology not supplied by the source constructors.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The aim was to quotient the newly exposed (U(1)) frame by harmless
channel conventions.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The minimal phase interface is the first cohomology of the authorized
incidence graph, with dimension equal to its cycle rank.
