# Conditional joint seam reconstruction with recoverable old state

## Result

**97 exact checks pass.** Using an explicitly declared spatial edge-component
comparison, the surviving three-mode carrier and a candidate missing seam mode
have a nonzero joint compatible line. Its projector changes the old compression,
but the old compatible state is recovered isometrically.

The calculation also exposes unresolved source data: both possible parent faces
for the missing mode give the same edge reading, while their raw mode lines
differ. Thus successful joint reconstruction does not uniquely select a full
source completion.

This is a conditional interface test, not a claim that the unchanged source
constructor already generated the missing mode or selected this coupling.

## Input and declared interface

Rebuild the original constructor after each of BC, CA, AD, DB is deleted. The
surviving cycle supplies three centroid-edge modes with equal squared norm 20/3
and the usual common-amplitude compatible line.

For primitive AB or BA lacking a generated coefficient port, construct two
candidate vectors by the existing cyclic-mode formula, using each possible
third vertex C or D:

    v_ab,c = centroid(a,b,c) + omega a + conjugate(omega) b.

These vectors reuse the source geometry and mode recipe, but constructing them
without a complete directed parent triangle is an explicit completion trial.
No absent primitive arrow or reverse source cycle is declared to exist.

Choose one fixed spatial reader d=B-A and impose equality of d^T times the two
incident coefficient vectors. This uses the supplied Euclidean coordinate
pairing; choosing edge-component equality as the interface is new, declared
input. Reversing d changes both sides' signs and leaves the equality unchanged.

For all candidates, d^T v is nonzero and opposite on the two directed seam
orientations. Both parent-face choices have identical values of this reading.

## Joint regeneration and recovery

Write a_0,a_1,a_2 for amplitudes on the surviving cycle and b for the candidate
seam mode. The old compatibility equations and new seam equation give

    a_0=a_1=a_2,       b=-a_0.

The joint kernel is spanned by v=(1,1,1,-1). Because all local mode norms agree,
the induced amplitude metric is a common scalar multiple of the identity. The
joint orthogonal return is therefore

    N_joint = v v*/4.

Its old three-by-three compression is J_3/4, whereas the old return was J_3/3.
Thus the new compression is **3/4 of the old projector**, as expected from the
append-only obstruction: joint feedback changes the old block.

Let u=(1,1,1)/sqrt(3), z=v/2 and W=z u*. Then

    W*W=N_old,       WW*=N_joint,       N_joint W=W N_old.

These are exact compatible-subspace recovery identities. On the joint line,
restricting to the original three coordinates and multiplying by 2/sqrt(3)
recovers the old normalized state. This is not recovery of arbitrary old raw
states from a one-dimensional quotient. Orthogonal complements must remain
separate retained records; their evolution is not specified by this test.

## What the edge reader does not determine

For each deleted source, the two orphan candidate modes have different raw
rank-one projectors. Their vector difference is annihilated by d^T. Therefore
the edge observable and the resulting amplitude compatibility equation cannot
choose between the raw completions.

One candidate can use the old missing port's parent face; the other can use the
surviving face with reversed local orientation. Neither is selected simply by
its successful edge readout. Reversal of a cyclic generator is an existing
mathematical operation, but source authority to perform it is additional data.

This is a concrete separation between an observer-sufficient interface and a
fully specified carrier completion. It is not grounds to erase the difference
or call the two raw realizations physically identical.

## Next actual obligation

The tested interface is a consistent candidate for joint regeneration, with
explicit recovery and visible normalization change. To select it as more than
a candidate, a source rule must justify the edge-component comparison and decide
what happens to the edge-invisible component or parent-face marking.

No exchange feature kernel, physical preparation, proton/electron interaction,
mediator update or energy normalization follows from this joint line alone.
Those remain distinct operation bindings rather than consequences of a nonzero
compatibility kernel.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_joint_seam_edge_reconstruction.py

Receipt: `results/joint-seam-edge-reconstruction.json`.
All four deletion cases and both candidate parent faces are checked. Original
constructor and source files remain unchanged; no owner receipt is overwritten.
