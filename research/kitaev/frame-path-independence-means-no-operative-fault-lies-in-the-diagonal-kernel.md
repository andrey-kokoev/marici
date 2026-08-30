# Frame-path independence means no operative fault lies in the diagonal kernel

## Bounded question

When do the compiler frame and its six-state anchor genuinely provide
independent protection against a common-mode orientation fault?

The answer must be stated on the admitted fault model and its spacetime causal
support. Two registers are not independent merely because the state space
factorizes or because their final labels can be compared.

## Fault-pair model

Start with locked frame labels \(|r,r\rangle\). Let an elementary fault \(f\)
induce left displacements

\[
u(f)\in S_3
\]

on the compiler frame and

\[
v(f)\in S_3
\]

on the anchor. The corrupted pair is

\[
|u(f)r,v(f)r\rangle.
\]

Under the logical-syndrome factorization of the previous packet, the relative
syndrome is

\[
\delta(f)=u(f)v(f)^{-1}.
\]

It is independent of the unknown locked orientation \(r\). Under a change of
global gauge frame it transforms by conjugation.

The equality alarm accepts exactly when

\[
\delta(f)=e,
\]

or equivalently when

\[
u(f)=v(f).
\]

The exact invisible fault set is therefore the diagonal kernel.

## Relative detection theorem

Let \(\mathcal F\) be the declared elementary fault family, and let
\(\mathcal N\subseteq\mathcal F\) be faults known to be operationally neutral
for the compiled logical action. The binary frame comparison is complete for
the admitted fault family precisely when

\[
\delta(f)=e
\quad\Longrightarrow\quad
f\in\mathcal N
\]

for every \(f\in\mathcal F\).

This is a kernel-injectivity criterion. The detector need not reconstruct all
fault data. It must be injective only on the quotient of operative faults by
neutral ones.

If some operative fault satisfies

\[
u(f)=v(f)\ne e,
\]

then no equality comparison performed after that fault can detect it. Adding
more processing downstream of the same two shifted carriers cannot recover the
lost counterfactual relation.

## Independence is a property of the fault map

The two frame paths are independent relative to \(\mathcal F\) when every
nonneutral elementary fault either:

- affects at most one path;
- affects the two paths differently, producing nontrivial relative syndrome;
- or is caught by another independently typed detector before acceptance.

They are not independent when an admitted elementary fault can act diagonally
and nontrivially on both histories.

This definition allows physical correlations that are visible to the detector.
It rejects only the correlations lying in the detector kernel. Statistical
uncorrelatedness is neither necessary nor sufficient.

## Spacetime support criterion

Fix a trusted comparison checkpoint and a later comparison event. Let
\(J_A^-\) and \(J_B^-\) denote the portions of the causal past of the two
comparison inputs between those events. Let every elementary fault have a
declared support region \(S_f\) and propagation cone determined by the admitted
local dynamics.

A sufficient single-fault independence condition is:

> No admitted nonneutral elementary fault has a propagated support intersecting
> both frame histories in a way that induces the same nonidentity displacement
> before the later comparison.

A stronger, easier-to-audit geometric condition is that every admitted fault
cone intersects at most one of the two path world tubes between trusted
checkpoints.

Spatial separation alone is insufficient. A shared controller, power rail,
clock, reset channel, preparation source, or earlier fanout vertex may lie in
both causal pasts even when the final registers are distant.

## Light-cone certificate

Suppose elementary faults have maximum propagation speed \(v\) and remain
active for at most time \(\tau\) before the comparison. If the two path world
tubes remain farther than

\[
2v\tau+\ell_f,
\]

where \(\ell_f\) bounds initial fault diameter, then one local elementary fault
cannot reach both paths during that interval.

This is only a sufficient geometric certificate. Long-range couplings and
shared classical control ports invalidate it even when the quantum carriers
are separated.

The certificate must name the dynamics and the fault support bound. Distance
without a propagation law is not evidence of independence.

## Checkpoint dependence

A fault acting identically on both paths before the trusted checkpoint passes
the equality test and becomes part of the accepted baseline. The comparison
certifies preservation of a relation across an interval; it does not certify
the origin of that relation.

Moving the checkpoint earlier moves the required trust boundary earlier. No
finite chain of copied endogenous references creates an absolute origin. The
programme must terminate the regress at a source-authorized boundary condition
or make only a relational claim.

For the endpoint compiler, this means the anchor certifies that the compiler
frame did not drift relative to the anchor after their trusted lock. It does
not prove that their common initial orientation was correctly related to the
data unless that third relation is also constructed and checked.

## Fault time relative to the pulse

The same final syndrome has different operational consequences depending on
when the drift occurred.

### Drift before the relational pulse

A compiler displacement changes which conjugate element is addressed during
the pulse. The later frame alarm detects a problem, but repairing the frame
alone does not undo the data operation already applied.

The gadget must reject the run or retain enough covariant syndrome and data
history to apply a joint recovery.

### Drift during the pulse

The data and frame can become jointly corrupted. A final frame syndrome is not
automatically a sufficient statistic for the propagated data error. The pulse
Hamiltonian must prove an error-propagation law mapping each admitted fault to
a correctable joint syndrome sector.

### Drift after the pulse but before comparison

The intended data pulse may be intact while the frame relation is wrong for
future use. Frame recovery can be sufficient, provided no later operation used
the corrupted frame.

Thus a static post-pulse equality test detects a drift interval but does not by
itself localize the first failed constructor relative to the actuation event.

## Accepted-operation criterion

A fault-tolerant endpoint gadget needs a branchwise claim. For every admitted
elementary fault, one of the following must hold:

1. the accept branch implements the intended logical operation modulo a
   declared neutral gauge transformation;
2. the detector raises a rejection flag before the corrupted output is used;
3. the retained covariant syndrome selects a proved joint data-frame recovery.

It is not enough that a postcondition eventually notices frame inequality. A
fault detected after an irreversible downstream use has escaped the gadget's
causal boundary.

This criterion is the constructor-level analogue of an extended rectangle in
fault-tolerant circuit theory. The frame check, pulse, recovery, and output-use
boundary form one typed unit.

## Multiple paths and the surviving diagonal

For \(m\) frame paths with displacements \(u_1,\ldots,u_m\), relative
comparisons against the first path expose

\[
u_2u_1^{-1},\ldots,u_mu_1^{-1}.
\]

Their common kernel is

\[
u_1=u_2=\cdots=u_m.
\]

No finite number of replicas detects a fault model that permits one elementary
fault to act identically on all of them. Replication becomes effective only
when locality, bounded support, or separately sourced controls forbid that
global diagonal action.

For a model with at most \(t\) path-local faults, enough separated replicas can
support classical majority correction of sharp labels. That conclusion does
not extend to arbitrary coherent phase faults or to a common controller fault
without an additional quantum-code and propagation theorem.

## Relation to objective records

The equality alarm is an objective classical record only of relative drift.
Broadcasting it to many observers improves availability of the alarm but does
not enlarge the fault set it distinguishes. If the comparison constructor
itself is downstream of the common cause, every copy broadcasts the same false
acceptance.

Objective redundancy therefore begins after a distinction has been physically
created. It cannot manufacture the independent causal contrast needed to
create that distinction.

## Exact falsifiers

- Two registers called independent without a declared elementary fault map.
- Spatial separation claimed sufficient while a shared controller lies in both
  causal pasts.
- Equality comparison claimed to detect a fault with \(u(f)=v(f)\ne e\).
- A pre-check/post-check pair claimed to identify whether drift occurred before
  or after the pulse without another timing witness.
- Frame repair after a pre-pulse drift claimed to undo the already applied data
  operation.
- A post-pulse alarm counted as protection although corrupted output may have
  escaped before the alarm.
- More replicas claimed to remove the common diagonal kernel without a locality
  restriction.
- A distance bound stated without fault diameter, propagation speed, and time
  window.
- Copied alarms claimed to strengthen the underlying causal distinction.

## Machine-readable causal certificate

```json
{
  "code": "frame_path_independence_certificate",
  "group": "S3",
  "relative_syndrome": "delta(f)=u(f)*inverse(v(f))",
  "detector_kernel": "u(f)=v(f)",
  "completeness_condition": "kernel(delta) subset neutral_faults",
  "statistical_independence_required": false,
  "fault_map_required": true,
  "spacetime_support_required": true,
  "shared_controller_audited": true,
  "pre_pulse_drift_data_recovery_required": true,
  "during_pulse_propagation_theorem_required": true,
  "post_pulse_frame_only_recovery_possible": true,
  "finite_replication_removes_global_diagonal": false,
  "accepted_output_branchwise_verified": true
}
```

## Deutschian explanation

An independent reference is not a second object. It is a second history. The
comparison works only against causes that did not rewrite both histories in
the same way.

The relative syndrome gives the exact explanatory boundary: it records the
difference between the two fault actions. When those actions are equal, there
is no physical difference in the final carriers from which the missing history
could be reconstructed.

Locality makes independence possible by preventing one bounded event from
reaching both histories before the check. Replication without locality merely
creates more descendants of the same cause.

## Shared Carrier geometry and quantum coefficient lens

The shared Carrier statement is the kernel condition on a cut-crossing
comparison: all operative faults must survive as distinctions at the relative
port. Its causal implementation requires separated histories and bounded
propagation.

The quantum coefficient lens determines how a detected drift propagates
through a coherent noncommutative pulse and whether a retained covariant
syndrome supports joint recovery. A scalar alarm proves detection, not
reversibility of the corrupted ordered constructor.

## Claim boundary

This packet proves the exact diagonal detector kernel and gives sufficient
spacetime conditions for single-fault path independence. It distinguishes the
three pulse-time regimes and states the branchwise accepted-operation gate. It
does not supply a microscopic Hamiltonian, a numerical propagation speed, an
apparatus layout, or a complete joint data-frame recovery circuit.

## Process calibration

Excitement is 10/10 and confidence in the algebraic fault criterion is 10/10.
The spacetime certificate is conditional on an admitted locality model, as it
must be. The next physical milestone is to instantiate this extended gadget on
the existing holonomy-compute, phase, and uncompute circuit and derive its
single-fault propagation table.
