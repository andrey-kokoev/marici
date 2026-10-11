# Eight record-sign actions with axis-dependent readout

## Question and scope

Iteration 1 tests whether the fixed projective source can be distinguished
from a canonical source with a composition-compatible relabelling of the
ideal herald/Alice/Bob bits. Physical admission is not a research gate.
SCC obligation: realize the native references, transport their attachments,
then compare complete record laws.

**Conjecture:** all eight actions have noise-parameter-independent predictions
from native reference records. They are all excluded exactly when four
observable contrasts are nonzero. Blind Z readers produce actual record
aliases even when both coherent bypass correlations are nonzero.

Rivals: informative X probes suffice; unknown noise must first be fitted or
physically admitted; the 11 reference is redundant; or record equality means
instrument equality. Contract: `contracts/record-sign-action-census.v1.json`.

The noise map is K tensor R_A,axis tensor R_B,axis, with five distinct common
column-stochastic channels K, AX, AZ, BX, BZ. Conditional independence is a
premise. Missing herald and detector records are ordinary retained categories;
no-click probabilities may depend on the ideal sign. Axis-dependent RESPONSE
channels do not mean axis-dependent SIGN ACTIONS: the latter would enlarge the
eight-action class and are not silently included here.

## Exhaustive action class

The three adjacent source transpositions generate the actual S4 action. For
an action in C2^3 their braid relations force all three generator images equal.
Thus 512 possible generator-image assignments leave exactly eight actions:

\[
\rho_v(g)=\operatorname{parity}(g)v,\qquad v=(v_H,v_A,v_B)\in\{0,1\}^3.
\]

These flip ideal labels BEFORE their stochastic record maps; they do not
rotate postmeasurement states. This is not a scalar unitary character.

## Source-generated references

Keep the existing two balanced X-prepared bypasses:

- P_B: B preparation with A-Z/B-X readout;
- P_A: A preparation with A-X/B-Z readout.

Add the supplied product00 state with the actual identity or flip_both, read
with Z/Z. Both actions are even, and both unitary implementations send the
basis state to the same ray: 00 or 11. Consequently every sign action is
inactive on these references. No herald instrument is requested in these
basis experiments; all nine detector cells are retained.

The detector marginals identify the Z response columns z_A^+,z_A^-,z_B^+,z_B^-.
The plus columns are already marginals of P_B and P_A. The 00 reference therefore
checks closure, while 11 identifies the previously unseen minus columns.

Marginalize P_B over Alice to obtain M_B(r,b), and P_A over Bob to obtain
M_A(r,a). For any normalized joint table M, define

\[
F(M)=2\mu\nu^T-M,\qquad C(M)=M-\mu\nu^T.
\]

Set M^[0]=M and M^[1]=F(M). The actual source instruments give the following
predictions entirely in terms of reference records:

\[
T_v(r,a,b)=z_A^{(-1)^{v_A}}(a)\,M_B^{[v_H\oplus v_B]}(r,b),
\]

\[
S_v(r,a,b)=z_B^{(-1)^{v_B}}(b)\,M_A^{[v_H\oplus v_A]}(r,a).
\]

The projective predictions are

\[
T_P(r,a,b)=z_A^+(a)F(M_B)(r,b),\qquad
S_P(r,a,b)=z_B^+(b)M_A(r,a).
\]

Generic entrywise polynomial identities verify these formulas. Since the
predictions depend only on references, refitting hidden noise parameters while
preserving ALL those reference records cannot change a prediction in the
stated model class. This is not a claim that the noise parameters themselves
are uniquely identifiable.

## Exact record degeneracies

Let A_Z and B_Z mean that the corresponding two Z columns differ; let C_A and
C_B mean that the corresponding centered bypass matrix is nonzero. A mask v
has the same two probe record tables as the projective model exactly when

\[
(v_A=0\ \lor\ \neg A_Z)\ \land
(v_H\oplus v_B=1\ \lor\ \neg C_B)\ \land
(v_B=0\ \lor\ \neg B_Z)\ \land
(v_H\oplus v_A=0\ \lor\ \neg C_A).
\]

Necessity follows by marginalizing each product distribution; sufficiency is
direct substitution. Normalization prevents unequal factors from cancelling.
If both C_A and C_B are nonzero, only 001 and 110 can survive: 001 requires a
blind B-Z reader, while 110 requires a blind A-Z reader. Therefore all eight
are excluded if and only if A_Z, B_Z, C_A and C_B are all nonzero.

This is a record criterion for these two probes. It does not identify source
channels or all quantum continuations. Those matrices are retained separately.
The census covers all 32 distinguishability patterns of K,AX,BX,AZ,BZ; symbolic
identities and the factor argument, not those examples alone, give the result
for arbitrary stochastic channels in the declared class.

## Strongest reference-deletion hostile

Remove only the 11 reference. For mask 001, set the unseen B-Z minus column
equal to its plus column. For mask 110, do the same to A-Z. These canonical
rivals are predicted to reproduce BOTH probes, BOTH coherent bypasses and
the 00 reference of an otherwise fully informative projective model.
The 11 reference must reject these refits. Calibration exposes blindness; it
cannot recover information actually erased by a blind channel.

## Tested disposition

The conjecture survives 6,514 checks: all 512 generator assignments, eight
accepted actions, 4,608 source-composition cells and 32 channel-distinguishability
strata. The latter realize all sixteen observable-contrast patterns. Every
reference-based predictor equals the direct native-instrument record law;
the generic polynomial identities and marginal-factor argument supply the
arbitrary-channel statement rather than extrapolating from those examples.

With both coherent bypass correlations nonzero, the exact census is:

| A-Z distinguishes signs | B-Z distinguishes signs | Surviving record aliases |
|---|---|---|
| yes | yes | none |
| no | yes | 110 |
| yes | no | 001 |
| no | no | 001 and 110 |

Bit order is herald/Alice/Bob, before their readout maps. The full census in
the result also retains cases with blind herald or X channels; the displayed
table must not be extrapolated to them.

Dropping only the 11 reference permits both predicted nuisance refits. Each
matches both coherent bypasses, the 00 reference and both probe record tables.
Restoring 11 rejects each with record L1 residual 1 in the exact fixture. The
00 reference adds a closure check but no new identifying column in this model.

The blind-Z aliases are NOT full-instrument identities. For mask 001 with
blind B-Z, the twist's reported postmeasurement matrices differ with entrywise
L1 residual 27/20. For mask 110 with blind A-Z, the swap matrices differ with
entrywise L1 residual 17/12. These are matrix-entry residuals, not probabilities
or trace distances. They prevent promoting record equivalence into source or
instrument equivalence.

## Verification

- Manifest validation: `e_38524_1791434905262178700_186`.
- Prospective freeze: `scc-freezes/nima-record-sign-action-census.d18396dd50544dde.json`.
- Frozen challenge: `e_38524_1791434924784746900_188`, survives.
- Fresh headless closure: `e_38524_1791434960738824500_189`, pass.
- Exact metrics/source check: `e_38524_1791434973138754500_190`.
- Failure/port controls: `e_38524_1791435234591865800_191`. Injected AssertionError
  and RuntimeError remove temporary old successes. A temporary actual-instrument
  mutation sending both preparations to A fails at `retained-preparation-binding`.
  Live source and predecessor/foreign receipts remain unchanged.
- Source reconciliation: `e_38524_1791435510634690300_192`; final check
  `e_38524_1791435809057557800_193`.
- Checker: `checkers/check_record_sign_action_census.py`.
- Receipt: `results/record-sign-action-census.json`, with all exact record tables,
  source ideal matrices, representative complete reported continuations,
  stochastic maps, alias lists and reference-deletion residuals.

The prospective notice is `ep_4fcd6639-da97-4553-b272-4c71943e083b`; the tested
report is `ep_5e12fbd3-a7fc-4671-88f5-b30d43656053`. That communication interval
and the owner artifacts remain uncommitted. All new records are exact model
calculations, not measured trials.

## Successor and bounded closure

`record-reference-decision.md` now completes step 4: a constructive necessary-
and-sufficient exact reference-consistency test, conservative full-record error
envelopes, and a nine-model rejection rule. Its 1,754 checks include all 288
candidate truths under rational perturbations and the near-blind boundary.
Negative reflected estimates are retained, and an incompatible point estimate
is not confused with an excluded error region. Steps 2-4 are complete in this
declared class; a larger noise class or sharper statistical test is a separate
objective. Physical admission is not a gate.
