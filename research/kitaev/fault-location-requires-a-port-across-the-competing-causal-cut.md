# Fault location requires a port across the competing causal cut

## Bounded question

Can agreement and disagreement among record replicas identify whether a fault
occurred before or after fanout, or does localization require an additional
intervention or observation port?

## Two indistinguishable realizations

Let the source record be a bit \(r\), and let \(Z\) be a Bernoulli fault with
parameter \(q\).

In the upstream-fault realization,

\[
\tilde r=r\mathbin{\mathsf{xor}}Z,
\qquad
(Y_1,Y_2)=(\tilde r,\tilde r).
\]

In the correlated downstream realization, first copy the correct bit and then
let one hidden fault variable act on both branches:

\[
(r,r)
\longmapsto
(r\mathbin{\mathsf{xor}}Z,
 r\mathbin{\mathsf{xor}}Z).
\]

For every source distribution and every \(q\), the two realizations induce the
same joint law on \((Y_1,Y_2)\). No passive output test can distinguish them.

Thus perfect replica agreement identifies a shared fault history, not the
physical location of the shared mechanism.

## Latent relocation principle

Consider an unobserved internal carrier \(M\) separating two portions of a
pipeline. If a latent variable can be absorbed into the channel before \(M\) or
into a correlated channel after \(M\) without changing the external process,
then its location is not identifiable from the external ports.

This is realization equivalence relative to the frozen tester packet. The two
internal causal stories may be physically different while every admitted
input-output experiment agrees.

The claim generalizes beyond bits. If an upstream channel \(K) is followed by
copying, then the same external law is obtained by copying first and applying a
downstream channel that uses one shared random seed to generate the same common
output. Moving the hidden seed across an unobserved cut changes the realization,
not the exposed process.

## Cut-port theorem

To distinguish two candidate fault loci separated by an internal cut, the
experiment packet must contain at least one operation whose authority crosses
that cut. The operation may be:

- an observation of the intermediate carrier;
- replacement of the upstream output by a trusted test value;
- bypass of one candidate mechanism;
- independent excitation on one side of the cut;
- or a source-derived witness that is transported across the cut and checked
  afterward.

Without such a port, the cut is hidden and latent fault mechanisms can be
relocated across it whenever the surrounding channel factorization permits.

This is a necessary condition for localization. It is not sufficient unless
the added port is itself calibrated and the competing models make distinct
predictions for it.

## Minimal intermediate observation

Add a trusted observation \(M\) immediately after the proposed fanout source
and before the proposed downstream common channel.

For the upstream-fault model,

\[
M=r\mathbin{\mathsf{xor}}Z.
\]

For the downstream-fault model,

\[
M=r.
\]

When the source bit \(r\) is known, the joint packet \((M,Y_1,Y_2)\) separates
the two models whenever \(0<q<1\). The first differing conditional is now at
the newly exposed cut.

The probe does not work by adding another terminal replica. It works by
intercepting the carrier between the competing causal mechanisms.

## Minimal replacement intervention

Suppose the intermediate carrier cannot be observed but can be replaced by a
trusted value \(m\). Under that intervention, an upstream fault is bypassed,
whereas a downstream common channel remains active.

If the output error persists after replacement, the upstream-only model is
falsified. If the error disappears, the downstream-only model is falsified,
subject to the intervention not altering the downstream mechanism.

This last qualification is essential. A replacement that also resets a shared
power rail, clock, seed, or environment does not isolate the cut claimed by the
causal diagram.

## Why branch-local interventions may be insufficient

Changing only one terminal branch after all shared mechanisms have acted can
test that branch's local transport. It need not distinguish an upstream fault
from a downstream shared fault, because both have already written the same
value into the other branch.

Localization requires an intervention between the competing mechanisms, not
merely anywhere in the graph. The relevant ordering is the partial order of
causal cuts.

## Definition of the first failed constructor

The first failed constructor is relative to three frozen objects:

1. a directed acyclic factorization of the admitted process;
2. a source-to-output execution path;
3. an intervention and observation packet that distinguishes candidate edges.

Along one path, a failed constructor is first when no earlier constructor on
that path fails under the same typed execution. Across branching paths there
may be several incomparable first failures.

If hidden realizations can move the defect across an unobserved cut, the first
failure is not identifiable. Reporting one location as first then exceeds the
evidence.

The correct output is a minimal unresolved fault region: the smallest causal
subgraph bounded by trusted ports inside which the defect can still be
relocated without changing admitted observations.

## Diagnostic resolution order

Adding ports refines fault regions monotonically. A new trusted cut can split
one unresolved region into smaller regions, but it cannot justify merging two
previously distinguished regions unless the tester packet or trust assumptions
are weakened.

This gives a structural meaning to diagnostic resolution:

- terminal scalar tests localize only to the full hidden realization;
- replica comparison separates some independent branch faults from shared
  faults;
- intermediate cut ports separate upstream from downstream shared faults;
- component-level interventions may isolate one constructor;
- physical teardown may distinguish realizations still operationally
  equivalent under all executable tests.

## Toric-code instance

Two decoders receiving the same wrong syndrome do not determine whether the
error arose in quantum extraction, shared classical storage, fanout, or a
correlated downstream controller fault.

Repeated extraction with independently prepared ancillas introduces a new
source interaction and can separate some extraction faults from later storage
faults. Reading the ancilla before shared storage exposes a different cut.
Neither test localizes quantum data faults unless the syndrome model predicts
their effect and the extraction circuit is trusted to the declared level.

## Optical instance

Several displays driven by one detector may agree because the optical event was
correctly detected or because one detector error was copied. Duplicating the
display does not cross the detector-electronics cut.

An independently coupled detector, a calibrated optical tap, or an accessible
intermediate pulse can cross that cut. Each changes the constructor packet and
tests a different causal factorization.

## Software instance

Several consumers agreeing on one event cannot locate an error among event
production, serialization, shared broker storage, or deterministic fanout.

A trace identifier alone adds correlation, not localization. A trusted capture
before serialization, broker-side checksum, replay from a known fixture, or
consumer-side independent recomputation crosses different cuts. Diagnostic
claims must state which cut the added port actually separates.

## DPC: fault-region rather than fault-point inference

The conjecture is:

> A programme should report a fault point only when admitted interventions or
> observations cross every causal cut across which the fault could otherwise be
> relocated. Without those ports, the explanatory object is a minimal unresolved
> fault region, not a preferred hidden realization.

This is a stronger Popperian demand than fitting the output distribution. The
proposed explanation must expose a test that would fail if the mechanism were
moved to another admissible location.

## Critics

### The physical layout already fixes the fault location

It fixes candidate components, not which component generated the observed
error. Schematics supply a causal hypothesis. Localization still requires
typed observations, interventions, or independently justified mechanism bounds.

### Correlation strength should reveal common cause location

Correlation can distinguish independent from shared histories under a frozen
model. It cannot generally distinguish two shared histories on opposite sides
of an unobserved cut.

### More replicas eventually identify the source

More terminal replicas estimate the exposed joint law more accurately. They do
not break an exact realization equivalence. A new causal port, not merely more
samples, is required.

### Intermediate observation may disturb the system

Correct. Then the observed and unobserved processes are different constructor
words. A nondemolition or disturbance-bound theorem is needed before the result
transfers back.

### Bayesian priors can prefer one locus

They can rank hidden explanations, but preference is not identifiability. The
claim must remain prior-relative unless a discriminating test is supplied.

## Exact falsifiers

- An upstream common fault localized solely from terminal replica agreement.
- A correlated downstream channel excluded without a port across the relevant
  cut.
- More terminal samples claimed to break exact realization equivalence.
- A branch-local intervention presented as isolating a shared upstream cut.
- A replacement intervention that also resets the allegedly downstream fault
  mechanism.
- One total order of failures imposed on causally incomparable branches.
- An internal trace label treated as a trusted intermediate observation without
  independent integrity authority.

## Machine-readable localization boundary

```json
{
  "code": "fault_location_not_identifiable",
  "candidate_region": ["upstream", "fanout", "shared_downstream"],
  "external_process_equal": true,
  "separating_cut_port": null,
  "terminal_replica_count": 2,
  "more_terminal_samples_sufficient": false,
  "required_action": "observe replace or bypass an intermediate carrier",
  "report_as": "minimal unresolved fault region"
}
```

## Deutschian explanation

Agreement reveals that replicas share a history. It does not reveal where that
history was written. A hidden random cause can be moved across any unobserved
cut that preserves the external process.

An explanatory localization therefore needs a way to interrupt the imitation:
observe the carrier between the rival mechanisms, replace it, or excite one
side independently. The new port matters because the rival stories no longer
predict the same thing there.

## Claim boundary

This packet proves a finite observational non-identifiability witness and gives
a necessary cut-port condition for fault localization. It does not provide a
complete causal-identifiability theorem for arbitrary cyclic, quantum, or
continuous systems.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was to prevent causal location from being
inferred from correlation alone.

Post-objective ratings are excitement 10/10, confidence 9.5/10, and realized
information gain 10/10. The exact explanatory object is now the smallest fault
region bounded by trusted ports; a point location requires an experiment across
the competing causal cut.
