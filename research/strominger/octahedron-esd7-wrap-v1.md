# Wrapping the symmetric octahedron over ESD7 without losing its records

## Result

**A record-preserving wrap over ESD7 can be constructed, but it is not a rigid whole-cell fold.**

The source is the current edge-7 P/E-symmetric octahedron: **224 P, 231 N, 224 E**, or 679 whole cells. The target is the existing whole-cell ESD7 carrier: 119 tetrahedra and 56 octahedra, or 175 cells. These are geometric records, not established particles.

A four-chart piecewise-affine map carries the entire octahedron bijectively onto the ESD7 envelope. Its inverse is explicit. Intersecting the transported source with the native target cellulation yields **2,000 labelled restriction pieces over all 175 target cells**. Every original source cell is recoverable. No original cell is discarded or reinterpreted as one particle.

**27 exact checks pass**, including shared seams, inverse recovery, transported metrics, full source/target volume coverage and a deletion hostile. The viewer is unchanged.

The active SCC obligations are **forward realization and attachment transport**, before readout descent. This settles a finite geometric representation problem, not phase/witness dynamics, nuclear stability or the proposed 256-record capacity.

## 1. Why an ordinary native fold fails

The strict candidate requires a continuous map that takes each whole source cell isometrically onto a whole native ESD7 cell and agrees on every shared vertex and triangular face. Distinct source occurrences may initially be allowed to share target geometry; their identities must still be retained.

Both native cellulations have an important property: each triangular face has at most one tetrahedral owner and at most one octahedral owner. Every interior face joins unlike kinds.

Fix the image of one source octahedron, including its vertex map. A neighboring tetrahedron must share the specified target face. There is at most one native tetrahedron there. Its position is forced, and it lies on the opposite side of the face. The alternative reflected placement on the same side is not a native target owner. The same argument propagates from a tetrahedron to its neighboring octahedron.

Because the source is face-connected, every subsequent cell is forced into the **same global rigid frame**. There is no independent crease choice that folds unlike neighboring cells onto a common target cell. The global rigid image cannot fit 679 distinct whole source cells into 175 target cells.

The finite checker also enumerates all possible initial octahedral frames: **56 target octahedra × 48 octahedral symmetries = 2,688 candidates**. None contains the entire source. The largest whole-cell overlap is 159. Roles are not used to reject placements, so permitting P/E exchange cannot repair this geometric obstruction.

This is a no-go for the specified native, unit-metric, full-face fold. It is not a ban on refinements, deformations, multiple charts, non-native target geometry or retained records over a smaller carrier.

The earlier [two-copy fibration fold](../realization-tower/fibration-folded-process.mjs) starts from a different construction: two reflected copies with 350 retained occurrences over 175 geometric cells. It is not a fold of this connected 679-cell native octahedron.

## 2. An explicit four-chart wrap

Let

\[
c=(1/2,1/2,1/2,-1/2),\qquad h=7/2,
\]

and choose the three orthogonal source axes

\[
a=(1,1,-1,-1),\quad b=(1,-1,1,-1),\quad d=(1,-1,-1,1).
\]

For a source point with coordinate sum one, define

\[
u=\frac{(q-c)\cdot a}{4h},\quad
v=\frac{(q-c)\cdot b}{4h},\quad
w=\frac{(q-c)\cdot d}{4h}.
\]

The source envelope is exactly

\[
|u|+|v|+|w|\leq1.
\]

Choose the diagonal through the two \(w\)-poles. The signs of \(u\) and \(v\) divide the octahedron into four tetrahedral charts. This choice comes from the octahedral geometry, **not an identification with the four cycle phases**.

Map the four equatorial poles to the four target corners:

- \(u+\) and \(u-\) go to corners 0 and 1;
- \(v+\) and \(v-\) go to corners 2 and 3;
- \(w+\) goes to the midpoint of target edge 01;
- \(w-\) goes to the midpoint of target edge 23.

Thus the four source tetrahedra map to the four target tetrahedra around the segment joining the midpoints of two opposite edges. This is a declared framing choice, not a uniquely selected physical operation.

For the explicit map, set

\[
e=\frac{1-|u|-|v|+w}{2},\qquad
f=\frac{1-|u|-|v|-w}{2}.
\]

Its target barycentric coordinates are

\[
\begin{aligned}
\beta_0&=e/2+\max(u,0), &\beta_1&=e/2+\max(-u,0),\\
\beta_2&=f/2+\max(v,0), &\beta_3&=f/2+\max(-v,0).
\end{aligned}
\]

They are nonnegative and sum to one. In the viewer's coordinate convention, the target corners have one coordinate \(-5\) and three coordinates 2, so

\[
q'_i=2-7\beta_i.
\]

The inverse is

\[
u=\beta_0-\beta_1,\quad
v=\beta_2-\beta_3,\quad
w=2\min(\beta_0,\beta_1)-2\min(\beta_2,\beta_3),
\]

\[
q=c+h(ua+vb+wd).
\]

These formulas prove bijectivity throughout the envelopes, not merely at sampled nodes. The chart formulas agree on the seams because their absolute-value expressions agree there.

## 3. Metric and duality must travel with the records

Each affine chart has determinant \(1/4\) in three independent coordinate components. The source envelope has four times the Euclidean volume of the target envelope. This is not a Euclidean isometry.

Source lengths can nevertheless be represented faithfully by carrying the metric. In three independent components the source metric is

\[
G=I+\mathbf1\mathbf1^T.
\]

For a chart matrix \(A\), attach

\[
G'=A^{-T}GA^{-1}.
\]

The checker verifies \(A^TG'A=G\) for all four charts. These transported metrics are **not** the standard native ESD7 metric. The native-unit-metric gate remains failed; changing coordinate representation must not be presented as repairing it.

Likewise source P/E inversion is \(D(q)=2c-q\). Its target action is the conjugate

\[
D'=FDF^{-1}.
\]

It is not ordinary Euclidean central inversion of the tetrahedron. Source roles remain attached to their original cell IDs. They cannot be read off from target tetrahedral colors. This constructs geometric dual transport, not a phase or witnessing operator.

## 4. Bind the wrap to the actual ESD7 cells

The envelope map alone does not land on the native cell complex. In particular, the two selected edge midpoints are half-integer points at edge length seven. There are **224 mapped vertices outside the native ESD7 vertex set**. Merely drawing the wrapped shape as a tetrahedron would hide this mismatch.

The source cells are first split at the two chart seams, without discarding their parent records:

- 679 original source cells;
- 91 source cells meet more than one chart;
- 784 chart fragments;
- 1,832 exact seam comparisons;
- 392 boundary fragment faces and 1,736 internal fragment faces.

Then intersect every mapped chart fragment with each overlapping native target cell. Each nonempty, positive-volume intersection retains

```
source cell ID
source P/N/E role
chart and parent fragment ID
target ESD7 cell ID
exact rational vertices and volume
```

The result is **2,000 restriction records**. The shared carrier is the common refinement, with a projection to the original source records and another projection to the 175 target cells. Neither projection licenses merging source identities.

Exact volume checks, using the three-independent-coordinate determinant convention, establish all of the following:

- each native target cell is fully covered;
- each original source cell retains its full mapped volume;
- source fragment volume is \(686/3\);
- target volume is \(343/6\), exactly one quarter of the source;
- every intersection vertex has the declared chart inverse;
- deleting one restriction piece violates both its source and target coverage contracts.

The source-cell vertex sets are recovered exactly from the tagged chart images. This is a concrete recovery test, not just equal aggregate counts.

**171 target cells carry all three source roles; four carry N records only.** Thus a single P/N/E color per ESD7 cell would erase the transported object. The four N-only cells are not identified with the four positional records of ledger 4332; the count does not supply that conjectural map.

## 5. What this permits next

A faithful viewer could offer an **ESD7 chart view** with:

1. the native ESD7 carrier drawn as a separate grid;
2. selectable source-cell records and their restriction pieces;
3. a source/wrapped toggle using the explicit inverse;
4. source-dual selection using the conjugated action;
5. counts labelled by source records, target cells and restriction pieces separately.

It should not recolor each target cell as a single particle, claim native unit geometry, or change 224/231/224 to 82/126/82. A physical-mode reduction would require a separate source-defined equivalence or readout with its own recovery and coherence obligations.

The remaining scientific gate is to attach the actual phase/witness operations and test their transported interfaces. A four-chart coordinate decomposition is not by itself the proposed four-subcycle law, and this calculation does not prove the two-cycle ceiling.

## Verification and provenance

- [Frozen attempt contract](contracts/octahedron-esd7-wrap-v1.json).
- [Exact checker](checkers/check_octahedron_esd7_wrap.py).
- [Verification and chart metrics](results/octahedron-esd7-wrap/verification.json).
- [Retained chart fragments](results/octahedron-esd7-wrap/retained-fragments.json).
- [Native-cell restriction records](results/octahedron-esd7-wrap/native-cell-restrictions.json).
- [Initial envelope-only receipt](results/octahedron-esd7-wrap/envelope-phase-verification.json).
- [SCC manifest](scc-models/octahedron-esd7-wrap-v1.json).

Reproduce:

```sh
python research/strominger/checkers/check_octahedron_esd7_wrap.py
python research/aspect/scc/scc.py validate research/strominger/scc-models/octahedron-esd7-wrap-v1.json
python research/aspect/scc/scc.py check octahedron-esd7-wrap-v1
```

The initial 20-check envelope result preceded the common-refinement continuation, which was recorded and frozen separately. The first continuation run exposed a triangle-only assumption in the plane helper; accepting polygonal fragment faces repaired that implementation error. The final 27-check version was frozen as `ea4d17e55859f0c6cee545764063ce4874442b0ad7f26e694792f33e56a0d5ff` and passed a fresh SCC-managed execution. SCC admission is bounded checker health, not physical truth certification.

No viewer, particle constructor, accepted isotope inventory or other owner's research was modified by this wrap investigation.

Graph report: proposal `ep_d2efdd03-5b23-41f0-8e88-5c294197c18a`, notices to `marici.Nima` and `marici.Voevodsky`. Its policy admission does not certify the scientific claims.
