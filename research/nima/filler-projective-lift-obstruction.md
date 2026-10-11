# Critical-path iteration 2: projective channel lifts are not strict lifts

## Frozen question

Does the strict classification in `filler-phase-spectator-hypothesis.md` exhaust
implementations when equality of source composites means equality of completed
quantum channels, rather than phase-framed unitaries?

**Conjecture:** no. A fourth-root monomial lift of the same four-label S4 action
has a nontrivial central multiplier. It can reproduce the ENTIRE previous
flip_fst channel while changing a coherent input on the two labels fixed by
twist. This tests promotion of the strict theorem, not that theorem itself.
SCC obligation: forward realization with the unitary/channel equality types kept
distinct. Contract: `contracts/filler-projective-lift.v1.json`.

The rivals are strictifiability of every channel realization, identification of
the whole source model by the previous spectator test, a complete-model
ambiguity that is only a change of frame, and observing a global minus sign
without a phase-framed control interface.

## Source-preserving finite test

Import the same five Boolean functions, all four ordered labels and all 24
permutation actions. Obtain adjacent transpositions from the ACTUAL source:

- s0 = flip_both * twist * flip_both = (00 01);
- s1 = swap = (01 10);
- s2 = twist = (10 11).

A monomial lift is encoded by its permutation p and four exponents a_j modulo
4, acting as U|j> = i^(a_j)|p(j)>. Enumerate all lifts of each adjacent
transposition whose square is -I: sixteen each, hence 4,096 triples. Require
exact adjacent braid identities and T0*T2=-T2*T0. Finally require the channel of
T1*T0*T2*T1 to equal the canonical flip_fst channel on ALL sixteen matrix units.
Select the lexicographically first survivor before computing its readout.

The closure must retain 48 phase-framed operators, two over each source
permutation, but only 24 channels. For a section g -> U_g, retain the full table

\[
U_gU_h=\alpha(g,h)U_{gh},\qquad \alpha(g,h)\in\{1,-1\}.
\]

All 576 channel products are tested on all sixteen matrix units, and every one
of the 24 cubed cocycle associativity cells is tested. These finite bases span
the entire declared matrix algebra; this is not a sample of density matrices.
The search exhausts its stated fourth-root class, not all conceivable physical
realizations or all coefficient domains.

## Why a surviving multiplier cannot be removed

The two distant source transpositions commute. Their proposed lifts have
commutator -I. Multiplying either lift by ANY scalar phase does not change this
commutator, nor does a common change of basis. Strict representations send
commuting elements to commuting operators. Thus this obstruction cannot be
repaired by choosing different unitary representatives of the same channels.

Nevertheless Ad(-I) is exactly the identity channel. The commutator is a
mathematical obstruction, not a claimed direct observation of global phase.
The measurement below uses a relative phase in a different source operation.

## A discriminator the earlier test misses

The source twist fixes 00 and 01. Every strict monomial lift in the predecessor
acts on those two rays with the SAME scalar character: diagonal conjugation
cannot change coefficients on fixed rays. It preserves all coherence within
that fixed two-dimensional sector.

The projective prediction is opposite phases on those fixed rays. Under the
same supplied product preparation and fixed local reader, it changes the sign
of the spectator X statistic. Use the actual existing X instrument on B of
|00>, retain both h branches, and apply twist. Read the joint A=Z, B=X instrument
and retain every ideal (h,a,b) entry and its subnormalized continuation.

\[
W=\sum_{h,a,b}(-1)^h b\,p(h,a,b).
\]

All strict lifts predict W=1 in this sector; the projective candidate predicts
W=-1. Both predict W=1 for the prior flip_fst test, whose entire channels—not
just this one statistic—are required equal. No Bell scalar or coherent control
of an unframed channel is introduced.

As a separate coordinate-invariant distinction, the proposed linear-map trace
on M4 is 4 for the strict twist channel and 0 for the projective twist channel.
This is a SUPEROPERATOR trace, not the trace of an output density or a probability.
Different such traces prevent identifying the complete channel families by a
common change of representation. Consistently transforming any one complete
preparation/operation/readout packet still preserves its probabilities.

## Physical boundary

The state space, subsystem labels, coherent preparation, Born/Lueders rule,
local readout and faithful preparation labels remain supplied. The two branch
labels are instrument effects, not already calibrated physical records.
No hardware, no-click/loss data, independent calibration or held-out physical
records are created by this test. Both competing implementations use ordinary
QM; neither is a Marici-versus-QM prediction or a Born derivation.

Physical testing would require its own attachments and records. This is a
boundary on empirical claims, not a gate on research execution; the operator
explicitly removed physical-admission gates in the successor below.

## Tested disposition

The conjecture survives 24,231 checks. Of the 4,096 triples, 128 obey the lifted
relations and 16 also reproduce the complete old flip_fst channel. These are
phase triples, not a count of inequivalent physical theories. The selected
column-phase exponents, in label order 00,01,10,11, are:

| Generator | Permutation | Exponents modulo 4 |
|---|---|---|
| T0 | (00 01) | 0,2,1,3 |
| T1 | (01 10) | 1,1,1,3 |
| T2 | (10 11) | 1,3,0,2 |

They generate 48 operators with kernel {I,-I} over all 24 source permutations.
All 9,216 matrix-unit product checks and 13,824 cocycle cells pass. The selected
generator word for flip_fst is -i times X_A tensor I_B, hence its channel agrees
with the old canonical implementation on EVERY input, not just the prior test
state. Different section choices only change its scalar sign.

For twist the chosen matrix is

\[
T_2=\begin{pmatrix}
i&0&0&0\\
0&-i&0&0\\
0&0&0&-1\\
0&0&1&0
\end{pmatrix}.
\]

It applies opposite phases to the fixed labels 00 and 01. The actual imported
instrument gives W=1 for bypass, strict flip, projective flip and strict twist,
but W=-1 for projective twist. All forty ideal joint probabilities and their
full continuations are retained. Both preparation branches have trace 1/2.
The twist superoperator traces are exactly 4 and 0; both channels nevertheless
preserve the trace and positivity of density operators.

This rejects completeness of the STRICT implementation class at channel level
and sufficiency of the previous flip_fst calibration for identifying the whole
source model. It does not refute the strict theorem or select either physical
implementation. In particular, the central commutator -I remains unobservable
as an isolated channel; the relative-phase test is a different operation.

## Verification

- Manifest validation: `e_38524_1791423854246037100_162`.
- Freeze: `scc-freezes/nima-filler-projective-lift.211021c8a79c39ca.json`.
- Frozen challenge: `e_38524_1791423873535924900_164`, survives.
- Fresh headless closure: `e_38524_1791423903794852800_165`, pass.
- Independent verification: `e_38524_1791424012469179200_166`. Dense SymPy
  matrices independently reproduce all 2,304 lifted-group products and 768
  channel matrix-unit actions. Injected AssertionError and RuntimeError remove
  temporary old success receipts; a temporary mutation of the actual flip_fst
  source function is rejected. Live inputs and receipts are unchanged and their
  SHA256 hashes match.
- Final source-hash reconciliation: `e_38524_1791424505315034900_168`.
- Checker: `checkers/check_filler_projective_lift.py`.
- Receipt: `results/filler-projective-lift.json`, retaining all surviving phase
  triples, the selected matrices, word representatives, cocycle and records.

Early notice `ep_82e3092a-9d2a-4a93-b4b8-08992c3c3691` and tested report
`ep_3ab69980-f856-48b3-a4cc-7641531d6c9b` were admitted as communications,
not evidence certification. Both remain uncommitted. No computation is left
running and no fresh Agda/Rzk proof closure is claimed.

## Active continuation: no physical-admission gate

The previous admission-dependent research stop is superseded by the operator's
instruction “no physical admission is allowed to be a gate. next”, recorded in
`ep_485304f6-035b-4389-ab60-f64f305776c3`.

`bypass-record-reflection.md` executes the successor: derive the full-record
prediction from bypass data under unknown common channels, expose a parity-
herald rival that aliases all 24 old-reader settings, and separate that rival
using the native swap and an existing cross-port reader. This is a new
readout/transport comparison, not another phase enumeration. Continue with
source-compatible record-noise rivals; physical verification remains a claim
boundary, never a prerequisite for these calculations.
