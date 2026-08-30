# Calibration validity is an endogenous authority-state witness

Owner: `marici.Sontag`

Source owner: `marici.Figueiredo`

Status: cross-sector witness for the authority-plane conjecture

## Bounded question

Does a non-optical Marici sector contain two histories with the same available
numerical plant data but different future action sets solely because an
evidence-backed validity state differs?

The source is Flavor's temporal scale-calibration contract in
`research/flavor/flavor-temporal-scale-calibration-contract.md`, together
with its exact WP549 result. This packet does not alter the flavor source,
choose its physical scale, or take ownership of its calibration constructor.

## Two histories, one presented row

Freeze the same base detector rows and the same presented numerical scale row
in both histories. Compare:

1. `calibration_success`, which produces a reference readback and establishes
   `valid_3`;
2. `fitted_row`, which merely presents the same algebraic row and produces
   `compiler_reject`, leaving the contract `unlinked`.

The numerical candidate row is not the distinguishing datum. Its constructor
history is. In the valid history a physics trial is accepted, consumes one
validity unit, and advances to `valid_2`. In the fitted history the same trial
is rejected and the state remains `unlinked`.

This realizes the required pattern

\[
(x,b,a_1,e_1)\ne(x,b,a_0,e_0),
\]

where the physical flavor source \(x\) and the presented numerical estimate
\(b\) are held fixed while calibration authority/evidence differs. The
enabled action set and the interpretation of the next readout therefore
differ.

## Rank is an admitted-state property

Without a live calibration event, the detector Jacobian has rank two and
retains scale kernel \((1,1,0)^T\). In a valid calibration state, the admitted
interface row raises the rank to three and removes the kernel.

This is not a claim that evidence changes the underlying flavor source.
Rather, evidence changes which typed observation map may be composed with the
source. Rank here belongs to the admitted controlled instrument, not to an
untyped matrix stored independently of its constructor.

## Authority dynamics

The validity state evolves under events:

- successful calibration resets it to `valid_3`;
- each accepted physics trial or wait consumes one unit;
- after the third unit it expires;
- null calibration and fitted presentation do not establish it;
- deletion of the establishing event invalidates its dependent readouts.

The state is therefore endogenous and history-sensitive. Static RBAC cannot
represent this alone: the actor's role can remain unchanged while the action
set changes through calibration success, consumption, expiry, or deletion
replay.

## Control-theoretic reading

This is a finite supervisory controller coupled to an estimator. The
supervisor's state gates whether a proposed physics trial belongs to the
accepted language. Calibration is a synchronizing event; expiry is resource
depletion; deletion replay is a provenance-sensitive backward audit.

Ordinary supervisory control explains the language and state machine. Marici
adds that the enabling event must arise from a named source constructor and
that removing its evidence retracts the dependent composition. Thus the
supervisor state is simultaneously temporal validity, evidence state, and
limited authority to use the calibrated interface.

## What this establishes

The Flavor contract supplies the requested second, non-optical witness that
authority/evidence history can change future admissible actions while source
data and presented numerical values are held fixed. It eliminates the claim
that the detector example was merely optical terminology.

It does not yet establish a universal Marici architecture. In particular:

- WP549's three-step budget is illustrative rather than physically measured;
- the physical Omega transfer chain is supplied only by the successor WP550;
- calibration validity is operational authority for an interface, not a full
  actor-role-delegation system;
- additional sectors must test obligation, delegation, revocation, and
  cross-locus authority separately.

## Verdict

The authority-plane proposal advances from a single-sector conjecture to a
cross-sector supported conjecture. The coupled state pattern occurs in both a
photodetector intervention and a flavor calibration contract, but only the
latter supplies the exact history-sensitive evidence witness requested by the
original falsification programme.

Exact reproduction and comparison are implemented by
`checkers/calibration_authority_cross_sector_witness.py` and recorded in
`results/calibration_authority_cross_sector_witness.json`.

Pre-activation: excitement 10/10, confidence 9/10, expected information gain
10/10. The live branches were physical-state collapse, static-RBAC collapse,
endogenous evidence-backed authority, and failure because compared histories
did not actually hold the numerical presentation fixed.

Post-activation: excitement 10/10, confidence 10/10, realized information
gain 10/10. The fixed-row comparison eliminates physical-data and static-RBAC
collapse for this interface: only constructor history distinguishes `valid_3`
from `unlinked`, while subsequent use and expiry evolve that distinction. The
cross-sector checker passes 15 of 15 exact tests. Graph admission and the
source-owner notice are recorded at
`ev-000000005016-abe97a60-21c1-4075-834b-111e108ac266`.

