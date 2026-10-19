# Sector reconstruction and anchored PN contact comparisons

## Frozen interface comparison

Reuse Nima's actual `anchored_contact_comparisons.prepare/recover` API, its
marked-contact descriptor and archived route packets. First freshly execute
`research/nima/checkers/check_anchored_pn_contact.py` without changing its source.
The owner checker regenerates its own deterministic outputs. Pin its receipt,
source hashes and gzip packet digest before the owner-local comparison.

Construct an adapter between source P spatial/N internal coordinates and the
packet's declared ports, using the actual retained P patch rotation matrices
and all18 two-component N ports. Then extract full continuous joint-sector
vectors from the native P/N projector matrices. The inverse is vector addition;
reject packets outside the specified sector ranges, rather than accepting any
four arbitrary vectors whose sum happens to match.

The first square compares direct packet preparation with preparation after
sector extraction and reconstruction. The second compares extraction before
preparation with extraction after packet recovery. Compare full fields and
all900 blocks, descriptor and anchor, not only a scalar or return value.
These squares describe alternative coordinate presentations of the same data;
they do not fill the failed PN geometric square.

## Fixtures and falsifiers

Use the owner's dense and rotated-dense packets, both full route packets for
each of two native contrast inputs, a zero case and common/relative phase
controls. Recover both route fields, rederive the exact weighted residual Gram
3I2, and verify native return erases that residual. Verify that sector weights
also fail to distinguish these route outputs while full sector vectors and
anchored packets do distinguish them.

Reject wrong-sector vector placement, replacing full vectors with scalar
weights, deleting the phase anchor on nonzero data and deleting a rectangular
cross block. A changed owner source, digest mismatch, failed source inverse or
comparison disagreement is a test failure, not a reason to weaken the task.

The comparison is exact on the tested fixtures. Its all-input reconstruction
argument uses the existing exact operator identity sum E_i=I and the source
prepare/recover anchor formula: reconstruction is linear, while preparation is
quadratic and phase-sensitive through its retained anchor. Do not call packet
preparation a linear map or claim a general nonlinear equality from fixtures
alone. Sector-range constraints give the other direct-sum inverse law.

## Scope

The output is an attachment-data comparison, not geometric sewing, a physical
face restriction, native motion permission, phase calibration, T9/state-root
preparation or a new Monster structure. The owner's contact label is retained
metadata; it does not identify the P and N fibers. The two native route outputs
remain different after recovery.

Replay after the owner checker:

    python research/strominger/checkers/check_anchored_sector_interface.py

Receipt: `results/anchored-sector-interface/verification.json`.
