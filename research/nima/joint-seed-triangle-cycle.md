# Joint seed-triangle cycle with explicit retained-record compatibility

## Reuse and objective

Extend the existing `two-triangles-shared-edge-half-phase.md` synchronization result and the six-arrow endpoint lift in `transported-reference-object-prior-research-synthesis.md`. Keep all six directed occurrences independent, in order

    x=(AB,BC,CA,AD,DB,BA).

The local triangle triples are (AB,BC,CA) and (BA,AD,DB). Apply the existing short half-phase S to both. This defines a unique block operation U on six coordinates. It is orthogonal and U^6=I, even for arbitrary input. The extra objective tested here is conservation of ALL three original cycle sums at every intermediate step, not merely recovery at step six.

## Exact joint compatibility

The triangular sums c1=AB+BC+CA and c2=BA+AD+DB are always preserved by U. The shared two-cycle h=AB+BA need not be.

Stacking h U^k-h for k=1,...,6 gives rank two. Its kernel, the maximal linear subspace conserving that record through the whole cycle, has dimension four and is exactly

    x=K(a,b,c,h)=(a,b,c,h-b,h-c,h-a).

Equivalently, paired positions of the two triangles must have the same sum:

    AB+BA=BC+AD=CA+DB=h.

On this subspace the induced update is

    (a,b,c,h) -> (S(a,b,c),h).

All six original values reconstruct from these four coordinates. Both local half-phase laws hold simultaneously, every retained cycle reading is constant, and six steps return the entire coefficient state. The pullback of the six-occurrence Euclidean metric, K^T K, is conserved. This is a counting-metric result, not a physical energy identification.

The cycle records necessarily obey

    c1+c2=3h.

Thus only two independent cycle sums remain on this compatible subspace. This is a restriction on admissible preparations, not a lossless compression of every arbitrary six-arrow input. The checker explicitly rejects a generic incompatible vector rather than silently projecting it. If one allows h to change, the full six-dimensional simultaneous U remains reversible; that is a different retention requirement.

For h=0, the second local triple is minus the first. This recovers the prior oriented-cochain synchronization exactly, with BA=-AB and the paired-occurrence metric. Nonzero h extends that result without imposing BA=-AB globally.

## Ordered alternative on the unrestricted seed

Construct F1 and F2 using the previously specified individual endpoint-increment lift: perform S on the selected triangle, keep its endpoint-total increment zero and its spectator increment zero, and update all seed arrows by exact endpoint differences. Each preserves all three arbitrary cycle sums and satisfies Fi^6=I.

They do not commute. Their serial composite F2 F1 differs from simultaneous U even on the synchronized subspace. Its inverse is F1^5 F2^5. Its exact trace is43/9, proving infinite order: a finite-order rational matrix has algebraic-integer eigenvalues and rational, hence integer, trace.

This trace argument proves no finite operator period, not absence of fixed or periodic individual states. It also does not by itself prove a bounded or positive-metric serial dynamics.

| Requirement | Simultaneous U | Serial F2 F1 |
|---|---|---|
| Both local S laws at the same step | Yes | No; each is applied at its own substep |
| All six arbitrary coefficients retained | Yes | Yes |
| All three cycle readings fixed throughout | Only on the four-dimensional compatible sector | Yes, for arbitrary input |
| Exact finite full-operator return | Six steps | None |
| Explicit inverse | U^5 | F1^5 F2^5 |
| Physical schedule selected | No | No |

## Exact contrast identification and absence of dynamical coupling

The defect update D=[[0,1],[-1,1]] is exactly the old triangle half-phase in a contrast basis. Define

    J=(1/3)*[[-1,-1],[2,-1],[-1,2]],
    Qdiff=[[-1,1,0],[-1,0,1]].

Then Qdiff J=I2, J Qdiff is the triangle contrast projector, and

    S J=J D.

Its pulled-back counting metric is J^T J=(2/3)*[[1,-1/2],[-1/2,1]]. Thus the defect's period and positive invariant form are inherited from the existing contrast plane, not a new oscillator supplied by coupling.

Let l=(AB,BC,CA), t=(BA,AD,DB). The defects are contrast coordinates of z=l+t. The other combination w=l-t also evolves by S. Both z and w are independent triples, with inverse l=(z+w)/2 and t=(z-w)/2. The full representation is therefore

    (common line + contrast plane) direct-sum
    (common line + contrast plane).

It has two fixed directions and two copies of the same contrast action. The earlier4+2 form chooses one original triple, the mean of z, and the contrast of z; it is invertible but asymmetric. The defect coordinates are independent of the four retained coordinates as data, while their operator type repeats an already existing triangle mode. They are not a third independent physical structure.

This makes a limitation explicit: on all six independent occurrences, U applies S separately to the two triples. No cross-response appears in either local evolution equation. Synchronization imposes a static compatibility restriction; it does not dynamically generate alignment or binding. The serial exact-endpoint lifts are a different operation and cannot lend their coupling to this simultaneous U.

The original shared reading is z0, so it sees the common part and contrast of the sum triple but cannot see the difference triple w. This is a concrete observation statement on the finite model. It is not an identification of z0 with the physical rung4 observation, which remains unconstructed for these coefficient spaces.

## Structural result and boundary

The original seam conditions now have a complete six-occurrence formulation. Simultaneous compatible evolution, arbitrary fixed cycle records, and a serial schedule cannot be conflated. The constructor must specify whether compatibility restricts the allowed source preparations or whether updates act in ordered substeps. An admissible retained history is not automatically permission to change a protected cycle reading.

This is a joint coefficient-cycle synthesis, not a two-particle realization. Neither a physical schedule, a native admission derivation nor a rung4 observation law has been derived. The four-dimensional compatible sector is not assigned the rung number four by dimension counting.

## Verification

    python research/nima/checkers/check_joint_seed_triangle_cycle.py

Exact rational checks pass: local operator identities, full-cycle constraint rank, reconstruction, nonzero shared-record parameter, cycle dependence, inherited metric, prior h=0 recovery, incompatible-state control, both endpoint lifts, noncommutation, serial inverse and infinite-order trace certificate. Existing matrix utilities are reused; no amplitudes are fitted.
