# Redundant gauge frames correct relative faults but not consumption or common-mode drift

## Bounded question

Can the six-state relational gauge frame required by the two-port
\(D(S_3)\) endpoint compiler be made reusable and fault tolerant by encoding
its orientation redundantly?

The answer separates three tasks:

- detecting disagreement among physical frame registers;
- preserving one coherent logical orientation;
- replenishing coherence consumed by a noncentral relational pulse.

Repetition helps with the first task. It does not solve the latter two.

## Locked frame code

For \(n\) regular \(S_3\) registers, define the locked subspace

\[
\mathcal C_n
=\operatorname{span}\{|r\rangle^{\otimes n}:r\in S_3\}.
\]

The logical orientation basis is

\[
|r\rangle_L=|r\rangle^{\otimes n}.
\]

Diagonal left multiplication acts as

\[
L_x^{\otimes n}|r\rangle_L=|xr\rangle_L.
\]

Thus \(\mathcal C_n\) contains one regular logical torsor, not \(n\)
independent orientations. Its invariant logical state is

\[
|+\rangle_L
=\frac1{\sqrt6}\sum_{r\in S_3}|r\rangle_L.
\]

Pairwise equality projectors can test whether all physical labels agree. They
commute with the diagonal gauge action and stabilize \(\mathcal C_n\).

## What repetition detects

A displacement on one coordinate,

\[
L_x^{(j)},
\]

takes a sharp codeword outside \(\mathcal C_n\) when \(x\ne e\). Equality
checks detect the disagreement. With a promised sparse classical displacement
model, majority decoding can identify and repair fewer than half of the
corrupted labels.

A common displacement,

\[
L_x^{\otimes n},
\]

preserves \(\mathcal C_n\) and every equality check. It acts as the logical
left-regular operation

\[
|r\rangle_L\longmapsto|xr\rangle_L.
\]

No internal agreement test can decide whether all registers moved together.
The code protects relational agreement, not the origin of the frame.

The same code also does not correct arbitrary quantum noise. Diagonal phase
errors can damage coherence between the six logical orientations while leaving
every sharp label agreement test unchanged. The construction is a repetition
code for coordinate displacement faults, not a complete quantum code.

## Logical relational pulse

The encoded relational flux projector is

\[
P_{q,L}
=\sum_{r\in S_3}
B^{rqr^{-1}}\otimes|r\rangle_L\langle r|_L.
\]

Its pulse is

\[
V_{q,L}(\theta)
=\sum_rW_r(\theta)\otimes|r\rangle_L\langle r|_L,
\]

where

\[
W_r(\theta)
=I+(e^{-i\theta}-1)B^{rqr^{-1}}.
\]

This is the same logical controlled unitary as for one regular frame. Encoding
changes the physical carrier but not the six logical branches.

## Redundancy does not improve the return law

For an encoded pure reference

\[
|\eta\rangle_L=\sum_r c_r|r\rangle_L,
\qquad
p_r=|c_r|^2,
\]

the probability of passing the encoded sharp return test is

\[
f_{\eta,L}(\rho)
=\operatorname{Tr}(\rho M_\eta^\dagger M_\eta),
\]

with

\[
M_\eta=\sum_rp_rW_r.
\]

The expression contains no \(n\). Therefore the worst-case return probability
of the invariant logical frame remains

\[
f_{\min}^{(q)}(\theta)
=1-\frac{4(k-1)}{k^2}\sin^2\frac\theta2,
\]

where \(k\) is the conjugacy-class size of \(q\).

For every repetition length:

- a transposition \(\pi\)-pulse has worst-case return probability \(1/9\);
- a three-cycle \(\pi\)-pulse has worst-case return probability zero.

Increasing the number of locked registers does not dilute coherent consumption.
The pulse addresses one logical torsor and writes the same record into its six
orientation branches.

## Independent copies are a different resource

The product preparation

\[
|+\rangle^{\otimes n}
\]

contains \(n\) invariant regular registers, but they are not one shared sharp
frame. They may supply \(n\) separate relational interactions, each with the
same one-use degradation law. They do not determine a common based element
unless an additional correlation constructor locks their relative
orientations.

Locking them produces the cat-like logical frame \(|+\rangle_L\), returning to
the previous theorem. One must choose between a stock of uncorrelated
invariant references and one coherently shared orientation. Dimension counting
alone conflates these resources.

## Pure reset exports the record

Let \(\{ |\phi_a\rangle_R\}\) be possible pure reference states after use,
labelled by a data branch or history \(a\). Suppose a physical reset has a
Stinespring isometry \(U\) satisfying

\[
U|\phi_a\rangle_R|0\rangle_E
=|\eta\rangle_R|e_a\rangle_E
\]

for every \(a\), where the reference is restored to one fixed pure state.
Isometry preserves inner products, so

\[
\langle\phi_a|\phi_b\rangle
=\langle e_a|e_b\rangle.
\]

The entire Gram matrix of the consumed reference ensemble appears in the
environment. Every distinction removed from the reference is exported rather
than annihilated by a clean reversible constructor.

If the environment is also required to return to one state independent of
\(a\), then

\[
\langle\phi_a|\phi_b\rangle=1
\]

for all \(a,b\). Hence all normalized input states are identical up to an
irrelevant common phase. A nontrivial consumed ensemble cannot be reset cleanly
with both reference and environment uncorrelated from its history.

This is the exact replenishment boundary.

## Mixed states and irreversible reset

A constant channel can always discard the old reference and prepare a fresh
invariant state. That operation is gauge covariant because the target state is
invariant. It does not restore a based pulse on the data and it is not a closed
catalytic cycle.

In a dilation, the discarded state and its correlations enter an environment.
If the reference had recorded which flux branch was addressed, the environment
becomes a record port. Repeating the protocol requires a supply of fresh
low-entropy reference carriers and an entropy sink.

Therefore symmetry does not forbid replenishment. It forbids describing
replenishment as free disappearance of the constructor history.

## Reset after tracing cannot recover the intended based gate

After the invariant frame is forgotten, the data channel is

\[
\Lambda_+(\rho)
=\frac1{6}\sum_rW_r\rho W_r^\dagger.
\]

A later reference reset acts only on the reference or its replacement. It
cannot convert this conjugacy-twirled channel into one chosen based unitary
without a new oriented control resource or retained correlation.

Thus the cycle “prepare invariant frame → apply relational pulse → discard and
reprepare”

is a valid repeated implementation of the averaged channel. It is not a
compiler for a fixed noncentral element operation on data alone.

## Fault-tolerant compiler theorem

For the locked repetition carrier \(\mathcal C_n\):

1. relative coordinate displacements can be detected by equality syndromes;
2. diagonal common-mode displacement is a logical frame operation and is
   syndrome invisible;
3. coherent noncentral use has the same return law as the unencoded frame;
4. restoration to a fixed pure frame exports the acquired Gram matrix to an
   environment;
5. a constant covariant reset supplies fresh invariant references but only
   implements repeated conjugacy-averaged data control when the frame record is
   discarded.

No repetition length converts an invariant relational frame into a sharp,
exactly catalytic, fault-independent origin.

## Minimal additional port

Detecting common-mode frame displacement requires a relation to something not
derived from the same locked carrier. Candidates include:

- an independently transported boundary frame;
- a second preparation path with separately typed common causes;
- a gauge-invariant Wilson relation crossing the frame-preparation cut;
- or a physical convention fixed by an external asymmetric apparatus.

This port need not reveal an absolute gauge coordinate. It must compare the
compiler frame with an independently sourced relation. A copied frame register
does not qualify.

## Exact falsifiers

- Equality checks claimed to detect \(L_x^{\otimes n}\).
- A locked \(n\)-register frame claimed to contain \(n\) independent logical
  orientations.
- Repetition claimed to improve the invariant-frame return law without
  changing the logical pulse.
- A three-cycle \(\pi\)-pulse on \(|+\rangle_L\) claimed to have nonzero
  worst-case return for some \(n\).
- Pairwise label checks claimed to correct arbitrary phase noise.
- A pure reset claimed to restore all consumed frame states while leaving one
  history-independent environment state.
- Discard-and-reprepare claimed to recover a fixed based element pulse from the
  conjugacy-twirled data channel.
- Copies derived from one frame called independent origin witnesses.

## Machine-readable result

```json
{
  "code": "redundant_relational_frame_limit",
  "group": "S3",
  "physical_registers": "n",
  "logical_orientation_dimension": 6,
  "relative_coordinate_displacement_detectable": true,
  "common_mode_displacement_detectable_internally": false,
  "arbitrary_phase_noise_corrected_by_equality_checks": false,
  "one_use_return_improves_with_repetition": false,
  "transposition_pi_worst_case_return": "1/9",
  "three_cycle_pi_worst_case_return": 0,
  "pure_reset_exports_input_gram_matrix": true,
  "constant_invariant_reset_covariant": true,
  "constant_reset_recovers_based_data_pulse": false,
  "independent_cut_crossing_reference_required": true
}
```

## Deutschian explanation

Many agreeing compasses do not establish north when every compass inherited
the same unverified orientation. Repetition reveals a compass that disagrees
with the others; it cannot reveal that all of them rotated together.

Nor does making the compass larger stop it from recording an interaction. The
six coherent logical orientations are still the degrees of freedom on which
the noncentral pulse acts differently. Encoding each orientation into many
physical registers protects its spelling, not its coherence budget.

Resetting the frame removes the record only from the frame. Reversible physics
moves that record into the reset apparatus. Irreversible physics consumes a
fresh carrier and an entropy sink. Either way, the constructor has a boundary
that the endpoint algebra alone does not show.

## Shared Carrier geometry and quantum coefficient lens

The shared Carrier geometry is a cut theorem. Redundancy internal to one side
of a cut detects relative faults but cannot certify a common origin. Erasing a
record from one carrier moves it through another port.

The quantum coefficient lens supplies the coherent logical cat state, the
controlled noncommutative pulse, phase faults invisible to classical equality
checks, and Gram-matrix preservation under Stinespring dilation.

The same Carrier pattern appears classically as common-mode controller failure
and irreversible reset. What is uniquely quantum here is that the protected
resource is coherence among gauge-related orientations rather than a stored
classical label.

## Claim boundary

This packet proves the locked-code common-mode obstruction, invariance of the
one-use return law under repetition, and the pure-reset information-export
theorem. It does not construct a full quantum error-correcting code for the
frame, price thermodynamic reset work, provide an independent physical origin,
or synthesize local fault-tolerant endpoint pulses.

## Process calibration

Excitement is 10/10 and confidence in the finite theorems is 10/10. The main
gain is that frame replenishment is no longer an undefined repair: repetition,
reset, and independent reference have different exact capabilities. The next
apparatus question is to classify the smallest cut-crossing relation that
detects common-mode frame drift while remaining gauge invariant.
