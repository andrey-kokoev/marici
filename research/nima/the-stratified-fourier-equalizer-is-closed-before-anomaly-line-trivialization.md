# The stratified Fourier equalizer is closed before anomaly-line trivialization

## General closed-equalizer lemma

Let \(X_j\), \(j\in\mathbb Z/4\), be complete locally convex spaces and let

\[
F_j:X_j\longrightarrow X_{j+1}
\]

be continuous isomorphisms satisfying

\[
F_3F_2F_1F_0=I.
\]

Define

\[
X_{\mathrm{hor}}
=
\left\{
(x_j):
x_{j+1}-F_jx_j=0
\right\}.
\]

This is the kernel of the continuous map

\[
\partial_F:\prod_jX_j\longrightarrow\prod_jX_{j+1},
\qquad
(\partial_Fx)_j=x_{j+1}-F_jx_j.
\]

Hence \(X_{\mathrm{hor}}\) is closed and complete.

Evaluation at any chart is a topological isomorphism, with inverse given by
parallel transport around the four-cycle.

## Primitive stratum

The primitive response current lives in a fixed finite-exponential-order dual
rung of the projective Köthe source. The analytic Fourier transition acts
inside each labelled feature fiber and is continuous on the test topology.

Its transpose is continuous on the strong dual because a continuous linear
map sends bounded test sets to bounded test sets. Therefore the four primitive
dual presentations form a closed horizontal equalizer.

Only fixed-rung currents are claimed. No statement is made for arbitrary
elements of the full algebraic dual.

## Square stratum

The square response lies in a Hilbert direct sum. Every Fourier transition is
unitary, so the horizontal square equalizer is closed and isometric to one
chart.

Cutoff projections commute with the transition maps, and finite packets
converge in Hilbert norm.

## Connected stratum

The connected return belongs to the declared Schatten or determinant-three
ideal. Unitary conjugation preserves every Schatten norm:

\[
\|F_jKF_j^{-1}\|_{\mathcal S_3}
=
\|K\|_{\mathcal S_3}.
\]

Therefore the connected horizontal equalizer is closed in
\(\mathcal S_3\), and

\[
\det_3(I-F_jKF_j^{-1})
=
\det_3(I-K).
\]

The connected determinant line descends with one copy and no norm loss.

## Endpoint and wall--jump strata

The complete endpoint observer plane is finite dimensional. Constant--delta
exchange is unitary, and the normalized Hadamard frame diagonalizes it into
wall and jump characters.

Thus its horizontal equalizer is closed. The wall line remains external; the
jump line retains the causal theta-to-window graph attachment. Neither is
quotiented by scalar synthesis.

## Archimedean line

The local Tate sewing operator is a gamma multiplier followed by spectral
reflection. On the sewing axis its multiplier has unit modulus, so the
archimedean line transition is unitary.

Off the axis, the line remains a continuous nonvanishing transition on compact
parameter sets avoiding its poles. Hence its horizontal equalizer is a closed
line bundle there, with compact-uniform metric equivalence.

## Stratified product

Let

\[
\mathcal B_j
=
\mathcal B_j^{(1)}
\oplus
\mathcal B_j^{(2)}
\oplus
\mathcal B_j^{(3)}
\oplus
E_{\partial,j}
\oplus
\mathcal L_{\infty,j}.
\]

Give each direct summand its declared topology and form the finite direct sum.
The block Fourier transition is continuous and invertible. Therefore

\[
\mathcal B_{\mathrm{hor}}
=
\operatorname{Eq}
\left(
\prod_j\mathcal B_j
\rightrightarrows
\prod_j\mathcal B_{j+1}
\right)
\]

is closed and complete.

Prime cutoffs preserve this equalizer because they commute with every
fiberwise transition.

## Response graph

The hyperbolic input--response pairing is preserved by the block transition
and its contragredient dual action. Consequently the graph of horizontal
sewing is maximal isotropic on the completed stratified boundary carrier.

The response-trace map is continuous stratum by stratum, so its graph remains
closed after completion.

This closes the topological part of the maximal-isotropic response theorem.

## What remains: scalar line totalization

Closed stratified descent does not yet identify its determinant line with the
completed scalar section.

The unresolved map is the source-derived trivialization

\[
\tau_s:
\mathcal L_{\mathrm{prim}}
\otimes
\mathcal L_{\mathrm{sq}}
\otimes
\mathcal L_{\det_3}
\otimes
\mathcal L_{\mathrm{seam}}
\otimes
\mathcal L_\infty
\longrightarrow
\mathbb C.
\]

It must satisfy:

1. primitive and square coordinates are the first two anomaly terms of the
   same ordered return;
2. the connected coordinate is its determinant-three section;
3. reciprocal overlap maps commute with \(\tau_s\);
4. the archimedean line carries the Gaussian Mellin character;
5. the resulting scalar is a nonvanishing unit times \(\Xi(s)\);
6. cutoff trivializations have no derived-limit anomaly.

These are determinant-provenance requirements, not completion-topology
requirements.

## Consequence

All five boundary modalities can coexist in one closed Fourier-horizontal
carrier without multiplying divisor multiplicity or losing response flux.
The earlier concern that distributional primitive currents prevent closed
descent is resolved by using the strong transpose on a fixed dual rung.

The remaining obstruction is one-dimensional but not trivial: construct the
anomaly-line totalization \(\tau_s\) from source operations.

## Hostiles

1. Use the algebraic dual instead of a fixed continuous dual rung.
2. Apply one Hilbert topology to all three arithmetic strata.
3. Descend \(\det_3\) but not its primitive and square anomaly lines.
4. Treat the gamma multiplier as uniformly bounded through its poles.
5. Scalarize before forming the horizontal equalizer.
6. Infer determinant identification from closedness of the response graph.

## Verdict

The four-presentation Fourier equalizer completes as a closed stratified
boundary carrier. Primitive transpose, square Hilbert, connected
determinant-three, endpoint, and archimedean transitions all descend in their
proper topologies.

The only remaining descent gate is the source-derived anomaly-line
trivialization identifying the descended relative determinant with completed
\(\Xi\).
