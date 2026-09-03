# Sewn `q_G12` conductor and lift audit

## Question

Does the sewn shared-wall cocycle admit the canonical normalized class needed for comparison with a lower-graph factorization object?

## Claim boundary

Three exact layers are available.

First, the sewn shared-wall boundary is a Čech cocycle. For each pair among `q_g1`, `q_g2`, and `q_g3`, opposite oriented Jacobians cancel; the pairwise Čech differential is zero. The mixed `q_g23`/`q_g31` double-residue numerator also vanishes. Execution `structured_command_execution:e_4616_1788296267714259400_64` verifies these statements at three exact rational kinematic points.

Second, the shared-wall Cayley–Menger restrictions are exact squares with squarefree reduced factors on the tested nonsoft fibers. The physical numerator and remaining marked denominator are coprime to those reduced factors. This localizes the sewn residues away from signed-energy conductor letters but does not perform their relative-cohomology reduction.

Third, the source normalization has a simple zero in the analytic grade and cancels a generic simple conductor pole. The normalized grade-zero term is the conductor residue; the finite remainder enters the next grade. This statement concerns the conductor analytic family, while common marked-wall endpoint poles still require source sewing.

## Obstruction

Čech closure guarantees existence of a lift of the physical wall cocycle into the rank-15 three-wall relative space. It does not select one. The exact sequence has ranks

\[
0\longrightarrow M_9\longrightarrow M_{15}\longrightarrow Q_6\longrightarrow0.
\]

Lifts of a fixed physical cocycle form a rank-nine torsor. Imposing zero elliptic quotient removes the rank-two elliptic sector but leaves a rank-seven `T7` torsor. Execution `structured_command_execution:e_4616_1788296321188733800_65` verifies that a lift exists while no canonical lift or `T7` coordinates are selected.

Therefore conductor-pole cancellation and Čech closure do not construct a canonical normalized factorization class.

## First missing arrow

The first missing object is a source-derived section

\[
s_{\rm phys}:Q_6^{\rm phys}\longrightarrow M_{15}
\]

of the wall quotient, or an equivalent physical covector that selects one point of the `T7` lift torsor. It must be compatible with source sewing, cyclic orientation, the analytic normalization, endpoint trivialization, and the lower-graph convention.

A dimension count, zero elliptic image, or generic numerator nonvanishing cannot select this section.

## Strongest falsification attempt

Set the elliptic quotient to zero and demand that this uniquely fixes the physical class. The surviving lift space still has rank seven, so uniqueness fails by an exact rank computation. Any selected `T7` coordinates without an additional source covector are presentation choices.

## Acceptance test

1. declare the physical source covector or splitting rule;
2. compute its `T7` coordinates in the frozen basis;
3. verify invariance under source sewing and cyclic relabelling;
4. check conductor-pole cancellation and endpoint compatibility;
5. map the selected class to an independently normalized lower-graph object;
6. perturb by a nonzero `T7` vector as a deliberate failure of source invariance.

## Disposition

The sewn boundary is closed and its analytic conductor pole is cancellable. Physical factorization is now localized to a canonical-lift problem: the source must select one class from a rank-seven torsor before comparison with a lower graph or Carrier wall is meaningful.

## Evidence

- `research/benincasa/physical_g12_shared_wall_cech_cocycle.py`
- `research/benincasa/physical_shared_wall_reduced_factors.py`
- `research/benincasa/results/rank26-source-normalization-cancels-conductor-pole.json`
- `research/benincasa/physical_shared_wall_no_canonical_t7_lift.py`
