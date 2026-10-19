# An arrow's local and configuration-wide response

## Question and claim boundary

Can the same elementary arrow have distinct responses to its incident relationships and to the full configuration, with the incident geometry held fixed?

The experiment uses the retained tetrahedral geometric carrier. It preserves all twelve labelled directed arrow occurrences. Its field realization is declared explicitly: a static surface-flux norm and its response operator. It is not the retained L/G/N dynamics, a recovered electromagnetic connection, a physical clock, or a particle-mass calculation. Here **full response** means the full declared field operator, not every relationship in the native 1836-transfer protocol. The four roles are comparison roles on one carrier, not successive simplices by definition.

## Frozen experiment

The [preregistration](C:/Users/andrey/src/marici/research/strominger/inputs/arrow-anchored-response-freeze.json) and checker were SCC-frozen before execution. The exact frozen fingerprint is `22ce0569e6a8e9517e51e1687cd2b5ec4ecb53741e4757facc76c699e6e3edbd`.

- **Problem:** separate anchored local response from configuration-wide response.
- **Bold conjecture:** moving the remote geometry while keeping AB's incident geometry and full local response row unchanged changes its full anchored response.
- **Rivals:** symmetry shields AB; a scalar readout hides an off-anchor change; the purported remote move actually changed an incident face.
- **Risky consequence:** the entire anchored response packet changes, not merely an aggregate of the configuration.
- **Strongest falsifier:** test the source's equal incident-face weights first, retain every response coordinate, and check two distinct response probes. Use a separately labelled unequal-weight control, fixed across the same geometry pair.
- **Disposition:** the universal sensitivity conjecture is falsified. The symmetry-protection rival survives. The control supplies a concrete distinction between local and configuration-wide dependence.

## Source and realization

The checker verifies the retained Merkle source, all 1836 native coefficient transfers, and both producer-input hashes. It does not rerun producers or change their stores.

There are twelve distinct directed geometric arrow occurrences. All remain present with the stipulated unit resource weight. Opposite orientations have opposite **field readouts**, not cancelling resource weights. Six antisymmetric field coordinates are therefore a readout convention, not six surviving arrows.

Each whole-face loop is obtained by adding its three actual source centroid-triangle boundary chains. Internal radial edges cancel exactly. In edge order `(AB,AC,AD,BC,BD,CD)` and source face order `(ABC,ABD,ACD,BCD)`, the comparison map is

\[
C=\begin{pmatrix}
1&-1&0&1&0&0\\
-1&0&1&0&-1&0\\
0&1&-1&0&0&1\\
0&0&0&-1&1&-1
\end{pmatrix}.
\]

An edge field `a` has loop curvature `b=C a`. The source closure is `sum(b)=0`; the vertex-gradient map `G` satisfies `C G=0`. Neither identity chooses a response metric.

Choose the norm of a face-averaged flux integrated over that face:

\[
Q(a)=\frac12\sum_f\frac{A_0}{A_f}(C_fa)^2,
\qquad K=C^T\operatorname{diag}(A_0/A_f)C.
\]

Here `A_0` is one source face area. This is the declared geometry-dependent weighting, not a fitted mass law. Complex field readouts could be treated by Hermitian extension; this first test uses the real subspace and does not select complex phases.

The response probe is

\[
R_s=(K+sI)^{-1},\qquad x=R_s e_{AB},\qquad s\in\{1,2\}.
\]

The probe makes the gauge kernel invertible for this comparison. It is not physical time, a chosen frequency, a rest-energy offset, or a mechanism for assigning mass. An independent environment-Schur reconstruction verifies every response packet.

## Remote change with the local patch fixed

Hold A, B and C fixed; rotate D properly about AB. The exact new point is `(5/3,-5/3,5/3)`.

All five side lengths appearing in ABC or ABD are preserved, as are their intrinsic face geometries. CD changes. Source face area squares are `(12,12,12,12)`; after the hinge they are `(12,12,128/9,128/9)`.

**Important scope:** ABD rotates in ambient space; its normal and the ABC–ABD dihedral angle change. Thus this holds the local intrinsic metric and the complete local row of the declared operator fixed, not the native ambient face projectors. If “the two faces unchanged” means their full embedded coordinates, a single tetrahedron offers no remote move: those faces already contain all four vertices. That stronger experiment requires an enlarged carrier with genuinely remote vertices.

Thus the incident metric entries stay `(1,1)`, while the remote entries become `3 sqrt(6)/8`. The entire AB row of K stays identical. The registry and all twelve unit resource weights stay identical.

## Results

At `s=1`, with the other coordinates clamped, AB responds by `1/3`. Letting the entire configuration respond gives

\[
x=(3/5,1/5,1/5,-1/5,-1/5,0).
\]

That is already a strict distinction between local and collective response. But the remote hinge leaves this **entire packet** unchanged, not just its AB entry. The curvatures are `(1/5,-1/5,0,0)`: both remote loops are dark to this anchored excitation.

The full resolvent nevertheless changes, with difference of rank two. Consequently, a globally different configuration need not be distinguished by every rooted measurement.

The shielding is exact, not a tolerance effect. For equal unit incident weights,

\[
K(K e_{AB})=4K e_{AB},\qquad
R_s e_{AB}=e_{AB}/s-K e_{AB}/[s(s+4)].
\]

The remote face rows annihilate `K e_AB`, so remote metric weights cannot enter this rooted packet. The second probe confirms the same protection.

### Deliberately unequal incident-weight control

Multiply the ABD face metric by two in **both** configurations. This control is an explicit constitutive perturbation, not a source-discovered rule. Its full AB row still stays fixed through the hinge.

At `s=1`, the local response is `1/4` in both configurations. The full AB response changes from

\[
23/40=0.575
\]

to

\[
\frac{2364-6\sqrt6}{4085}\approx0.575104788627491.
\]

The difference is exactly `(121-48 sqrt(6))/32680`, which is positive. The full rooted packet also changes. The source control has remote curvatures `(-1/40,-1/40)`, rather than zero.

This exposes the mechanism:

\[
\frac{\partial (R_s)_{AB,AB}}{\partial w_f}
=-(C_fR_se_{AB})^2.
\]

A remote relationship changes the anchored response when the anchored excitation reaches that relationship. Geometry changing elsewhere is insufficient when those channels are shielded.

## Contribution to the four roles

These are retained comparison aspects in this realization, not definitions that exhaust the user's four roles or the native transfer relationships.

1. **Arrow:** all twelve persistent labelled unit occurrences survive every comparison.
2. **Relationships between arrows/configuration:** source loop comparisons plus the full geometric metric and operator.
3. **Arrow relative to its relationships:** AB's incident packet, complete local operator row, and clamped response.
4. **Arrow relative to all relationships:** its complete collective response, all twelve occurrence readouts, all four curvatures, the environment Schur complement and the full configuration resolvent.

The fourth role is not exhausted by the tetrahedral closure scalar. Nor does it guarantee that any single anchored readout distinguishes every global change. Here the primitive remains the anchor, collective response differs from local response, and symmetry decides which further relationships are visible to it.

## Executable record

The [checker](C:/Users/andrey/src/marici/research/strominger/checkers/check_arrow_anchored_response.py) passed eleven exact checks. The [result packet](C:/Users/andrey/src/marici/research/strominger/results/arrow-anchored-response.json) retains every response coordinate, all operators and resolvents, source boundary chains, primitive readouts and source hashes. SCC records the challenge as **falsifying** the universal-sensitivity conjecture, not proving it.

Registry-wide SCC inspection also reported an unrelated invalid Nima manifest (`four-channel-yoneda`: empty checks). It was not repaired here; the owner-local manifest validates and its frozen challenge ran successfully.
