# A recording instrument changes the future carrier

## Bounded question

Which future tests remain predictively valid after a sharp quantum record is
created, and when can sequential measurement reproduce the original marginals
of two tests?

## Frozen sharp instrument

Let

\[
\{P_i\}_{i=1}^r
\]

be a projective measurement:

\[
P_iP_j=\delta_{ij}P_i,
\qquad
\sum_iP_i=I.
\]

Its Lüders instrument has branches

\[
\mathcal I_i(\rho)=P_i\rho P_i
\]

and unrecorded channel

\[
\Lambda(\rho)=\sum_iP_i\rho P_i.
\]

The dual action on future effects is

\[
\Lambda^*(B)=\sum_iP_iBP_i.
\]

The effect \(P_i\) determines the probability of record \(i\); the branch map
determines the post-record state. Closure must retain both.

## Fixed-effect theorem

For any operator \(B\), the following are equivalent:

1. \(\Lambda^*(B)=B\);
2. \(P_iBP_j=0\) for every \(i\neq j\);
3. \([B,P_i]=0\) for every \(i\).

### Proof

The pinching map keeps the diagonal blocks \(P_iBP_i\) and removes every
off-diagonal block. Thus equality with \(B\) is equivalent to vanishing of all
off-diagonal blocks. A block-diagonal operator commutes with every block
projector, and the converse follows by inserting the resolution of identity.

Therefore the algebra of future effects whose statistics survive the unrecorded
Lüders measurement on every input is exactly

\[
\{P_i\}'
=
\{B:[B,P_i]=0\text{ for all }i\}.
\]

This commutant is the preserved future-effect algebra.

## Statistical nondisturbance

A future effect \(B\) is statistically nondisturbed when

\[
\operatorname{Tr}[B\Lambda(\rho)]
=
\operatorname{Tr}(B\rho)
\]

for every input \(\rho\). By duality this is exactly

\[
\Lambda^*(B)=B.
\]

For the sharp Lüders instrument, statistical nondisturbance is therefore
equivalent to commutation with every \(P_i\).

Agreement on a restricted source family is weaker. It may occur accidentally
even when \(B\) is disturbed on other states. The source family must be
tomographically complete before restricted equality becomes an operator
identity.

## Sequential joint-record theorem

After recording \(i\), measure a second projective observable
\(\{Q_j\}\). The sequential joint effects are

\[
G_{ij}=P_iQ_jP_i.
\]

They are positive and normalized:

\[
\sum_{i,j}G_{ij}=I.
\]

Their first marginal is always correct:

\[
\sum_jG_{ij}=P_i.
\]

Their second marginal is

\[
\sum_iG_{ij}=\Lambda^*(Q_j).
\]

Hence the sequential record has both original sharp marginals exactly when

\[
[P_i,Q_j]=0
\]

for every \(i,j\).

For sharp projective tests, Lüders sequencing compiles a joint sharp record
exactly in the commuting case.

## Compatibility versus nondisturbance

Keep four properties distinct.

### Compatibility

Some joint POVM has the desired marginals.

### Nondisturbance

A specified first instrument preserves the statistics of a specified future
test on every admitted input.

### Repeatability

Repeating the same test after its instrument returns the same recorded value
with certainty.

### Nondemolition

A source-typed observable or algebra remains available under repeated dynamics
and recording, usually with an explicit system–apparatus coupling and future
access condition.

For sharp Lüders measurements, these properties align strongly with
commutation. For general unsharp POVMs and instruments, compatibility need not
imply that a chosen instrument is nondisturbing, and equal effects do not fix
the state update.

## Minimal Pauli witness

For a sharp \(X\) measurement,

\[
P_{X\pm}=\frac12(I\pm\sigma_x).
\]

The unrecorded Lüders channel deletes the \(y\) and \(z\) Bloch components. In
particular,

\[
\Lambda_X^*(\sigma_z)=0.
\]

A subsequent sharp \(Z\) measurement therefore has zero expectation for every
post-\(X\) state, rather than the original expectation

\[
\operatorname{Tr}(\rho\sigma_z).
\]

The first \(X\) record is repeatable, but the conjugate \(Z\) information has
been removed from the system carrier.

The missing information may remain in an apparatus or environment correlation.
Recovering it requires reopening and controlling that port; the reduced system
channel alone no longer carries it.

## Recording is an intervention

A record is not a passive annotation attached to a pre-existing state. The
instrument maps

\[
\rho
\longmapsto
\{i,\mathcal I_i(\rho)\}.
\]

It creates a classical record and a conditional future system state. The
complete post-record carrier is therefore system plus record, and possibly a
retained environment.

If the record is discarded, the carrier follows \(\Lambda(\rho)\). If the
record is retained, future feedback can condition on \(i\). These have the same
unconditioned system channel but different constructor capabilities.

Thus “real-world interaction gets recorded by closure” must be sharpened:
recording is a source-authorized instrument that transforms the carrier and
writes a stable port. It does not merely reveal an unchanged hidden scalar.

## Predictive equivalence after recording

Before measurement, predictive equivalence is defined using the original
future tester family. After measurement, the state space changes to a
system–record packet. The new future equivalence must include:

- conditional continuations depending on \(i\);
- the disturbed branch state;
- any retained apparatus degrees of freedom;
- and the possibility of forgetting or coarse-graining the record.

Applying the old equivalence relation to the post-record state commits a carrier
typing error. The instrument is a transition between predictive-carrier
theories, not merely another scalar test inside one fixed quotient.

## Preserved-algebra closure

For a channel \(\Lambda\), define the fixed future-effect space

\[
\operatorname{Fix}(\Lambda^*)
=
\{B:\Lambda^*(B)=B\}.
\]

For Lüders pinching this is a unital operator algebra, the commutant of the
projectors. For a general channel, the fixed-point space need not support every
algebraic property without additional hypotheses, though finite-dimensional
unital channel fixed-point theorems give stronger structure in suitable cases.

The fixed effects are exactly the future questions unaffected by forgetting
the record. Conditional feedback can access more because it uses the branch
maps, not only the summed channel.

## Toric-code instance

Commuting stabilizer generators admit sequential syndrome extraction without
changing each other's sharp eigenvalue statistics under the ideal Lüders
model. Their common commutant contains the logical algebra, which explains why
local syndrome recording does not choose a logical sector.

A logical loop probe anticommuting with another logical probe disturbs the
conjugate future readout on the same code copy. The primal–dual intersection
pairing therefore governs both algebraic anticommutation and sequential record
compatibility.

Fault-tolerant syndrome extraction is stronger than the ideal commutant
theorem. It requires ancilla, propagation, locality, and repeated-round error
analysis.

## Polarizer instance

An ideal transmitted polarizer branch is a trace-decreasing projection, not a
trace-preserving Lüders measurement with both records retained. Conditioning on
transmission prepares the polarizer ray and removes the orthogonal component.

A later analyzer therefore probes the new prepared carrier. Its intensity is
an ordered transition probability, not the value the original field would have
given under that analyzer without the first filter.

Keeping both transmitted and reflected ports with stable records gives a fuller
instrument. Discarding one port creates loss and a different future theory.

## Software contrast

A read-only pure query can often create a record without changing domain state.
Then its update channel on the domain is identity and every future query is
nondisturbed.

But logging, rate limits, consumed tokens, locks, cursor advancement, privacy
budgets, and observation-triggered workflows make many software reads genuine
instruments. Their side effects change the future carrier even when the returned
payload is called a query.

The correct contract states both the response effect and the post-read state
transition.

## DPC: record-transition principle

The conjecture is:

> A physical record must be modeled as a carrier transition plus a stable
> readout port. The future questions preserved after recording are the fixed
> effects of the unconditioned transition, while retained branch records enable
> additional conditional constructors. Treating a record as a scalar without
> its state update is explanatorily incomplete.

The sharp Lüders theorem proves the finite projective case. The broader source
task is deriving the actual instrument and retained ports.

## Critics

### Other instruments can measure the same PVM

Correct. Effects determine record probabilities, not post-measurement states.
The fixed-algebra theorem here is for the declared Lüders instrument.

### Nondisturbance may hold on the admissible source subset

Correct. Then it is source-relative nondisturbance, not a full operator identity.
The subset and future tester family must be frozen.

### The apparatus may preserve information lost from the system

Correct. The reduced channel reports system loss. Reopening the apparatus
requires a retained-port theorem.

### Commuting sharp tests can still be hard to implement jointly

Correct. Algebraic compatibility does not price locality, ancillas, control,
noise, or fault propagation.

## Machine-readable witness

```json
{
  "code": "recording_instrument_disturbs_future_test",
  "instrument": "Luders(P)",
  "future_effect": "B",
  "dual_residual": "Lambda_star(B)-B",
  "commutator_residuals": ["[B,P_i]"],
  "source_family_tomographically_complete": true,
  "record_retained": true,
  "conditional_feedback_authorized": false,
  "apparatus_port_retained": false
}
```

## Exact falsifiers

- A record probability specified without a branch state update and called a
  complete instrument.
- A future effect called nondisturbed while \(\Lambda^*(B)\neq B\).
- Sequential sharp marginals claimed equal to the originals despite a nonzero
  projector commutator.
- Agreement on one source state promoted to operator-level nondisturbance.
- Repeatability of the first record used to infer preservation of conjugate
  tests.
- Information lost from the reduced system declared recoverable without a
  retained apparatus port.
- A non-Lüders instrument analyzed using the Lüders fixed-algebra theorem.
- Ideal commutation promoted to fault-tolerant measurement without a circuit
  and propagation analysis.

## Deutschian explanation

Recording changes what can happen next because it is an interaction, not a
label. A sharp record pinches the state into sectors. Future questions that are
block-diagonal survive; off-diagonal questions lose their system-level signal.

The commutant identifies the exact preserved future algebra. Retaining the
record adds conditional control, while discarding it yields the summed channel.
This explains both the information gained and the counterfactual capabilities
destroyed by making that information stable.

## Claim boundary

This packet proves the fixed-effect and sequential-marginal theorems for finite
sharp Lüders measurements. It does not classify general instruments or prove a
physical nondemolition implementation.

## Process calibration

Pre-objective: excitement 10/10, confidence 9.5/10, expected information gain
10/10. The target was to type recording as a carrier transition rather than a
passive scalar.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The preserved future-effect algebra is exactly the projector commutant,
and sequential sharp marginals coexist exactly under commutation. Recording,
repeatability, nondisturbance, and nondemolition are now separate gates.
