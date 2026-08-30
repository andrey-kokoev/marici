# Three locked gauge frames correct one differential right shift

## Bounded question

What is the smallest gauge-invariant redundancy packet that detects or corrects
right-regular faults on the six-state relational (S_3) frame?

## Relative displacement observables

Let two frame registers (A) and (R) have basis states 

\[
|a,r\rangle.
\]

Their relative right displacement is

\[
d=a^{-1}r.
\]

Under a diagonal left gauge transformation,

\[
(a,r)\longmapsto(xa,xr),
\]

the relative displacement is invariant:

\[
(xa)^{-1}(xr)=a^{-1}r.
\]

For each (d\in S_3), define

\[
\Pi_d
=
\sum_{a\in S_3}
|a,ad\rangle\langle a,ad|.
\]

The six projectors are mutually orthogonal, sum to the identity, and commute
with the diagonal left gauge action. They provide a complete gauge-invariant
measurement of relative frame displacement.

## Two-frame detection theorem

The locked subspace is

\[
\mathcal C_2
=
\operatorname{span}\{|r,r\rangle:r\in S_3\}.
\]

It is the (d=e) sector. A nontrivial right shift on either one frame moves the
state into a sector with (d\neq e), so the projector 

\[
\Pi_e
\]

detects every one-register discrete right shift.

Two frames do not identify which register moved. For example, a shift on the
first register and a related shift on the second can produce the same relative
syndrome from different logical orientations. Detection is exact; correction
is not authorized without an additional fault-location assumption.

This is the group-valued analogue of two-copy equality comparison.

## Three-frame code

Define the six-dimensional code

\[
\mathcal C_3
=
\operatorname{span}
\{|r,r,r\rangle:r\in S_3\}.
\]

Write the logical frame basis as

\[
|r\rangle_L=|r,r,r\rangle.
\]

The diagonal left gauge action preserves the code:

\[
L_x^{\otimes3}|r\rangle_L=|xr\rangle_L.
\]

The uniform encoded state

\[
|+\rangle_L
=
\frac{1}{\sqrt6}
\sum_r|r,r,r\rangle
\]

is gauge invariant.

## Exact single-shift correction

Let the admitted discrete error family contain right shifts on at most one
register:

\[
E_{i,k}=R_k^{(i)},
\qquad
i\in\{1,2,3\},
\quad
k\in S_3.
\]

For the code projector (P_3), the Knill--Laflamme compressions satisfy

\[
P_3E_{i,k}^{\dagger}E_{j,l}P_3
=
c_{(i,k),(j,l)}P_3.
\]

When (i=j), the compression vanishes unless (k=l). When (i\neq j), it
vanishes unless both errors are the identity. Therefore the full one-register
right-shift family is exactly correctable.

The result is non-Abelian: no commutativity of (S_3) is used. The order of
the inferred correction is fixed by the relative displacement convention.

## Explicit syndrome table

Measure the two relative displacements

\[
d_{12}=r_1^{-1}r_2,
\qquad
d_{13}=r_1^{-1}r_3.
\]

Starting from ((r,r,r)), the syndromes are:

| Fault | Syndrome |
|---|---|
| none | ((e,e)) |
| (R_k) on frame 1 | ((k^{-1},k^{-1})) |
| (R_k) on frame 2 | ((k,e)) |
| (R_k) on frame 3 | ((e,k)) |

For (k\neq e), these patterns identify both the faulty register and the right
shift. Apply (R_{k^{-1}}) to that register to restore the locked codeword.

The syndrome uses only relative, gauge-invariant data. No absolute frame origin
is needed to correct one differential displacement.

## Minimality

One frame has no internal relative check. Every right shift maps a valid frame
orientation to another valid orientation.

Two frames detect one differential shift because it leaves the equality
subspace. They do not correct the full unknown-location error family: cross
compressions between faults on different registers act nontrivially on the
logical frame.

Three frames satisfy the exact correction conditions. Therefore, within the
repetition-frame architecture:

- one register carries the frame;
- two registers minimally detect one differential right shift;
- three registers minimally correct one differential right shift.

## Common-mode logical displacement

A simultaneous right shift acts as

\[
R_k^{\otimes3}|r\rangle_L=|rk\rangle_L.
\]

Both relative syndromes remain trivial. The operation is a logical right shift
of the encoded frame and is invisible to the internal correction circuit.

Thus the code protects relative agreement, not the global frame origin.

An independent external anchor or boundary condition is still required to
detect common-mode semantic displacement.

## Phase and decoherence faults

The repetition-frame code corrects the declared right-shift family. It does not
automatically correct diagonal phase errors in the (|r\rangle) basis,
left-right convolution errors of arbitrary support, leakage, or loss of a frame
register.

A complete quantum frame memory would require a larger error basis and a code
whose Knill--Laflamme conditions cover it. The present packet is a minimal
fault-specific theorem, not a general six-level quantum-memory code.

If the frame is used only as a classical sharp orientation, dephasing may be
harmless while right shifts are semantic errors. If coherent frame superposition
is required, phase protection becomes essential. The coefficient lens decides
which fault family matters.

## Ancilla implementation of the relative syndrome

Initialize a six-state syndrome ancilla in 

\[
|e\rangle.
\]

Controlled group multiplication can compute (a^{-1}r) into the ancilla using
one inverse-controlled multiplication from the first frame and one controlled
multiplication from the second. Measuring the ancilla yields (d).

For three frames, compute (d_{12}) and (d_{13}) into two syndrome ancillas.
The frame registers are unchanged on basis codewords. For coherent
superpositions, the measurement is nondemolition on the locked code space but
projects superpositions of different relative-error sectors.

This is an explicit conditional circuit surface. Physical availability of the
controlled six-level multiplications, clean ancillas, and measurement remains a
source obligation.

## Transport packet

The encoded frame can be distributed across three apparatus locations while
preserving only relative orientation. Diagonal left gauge transformations act
consistently on all rails.

After transport, pairwise relative checks verify that no single rail suffered a
right displacement. They do not prove that all rails avoided one shared
displacement during common preparation or transport.

The three rails must traverse independently typed fault domains for the
single-error assumption to be explanatory rather than diagrammatic.

## Scheduling with endpoint pulses

If one frame rail controls several element-resolved endpoint pulses in sequence,
a persistent right fault can conjugate every later port before final correction.
Correcting the frame at the end restores the register but does not undo semantic
errors already written into the data.

Therefore a one-fault-tolerant schedule must do at least one of:

- verify or correct the frame between data contacts;
- use separate verified frame rails transversally for separate contacts;
- prove that a single frame displacement cannot create more than one
  correctable data fault;
- or record the displacement history and apply a corresponding data recovery.

Frame-memory correction and fault-tolerant use of the frame are different
theorems.

## Relation to endpoint-control rank

The encoded frame does not enlarge the 34- or 36-dimensional endpoint control
algebras. It protects the semantic coordinate in which the two required flux
ports are named.

This is a control-plane code rather than a data-plane endpoint algebra. Its
success criterion is correct port meaning under the admitted frame-fault model,
not increased operator span.

## DPC: correct the reference before trusting the constructor

The conjecture is:

> A relational control frame must be protected as a typed information carrier.
> Two locked copies detect one differential frame displacement; three correct
> one. Common-mode displacement remains a logical frame error and requires an
> independently prepared anchor. Correcting the frame after it has controlled
> data does not by itself repair the operations already mislabelled.

This locates reference protection inside the constructor schedule rather than
outside the physical model.

## Critics

### The frame is gauge, so encoding it is redundant

Global left orientation is gauge. Relative right orientation determines which
noncentral element port the apparatus applies and is operational once compared
with a boundary or recovery specification.

### Two frames reveal the relative shift, so they should correct it

They reveal a mismatch but not which frame is authoritative. With an explicit
trusted-anchor assumption, two can correct the untrusted frame. Without that
asymmetry, three are minimal for unknown-location correction.

### Three frames are independent because they occupy different registers

No. Independence is a source and fault-path claim. A common preparation fault
can implement the logical shift (R_k^{\otimes3}).

### The code corrects arbitrary frame noise

No. It corrects the finite one-register right-shift family. Phase, leakage, and
correlated convolution faults require additional structure.

### Final correction restores the whole computation

It restores the frame memory. Data operations executed under the displaced
frame may require their own rollback or recovery.

## Exact falsifiers

- A nontrivial one-register right shift remaining in the two-frame locked
  subspace.
- A two-frame code correcting unknown shifts on either register without a
  trusted-anchor assumption.
- Failure of the three-frame Knill--Laflamme compressions.
- A nontrivial one-register fault producing the trivial two-syndrome pattern.
- A common right shift detected by internal relative checks.
- Single-register correction claimed for phase or leakage faults outside the
  frozen error family.
- End-of-schedule frame correction claimed to undo earlier miscalibrated data
  pulses automatically.

## Machine-readable frame-code packet

```json
{
  "code": "three_frame_right_shift_correction",
  "group": "S3",
  "frame_dimension": 6,
  "two_frame_detection": true,
  "two_frame_unknown_location_correction": false,
  "three_frame_single_shift_correction": true,
  "relative_syndromes": ["r1^-1 r2", "r1^-1 r3"],
  "common_mode_right_shift_detected": false,
  "phase_faults_corrected": false,
  "independent_anchor_supplied": false,
  "fault_tolerant_data_use": "unproved"
}
```

## Deutschian explanation

Three frames correct one displacement because two retain a common relational
history and identify the outlier. No absolute orientation is needed. What the
code preserves is agreement about the frame.

When all three move together, there is no internal disagreement. The frame code
then performs exactly as designed while the entire apparatus changes its
meaning relative to the outside. That remaining logical displacement is the
place where an independent source reference must enter.

## Claim boundary

This packet proves two-frame detection and three-frame exact correction for one
discrete right-shift fault. It does not protect general six-level noise, derive
independent fault domains, or prove a one-fault-tolerant schedule for endpoint
data contacts.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was the smallest anchored relative-frame
verification and correction packet.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Relative frame protection has the exact one/two/three
redundancy hierarchy; common-mode origin remains the independent-anchor boundary.
