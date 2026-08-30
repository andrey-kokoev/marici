# Semantic saturation does not imply quantum joint measurability

## Bounded question

When several quantum tests all factor through the same predictive state, what
additional theorem is required to compile them into one physical record?

## Frozen qubit effects

A binary qubit effect with unbiased outcomes has the form

\[
A_+=\frac12(I+a\cdot\sigma),
\qquad
A_-=I-A_+,
\]

where \(a\in\mathbb R^3\) and \(\|a\|\leq1\). A second binary effect is

\[
B_+=\frac12(I+b\cdot\sigma),
\qquad
B_-=I-B_+.
\]

Both effects are semantically saturated relative to the full density operator:
their probabilities are functions of the same predictive state \(\rho\).

Joint measurability asks for a stronger object: one four-outcome POVM

\[
\{G_{jk}:j,k\in\{+,-\}\}
\]

with marginals

\[
\sum_kG_{jk}=A_j,
\qquad
\sum_jG_{jk}=B_k.
\]

This is a constructor existence problem, not a semantic factorization problem.

## Binary joint-effect reduction

Two binary POVMs are jointly measurable exactly when there exists one effect
\(C=G_{++}\) satisfying

\[
0\leq C\leq A_+,
\qquad
C\leq B_+,
\qquad
A_++B_+-I\leq C.
\]

Given \(C\), the joint effects are forced:

\[
G_{++}=C,
\]

\[
G_{+-}=A_+-C,
\]

\[
G_{-+}=B_+-C,
\]

\[
G_{--}=I-A_+-B_++C.
\]

The four inequalities are precisely positivity of these four operators.

This reduction gives the smallest finite incompatibility certificate: prove
that the four operator intervals have empty intersection.

## Exact unbiased-qubit criterion

For the unbiased effects above, joint measurability is equivalent to

\[
\|a+b\|+\|a-b\|\leq2.
\]

The criterion is invariant under common unitary rotations of the Bloch vectors.
It depends on both sharpness and relative angle.

The theorem can be obtained by writing the candidate joint effect in Bloch form
and reducing the four positivity inequalities to intersection of Euclidean
balls. The resulting intersection is nonempty exactly under the displayed
inequality.

This criterion is part of the quantum coefficient lens. The shared Carrier
statement “both tests descend from the same state” does not contain it.

## Orthogonal Pauli threshold

Take noisy \(X\) and \(Z\) measurements with common sharpness \(\eta\):

\[
a=\eta\hat x,
\qquad
b=\eta\hat z.
\]

Then

\[
\|a+b\|=\|a-b\|=\eta\sqrt2,
\]

so joint measurability holds exactly when

\[
\eta\leq\frac1{\sqrt2}.
\]

At and below this threshold, one explicit joint POVM is

\[
G_{jk}
=
\frac14
\left[
I+j\eta\sigma_x+k\eta\sigma_z
\right],
\qquad
j,k\in\{+1,-1\}.
\]

Its positivity is equivalent to

\[
\eta\sqrt2\leq1,
\]

and its marginals are the desired noisy Pauli effects.

For sharp \(X\) and \(Z\), \(\eta=1\), the criterion fails maximally:

\[
2\sqrt2>2.
\]

Both tests are perfectly meaningful functions of \(\rho\), but no single-copy
joint POVM has those sharp marginals.

## Four notions of joint availability

The following must remain distinct.

### Semantic joint availability

All desired probabilities are functions of one predictive state or quotient.

### Single-copy joint measurability

One instrument produces a joint record whose marginals reproduce every desired
effect on the same input copy.

### Multi-copy estimability

Repeated preparations permit different incompatible measurements on different
copies, allowing estimation of all expectation values.

### Sequential accessibility

Measurements are performed in an order on one copy, with later statistics
computed on the disturbed post-measurement state.

Only the second supplies one joint record with the original marginals. The
third supplies ensemble reconstruction. The fourth supplies an ordered process
whose statistics generally depend on disturbance.

## Sequential disturbance witness

Perform a sharp Lüders \(X\) measurement and discard its outcome before a sharp
\(Z\) measurement. The intermediate channel is

\[
\Delta_X(\rho)
=
P_{X+}\rho P_{X+}+P_{X-}\rho P_{X-}.
\]

For every input, the post-channel Bloch vector retains only its \(x\)
component. Hence the later \(Z\) expectation is zero, not the original
\(\operatorname{Tr}(\rho\sigma_z)\) in general.

Reversing the order preserves the sharp \(Z\) marginal and disturbs the later
\(X\) marginal instead. Sequential records therefore do not solve sharp joint
measurement by mere ordering.

They define a different ordered tester.

## Multiple copies do not create per-copy values

With many identically prepared copies, measure \(X\) on one subensemble and
\(Z\) on another. Both expectation values can be estimated arbitrarily well.

This does not establish that each copy carried a joint pair of sharp values or
that one instrument recorded such a pair. The ensemble protocol estimates two
effect values from two context families.

The distinction is the same as score-tower faithfulness versus one-shot
instrument accessibility: a jointly faithful family of experiments need not be
one jointly executable experiment.

## Noise as a compatibility constructor

Reducing \(\eta\) adds classical or quantum noise and moves the effects inward
in the Bloch ball. At \(\eta=1/\sqrt2\), the compatibility obstruction first
disappears.

This is not cost-free recovery of the sharp measurements. The joint apparatus
returns degraded marginals. A complete report must retain:

- the sharpness parameter;
- the joint POVM;
- the information loss relative to the original tests;
- and whether the noise mechanism is source-authorized.

Fitting noise after demanding compatibility is an interface enlargement, not a
proof that the sharp effects were jointly measurable.

## Predictive quotient versus instrument algebra

Let \(R\) be the predictive equivalence induced by a complete state tester
family. Every saturated effect is constant on \(R\). Joint measurability asks
whether selected effects lie in the marginal image of one positive normalized
instrument.

Thus the architecture has two maps:

\[
\text{effects}
\longrightarrow
\text{functions on predictive classes},
\]

and

\[
\text{joint instruments}
\longrightarrow
\text{compatible effect tuples}.
\]

The first is semantic descent. The second is physical marginalization. Their
images need not coincide.

## Toric-code warning

Commuting stabilizer and logical parity probes can be jointly measured when an
authorized stabilizer circuit exists. Anticommuting logical \(X\)- and
\(Z\)-type loops cannot be assigned one sharp joint projective readout on a
single code copy.

Their anticommutation is exactly the quantum coefficient-lens obstruction. The
Carrier geometry supplies intersecting noncontractible cycles; the Pauli
intersection pairing determines compatibility.

A statement that “two loop coordinates classify the logical packet” must
therefore specify whether the coordinates are:

- commuting syndrome-like labels;
- alternative conjugate probes on separate copies;
- or marginals of an explicitly unsharp joint instrument.

Classification by counterfactual tests is not automatically one-shot readout.

## Polarizer warning

Different polarization analyzer settings can reconstruct a Stokes vector over
repeated preparations. They are not simultaneously sharp values recorded from
one photon. Intermediate polarizers also disturb the state and define ordered
tests rather than passive joint queries.

The optical Carrier geometry and qubit effect algebra meet here exactly: route
contexts generate informative tests, while joint measurability determines
which can coexist in one record.

## Software contrast

Pure functions of a stored predictive state are ordinarily jointly computable,
so semantic saturation often compiles directly into one response object.

The analogy breaks when queries have side effects, consume tokens, race with
updates, depend on distributed snapshots, or enforce privacy views. Then joint
availability again requires a transaction or snapshot constructor, not merely
two individually defined endpoints.

## DPC: saturated-test compiler

The conjecture is:

> Semantic saturation identifies every admitted question determined by the
> predictive state. Physical joint availability requires an independently
> derived instrument whose positive marginals realize the selected questions.
> In quantum sectors, incompatibility is a genuine coefficient-lens obstruction,
> not missing Carrier information.

The unbiased binary-qubit criterion proves the smallest nontrivial case. Larger
effect families require semidefinite feasibility or structural commutation
theorems.

## Critics

### Joint measurability is not the only implementation notion

Correct. Nondemolition measurement, repeatability, locality, fault tolerance,
and detector efficiency are stronger requirements.

### Unsharp joint measurement may be enough operationally

Correct. Then the degraded effects and sharpness threshold are the declared
target. They must not be presented as the original sharp probes.

### Tomography provides all desired numbers

On an ensemble, yes. It does not provide one joint single-copy record or erase
measurement disturbance.

### Commutativity is not necessary for general unsharp compatibility

Correct. The exact Bloch criterion, not a simplistic commutator test, decides
the binary unbiased qubit case.

## Machine-readable obstruction

```json
{
  "code": "saturated_effects_not_jointly_measurable",
  "effects": ["A", "B"],
  "semantic_saturation": true,
  "bloch_vectors": ["a", "b"],
  "compatibility_lhs": "norm(a+b)+norm(a-b)",
  "compatibility_bound": 2,
  "single_copy_joint_instrument": false,
  "multi_copy_estimable": true,
  "sequential_disturbance": "typed residual",
  "minimum_noise_threshold": "eta <= 1/sqrt(2)"
}
```

## Exact falsifiers

- Saturated effects presented as jointly measurable without a positive joint
  POVM.
- Sharp orthogonal Pauli effects claimed compatible despite
  \(2\sqrt2>2\).
- A proposed joint POVM with a negative eigenvalue.
- Sequential measurement marginals compared to original-state marginals after
  ignoring disturbance.
- Multi-copy tomography presented as one-copy joint recording.
- Added noise omitted from the reported effect definitions.
- Anticommuting logical loops presented as simultaneous sharp coordinates on
  one code copy.
- A software-style pure postprocessing assumption imported into an incompatible
  quantum instrument packet.

## Deutschian explanation

The predictive state contains enough information to answer many alternative
questions, but a physical record is produced by one positive instrument. The
instrument's marginals must coexist inside a single normalization constraint.
Quantum geometry can forbid that coexistence even when every question is
individually well defined.

Noise restores compatibility by moving the effects away from the sharp
boundary, not by revealing pre-existing joint sharp values. The threshold
identifies exactly how much precision must be surrendered for one record to
exist.

## Claim boundary

This packet proves and applies the exact compatibility criterion for two
unbiased binary qubit effects. It does not classify arbitrary POVM families or
compile a laboratory measurement circuit.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The target was the smallest exact instrument-compiler obstruction after
semantic saturation.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Joint measurability supplies the missing quantum gate. Orthogonal Pauli
effects require sharpness at most \(1/\sqrt2\); ensemble tomography and
sequential access remain distinct from a single-copy joint record.
