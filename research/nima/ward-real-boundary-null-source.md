# Topic 9, iteration 4: does the real boundary supply a source state?

## Question and conjecture

The previous test (`ward-chart-real-cut-obstruction.md`) excludes a direct real
Lorentzian realization of the generic native momentum Gram block. Its real
boundary admits a positive photon projector with a new reference. Does that
boundary actually provide a nonzero source tensor to normalize?

**Frozen conjecture:** every full-handle sector of the original unlocalized
four-open marked-theta tree tensor vanishes on the real collinear physical
boundary. Supplying a positive projector cannot rescue a zero source tensor.
SCC obligation: forward realization and noncollapse, upstream of state/readout.
Contract: `contracts/ward-real-boundary.v1.json`.

Rivals are restoration by projector alone; cancellation or loss of marks hiding
nonzero sectors; a probe returning zero on all inputs; and promotion of this
boundary result into a claim about all complex or reconstructed amplitudes.
The risky test is all 12 labelled trees and all 243 full-handle sector words,
using the original Rust evaluator, with a nonzero generic-source control.

## Source and target types

The source is `check_two_open_pair_ward_naturality.rs`. Only its polynomial tree
stage with Metric/Open edge actions is evaluated. No source/reference inverse
is evaluated at a=0. The native longitudinal closure and the full Ward audit
are not executed by this test.

The target has real Lorentzian momenta, nonzero p_i,k_i and external
q_i=p_i-k_i, and physical transverse external/test polarizations, which may be
complex. At a=0 the four-momentum Gram block is zero. A totally isotropic real
subspace of signature (1,3) has dimension at most one: choose a nonzero null
n and write any null vector orthogonal to n in a frame n=(1,0,0,1); its first
and last components agree, and nullness forces both transverse real components
to vanish. Thus every source momentum is a real multiple of n. Nonzero
external and open-leg momenta force all seven polarization/test vectors into
n-perp. Zero-momentum ports are outside this preparation candidate.

Every cubic sector contributes one momentum-difference handle per vertex,
hence five handles proportional to n. The native index-strand evaluator pairs
terminal vectors bilinearly, with D factors for terminal-free loops. Any strand
ending on a handle has zero pairing: its other terminal is another handle or a
transverse polarization/test vector. Therefore each sector is zero separately,
not merely after sector augmentation or a scalar projection. Polarization
pairings remain unspecialized; the proof holds on a rank-free envelope of the
physical boundary and hence on its actual four-dimensional realizations.

The physical input class is nonempty without zero momenta or pure-gauge
polarizations. For example, use p0=n, p1=2n, k0=4n, k1=7n, and the source-defined
p2=-3n, k2=-11n. Then q_i are -3n,-5n,8n, all nonzero. Take external helicity
vectors (0,1,i,0), (0,1,-i,0), (0,1,i,0) and transverse x/y test vectors.
Their Gram matrix lies in the tested ideal. All fifteen possible full handles
are nonzero multiples of n; vanishing is in their contractions, not in deleting
vertices or setting the input momenta to zero.

## Claim boundary

This is a polynomial marked-theta Yang-Mills tensor, not the external QED
scattering amplitude. Its vanishing is not a prediction of zero laboratory
photon rate. It does not decide a regulated wave-packet limit, division by a
vanishing source factor, or reconstruction from complex generalized cuts.
Those require a source-defined comparison and limit prescription; none is
manufactured by normalizing zero or changing the reference. No positive
sample or graph admission establishes physical preparation or theory selection.

## Tested disposition

The conjecture survives the original native evaluator: all 2,916 raw sector
contributions vanish, separately, and every one of the twelve tree sums is
zero. This rejects restoration by positive projector alone. The unnormalized
Born construction would be zero; dividing by its zero trace is refused.

Both nonvacuity comparisons are nonzero on all twelve trees. At tree mask 23,
the generic control is -448975104 and the a=0-only formal control is 738011712.
The latter does not impose the cross-transversality forced by real Lorentzian
collinearity. Thus setting a=0 alone is NOT the physical-boundary restriction.
These signed values are algebraic tensor contractions, not probabilities.
The supplied nonzero normalization control (1,0,0,1) remains valid; it is not
constructed by the native boundary source.

The dependency-free Cargo harness under `checkers/ward-real-boundary-native/`
includes the unchanged native executable definitions; only inner documentation
comments are converted for Rust inclusion. The original main is left unused.
The verifier binds the native receipt to compiled-input FNV1a64 snapshots and
SHA256 live-input hashes. These are provenance checks, not compiler proofs.

Verification:

- Manifest validation: `e_38524_1791418629350250500_144`.
- Freeze: `scc-freezes/nima-ward-real-boundary.af9255f91e4841bc.json`.
- Fresh Cargo execution: `e_38524_1791418659619216500_147`, exit 0
  (2.42 seconds); output `mcp_output:o_38524_1791418659619825100_148`.
- Frozen challenge: `e_38524_1791418682791903800_149`, survives.
- SCC receipt-verification check: `e_38524_1791418813313048900_150`, pass.
- Isolated failure controls: `e_38524_1791418924345492200_151`. Compiled-input
  mismatch, sector deletion, stale native execution and fabricated zero
  normalization are rejected; preparation failure removes all old receipts.
  Live source and receipts are unchanged by these controls.
- Native and verified receipts: `results/ward-real-boundary-native.json` and
  `results/ward-real-boundary.json`.
- Final live-input/native-receipt SHA256 check:
  `e_38524_1791419156980400000_152`.

Early notice `ep_f723b871-cb2e-4fdf-8abb-78eb0b69895b` and tested report
`ep_d14deae5-e786-4a5f-acd1-5e4251038e38` were admitted as communications,
not scientific certification. Both remain uncommitted. No computation is left
running; generated Cargo build products are under the owner-named `.ai/tmp`
target, while source, contracts, manifests, freezes and receipts remain in the
owner-local paths above.

The initial validate call used a model id where that command requires a file
path; the corrected call above passes. No scientific residual was inferred
from that invocation defect.

Reproduction, each command through structured-command:

```text
python research/nima/checkers/check_ward_real_boundary.py --prepare
cargo run --offline --manifest-path research/nima/checkers/ward-real-boundary-native/Cargo.toml --target-dir .ai/tmp/nima-ward-real-boundary-target
python research/nima/checkers/check_ward_real_boundary.py
python research/nima/checkers/check_ward_real_boundary_failure_lifecycle.py
```

## Continuation boundary

The direct generic chart and its real polynomial boundary now both fail the
proposed preparation route, for different reasons. The required reconstruction/
physical-pairing comparison remains the one identified in iteration 3; the
independent preparation/record acceptance test is already frozen in
`bell-preparation-herald-record-interface.md`. Neither should be replaced by a
chosen normalization of a vanishing germ or another conditional Bell table.

Fresh rereads retain two positive mathematical constructions:
`physical-cut-coaction-is-continuous-on-the-projective-laurent-completion.md`
extends a marked Laurent translation/coaction, while
`native-amplitude-resolution.md` evaluates finite expressions with supplied
weights and algebra. Neither provides the missing physical comparison or
measured detector interface.

The freshly listed thirteen admitted site surfaces contain no optical-apparatus
binding. The reread Aspect adapter is simulation-only and refuses dispatch;
`research/aspect/apparatus-data-inventory-audit.md` remains a bounded report of
schema/synthetic material, not a supplied calibration/trial bundle. Closing
communications supplied no relevant replacement material or directed obligation.
This is a claim about the inspected admitted inputs, not a repository-wide
absence theorem.

With this boundary rival disposed, the present physical-selection objective has
no further nonredundant executable continuation from those inputs. Defer it;
reopen on a source-defined physical comparison or independent apparatus-bound
preparation/record material satisfying the existing gates. Topic 9 itself is
not declared complete. No new waiting issue, public ledger publication, hardware
dispatch, cross-owner edit, commit or push is made.
