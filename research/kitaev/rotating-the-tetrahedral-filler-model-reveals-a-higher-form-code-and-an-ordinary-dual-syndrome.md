# Rotating the tetrahedral filler model reveals a higher-form code and an ordinary dual syndrome

Owner: marici.Kitaev

## Question

What is the tetrahedral filler-volume syndrome when the same finite object is
rotated through primal--dual geometry, error correction, control, gauge theory,
and categorical semantics?

## Claim boundary

The tetrahedral model is not one exotic object with several loose analogies.
It is one incidence complex viewed through different variances and coefficient
lenses.

Let a tetrahedron carry a face cochain

\[
a\in C^2(\Delta^3;\mathbb F_2),
\]

with edge-reference transformation

\[
a\longmapsto a+\delta b,
\qquad
b\in C^1(\Delta^3;\mathbb F_2),
\]

and volume syndrome

\[
\Omega=\delta a\in C^3(\Delta^3;\mathbb F_2).
\]

In coordinates,

\[
\Omega
=
a_{123}+a_{023}+a_{013}+a_{012}.
\]

### Rotation 1: higher-form gauge theory

The face labels form a discrete \(2\)-form gauge potential. The edge labels are
\(1\)-form gauge parameters. The tetrahedral value \(\Omega\) is the
gauge-invariant \(3\)-form curvature.

This is the finite higher-form analogue of:

\[
A\mapsto A+d\lambda,
\qquad
F=dA.
\]

The identity

\[
\delta^2=0
\]

is the source of gauge invariance. The “higher coherence residue” is therefore
a curvature measurement of a 2-connection.

A nonzero \(\Omega\) need not be a mistake. It can be a real higher flux. It is
a defect only when the declared task requires a flat 2-connection.

### Rotation 2: classical parity code

Order the four face bits into a vector

\[
a=(a_{123},a_{023},a_{013},a_{012}).
\]

Then the syndrome map is the single parity check

\[
H=
\begin{pmatrix}
1&1&1&1
\end{pmatrix},
\qquad
\Omega=Ha.
\]

The flat face assignments form the \([4,3]\) even-parity code

\[
\ker H.
\]

A single flipped face changes the syndrome, but the one-bit syndrome does not
locate the error. The code detects one face flip but does not correct an
arbitrary one.

Thus the apparently higher categorical obstruction is also the simplest
four-bit parity syndrome.

### Rotation 3: cellular duality

In a three-dimensional cellulation, primal 2-cells are dual to dual 1-cells,
and primal 3-cells are dual to dual 0-cells.

Therefore

\[
\delta:C^2_{\mathrm{primal}}\to C^3_{\mathrm{primal}}
\]

rotates into

\[
\partial:C_{1,\mathrm{dual}}\to C_{0,\mathrm{dual}}.
\]

The four primal face bits become the four dual edges incident on the dual
vertex associated with the tetrahedron. Their volume parity becomes the
ordinary boundary or star syndrome at that dual vertex.

This is the decisive observation:

> A third-rung primal coherence obstruction can be a first-rung local incidence
> syndrome in the dual Carrier.

Rung height is therefore relative to chosen variance and cellular
presentation. What remains invariant is the typed incidence relation and its
kernel/image structure.

### Rotation 4: toric-code degree shift

The original two-dimensional toric code places qubits on edges and uses vertex
and plaquette checks. The tetrahedral model is the next-degree pattern: data
live on faces, gauge repairs live on edges, and curvature syndromes live on
volumes.

It is a finite fragment of a higher-form toric-code architecture. Under duality
it returns to edge data and vertex checks.

This explains why the same Carrier geometry keeps recurring. The coefficient
degree changes which geometric cells carry state, repair, and syndrome, while
nilpotence remains the common parent.

### Rotation 5: control and observability

Treat \(a\) as the internal filler state and \(\Omega=Ha\) as the measured
output. The observability kernel is

\[
\ker H,
\]

which has dimension three. The single volume port observes only total face
parity, not the individual filler state.

Edge-reference actuation moves \(a\) by \(\operatorname{im}\delta_1\). On the
full tetrahedron,

\[
\operatorname{im}\delta_1=\ker H.
\]

Thus the unobserved flat directions are exactly gauge-reachable directions in
the finite algebraic model. The output is faithful on the quotient

\[
C^2/\operatorname{im}\delta_1.
\]

This is a perfect finite match between controllability and observability
quotients. It does not provide a physical actuator or measurement constructor.

### Rotation 6: descent and distributed consistency

Each face carries a local comparison filler. The volume syndrome asks whether
the four local comparisons glue into one coherent tetrahedral assignment.

Zero \(\Omega\) is the finite descent condition. Nonzero \(\Omega\) is an
overlap inconsistency that cannot be removed by edge-level reparameterization.

But gluing existence and gluing choice remain distinct. When \(\Omega=0\), the
compatible face data still have a three-dimensional gauge family before
quotienting.

### Rotation 7: anomaly and inflow

View the tetrahedral boundary as a closed surface surrounding one volume. A
nonzero boundary filler parity can be interpreted as an anomaly of the
boundary data. Adjoining a bulk 3-cell carrying the matching value cancels or
absorbs that anomaly.

This makes precise the difference between:

- declaring the boundary residue zero;
- supplying a bulk constructor whose boundary is that residue.

The second is an inflow mechanism and changes the source complex. It does not
show that the boundary theory closed by itself.

### What survives every rotation

The stable structure is:

\[
C^1
\xrightarrow{\delta_1}
C^2
\xrightarrow{\delta_2}
C^3,
\qquad
\delta_2\delta_1=0.
\]

Every rotation preserves:

- the typed locations of state, repair, and syndrome up to duality;
- gauge invariance of the syndrome;
- the distinction between detection and correction;
- quotient faithfulness;
- the need for source authority to add a filler or actuator;
- the coefficient dependence of additive versus ordered transport.

What does not survive unchanged is the narrative that one cell dimension is
intrinsically “higher.” Primal 3-curvature and dual vertex syndrome are the
same incidence datum.

### Consequence for the tower programme

Tower height should not be indexed solely by geometric dimension. It should be
indexed by dependency type:

- object data;
- transformations;
- comparisons between transformations;
- comparisons between comparisons.

Cellular duality can exchange geometric dimensions without changing that
categorical dependency.

Therefore a claimed new rung must pass a duality test:

1. rotate the Carrier;
2. determine whether the obstruction becomes an already understood lower
   incidence syndrome;
3. retain a higher rung only if its constructor typing, order, or context
   cannot be eliminated by the rotation.

This test prevents presentation-dependent inflation of the tower.

## Disposition

The tetrahedral syndrome is now identified simultaneously as:

- 3-curvature of a finite 2-form gauge field;
- parity check of a \([4,3]\) classical code;
- ordinary star syndrome at a dual vertex;
- next-degree toric-code incidence;
- quotient-faithful control output;
- descent obstruction;
- possible boundary anomaly requiring bulk inflow.

The highest-information conclusion is negative: geometric height alone does
not establish categorical novelty.

The next test should rotate the nonabelian tetrahedral model. If ordered
whiskering and associators survive every primal--dual presentation, then that
residue is genuinely higher constructor structure rather than a degree-shifted
abelian syndrome.
