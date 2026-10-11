# The existing reversible memory lift works on the native phase/seam records

## Result

The prior projection-memory construction is now instantiated on the actual belt
coefficient carrier, not on a replacement comparison graph:

- 36 intrinsic complex carrier coordinates in the retained physical metric;
- 18 local phase-rejection directions, reconstructed from the stored oriented
  triangle modes;
- all 21 exact seam-mismatch projectors recovered by the geometric phase bridge;
- one complex amplitude record for each rejected direction: 39 records and 75
  complex coordinates in total.

Every local lift is an exact metric-unitary involution. The entire scheduled
sweep has exact reverse recovery, tested on every basis vector of the full
75-dimensional space, including populated record inputs.

This is a uniform existence witness using the previously admitted construction.
It does not require uniqueness of the physical realization.

## Construction with no hidden metric change

Let G=diag(1/d_i) be the native carrier metric. For each rank-one rejected
projector P, choose a deterministic nonzero column u of P and put

    h = u^* G u > 0,
    a = u^* G q / h,
    Pq = u*a.

Give the scalar record z metric h. The existing memory rule becomes

    q' = (I-P)q + u*z,
    z' = a.

It exchanges the rejected carrier coordinate a with the record coordinate z.
All other carrier and record components are unchanged. Therefore

    U^2 = I,
    U^sharp = U,
    ||q'||_G^2 + h*|z'|^2 = ||q||_G^2 + h*|z|^2.

At a ready record z=0, the carrier undergoes the intended projection I-P, with
the removed amplitude retained rather than erased. No square-root normalization
or Euclidean replacement of the numerator metric is used.

For local phase records, P is the orthogonal complement of the selected native
character line in its two-dimensional intrinsic triangle plane. This implements
phase **selection with memory**, not the nonunitary triangle cycle A itself.
For seams, P is exactly the previously constructed normalized mismatch projector.
All 39 projectors annihilate the coherent return N.

Reframing u as 2u and z as z/2 conjugates the gate and changes the record metric
to 4h. The checker verifies this re-encoding and its invariant budget. It adds
no resource and changes no represented dynamics.

## Concrete forward, reverse and reuse tests

Schedule the 18 local phase gates followed by the 21 seam gates, retaining the
stored triangle and seam order. This is a declared schedule, not a source proof
that this order is unique.

Two exact inputs are tested: the native collective vector w plus a mismatch
from the first local phase projector, and w plus a mismatch from the first seam
projector. All records start ready.

For both inputs:

1. The completed carrier is exactly w.
2. The records have strictly positive squared budget, equal to the lost carrier
   squared budget. Nothing has been erased.
3. Reversing gate order recovers the original carrier and empties all records.
4. Executing another forward sweep with the populated records returns amplitude
   to the carrier. The selected carrier is no longer w.

For the seam input, two forward sweeps are not the identity; noncommuting local
operations make reversal of the order essential. For the isolated phase input,
two forward sweeps happen to undo the swap. The full-space inverse test does not
rely on either special fixture.

A carrier initially at w with every record empty is fixed by the whole sweep.
Complex phase in w alone therefore does not create mismatch memory. Nonzero
memory in these fixtures records a real preparation history.

## Energy: three observables kept distinct

### Conserved carrier-plus-memory budget

The exact metric norm transferred above is the same quadratic budget as in the
prior comparison-memory construction. It remains invariant under every gate and
under record re-encoding. No absolute energy scale is newly assigned to it.

### Existing positive spectral gate energy

Apply the already proved uniform involution constructor:

    Q_gate=(I-U)/2,
    H_gate=pi*Q_gate.

The checker verifies Q_gate is a metric-self-adjoint rank-one projector and
commutes with U. The existing analytic formula

    exp(-it H_gate) = I-Q_gate + exp(-i*pi*t)*Q_gate

implements U at t=1, conserves that gate's energy and preserves the inherited
metric for all t. This is the same uniform rule, not a fitted Hamiltonian.
A switched sequence of these generators is not automatically a single autonomous
storage Hamiltonian; switching/control accounting is not silently omitted.

### Original carrier constraint Hamiltonian

The old native phase/alignment/seam Hamiltonian is retained unchanged, with zero
extension on the records. Every one of the 39 lifted gates fails to commute with
that bare carrier Hamiltonian. In the two displayed fixtures, its quadratic
form decreases from positive to zero while record amplitude remains nonzero.

The measured native constraint-energy decrease is not identified with the
record norm by fiat. They are different forms. Reported numerical energy values
are unnormalized quadratic forms of the supplied exact vectors, in the stored
4H/pi convention, not calibrated particle energies.

Thus we have checked actual reversible transfer into retained memory and supplied
the existing positive gate dynamics. We have not proved conservation of the old
bare-carrier energy without a coupling/control account, nor identified amplitude
memory with the separate binary bond-occupation registers.

## Verification and sources

    python research/voevodsky/checkers/check_native_phase_seam_memory.py

Fresh execution passed after the final checker edits. Receipt:
`results/native_phase_seam_memory.json`.

The checker reads the content-addressed source snapshot recorded by
`results/phase_occupation_necessity.json`, verifies its digest, and verifies that
the intrinsic coefficient file matches the hash in the frozen geometric bridge.
The receipt retains all 39 record directions and their exact metrics, source
hashes, fixture results and checker hash.

Reused prior work:

- `research/nima/comparison-update-dynamics-and-energy-normalization.md`
- `research/nima/uniform-local-core-proof.md`
- `prior-retained-energy-mechanism-recovery.md`
- `geometric-phase-energy-bridge.md`

## Updated frontier

The amplitude-memory bridge is now constructed and tested. Do not reopen it as
an unimplemented abstract mechanism. Reusing the records produces back-action,
not a stationary latch. Connecting this memory to persistent bond occupation or
a joint storage/control energy remains a distinct operation-level task. The
existing conditional occupation theorem remains valid, earlier mass-comparison
failures remain in force, and electron five-cell transport is still open.
