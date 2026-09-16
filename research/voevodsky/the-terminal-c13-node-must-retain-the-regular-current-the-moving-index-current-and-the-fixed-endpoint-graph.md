# The terminal \(C_{13}\) node must retain the regular current, the moving index current, and the fixed endpoint graph

## Prior-research alignment

Prior work already splits a localized relative Hardy trace into regular and index parts:

\[
\Delta Q_L
=
\Delta Q_L^{regular}
+
\Delta Q_L^{index}.
\]

It also retains the fixed completed endpoint evaluations at \(z=\pm i/2\) in a separate analytic graph sector.

The missing issue is therefore not invention of another scalar current. It is typing these three channels together at the terminal source-to-spectral presentation, choosing a topology that retains both one-sided crossing limits, and supplying the affine spectral-flow clutching that identifies them.

## Existing terminal edge

The final source-to-spectral step is

\[
C_{13,6}
=
(B_S,J_{loc,S})
\longrightarrow
C_{13,7}
=
(H_S^+,H_S^-,B_S,V_{loc,S}).
\]

The notation \(V_{loc,S}\) is adequate only on a stratum where the phase has a fixed smooth branch and no pole crosses the boundary.

## Augmented terminal object

Replace the terminal presentation by

\[
C_{13,7}^{aug}
=
(
H_S^+,
H_S^-,
B_S,
\mu_{reg,S},
\mu_{idx,S},
\beta_{end,S}
).
\]

The three current coordinates have distinct roles.

### Regular current

\[
\mu_{reg,S}
=
\frac1{2\pi i}
\partial_t
\log J_{loc,S}(t)
\,dt
\]

on every fixed divisor stratum after branch and pole terms are removed.

It acts on source polarization by

\[
\langle
\mu_{reg,S},
\overline{m_h}m_g
\rangle.
\]

### Moving index current

For a deformation parameter \(a\) along which poles cross the spectral boundary, \(\mu_{idx,S}\) is the atomic spectral-flow current.

For the symmetry-completed hostile fixture,

\[
\mu_{idx,0^+}
=-
(
\delta_\gamma+
\delta_{-\gamma}
),
\]

\[
\mu_{idx,0^-}
=+
(
\delta_\gamma+
\delta_{-\gamma}
)
\]

up to the declared orientation normalization.

Its source pairing is

\[
\langle
\mu_{idx,S},
\overline{m_h}m_g
\rangle
=
\sum_j
n_j
m_g(t_j)
\overline{m_h(t_j)}.
\]

### Fixed endpoint graph

\[
\beta_{end,S}(g)
=
\begin{pmatrix}
m_g(i/2)\\
m_g(-i/2)
\end{pmatrix}
\]

with swap metric

\[
J_{end}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

This is not part of the moving real-boundary atomic current.

## Current target space

For a fixed compact boundary interval \(I\), choose

\[
\mathscr I_I
=
H^{-s}(I),
\qquad
s>
\frac12.
\]

Then point masses belong to \(\mathscr I_I\), and Poisson crossing profiles converge to their delta limits.

Globally, use the projective weighted distribution carrier

\[
\mathscr I_\partial
=
\varprojlim_{I,w}
H^{-s}(I;w),
\]

with weights chosen to accept the completed logarithmic growth while retaining Schwartz source pairing.

The exact global weight is not fixed by the crossing fixture and must be inherited from the completed gamma--prime estimates.

## Continuity on the source core

For Mellin--Schwartz observers,

\[
\overline{m_h}m_g
\in
\mathcal S(\mathbb R).
\]

Therefore regular tempered currents and finite atomic index currents act continuously on every fixed source pair.

A completed source theorem requires a bound of the form

\[
|\langle
\mu,
\overline{m_h}m_g
\rangle|
\le
C_\mu
\|g\|_{\mathscr G_r}
\|h\|_{\mathscr G_r}
\]

uniformly on the admitted deformation and regulator stratum.

This uniform estimate is not presently proved for moving divisor families.

## Successor law

Let a convolution successor act by Mellin multiplication with \(m_a\). Then the current itself is unchanged as a distribution attached to the background multiplier, while its observed pullback transforms by

\[
\overline{m_h}m_g
\longmapsto
|m_a|^2
\overline{m_h}m_g.
\]

For an atom at \(t_j\),

\[
\delta_{t_j}
\longmapsto
|m_a(t_j)|^2
\delta_{t_j}
\]

at the level of observed forms.

If \(m_a(t_j)=0\), that successor annihilates the atomic observation. This is loss of source faithfulness at \(t_j\), not cancellation of the background index.

## Dagger law

The source dagger acts on the real boundary by

\[
t
\longmapsto
-t.
\]

Hence

\[
D_\partial
\delta_\gamma
=
\delta_{-\gamma}.
\]

For symmetry-completed packets, the atomic pair

\[
\delta_\gamma+
\delta_{-\gamma}
\]

is dagger invariant, while its orientation sign changes under reversal of the crossing parameter.

## Green readout

The terminal spectral presentation maps to the Green/trace presentation by

\[
H_{134}^{aug}
=
H_{134}^{reg}
+
H_{134}^{idx}
+
H_{134}^{end}.
\]

Here:

1. \(H_{134}^{reg}\) is the localized relative Hardy trace of the smooth phase derivative;
2. \(H_{134}^{idx}\) is the finite-rank spectral-flow projection associated with moving boundary crossings;
3. \(H_{134}^{end}\) is the fixed completed endpoint residue form.

Prior research constructs the first and third channels on fixed strata and declares an index channel for winding and pole crossings. The missing theorem is one joint deformation-stable Green identity with all three channels and uniform graph bounds.

## Lattice placement

No ninth sequential edge node is required for the static signed lattice. The decomposition is retained as internal data of

\[
C_{13,7}^{aug}.
\]

Every tetrahedron incident to the terminal \(C_{13}\) segment is enriched by the same three-channel target.

The parameterized crossing family lives over an oriented blow-up of

\[
\operatorname{esd}_7(\Delta^3)
\times
I_a
\]

at the crossing stratum. Its before and after lattices are related by an affine spectral-flow clutching map. The moving index current supplies the transverse comparison data; it is not an ordinary continuous vector-valued coordinate at the unblown crossing point.

## What is constructed

The following typing is now fixed:

1. regular current, moving index current, and fixed endpoint graph are separate coordinates;
2. their one-sided source pairings are explicit;
3. convolution-successor and dagger laws are explicit;
4. the correct terminal \(C_{13}\) placement is identified;
5. no confusion remains between moving boundary atoms and the fixed odd endpoint line.

## What remains analytical

The following are still open:

1. a global weighted distribution topology for the complete current;
2. uniform source-graph bounds under divisor motion;
3. insertion of the affine index clutching into the joint Green identity;
4. compatibility with infinite divisor accumulation;
5. physical positive compression after all current channels are retained.

## Disposition

The missing construct is represented as an enrichment of the terminal \(C_{13}\) node, not as an additional arbitrary lattice vertex.

The canonical eight-level signed lattice survives. Deformation through a crossing adds one external parameter direction, while the moving spectral-flow current supplies its transverse analytic data.
