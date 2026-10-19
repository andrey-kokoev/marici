# Prior identity persistence: barycentric, spectral and retained presentations

Operator clarification: the identity-bearing barycenter advances stepwise as a
vector from the previous barycenter. Search performed across research and the
ledger, then the following original source notes were read. Reported older
verification counts below are historical receipts, NOT fresh reruns in this turn.

## Direct prior constructions to reuse

1. `research/nima/barycenter-assembly-walk.md`.
   For all24 orders of a regular tetrahedron's four vertices, the complete indexed
   prefix-barycenter walk is faithful, although all final centers coincide.
   It proves exact recovery

       x_(n+1)=(n+1)c_(n+1)-n c_n,
       c_(n+1)=c_n+(x_(n+1)-c_n)/(n+1).

   Thus the next center is the previous one plus a specified displacement.
   The regular-source displacements have squared lengths2,2/3,1/3 and are
   orthogonal; a nonregular control rejects incidence-only orthogonality.
   Source checker: `research/nima/checkers/check_barycenter_assembly_walk.py`.
   This is a prefix-assembly law, not a general physical motion law.

2. `research/nima/retained-tetrahedral-package.md` and
   `research/nima/tetrahedral-hierarchy-at-vertex.md`.
   Actual Agda packages retain four marked values, six edge witnesses, four
   triangle witnesses and a tetrahedral coherence. The marked view

       View(mark)=(x, full_package, vertex(full_package,mark)=x)

   has checked round trips. This is an ALREADY CONSTRUCTED way for a single
   visible vertex to carry the full hierarchy. A bare vertex-value projection
   does not. The source note explicitly separates this retained view from a
   subsequent dynamics that consumes it.

3. `research/nima/barycentric-witness-packet.md`.
   Barycentric subdivision turns each of15 nonempty faces into a marked vertex
   retaining its occurrence, type and witness, with Agda recovery proofs.
   Coincident types/values cannot recover erased occurrence marks. Geometry
   presents an already retained typed packet rather than generating its identity.

4. `research/nima/nested-four-part-coherence.md`.
   The barycenter plus three retained mismatch components recovers all four
   inputs. All36 order-frame maps and216 compositions are checked, including
   braid coherence. This is another existing identity-retaining presentation;
   an independent append-only raw log is not its sole possible realization.

5. `research/voevodsky/retained-potential-realization.md`.
   The resolved tetrahedron keeps direction v at its visible center. The radial
   blowdown beta(t,v)=(1-t)b+t v is explicitly forgetful at t=0. A checked inward
   realization retains the direction sphere and original fold owners at the
   final mark. The historical eight-process closure records163 checks.
   Therefore the center's retained fiber is not a new missing mechanism.

6. `research/strominger/demos/particle-overlap-tetrahedron/README.md` and
   its actual `model.mjs`, already read for the latest prototype.
   In pentachoron mode the fifth source vertex C2=(0,0,0,sqrt(5)) projects at
   zero4D rotation to the C0/M0/C1/M1 facet's barycenter. It remains a DISTINCT
   original4D vertex; its source data must survive projection. This is the
   specific geometric presentation closest to the operator's example.
   A projected barycenter and the full fifth vertex are not the same information
   type. The alternate barycenter display mode is separately declared.

7. Ledger4322, `src/ledger/20261014-4322 Configuration Coherence and the Candidate Constant 1836.md`.
   The mark at the barycenter is both a realized term and access to the retained
   coherence package. Its capabilities and admitted continuations determine
   what must persist. It does not require arbitrary raw history when no admitted
   continuation consumes it. This distinguishes identity persistence from mere
   current-coordinate equality or one mandatory storage implementation.

## Correct reading of the vector update

When the new barycenter supplies a LOCAL displacement delta_k,

    p_(k+1)=p_k+F_k delta_k,

where F_k transports its frame into the previous/global frame. If all steps
already use one frame, F_k=I. Adding two absolute affine positions without an
origin convention is not the same operation. The prefix-average formula above
is one already verified source law determining delta_k, not the only possible
center propagation law.

The mark carries the retained typed realization through the step. A barycenter
coordinate alone is not expected to reproduce all witnesses. Existing packet,
marked-view, mismatch-coordinate and direction-fiber constructions provide
several realizations of the required persistence.

## Correction to the latest CMC/MCM chain

The new glide candidate has tetrahedron barycenters p_i=(-2i,0,0), so its center
already advances by(-2,0,0); its local z frame alternates and must be retained.
But this was only a new geometric chain, not an attachment to the existing
identity constructor. Calling its explicit archive the newly missing identity
mechanism was too strong: it is one test implementation of a restricted raw-value
recovery task, not a replacement for the prior retained-package theory.

There is also a concrete naming/attachment issue: the new glide chain's C2 is a
new outer point(-3,1,1). The ORIGINAL pentachoron view's C2 is the fifth4D vertex
projecting to the facet center. They are NOT the same source occurrence just
because the labels match. The original walk is

    C0->M0->C1->M1->C1->C2,

not the naive indefinitely alternating glide walk. Its repeated C1 occurrence
and electron MCC window must remain. No existing receipt licenses erasing that
difference or identifying the two C2 constructions.

## Next proper attachment

Reuse the existing full retained identity package at the moving barycentric mark.
Construct explicit source maps comparing its stepwise displacement and
pentachoron-vertex presentation with the local CMC/MCM face flags. Retain frame,
occurrence and witness transport and check the original walk/readers, including
the repeated C1 and fifth source vertex. Do not reopen solved persistence as
though no mechanism existed, and do not silently substitute the glide candidate
for the earlier source model. Prior geometric tests remain valid at their
stated scope; native physical C/M and particle identification are still separate.

## Eigenline development: recovered direct research thread

The operator additionally requested the eigenline view. These current original
notes were read, including their later corrections/continuations, not merely
searched by title. No fresh rerun of their old calculations is asserted here.

### A. Triangle -> spectral identity -> reusable promoted record

`research/nima/triangle-half-phase-primitive.md` derives the cyclic successor C
from three actual composable packet occurrences. With an explicit counting
metric, its modes are1,omega,conjugate(omega); the common projector Q and contrast
projector P give a complex structure J and rank-one identities

    E_plus=(P-iJ)/2, E_minus=(P+iJ)/2.

These are identity ON their eigenlines. They are not extra seed vertices,
arbitrary half-amplitudes or automatically selected physical states. The short
half-phase root and its three/six-step returns are also already constructed.

`research/nima/record4-spectral-promotion.md` goes further: an actual retained
nested return supplies the cyclic operator, and its selected mode is promoted to

    (fresh label, rank-one projector, eigenvalue, source/history window, depth).

The window recovers the entry arrow, nested continuation, all three primitive
occurrences and both fold presentations. E is independent of the eigenvector's
nonzero phase/scale choice, while different histories with identical E retain
different labels/windows. Collapsing the internal cycle to C^3=I destroys the
simple-spectrum selection and is explicitly rejected.

`research/nima/spectral-promotion-nine-cycles.md` checks nine re-entry/promotions
for EACH of the three modes:27 fresh records, fixed rank-one mode projectors,
unchanged original occurrence recovery and fixed ancestry depth. The eigenphase
and half-phase powers evolve while the projector remains unchanged. These are
repeated executions, not an expanding family of triangle operands or recursive
arity-squaring closure. This is the most direct prior identity-development
construction and should be REUSED, not rediscovered as a bare loop invariant.

### B. Body -> source-selected eigenlines -> reconstructed body

`research/nima/machian-thing-eigenline-cycle.md` derives a four-state body from
seed cycles. Group averaging gives E=J4/4 and H=I-E. Its points q_p=H e_p yield
local projectors P_p=(4/3)q_p q_p^T. The rest-of-body source

    K_p=sum_(q!=p) w_q P_q

selects its lowest contrast eigenline, and q'_p=P'_p e_p reconstructs the new
body. The symmetric point is exact; changing one source changes other local
lines and yields an explicit positive simplex. The common identity line remains
span(1,1,1,1) in the retained label coordinates after recentering.

The sequel `research/nima/machian-cycle-completed-calculation.md` MUST accompany
this positive result: full replacement has two unstable shape multipliers-5/3;
normalized lines erase radial scale. A separately specified continuous alignment
rule works in the tested family, not as a derived universal law. This is a
valuable prior geometric response constructor, not established physical dynamics.

### C. Shared triangles and two tetrahedral bodies already have a coupled identity

`research/nima/two-triangles-shared-edge-half-phase.md` constructs the shared
fixed line a(1,1,1,-1,-1) for the actual six-occurrence seed pair. Generic local
updates conflict at the seam; synchronized and serial protocols are separately
checked. Occurrence metrics matter, and the choice of protocol is not automatic.
`research/nima/shared-seed-pair-prior-construction-map.md` already explicitly
warned to reuse this source pair instead of inventing arbitrary sections.

`research/nima/twenty-four-triangle-shared-seed.md` constructs T and-T from the
same seed via a declared exterior-square action, with shared octahedral core,
positive assembly and transported cyclic eigenlines. Each branch has its common
identity line; the cross-exchange comparison graph has rank23 on24 positions,
leaving ONE shared identity. Removing exchange leaves TWO independent identities.
This is a much richer existing paired-tetrahedron construction than an unmarked
picture of two shapes. It is not a native P/N assignment or a force derivation.

### D. Phase and moving-frame development were also retained

`research/nima/retained-rotor-phase-transport.md` (current corrected version)
and `retained-rotor-history-clock.md` explicitly distinguish projective identity,
fiber phase and unwrapped history. Rotor and reversing-frame composition,
central signs and winding transport are retained. The angular reading transforms
as T->o(g)T+theta; it is not an ordinary additive scalar when reversers occur.
The module/metric/continuous-lift and physical calibration assumptions remain
explicit. Older superseded text in quarantine must not replace these versions.

## Correct synthesis for the current CMC/MCM proposal

Keep distinct but connected:

* spatial/barycentric anchor and its stepwise displacement;
* spectral line/projector and its transported phase/eigenvalue;
* full source-generated packet, marked occurrences and continuation witnesses.

A useful schematic for the retained identity is

    I_k=(mark_k, E_k, lambda_k, source/window_k, frame/transport_k).

This is a synthesis of existing interfaces, not a claim one prior theorem already
identifies all of them. Under an admitted unitary transport U, E transforms as
U E U^dagger; for a non-isometric change, the retained metric must also be
transported. A scalar barycenter or rank-one projector alone is not expected to
encode every field. Neither does identity preservation universally require an
external append-only duplicate of all history: the admitted continuation task
and the existing retained package decide what information must survive.

The new work is an explicit attachment of THESE existing constructors to the
CMC/MCM marked-window geometry and its original fifth-vertex/return walk. Do
not report spectral persistence, phase-aware re-entry, or geometric body-from-line
reconstruction as wholly missing. Keep the still-open source/native C/M and
physical identification bridges separate from those already constructed results.
