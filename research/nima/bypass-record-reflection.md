# Bypass record reflection and a source-parity herald rival

## Question and policy

Operator: “no physical admission is allowed to be a gate. next”. This supersedes
admission-dependent research stopping instructions, not the distinction between
model calculations and measured records. SCC obligation: attachment transport,
then full-record comparison. No apparatus, new physical data or Born derivation
is asserted or required to execute this comparison.

**Conjecture:** the actual projective twist exchanges the two B-X preparation
branches. A bypass table therefore predicts its complete record law without
identifying common herald/readout errors. However, a canonical strict source
with a source-parity-dependent herald flip can imitate all 24 source settings
under the old reader. An existing source swap with a different existing reader
should separate that rival.

Rivals: uncentered sign reversal is sufficient; record reflection identifies the
source operator; additional source words alone remove the alias; A/B calibration
can be relabelled without a transport; or click conditioning preserves the law.
The frozen contract is `contracts/bypass-record-reflection.v1.json`.

## Derivation before scalar readout

The live source supplies subnormalized preparations sigma_h with trace 1/2.
For the B preparation the strict twist fixes sigma_h, whereas the selected
projective twist sends it to sigma_(1-h). Let K be an unknown common
column-stochastic map from h to the reported herald r, including missing
records. Let Q(y,h) be the complete conditional readout law, including joint
click/no-click labels, with the same downstream instrument in both modes.
Herald and readout are conditionally independent given h.

With J exchanging the two source labels,

\[
P=\tfrac12KQ^T,\qquad
\mu=\tfrac12K\mathbf1,\qquad
\nu=\tfrac12Q\mathbf1,
\]

\[
P_{\rm strict}=P,\qquad
P_{\rm projective}=\tfrac12KJQ^T=2\mu\nu^T-P.
\]

This is an entrywise polynomial identity, not an inference from finitely many
noise samples. It holds for every declared finite record alphabet. Detector
loss may depend on its ideal label; no equal-efficiency assumption or rejection
of no-clicks is needed. Commonness and conditional independence are premises,
not conclusions of the identity.

The centered table C=P-mu*nu^T changes to -C. Entrywise expansion also gives

\[
C=\tfrac14(K_{\cdot0}-K_{\cdot1})(Q_{\cdot0}-Q_{\cdot1})^T.
\]

Thus the two predictions differ exactly when BOTH channels distinguish the
source branches, and their L1 separation is 2||C||_1. The full matrix C is the
criterion: a particular scalar score can vanish despite a nonzero C. An
uncentered signed statistic includes a product-of-marginals offset and need
not reverse.
The same linear comparison holds for each postmeasurement matrix:

\[
S_{\rm projective}(r,y)=2\mu_r\sum_{r'}S(r',y)-S(r,y).
\]

Matrices are retained before taking traces. Equality of record probabilities
alone does not identify quantum continuations.

For estimated normalized tables with L1 errors epsilon_0 and epsilon_T, the
reflection map has the conservative Lipschitz bound 5*epsilon_0. Strict and
projective residual bounds are epsilon_T+epsilon_0 and
epsilon_T+5*epsilon_0 respectively. Their prediction balls are disjoint if the
predicted separation exceeds 2*epsilon_T+6*epsilon_0. This is an error-propagation
statement, not a claim that any experimental error bound has been measured.
An exact negative reflected cell refutes the exact paired-source model for that
table; finite-sample negative cells must be assessed with their uncertainty,
not clipped away.

## Strongest source-attribution hostile

Keep the canonical unitary source, but replace K by K*J^parity(g) for source
action g. Parity is computed from the actual source permutation and respects
composition. This is a classical herald relabelling, NOT a global unitary sign.
The proposed exhaustive test compares all 24 source actions, all ideal
postmeasurement matrices and the 27 reported cells under A-Z/B-X readout.
If they alias, adding more words without changing the final instrument supplies
no new discrimination within this source group.

The only homomorphisms S4 -> C2 are trivial and parity: the adjacent braid
relations force the three adjacent-generator values equal. This classification
is only of binary composition-compatible herald flips, not arbitrary noise.

## A native port-transfer test

Use the actual swap and the existing A-X/B-Z reader. Both selected source
implementations should send each B-X preparation sigma_B,h to the A-X
preparation sigma_A,h. This supplies a tested transport instead of silently
relabeling a calibration. An A-X-prepared identity reference uses the SAME
reader as the swap test.

The three predictions, as relative centered-table signs against their matching
bypasses, are:

| Model | twist, B preparation, A-Z/B-X | swap, B preparation, A-X/B-Z |
|---|---|---|
| Canonical strict | + | + |
| Selected projective | - | + |
| Canonical plus parity-herald flip | - | - |

The swap statement concerns these fixed implementations; it is not a theorem
about every diagonal-conjugated strict lift. Transfer of K between preparation
ports and operation-independent downstream readout are explicit model
premises. More general setting-dependent record maps are not ruled out.

## Tested disposition

All 2,780 checks pass. The polynomial identity and the full matrix-valued
comparison hold. For the frozen asymmetric herald and label-dependent loss
maps, the uncentered scores are 5/16 and -49/160: they do NOT negate each other.
Centering gives 99/320 and -99/320. All 27 reported cells, including missing
herald and detector records, are retained; the twist-table L1 separation is
7/10. None of these rational model values is a measured count or probability
estimate.

The stronger hostile survives the entire old source orbit: all 24 actions have
identical reported laws AND final quantum continuations under the projective
source and the canonical source with parity-herald noise. Eight actions keep
the preparation pair within one A sector; sixteen place it across A sectors,
where the final A-Z instrument removes that coherence. This is equivalence for
that experiment family, not equality of the source channels.

The actual swap transports each B-X preparation to its A-X counterpart under
both fixed implementations. With the matching A-X/B-Z reference, the parity
rival differs from the projective source by L1 distance 7/12. The two-probe sign
table above is therefore verified. A native transport and a different existing
reader, not physical admission, supply the extra discrimination.

Hostile residuals:

- Erasing herald information gives zero centered table and exact degeneracy.
- Unbalancing the preparation weights gives reflection residual 2/5.
- Retaining only Bob clicks gives reflection residual 7/102.
- Reflecting the exact three-state diagonal table I3/3 produces diagonal
  entries -1/9; they are retained as incompatibility, never clipped.

The error example uses rational perturbations, not simulated shot counts. Its
errors are epsilon_0=1177/60000 and epsilon_T=2281/240000; the stated prediction
balls are disjoint. The factor-five bound follows from marginal contraction
in L1 and

\[
\|2\widehat\mu\widehat\nu^T-\widehat P-(2\mu\nu^T-P)\|_1
\leq 2\|\widehat\mu-\mu\|_1+2\|\widehat\nu-\nu\|_1
      +\|\widehat P-P\|_1.
\]

## Verification and continuation

- Manifest validation: `e_38524_1791428819071504200_176`.
- Prospective freeze: `scc-freezes/nima-bypass-record-reflection.92175ddcd778a0e4.json`.
- Frozen challenge: `e_38524_1791428836647258200_178`, survives.
- Fresh headless check: `e_38524_1791429001210843100_179`, pass.
- Failure/port hostiles: `e_38524_1791429120733353300_181`. AssertionError and
  RuntimeError remove temporary stale successes. A temporary actual-instrument
  mutation that maps both preparation ports onto A fails at `ports-not-identical`.
  Live code and predecessor/foreign receipts remain unchanged.
- Source hashes current: `e_38524_1791429270534334000_182`; final reconciliation
  `e_38524_1791429707064784800_183`.
- Checker: `checkers/check_bypass_record_reflection.py`.
- Complete result: `results/bypass-record-reflection.json`, including the
  source-orbit postmeasurement matrices and reported continuations.

The operator directive and early notice are recorded in
`ep_485304f6-035b-4389-ab60-f64f305776c3`; the tested result was reported in
`ep_c4a5d057-a12d-4c1c-96ae-16b997a31b6a`. These communications and the owner
artifacts remain uncommitted. Physical admission is no longer a research gate.

`record-sign-action-census.md` now executes the wider herald/detector-sign test
with distinct axis channels. It classifies all eight actions and every channel-
distinguishability stratum, constructs reference-based predictions, and exposes
the surviving blind-Z cases. The 11 basis reference prevents hidden-column
refits; it cannot repair genuinely erased information. Continue with that
packet's finite-error/reference-consistency task, not another herald-only
census. Arbitrary context-dependent noise remains outside the declared class.
