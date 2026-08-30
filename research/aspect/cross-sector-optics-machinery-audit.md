# Cross-sector optics machinery audit

Owner: `marici.Aspect`

## Purpose and authority boundary

This packet identifies optical apparatus maps that can serve as exact finite
implementation templates for adjacent Marici sectors. A shared matrix shape
does not transfer source authority, coefficient groups, physical meaning, or
completion theorems. Every bridge below names both the reusable structure and
the prohibited identification.

## Control: frozen plant before inference

Source: `research/sontag/reciprocal-lossy-cavity-control-audit.md`.

The optical cavity exports its ordered plant `(A,B,C,D)`, port metric, and
unitary dilation. Sontag's control audit may then test controllability,
observability, feedback well-posedness, and storage without changing those
ports. At the reflected dark locus, the optical output is zero while the
scalar cavity state is nonzero; because the incident input is known and the
state coefficient is nonzero, this does not imply an observability defect.

Reusable: typed state/output factorization and complete supply identity.
Prohibited: deriving optical ports by fitting a desired controller property,
or promoting sampled scalar observability to the continuum delay history.

## Topological transport: ordered path product and holonomy

Sources:
`research/kitaev/nonabelian-frame-transport-is-classified-by-ordered-holonomy.md`
and `research/kitaev/phase-ports-are-cycle-holonomies.md`.

An ordered Jones network supplies edge transports. Under local polarization
frame changes, a based loop product transforms by conjugation. Tree-edge
phases can be gauged away, while independent cycle holonomies remain. This is
an optical implementation of ordered transport, but the coefficient group is
the physically admitted Jones subgroup; it is not automatically `S3`, a
topological anyon group, or the coefficient group of another sector.

Reusable: ordered multiplication, frame conjugation, and cycle-rank counting.
Prohibited: replacing noncommuting products by unordered phase sums, or
inferring full endpoint state from a central/character readout.

## Flavor: calibrated analyzer rank

Source: `research/flavor/flavor-coordinate-map-observability-gate.md`.

One Jones analyzer row has rank one and a one-dimensional kernel; two
independent calibrated rows have rank two on the declared Jones class. This is
an exact laboratory realization of the flavor gate that a two-coordinate
error map needs a calibrated rank-two probe.

Reusable: rank, kernel, and calibration pre-registration.
Prohibited: treating optical analyzer calibration as authority for flavor
width/background coordinates, or treating untyped rank as physical descent.

## Radiative scattering and memory: carrier versus integrated readout

Source: `research/strominger/soft-bms-memory-source-boundary.md`.

The radiative packet keeps the carrier field, soft mode, charge, and memory
readouts distinct, with memory an integrated/DC boundary observable. Optical
temporal-mode machinery gives the same warning: integration can retain an
endpoint or zero-frequency record while losing waveform distinctions. Two
different optical time profiles can have the same integrated detector value.

Reusable: typed carrier, zero-frequency prescription, boundary orientation,
and kernel quotient before inversion.
Prohibited: identifying optical field amplitudes with Bondi news, importing
BMS boundary conditions, or reconstructing a full waveform from memory alone.

## Distinction-preserving completion

Source: `research/strominger/distinction-preserving-completion.md`.

For an optical compression `Q` and required later readout `R`, descent through
the compressed record requires `ker(Q)` to lie inside `ker(R)`, plus continuity
and uniform bounds at completion. The exact hostile `Q=(1,0)`, `R=I` loses the
second field coordinate, so no reconstruction of the full Jones packet can
descend through `Q`.

Reusable: kernel inclusion and uniform completion bounds.
Prohibited: calling finite rank at each cutoff a uniform completion theorem.

## Theta/scattering: phase is not amplitude

Sources:
`research/grothendieck/critical-line-scattering-phase-collapse.md` and
`research/nima/theta-scalar-zero-is-a-transmission-zero-not-an-observability-defect.md`.

Optical phase-only readout identifies nonzero amplitudes with the same phase
and is undefined at zero amplitude. Complete multiport tomography can retain
amplitude and route distinctions, yet a selected scalar detector channel can
still have a transmission zero. Hence neither phase unitarity nor tomography
is a zero-exclusion law.

Reusable: the separation of operator/multiport scattering, phase quotient,
selected scalar amplitude, and Rosenbrock zero.
Prohibited: importing an optical phase or dark-port classification as an RH
argument, or defining exceptional operator domains from the target zero set.

## Exact audit fixtures

The companion checker verifies:

1. the cavity dark locus with nonzero state and nonzero observation
   coefficient;
2. noncommuting ordered transports;
3. rank-one versus rank-two analyzer families;
4. distinct temporal profiles with equal integrated memory readout;
5. failure of full-state descent through a scalar projection;
6. phase-readout nonfaithfulness and its zero-amplitude domain boundary;
7. the selected-channel zero with faithful complementary output.

## Verdict and remaining boundary

Optics now supplies reusable laboratory machinery for factorization,
holonomy, calibrated observability, memory compression, distinction-preserving
completion, and transmission-zero taxonomy. None of these bridges identifies
the underlying sector carriers. Further cross-sector use requires each owner
to provide source-derived ports, coefficient groups, metrics, and completion
maps.

Run `python research/aspect/checkers/cross_sector_optics_machinery_audit.py`.
The result is
`research/aspect/results/cross_sector_optics_machinery_audit.json`.
