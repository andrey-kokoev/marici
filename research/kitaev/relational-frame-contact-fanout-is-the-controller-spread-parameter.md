# Relational-frame contact fanout is the controller spread parameter

Owner: `marici.Kitaev`

## Bounded question

When a protected six-state relational frame controls element-resolved
`D(S3)` endpoint contacts, what exact scheduling condition prevents one frame
fault from becoming several data faults?

This packet treats discrete right shifts at contact boundaries. It does not
claim protection against arbitrary six-level noise or faults internal to an
uncompiled contact.

## Frozen frame covariance

Let

\[
R_k|r\rangle=|rk\rangle
\]

be a right displacement of the frame. The relational flux projector is

\[
P_q=\sum_r B^{rqr^{-1}}\otimes|r\rangle\langle r|.
\]

Its exact covariance law is

\[
(I\otimes R_k)P_q(I\otimes R_k^{-1})=P_{k^{-1}qk}.
\]

Any contact obtained by functional calculus from this projector has the same
covariance. For example,

\[
C_q(\theta)=\exp(-i\theta P_q)
\]

satisfies

\[
(I\otimes R_k)C_q(\theta)(I\otimes R_k^{-1})
=C_{k^{-1}qk}(\theta).
\]

A persistent frame displacement therefore does not merely damage the frame
register. It replaces every later intended label (q) by (k^{-1}qk) until the
displacement is removed.

## Contact-history theorem

Consider an ordered contact schedule

\[
\mathcal S=(C_{q_1}^{(b_1)},\ldots,C_{q_m}^{(b_m)}),
\]

where (b_j) names the data fault domain touched by contact (j). Suppose a
single right shift (R_k) occurs after contact (a) and is corrected after
contact (b). Then precisely the contacts

\[
a<j\leq b
\]

are relabelled:

\[
C_{q_j}^{(b_j)}\longmapsto C_{k^{-1}q_jk}^{(b_j)}.
\]

Contacts for which (k\in C_{S_3}(q_j)) are unchanged. All other contacts are
semantically faulty even though the frame is eventually restored.

The exact data discrepancy over the affected interval is

\[
D_{a,b}(k)
=
\left(\prod_{j=b}^{a+1}C_{k^{-1}q_jk}^{(b_j)}\right)
\left(\prod_{j=a+1}^{b}C_{q_j}^{(b_j)}\right)^{-1},
\]

with products written in physical time order. This expression retains the
ordered history. In a noncommutative endpoint algebra it cannot in general be
replaced by a set of faulty labels or by a scalar residual.

## Exact schedule criterion

Let (\mathcal E_{\mathrm{data}}) be the data-error family correctable by the
chosen recovery layer. A checked schedule contains one admitted frame shift
exactly when

\[
D_{a,b}(k)\in\mathcal E_{\mathrm{data}}
\]

for every check interval, every allowed fault boundary (a), and every admitted
nonidentity (k).

This is the exact criterion. Contact counting is a structural certificate for
it, not a substitute for it.

Under the hostile independent-contact model, each changed contact on a
different data domain may create an independent correctable-coordinate error.
Define the sensitive fanout of a check interval by

\[
\phi
=
\max_{k\neq e}
\left|
\{b_j:k\notin C_{S_3}(q_j)\}
\right|,
\]

where repeated contacts on one data domain are counted once only if their
combined discrepancy has separately been proved to remain one correctable
fault.

If the data code corrects at most (t) adversarial domain faults, the robust
incidence condition is

\[
\phi\leq t.
\]

For the audited distance-three subcompiler, (t=1). Thus one unverified frame
rail may have sensitive fanout at most one between correction layers unless a
stronger propagation calculation proves that several contacts collapse to one
correctable data error.

## Four sufficient schedule architectures

One-frame-fault containment follows from any one of these independently typed
architectures.

1. Correct the frame before every sensitive data contact.
2. Use a fresh verified frame rail for each sensitive contact and never reuse
   that rail before frame recovery.
3. Prove directly that every interval discrepancy belongs to the data
   correctable set, even when the interval contains several contacts.
4. Record the right displacement and its time interval, then apply the ordered
   data rollback (D_{a,b}(k)^{-1}) before ordinary recovery.

The fourth architecture requires a constructor for the rollback. Knowing the
classical history does not make its inverse physical.

## Why final frame correction is insufficient

Frame recovery acts on the controller register. The interval discrepancy
(D_{a,b}(k)) acts on the data. Once a faulty contact has occurred, these are
different subsystems.

Correcting (R_k) at the end removes future relabelling but leaves the earlier
data discrepancy unchanged. It repairs the controller state, not the
controller's causal history.

Only a typed data recovery or an ordered rollback can remove the written
error. In particular, a scalar comparison of final outputs cannot infer the
required inverse in a noncommutative schedule.

## Transversal use of the three-frame code

The three-frame repetition code corrects one differential right shift in frame
memory. To turn it into a one-fault controller, the contact schedule must also
be transversal in fault influence.

A sufficient pattern assigns separate verified frame rails to separate data
contacts and checks the frame code before a faulty rail can control a second
sensitive domain. A single rail displacement can then cause at most one data
fault plus one correctable frame fault.

Reusing one displaced rail for several contacts defeats this conclusion even
though the three-frame memory is corrected perfectly afterward.

Thus there are two independent distance statements:

- frame distance controls whether the semantic coordinate is recovered;
- contact fanout controls how far a semantic error spreads into the data.

## Common-mode boundary

A common displacement

\[
R_k^{\otimes3}
\]

preserves all internal relative syndromes. It conjugates the meaning of every
element-resolved port coherently. No schedule using only the three locked
frames can detect it.

An external boundary anchor can compare the pair of exact element labels to an
independent specification because the common stabilizer of one transposition
and one three-cycle is trivial. The anchor must be independently prepared or
transported; another copy downstream of the same common cause is not
independent.

## The syndrome-extraction recursion

The natural coherent measurement of a relative frame coordinate computes

\[
r_i^{-1}r_j
\]

into a six-state ancilla. This uses controlled inversion and controlled group
multiplication.

In the frozen product-Pauli resource theory, full (S_3) multiplication contains
qubit-controlled qutrit inversion and is non-Clifford. It is one of the known
obstructions to the complete endpoint compiler.

Therefore the abstract three-frame correction theorem does not by itself
supply an executable correction circuit. Its coherent syndrome extractor
requires the same missing nonstabilizer resource family that appears in the
data compiler.

There are only three honest exits:

- admit and verify the required nonstabilizer resource;
- restrict the frame to a sharp classical register and authorize destructive
  classical comparison;
- find a different source-generated gauge-invariant syndrome instrument and
  prove it executable in the frozen theory.

This recursion is not circular reasoning. It is a shared resource obstruction:
non-Abelian semantic control and coherent protection of its reference both
need an operation outside the current stabilizer envelope.

## Constructor-level interpretation

The endpoint algebra answers which transformations exist abstractly. The
relational frame names the noncentral transformations. The frame code protects
that naming coordinate. The contact schedule bounds the causal spread of a
wrong name. The anchor determines whether all internal names have shifted
together.

These are four different layers:

```text
endpoint reachability
    -> semantic calibration
    -> controller-memory protection
    -> fault-contained physical use
```

Passing an earlier layer does not certify a later one.

## DPC: controller distance includes semantic fanout

The conjecture is:

> A fault-tolerant topological constructor must protect not only its data and
> its reference memory, but also the causal fanout of that reference between
> verification events. The correct controller distance is jointly determined
> by frame-code distance, sensitive contact fanout, and independent anchoring
> of common-mode semantics.

For the finite `D(S3)` model, the exact hostile prediction is that a schedule
with two sensitive data domains controlled by one unchecked frame rail admits
a single frame shift whose final frame syndrome is repairable while its data
discrepancy exceeds a one-domain recovery contract.

## Critics

### The frame code has distance three, so one frame fault is already handled

It handles the stored frame. A controller fault can act on data before memory
recovery. Code distance does not bound output fanout.

### The displaced ports still generate the full endpoint algebra

Reachability rank is invariant under simultaneous conjugation. The apparatus
can remain algebraically universal while executing the wrong labelled
programme.

### Measuring the relative frame syndrome is cheap bookkeeping

Only for an already classical sharp frame with an authorized classical
comparison channel. Coherent non-Abelian relative-coordinate extraction is an
operator constructor and is nonstabilizer in the frozen implementation.

### Several wrong contacts might cancel

They may in a specially proved schedule. The exact discrepancy formula permits
that possibility. Cancellation cannot be inferred from label counts or scalar
output equality.

### A final calibration measurement can identify what happened

It may identify the terminal displacement. It does not generally locate its
time of occurrence, reconstruct the ordered faulty history, or synthesize the
required data inverse.

## Exact falsifiers

- Failure of the frame-contact covariance law.
- A persistent right shift changing a contact whose label centralizes the
  shift.
- A schedule declared contained although some interval discrepancy lies
  outside the frozen data correctable set.
- Frame correction alone removing an already written data discrepancy.
- A reused frame rail certified by frame distance without a contact-fanout
  audit.
- A common right shift detected by internal relative syndromes.
- Coherent relative-syndrome extraction declared stabilizer-executable despite
  the controlled (S_3) multiplication obstruction.
- Ordered rollback inferred only from a scalar terminal record.

## Machine-readable theorem summary

```json
{
  "code": "relational_frame_contact_fanout",
  "group": "S3",
  "frame_error": "right_shift",
  "frame_memory_single_shift_correctable": true,
  "data_containment_automatic": false,
  "exact_gate": "all_interval_discrepancies_are_data_correctable",
  "distance_three_hostile_fanout_bound": 1,
  "final_frame_recovery_repairs_prior_data": false,
  "common_mode_detected_internally": false,
  "coherent_relative_syndrome_stabilizer_executable": false,
  "independent_anchor_required": true
}
```

## Claim boundary

This packet derives the exact propagation and containment criteria for
boundary-timed discrete right shifts. It does not compile the missing
nonstabilizer syndrome circuit, establish independent fault domains, protect
general frame noise, or certify the full endpoint schedule.

Its new conclusion is that frame-code distance and physical controller fault
tolerance are separated by a schedule invariant: sensitive contact fanout
between verification events.
