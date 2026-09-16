# The linear trace growth is a pro-horn obstruction in the terminal six-to-seven slab of the eight-lattice tetrahedron

## Nature of the obstruction

For every finite Paley--Wiener window \(L\), the affine crossing identity closes exactly:

\[
\Delta T_{\nu,L}
+
2\Delta T_{I,L}
=0.
\]

Thus there is no algebraic defect in any fixed signed tetrahedron.

The obstruction appears only under cutoff exhaustion:

\[
\|P_{\gamma,L}\|_1
=
\frac{2L}{\pi}
\longrightarrow
\infty.
\]

Therefore it is not a missing signed face. It is failure of the finite-window fillers to define a bounded compatible filler in the pro-limit.

## Location in the eight-node lattice

The atomic current is created by the final source-to-spectral arrow

\[
d_{13,6}:
C_{13,6}
	o
C_{13,7}^{aff}.
\]

The physical cutoff and its volume subtraction are carried by the geometry-to-trace edge

\[
C_{24,4}
	o
C_{24,5}
	o
C_{24,6}
	o
C_{24,7}.
\]

Since \(C_{13}\) and \(C_{24}\) are opposite tetrahedral edges, their comparison is not one triangular face. It passes through the central tetrahedral filler assembled from the four adjacent faces.

Hence the divergence is localized in the terminal level slab

\[
6
	o
7
\]

of the central comparison between the opposite edges.

## Four-face horn

At finite \(L\), the terminal horn has the following faces.

### Source--spectral face \(H_{123}\)

This face constructs the atomic source form

\[
(p,q)
\longmapsto
m_p(\gamma)
\overline{m_q(\gamma)}
+
m_p(-\gamma)
\overline{m_q(-\gamma)}.
\]

It is bounded on the finite-window source graph.

### Spectral--trace face \(H_{134}\)

This face realizes that form by

\[
P_{\gamma,L}
=
|k_{\gamma,L}\rangle
\langle k_{\gamma,L}|
+
|k_{-\gamma,L}\rangle
\langle k_{-\gamma,L}|.
\]

Its trace norm is \(2L/\pi\).

### Source--geometry face \(H_{124}\)

This face transports the observer into the physical cutoff geometry. It must determine the normalization with which point observations enter the cutoff trace.

No established comparison currently shows that this normalization contributes a reciprocal volume factor.

### Geometry--trace face \(H_{234}\)

This face contains the Plancherel-volume subtraction and relative cutoff trace. Its coefficient is already known exactly from Mellin--Plancherel normalization.

However, its observer dependence is the bulk functional

\[
2Lh(1)
=
\frac L\pi
\int_{\mathbb R}
|m_g(t)|^2dt,
\]

whereas the localized hostile rotor has leading trace

\[
\frac L\pi
\left(
|m_g(\gamma)|^2
+
|m_g(-\gamma)|^2
\right).
\]

These are different functionals. Therefore the canonical volume subtraction cannot cancel the atomic rotor growth for all observers. A new crossing-specific finite-rank geometric/index row is required; no theorem currently constructs it on the \(C_{24}\) carrier.

## The missing filler

The unresolved cell is a central terminal filler

\[
F_{6,7,L}
\]

whose boundary compares

\[
P_{\gamma,L}
\]

on the spectral side with the relative-volume term on the geometric side.

A successful filler must establish one of two mechanisms.

### Crossing-specific cancellation mechanism

Construct a finite-rank geometric/index counterterm \(V_{\gamma,L}\), distinct from the ordinary Plancherel-volume subtraction, such that

\[
\sup_L
\|P_{\gamma,L}-V_{\gamma,L}\|_1
<
\infty.
\]

For complete cancellation one would have

\[
\operatorname{Tr}V_{\gamma,L}
=
rac{2L}{\pi}
+o(1).
\]

### Renormalized-density mechanism

Show that the physical trace naturally includes the inverse Plancherel volume

\[
\frac{\pi}{L}.
\]

Then

\[
\frac{\pi}{L}
P_{\gamma,L}
\]

has trace two. This mechanism is valid only if the same normalization is forced by the \(C_{24}\) cutoff trace; inserting it solely on \(C_{13}\) changes the Green current.

## Pro-horn formulation

Let \(L_1<L_2<\cdots\) be a cofinal cutoff sequence. For every \(L_n\), there is a finite-window terminal filler

\[
F_{6,7,L_n}.
\]

The required global object is a compatible pro-filler

\[
F_{6,7,\infty}
=
\varprojlim_n
F_{6,7,L_n}
\]

in the declared trace or graph category.

The affine identities ensure algebraic compatibility, but the estimate

\[
\|P_{\gamma,L_n}\|_1
	o
\infty
\]

shows that the family is not bounded in the trace-class bornology. Therefore the horn has fillers levelwise but no admitted bounded pro-filler with the current data.

## Tetrahedral obstruction class

The obstruction may be recorded by the growth class

\[
\omega_{\gamma}(L)
=
[
P_{\gamma,L}
]
\]

in the quotient of levelwise trace-class terminal fillers by uniformly trace-bounded families.

Its scalar shadow is

\[
\operatorname{Tr}
\omega_{\gamma}(L)
=
rac{2L}{\pi}.
\]

The affine spectral-flow correction kills the signed jump inside each finite tetrahedron, but it does not kill \(\omega_\gamma\). These are distinct obstructions:

1. affine clutching controls deformation in \(a\);
2. the pro-horn class controls exhaustion in \(L\).

## Two external directions

The full family is indexed by both crossing and cutoff parameters:

\[
\operatorname{esd}_7(\Delta^3)
\times
\widetilde I_a
\times
\mathbb R_{L,+}.
\]

The \(a\)-direction has affine transition cycle \(A_\gamma\). The \(L\)-direction has linear trace growth \(2L/\pi\).

The mixed square asks whether affine clutching commutes with cutoff renormalization. This mixed coherence is not yet proved.

## Regression criterion

A proposed global physical realization must provide a terminal central filler satisfying:

1. the finite-window affine identity;
2. compatibility under \(L\)-transition maps;
3. a uniform relative trace-class bound after the declared geometric subtraction;
4. preservation of dagger symmetry;
5. preservation of successor pullbacks;
6. no ad hoc rescaling of only the spectral face.

Failure of item 3 is exactly the current hostile obstruction.

## Disposition

In the canonical eight-lattice tetrahedron, the remaining linear divergence is represented by a pro-horn obstruction in the terminal \(6\to7\) central slab comparing the opposite edges \(C_{13}\) and \(C_{24}\).

Every finite tetrahedron fills. The family of fillers is not uniformly admitted as \(L\to\infty\). The ordinary geometric volume counterterm is already formed but has the wrong observer functional to cancel the rotor. The missing theorem is a crossing-specific finite-rank geometric/index row on \(H_{234}\), or an operator realization proving an equivalent cancellation, that matches the rank-two growth on \(H_{134}\).
