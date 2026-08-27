# Right-regular frame faults preserve control rank while conjugating port meaning

## Bounded question

Which coherent faults can act locally on the six-state relational gauge frame
without violating gauge symmetry, and which endpoint-control claims survive
such faults?

## Left gauge action and right frame action

Let the frame Hilbert space be 

\[
H_R=\mathbb C[S_3]
\]

with basis 

\[
\{|r\rangle:r\in S_3\}.
\]

The gauge action is left multiplication:

\[
L_x|r\rangle=|xr\rangle.
\]

Define right multiplication by

\[
R_k|r\rangle=|rk\rangle.
\]

The two actions commute:

\[
[L_x,R_k]=0.
\]

Therefore every right displacement is a gauge-invariant coherent operation on
the frame register.

## Frame-commutant theorem

The commutant of the left-regular representation is the right group algebra:

\[
\{L_x:x\in S_3\}'
=
\operatorname{span}\{R_k:k\in S_3\}.
\]

Hence the most general coherent frame operator respecting the left gauge action
is a right convolution operator. The six right permutations are its discrete
orientation shifts.

Gauge symmetry therefore does not freeze the relational frame. It permits a
full right-regular fault algebra.

## Action on relational flux ports

Recall the relational projector

\[
P_q
=
\sum_r
B^{rqr^{-1}}\otimes|r\rangle\langle r|.
\]

Conjugating the frame by a right displacement gives

\[
(I\otimes R_k)P_q(I\otimes R_k^{-1})
=
P_{k^{-1}qk}.
\]

Thus a gauge-invariant frame fault conjugates the physical meaning of the
element label while preserving its conjugacy class.

For a transposition (t), the fault permutes the three transposition ports. For
a three-cycle (c), an odd (k) exchanges (c) and (c^{-1}), while an even
(k) preserves the chosen cycle orientation.

## Rank certificates survive

The two-port endpoint theorem requires one transposition and one three-cycle.
Right conjugation preserves those two conjugacy types. Therefore the faulty pair

\[
P_{k^{-1}tk},
\qquad
P_{k^{-1}ck}
\]

still generates the full 36-dimensional associative endpoint algebra together
with gauge actions.

The projective Lie rank and central-rank counts are likewise unchanged under
simultaneous conjugation of the calibrated port pair.

Consequently, all algebra-dimension tests can pass while the apparatus acts in
the wrong relational frame.

This is not loss of controllability. It is loss of semantic calibration.

## Common-mode port fault

Both element ports use the same six-state frame. One right displacement changes
their labels coherently. Internal relations, conjugacy types, and closure ranks
remain correct.

Duplicating either port after the shared frame reproduces the same displaced
meaning. Equality comparison and rank checks are silent.

The fault is common mode because it acts before the control interface branches
into transposition and three-cycle uses.

## Stabilizers of individual ports

A right displacement leaves (P_q) unchanged exactly when

\[
k\in C_{S_3}(q).
\]

Therefore the invisible discrete stabilizer has order two for a transposition
port and order three for a three-cycle port.

For the ordered pair ((t,c)), the common stabilizer is

\[
C_{S_3}(t)\cap C_{S_3}(c)=\{e\}.
\]

No nontrivial right displacement fixes both exact element labels. If both ports
can be compared to an independently anchored specification, their joint label
is faithful on the frame torsor.

Without an independent anchor, a simultaneous relabelling remains a gauge of
the apparatus description rather than an internally detectable error.

## Class readout is completely blind

Conjugacy-class projectors satisfy

\[
P_C
=
\sum_{q\in C}P_q.
\]

Every right displacement permutes the summands and leaves (P_C) unchanged.
Thus class-only syndrome or flux readout is blind to the entire right-regular
orientation group.

Element-resolved control contains the missing odd information only relative to
the frame. Class readout cannot validate that frame.

## Coherent convolution faults

A general element of the right group algebra can coherently mix orientations,
not merely permute them. Such a fault can entangle or superpose relational port
frames.

After tracing out the frame, these coherent errors can appear as dephasing or
mixtures among conjugate element controls. Their exact effect depends on the
initial frame state and whether the frame remains accessible.

The discrete (R_k) faults are the minimal exact witnesses. They already prove
that gauge covariance and full algebraic rank do not guarantee calibrated
element control.

## Minimal calibration packet

To certify one sharp frame against discrete right displacements, a trusted
reference signature must distinguish the six states

\[
\{|rk\rangle:k\in S_3\}.
\]

This requires six distinguishable outcomes, or at least three trusted binary
coordinates, for full displacement identification.

If only fault detection from one trusted origin is required, one origin flag can
detect departure but cannot identify (k). If the starting frame is uncertain,
uniform transition detection again requires full frame identification.

This is the torsor-reference capacity theorem instantiated on the physical
right-regular fault group.

## Relational check across two anchors

Suppose the control frame (R) is locked to an independently prepared anchor
(A). The relative displacement observable depends on

\[
r_A^{-1}r_R.
\]

A right fault on (R) changes this relation and can be detected. A common right
fault on both (A) and (R) remains invisible.

The anchor must therefore cross a genuinely different preparation or transport
cut. A second register copied from (R) is not independent evidence.

## Fault-tolerant scheduling consequence

The frame should be verified before the first element-resolved pulse and after
the last pulse whose semantic correctness depends on it. Intermediate checking
is required if one frame fault can persist across several data contacts.

A mobile frame ancilla contacting many plaquettes has the same suffix-spread
hazard as a mobile Wilson-loop ancilla. A persistent right-displacement fault can
conjugate every later port in the schedule.

Distributed locked frames reduce contact depth but introduce a frame-state
preparation and verification problem. Their equality constraints certify
relative consistency, not global origin.

## Toric and quantum-double distinction

For an Abelian coefficient group, conjugation is trivial. Left and right frame
actions do not create the same element-label ambiguity. This fault sector is
therefore specifically non-Abelian.

The Carrier geometry of a based plaquette is shared with Abelian models. The
nontrivial right-frame fault action comes from the quantum coefficient lens.

This is one exact sense in which the (D(S_3)) implementation problem is not
merely a larger toric-code controller.

## DPC: algebraic controllability must be frame calibrated

The conjecture is:

> A non-Abelian element-control theorem is physically meaningful only relative
> to a calibrated relational frame. Gauge-invariant right-regular faults can
> preserve all rank and closure certificates while conjugating port meaning.
> Therefore frame calibration and its independent fault cut must be part of the
> executable constructor packet.

This separates control capacity from control semantics.

## Critics

### Simultaneous conjugation is only a change of convention

It is a convention when every source, target, and consumer is transported with
the frame. It is a physical error when the apparatus is compared to an external
anyon label, boundary condition, or recovery action that is not transported.

### Full endpoint rank means every desired operation remains available

Available up to the displaced frame, yes. The compiler may execute the wrong
named operation relative to the external specification while retaining full
rank.

### Class measurements can recalibrate the frame

No. They are invariant under conjugation and contain no element-orientation
information.

### Two exact element ports internally determine the frame

Their ordered pair has trivial stabilizer, but internal determination still
needs a trusted specification of which pair is intended. A coherent relabelling
of the entire apparatus is invisible without an external anchor.

### Right-convolution errors are too general to audit

The discrete right shifts are a finite generating witness. General coherent
faults can be bounded after a frame norm and noise model are frozen.

## Exact falsifiers

- A frame-local operator commuting with every left action but lying outside the
  right group algebra.
- Failure of the covariance law mapping (P_q) to (P_{k^{-1}qk}).
- A right displacement changing transposition into three-cycle type.
- A nontrivial right displacement fixing both the chosen transposition and
  three-cycle.
- Class-only readout detecting a pure right conjugation.
- A full rank certificate used to infer correct external port calibration.
- A copied frame register presented as an independent calibration anchor.

## Machine-readable fault packet

```json
{
  "code": "right_regular_frame_fault",
  "gauge_action": "left_regular",
  "frame_commutant": "right_group_algebra",
  "discrete_fault": "R_k",
  "port_action": "q -> k^-1 q k",
  "conjugacy_types_preserved": true,
  "endpoint_rank_preserved": true,
  "exact_port_calibration_preserved": false,
  "class_readout_detects_fault": false,
  "independent_anchor_required": true
}
```

## Deutschian explanation

Gauge symmetry removes absolute left orientation, but it leaves a physical
right action on the relational frame. That action changes which element the
apparatus calls a transposition or a directed cycle without changing the size
of the control algebra.

The machine can remain fully capable and consistently wrong relative to an
external specification. Rank certifies what transformations the displaced
machine can span; a reference certifies what those transformations mean.

## Claim boundary

This packet proves the finite frame-commutant and port-conjugation theorems. It
does not derive a physical anchor, a noise rate for right-convolution faults, or
a fault-tolerant frame-verification circuit.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was the first exact fault classification for
the relational frame.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. The common-mode frame fault group is right regular; it
preserves controllability ranks while conjugating semantic port labels.
