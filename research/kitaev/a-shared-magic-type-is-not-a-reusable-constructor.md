# A shared magic type is not a reusable constructor

Owner: `marici.Kitaev`

## Bounded question

Controlled inversion is required both by the `S3` endpoint multiplier and by
the coherent relational-frame syndrome. Does identifying the shared gate type
also identify one reusable physical resource?

No. The answer depends on the supplied interface. A native gate may be called
repeatedly, a teleported magic state is consumed once, and a code switch is a
third constructor with different fault and scheduling obligations.

## Exact multiplier factorization

Use the frozen coordinates

\[
(e,k)(f,l)
=
(e+f,\;k+(-1)^e l).
\]

An in-place multiplication into the second register can be implemented by:

1. controlled inversion of (l) by (e);
2. qutrit SUM adding (k) into (l);
3. qubit SUM adding (e) into (f).

Only the first step is non-Clifford in the frozen product-Pauli theory.
Therefore one logical `S3` multiplication has exact controlled-inversion
demand

\[
N_{CI}^{\mathrm{mult}}=1.
\]

The statement is about this native semidirect-product factorization. It does
not say that the remaining encoded SUM operations are physically free; their
separate Clifford-teleportation interfaces remain required.

## Exact three-frame syndrome demand

Correction of one unknown right shift on three frames requires two independent
relative coordinates, for example

\[
d_{12}=r_1^{-1}r_2,
\qquad
d_{13}=r_1^{-1}r_3.
\]

Each exact coherent relative coordinate contains one controlled inversion.
Thus one full frame-syndrome round has demand

\[
N_{CI}^{\mathrm{frame}}=2.
\]

One relative coordinate is insufficient: it leaves one frame rail outside the
comparison graph and cannot locate every single-rail displacement. Any two
coordinates that connect three vertices form a spanning tree. Its two edges
share a vertex.

Under a two-body disjoint-contact rule, the two controlled inversions therefore
cannot occur in the same physical layer. The native lower bounds are

\[
N_{CI}^{\mathrm{frame}}=2,
\qquad
\operatorname{depth}_{CI}^{\mathrm{frame}}\geq2.
\]

A collective higher-arity syndrome interaction could change the depth, but it
would be a new authorized constructor rather than an optimization of the
frozen two-body interface.

## Aggregate logical demand

Let a bounded endpoint schedule contain (M) logical `S3` multiplications and
(R) coherent three-frame correction rounds. Any implementation using the
native factorizations has controlled-inversion call count

\[
N_{CI}=M+2R.
\]

This is a logical lower count before:

- encoded injection overhead;
- rejected factory attempts;
- verification ancillas;
- recovery layers;
- routing and waiting;
- the other missing controlled phases and coherent lookup resources.

It is therefore neither a full physical gate count nor a complete magic-state
census.

## Three inequivalent resource interfaces

### Native gate interface

A Hamiltonian or hardware primitive may implement (CI) directly on admitted
logical or physical coordinates. The gate type is reusable in the sense that
the apparatus can be called again. Each call still occupies time, participates
in a fault path, and may require recovery.

Required evidence includes:

- the local interaction generating the gate;
- its normalization and duration;
- leakage and coherent-error bounds;
- a fault-tolerant encoded lift;
- compatibility with both data and frame registers.

### Injection-state interface

A verified resource state may implement one (CI) call by teleportation or an
equivalent measurement gadget. In the standard Choi construction, the
resource block is consumed by destructive Bell measurements.

One accepted state therefore supplies one call, not an indefinitely reusable
gate. The lower accepted-state demand is

\[
N_{\mathrm{accepted\ CI}}\geq M+2R.
\]

Equality requires a deterministic one-state injection gadget with admissible
feed-forward and no additional (CI)-type correction. The existing naive Choi
gadget does not meet this contract: 32 of its 36 branches require
non-Clifford feed-forward. A different verified injection protocol remains a
source obligation.

### Code-switch interface

A code switch may move the relevant registers into an encoding where (CI) is
transversal or otherwise fault tolerant, apply several calls, then return.
This can amortize switching overhead across a batch.

It is not equivalent to state injection. Its contract must specify:

- which data, frame, and syndrome registers cross the code boundary;
- whether their relational gauge coordinate is preserved;
- switch-in and switch-out fault spread;
- the maximum safe batch size between recoveries;
- whether common-mode frame shifts remain detectable after return.

No such code-switch surface is present in the frozen theory.

## Sharing means factory sharing, not state reuse

The data multiplier and frame syndrome require the same output gate type. One
factory specification can therefore serve both if its output contract is
polymorphic over the two admitted register roles.

But each injected output is consumed by one use. The correct architecture is

```text
verified CI factory
    -> accepted output 1 -> endpoint multiplier
    -> accepted output 2 -> frame syndrome edge 12
    -> accepted output 3 -> frame syndrome edge 13
```

It is not

```text
one CI state
    -> endpoint multiplier
    -> frame syndrome
    -> returned unchanged
```

The latter is an exact catalytic-resource claim. No catalytic protocol or
resource monotone certificate has been supplied.

## Common-factory correlation theorem

Using one factory for both planes creates a shared causal ancestor. A single
factory fault may correlate:

- an endpoint multiplication error;
- the frame-syndrome error intended to diagnose semantic calibration;
- several accepted outputs used in the same correction epoch.

The existing one-fault distance-three schedule assumes that a macro fault
leaves at most one erroneous rail or one typed correctable output. This does
not automatically cover a shared factory event producing correlated errors in
multiple accepted blocks.

Hence a common factory is fault-tolerantly admissible only if at least one of
the following is proved:

1. every single factory fault is rejected or reaches at most one accepted
   output block;
2. outputs used in one causal epoch come from independently verified factory
   instances;
3. the joint correlated output family lies in the combined data--frame
   correctable set;
4. the schedule serializes use and verifies the factory boundary before its
   next output can influence another fault domain.

Logical gate-type equality proves none of these correlation conditions.

## Controller self-protection recursion

The frame syndrome is supposed to protect the semantic controller used by the
endpoint circuit. If both depend on outputs from one faulty factory, the
protection channel can fail in a way correlated with the data operation it is
checking.

This is not an infinite regress. It identifies the boundary at which an
independently verified resource must enter. The recursion closes only when the
factory acceptance record and output-error contract are established without
assuming the correctness of the same unverified semantic frame.

An acceptance test downstream of the same displaced frame is common mode. It
cannot serve as the independent anchor required by the frame theorem.

## Minimum typed interface

The smallest presently meaningful extension is not “magic available.” It is a
typed accepted-output port with the following fields:

```json
{
  "resource": "controlled_qutrit_inversion",
  "logical_action": "|e,k> -> |e,(-1)^e k>",
  "input_roles": ["data_multiplier", "frame_syndrome"],
  "uses_per_output": 1,
  "deterministic_feedforward": "required",
  "single_fault_output_contract": "at_most_one_correctable_block_error",
  "cross_output_correlation_bound": "required",
  "independent_acceptance_anchor": "required",
  "factory_supplied": false
}
```

Until that port is supplied, (M+2R) is a demand formula over an absent
resource, not an executable resource count.

## DPC: shared obstruction does not imply free reuse

The conjecture is:

> When a data constructor and the protection of its semantic frame require the
> same non-Clifford gate type, the minimal completion is a verified production
> interface with an explicit consumption and correlation contract. Naming one
> shared magic type does not make one state catalytic, and sharing one factory
> can create a common-mode fault between the operation and its diagnostic.

The explanatory content is the shared semidirect-product mechanism together
with the new causal obligation at the factory boundary.

## Critics

### The gate is an involution, so the resource can be reused

The logical unitary satisfying (CI^2=I) says nothing about whether a state used
to inject it survives the injection measurement. Unitary order and resource
consumption are different types.

### One factory is enough because both consumers request the same state

One factory type may be enough. The number of accepted outputs and their
correlation structure remain part of the proof.

### Two frame syndromes can be parallelized

Not under the frozen two-body disjoint-contact rule: every two-edge spanning
tree on three frame registers shares a vertex. A collective interaction or
copied coherent control would require another constructor and its own fanout
audit.

### Factory verification removes all correlation

Only a concrete verification theorem can establish that. Acceptance by itself
does not imply independent accepted outputs.

### The frame can use destructive classical comparison instead

Yes, if the architecture explicitly types the frame as classical and supplies
fresh trusted preparation. That changes the controller model and removes the
coherent-frame claim.

## Exact falsifiers

- An in-place native `S3` multiplier needing no (CI) call.
- Exact coherent extraction of either relative coordinate needing no (CI) or
  equivalent cross-species operation.
- Correction of an unknown one-rail shift on three frames using only one
  pairwise relative coordinate.
- Two pairwise two-body (CI) contacts on three frames occupying one disjoint
  circuit layer.
- A standard Choi resource remaining unchanged after destructive Bell
  injection.
- One shared factory certified without any cross-output correlation contract.
- A supplied deterministic, catalytic, fault-tolerant (CI) protocol; this
  would replace the consumptive branch of the classification.
- A supplied code switch with proved frame transport and fault spread; this
  would instantiate the third branch rather than refute the trichotomy.

## Machine-readable theorem summary

```json
{
  "code": "shared_ci_type_not_reusable_resource",
  "ci_per_s3_multiplication": 1,
  "ci_per_three_frame_syndrome_round": 2,
  "two_body_ci_depth_per_frame_round_lower_bound": 2,
  "aggregate_logical_ci_demand": "M+2R",
  "native_gate_reusable_interface": "unprovided",
  "standard_choi_state_consumed_per_use": true,
  "deterministic_ci_injection": "unprovided",
  "code_switch_interface": "unprovided",
  "shared_factory_type_possible": true,
  "shared_output_state_reusable": false,
  "cross_output_fault_independence_proved": false,
  "full_endpoint_compiler_completed": false
}
```

## Claim boundary

This packet counts logical controlled-inversion calls for the native
multiplier and pairwise frame-syndrome constructions. It does not give a
physical magic-state count, construct a deterministic injection gadget, prove
factory yield, or supply a code switch.

Its structural conclusion is that the common resource type unifies the
obstruction but not the implementation: consumption, verification, scheduling,
and common-factory correlations remain independent constructor obligations.
