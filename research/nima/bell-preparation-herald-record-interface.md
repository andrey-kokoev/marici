# Topic 9, iteration 1: both preparation branches and a calibrated record interface

## Frozen question

Can the actual twist/X-instrument preparation be connected to a full,
herald-normalized record law using an independent calibration rather than a
Bell-fitted visibility? Preserve both preparation branches and all no-clicks.
SCC obligation: forward realization of the preparation instrument, then record
transport/readout descent. Fixed premises and predicted hostiles are in
`contracts/bell-preparation-herald-record.v1.json`.

**Conjecture:** an identity-filler bypass calibrates the herald record channel;
with that same channel, local frame decoding predicts the twist-route records
without discarding the minus branch. Forgetting the herald does not preserve
that readout. This is a comparison of operational implementations inside the
supplied quantum model, not a discriminator between Marici and quantum mechanics.

**Rivals:** the herald can be forgotten; a coherent phase gate or rejection of
the minus branch is necessary; balanced herald frequencies fix its meaning; or
calibration can be transferred without a common record-channel contract.

**Closure:** construct the full comparison, reject those specified rivals where
appropriate, and identify the first physical input needed to test it. No new
probability law, apparatus fiction or repeated Bell-value scan counts as closure.

## Strongest predecessors and source preservation

Use the five original Bool filler FUNCTIONS on their ordered four labels,
not a two-amplitude replacement. Their given C4 permutation realization makes
the actual twist CNOT. Retain the complete existing Aspect joint/sequential
instrument and Nima analyzer convention. Earlier record-descent independence,
no-click gates and coherent-refinement-loop constructions remain closed.

The original quantum comparison supplies the X+ branch, not an unconditional
Bell preparation. This packet does not accuse it of the latter claim. Its new
comparison keeps the complementary branch and binds record decoding to a
separate source operation already present in that source: the identity filler.

The fresh inventory read found an explicitly simulation-only apparatus adapter;
the current Marici fabric has no optical-apparatus binding. The apparatus-data
inventory and hardware-bound pushforward packet provide schemas/synthetic data,
not independently calibrated physical trials. The external photon-scattering
packet supplies a different physical-theory realization, not a demonstrated
implementation of this Bool twist. No repository-wide absence is inferred.

## Full preparation before scalar readout

Starting with the GIVEN state |00>, use the existing X instrument, with h=0 for
its plus effect and h=1 for its minus effect, followed by the actual twist T:

\[
\sigma_h=T\,\mathcal I_{X,(-1)^h}(|00\rangle\langle00|)\,T^\dagger
        =\tfrac12|\Phi_h\rangle\langle\Phi_h|,
\qquad
|\Phi_h\rangle=\frac{|00\rangle+(-1)^h|11\rangle}{\sqrt2}.
\]

The complete preparation is the classical/quantum block state
\(\sum_h |h\rangle\langle h|\otimes\sigma_h\).
Here h is an instrument-effect label, not an established physical record.
Forgetting it gives the separable equal mixture of |00> and |11>, whose fixed
analyzer CHSH value is sqrt(2). This does not refute event-ready selection of
X+: that is a different, explicitly conditioned protocol.

A calibrated source record r permits the LOCAL readout rule

\[
a'=(-1)^{rx}a
\]

on Alice clicks at her own setting x. Bob is unchanged; no-click stays no-click.
When r=h, the complete conditional instrument comparison is the ordinary
Z^h frame conjugation with the Alice label transported. This constructs a
classical record correction; it does not require physically applying that
coherent gate. Both source branches can contribute, with no selection by the
remote setting or detector result. This is a frame-aware classical/quantum
packet, not an unconditional, record-independent Phi+ density. Physical access
to that source record and its setting independence remain explicit requirements.

For each fixed shared source record, decoding only relabels Alice's own response.
After the fixed no-click assignment a deterministic local strategy still has
four signs A0,A1,B0,B1, so its CHSH expression
A0(B0+B1)+A1(B0-B1) is +2 or -2. Convex mixing over a setting-independent source
record preserves that bound. The local decoding does not manufacture a Bell
violation from Bell-local trials.

## Independent calibration, not a fitted Bell parameter

Let the reported-herald channel, with rows r and columns h, be

\[
K=\begin{pmatrix}1-e_0&e_1\\e_0&1-e_1\end{pmatrix},
\qquad 0\leq e_0,e_1\leq1.
\]

Use SEPARATE calibration trials with the identity filler instead of twist and
Alice's existing X analyzer. X repeatability then identifies the effect label:
the ideal Alice sign is d=(-1)^h. Under independent classical record erasure
with retention etaA>0, the observed calibration probabilities C satisfy

\[
C(r,d)=\frac{\eta_A}{2}K_{r,h(d)},
\qquad K_{r,h}=\frac{2C(r,(-1)^h)}{\eta_A}.
\]

Retention is measured from the same complete calibration distribution, including
no-clicks. Bob's retention etaB is separately readable there. No calibration
measurement is silently inserted into a Bell trial. Applying this calibration
to the twist route requires the SAME herald and erasure channels in both modes,
independent of analyzer settings and ideal detector labels.

Repeatability and the faithful click-label convention are premises of the
supplied instrument. This is not a self-calibration theorem for an unknown X
analyzer or unknown preparation continuation. Without independent reference for
those ports, calibration can conflate their errors with herald-record errors;
one must not promote an inferred effective channel into uniquely identified
physical herald noise.

The detector model is classical erasure of ideal instrument records. All ideal
postmeasurement continuations are retained before this classical map. It does
not identify erasure with an absorptive detector's quantum continuation.

For the frozen assignment of each no-click to +1 AFTER frame decoding, the
full-record prediction is

\[
S=\sqrt2(2-e_0-e_1)\eta_A\eta_B
  +2(1-\eta_A)(1-\eta_B).
\]

The comparison is of the entire record law, not this scalar alone. Herald
errors affect the X correlations but not the Z correlations; one fitted
visibility is not their full channel. At unit retention, correct decoding gives
2 sqrt(2), forgetting h gives sqrt(2), and a completely inverted record frame
gives zero. The first and last have identical balanced herald marginals.

## Risky tests and physical acceptance boundary

- Derive both preparation branches and every analyzer continuation from the
  actual imported implementations; retain all five filler actions.
- Transport the minus branch's full continuation with its frame, not just its
  Bell scalar; check normalization and no-signalling before and after erasure.
- Recover K and both retentions from the identity-route calibration and predict
  the full twist-route law without looking at its Bell scalar.
- Change only the test-mode channel from K=I to K=swap while leaving calibration
  unchanged. The predicted and actual record laws must disagree; balanced
  herald frequencies must not hide the disagreement.
- Reject zero-retention calibration and fail required gates with nonzero
  execution behavior. Preserve predecessor and cross-owner receipts.

The independently needed physical object is one preparation/readout bundle
with source and device identity, both herald records, labelled settings and
click/no-click trials, a fixed frame-decoding convention, independent bypass
calibration, uncertainties and authority to transport that calibration to the
twist mode. Its preparation instrument must leave an available two-subsystem
output for the twist: an absorptive first detector with the same effect
probabilities is not the required continuation. The compound model is rejected
if its held-out full-record prediction
fails within that calibrated domain; a mismatch alone does not uniquely blame
herald noise rather than source or detector failure.

Until that bundle exists this branch is physically deferred. No hardware was
requested or run; no waiting issue is created. More synthetic Bell statistics
would not supply the absent physical interface or distinguish Marici from QM.

## Disposition and verification

The frozen comparison survives. The herald-forgetting and marginal-only rivals
are rejected on the actual source; coherent Z actuation and rejection of the
minus branch are not necessary for the stated frame-aware readout. Calibration
predicts all 72 reported-record probabilities under the declared common-channel
contract. The mode-dependent-channel hostile is rejected with CHSH residual
2 sqrt(2), despite unchanged balanced herald marginals. Zero-retention calibration
is explicitly refused. No physical implementation or new selection law follows.

- Validated owner manifest: `e_38524_1791413228059029400_106`.
- Preregistered freeze: `scc-freezes/nima-bell-preparation-herald-record.9b78ab98959416e9.json`,
  execution `e_38524_1791413228308652000_107`.
- Frozen challenge, zero meaning survives:
  `e_38524_1791413247745884600_108`, exit 0.
- Fresh owner-model check: `e_38524_1791413320688109200_109`, exit 0.
- Failure-lifecycle controls: `e_38524_1791413383550121900_110`. Injected
  AssertionError and RuntimeError both propagate and remove temporary prior
  pass receipts; live source and receipt remain unchanged.
- Closing SCC status: `e_38524_1791413867847996100_111`, current checks passed.
- Final receipt/source-hash verification: `e_38524_1791414082196338500_113`;
  five actions, 32 twist continuations, 72 raw and 72 decoded records retained.

Checker: `checkers/check_bell_preparation_herald_record.py`.
Receipt: `results/bell-preparation-herald-record.json`, retaining all five source
actions, both-branch preparations, the full CQ state, twist continuations,
calibration and raw/decoded record laws. Predecessor and cross-owner receipts
remain unchanged. No fresh Agda/Rzk closure or physical experiment is claimed.

Aspect was asked for an EXISTING independently calibrated preparation/record
bundle, not a new template or apparatus dispatch (proposal
`ep_4793e857-5ad1-4aa0-9c69-1b9741ea9abc`); the bounded result was reported in
`ep_677d80a4-ae9e-4458-9f8b-192fc2eddc1a`. Absent that input, physical validation
of this heralded optical route has no admitted executable continuation; repeated
symbolic Bell values or synthetic acquisitions are not its successors.

## Continuation disposition

The proposed scattering-source inspection was performed in Topic-9 iterations
2-4. `compton-record-compatibility.md` excludes the declared Compton-rebinning
interface; `ward-chart-real-cut-obstruction.md` and
`ward-real-boundary-null-source.md` exclude direct physical preparation from
the generic native chart and its real polynomial boundary. Reconstruction from
complex cuts still needs its own source-defined physical comparison; do not
repeat the completed inspection or substitute a normalized helicity shadow.

The subsequent four-gate plan opens a different, model-level comparison in
`filler-phase-spectator-hypothesis.md`: the existing Boolean action and
composition do not independently fix their physical quantum lift. That test
does not supply the apparatus/calibration bundle required by the present packet,
nor establish that scattering implements the Bool twist.

## 2026-10-08 physical-bundle intake

The operator prioritized acquisition of the actual preparation/readout bundle
(stimulus/notice `ep_36da07ce-8dc8-4551-a327-a52e0d14f170`). Fresh intake is
recorded in `results/preparation-readout-acquisition-audit.json`, with input
hashes and bounded scan roots. It is an access/provenance audit, not acquisition
or a new physical result.

- The current thirteen admitted site surfaces contain no optical-apparatus
  binding. Pure inspection of the reference implementation returns
  `simulation_only`, fixture attestation and no device receipts; no server or
  apparatus was started and dispatch was not called.
- The eight-event candidate explicitly says `synthetic_reference`. The receipt
  gate explicitly uses `fixture_hmac_sha256_not_hardware_identity`; valid fixture
  signatures and content hashes cannot authenticate physical acquisition.
- The comparison-loop contract still declares hardware identity, physical
  calibration and physical trials all unbound/false.
- An inclusive filename scan covered 1,449 files in the four recorded result/
  input directories without finding the listed common raw-data formats. This
  does not exclude differently encoded or externally held data. Bounded JSON
  searches found no affirmative physical-acquisition flags in those roots.
- The artifacts MCP returned `nars_session_missing`; `artifacts_doctor` reports
  `not_configured`, no session id and no session/artifact indexes. This is an
  access blocker, not an empty-registry finding. No other session was guessed
  or accessed.
- The older Bell checker passes `on_alice=True` to the preparation instrument;
  the current projective discriminator passes `False`. Reusing an A-X
  preparation calibration for that B-X coherence test requires an explicit
  port-transfer justification or matching calibration. No physical data was
  relabelled to hide this difference.

SCC reports the projective source model's existing checks current; this supplies
no physical gate. Closing inbox/lifecycle reads supplied no replacement bundle
or directed acquisition obligation. No waiting issue, additional acceptance
schema or synthetic acquisition is created. The objective remains blocked at
the first missing physical binding/calibration/raw-record object. Reopen on an
accessible measured bundle with provenance, or an admitted apparatus connection
with separately scoped acquisition authority. No further iteration on unchanged
inputs constitutes acquisition progress. Fresh receipt/hash verification:
`e_38524_1791427342040531000_173`. Tested scope and blocker were reported to
Aspect in `ep_0c4201ec-f3e1-4404-8b39-f5b3064cca88`. The stimulus-through-report
communication interval and owner audit/packet remain uncommitted.

## Superseding research directive

The operator subsequently instructed: “no physical admission is allowed to be
a gate. next” (`ep_485304f6-035b-4389-ab60-f64f305776c3`). The intake result
above remains an acquisition fact, but its admission-dependent research stop
is withdrawn. Do not require a new apparatus or authorization packet before
continuing source-bound calculations.

`bypass-record-reflection.md` supplies the next calculation and the previously
missing native port comparison: both fixed source implementations transport
B-X preparation to A-X preparation through the actual swap. Its complete-record
prediction and noise hostile are tested without creating measured data.
Experimental nonverification is a claim boundary, not the active frontier.
