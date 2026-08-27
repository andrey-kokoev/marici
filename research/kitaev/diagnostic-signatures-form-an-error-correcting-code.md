# Diagnostic signatures form an error-correcting code

## Bounded question

How does a jointly faithful diagnostic packet behave when some of its record
ports are themselves faulty, and what redundancy is required to detect or
correct those faults?

## Frozen signature code

Let \(\mathcal M\) be a finite family of control-relevant candidate mechanisms,
and let

\[
F=\{t_1,\ldots,t_k\}
\]

be a finite authorized diagnostic family. The joint signature is

\[
\sigma_F(m)
=
(o_{t_1}(m),\ldots,o_{t_k}(m)).
\]

Define the diagnostic code

\[
\mathcal C_F
=
\{\sigma_F(m):m\in\mathcal M\}
\subseteq
O_{t_1}\times\cdots\times O_{t_k}.
\]

This need not be a linear code. It is the finite set of valid record patterns
predicted by the frozen mechanism family.

## Distance hierarchy

Use Hamming distance on joint signatures:

\[
d(c,c')
=
|\{i:c_i\neq c_i'\}|.
\]

Let \(d_{\min}\) be the minimum distance between distinct codewords.

Then:

- clean-state diagnostic faithfulness holds exactly when \(d_{\min}\geq1\);
- every nonzero corruption of at most \(e\) ports is detected when
  \(d_{\min}\geq e+1\);
- every corruption of at most \(e\) ports is uniquely corrected when
  \(d_{\min}\geq2e+1\);
- every pattern of at most \(e\) known erasures is recoverable when
  \(d_{\min}\geq e+1\).

Thus joint faithfulness is only the distance-one gate. A diagnostic interface
that must survive faulty observations needs a stronger separation theorem.

## Proof of detection

Suppose a valid codeword \(c\) is changed in at most \(e\) coordinates. If the
corrupted word equals another valid codeword \(c'\), then

\[
d(c,c')\leq e.
\]

This contradicts \(d_{\min}\geq e+1\). Hence no nonzero corruption within the
budget can masquerade as another admitted mechanism.

## Proof of correction

If one received word \(y\) were within distance \(e\) of two distinct
codewords \(c,c'\), the triangle inequality would give

\[
d(c,c')
\leq
d(c,y)+d(y,c')
\leq2e.
\]

Therefore \(d_{\min}\geq2e+1\) makes the decoding balls disjoint. Nearest-codeword
decoding is then unique inside the declared fault budget.

## One, two, and three copies

For one binary record, use codewords

\[
0,
\qquad
1.
\]

Their distance is one. The record distinguishes the two states when clean, but
one flip converts either valid word into the other and is undetectable.

Two identical ports give

\[
00,
\qquad
11.
\]

Their distance is two. One independent flip yields \(01\) or \(10\), which is
invalid and therefore detected. It cannot be uniquely corrected because the
received word is equally close to both codewords.

Three identical ports give

\[
000,
\qquad
111.
\]

Their distance is three. One independent flip is uniquely corrected by
majority.

This reproduces the classical redundancy hierarchy without treating replica
count as the theorem. Distance is the invariant; repetition is one way to
obtain it.

## Common-mode automorphisms

Suppose a fault acts on every coordinate and maps valid codewords to valid
codewords. For the repetition code, simultaneous bit flip sends

\[
000\longleftrightarrow111.
\]

The received word remains in \(\mathcal C_F\). No validity check detects the
fault, regardless of repetition length.

More generally, a common-mode fault \(g\) is invisible to code-membership tests
when

\[
g(\mathcal C_F)=\mathcal C_F.
\]

It acts as an automorphism or permutation of the diagnostic code. Detecting it
requires a reference that is not transported by the same action. This is the
coding form of the torsor-origin problem.

## Reference rows

Let \(g\) be a nontrivial code automorphism. Add a trusted reference row
\(r(m)\). The extended signature is

\[
\widetilde\sigma(m)=(\sigma_F(m),r(m)).
\]

The common-mode action becomes detectable only if it fails to preserve the
extended codeword:

\[
r(gm)\neq r(m)
\]

for the relevant candidate. A reference duplicated from the same transported
frame does not help. The new row needs an independent origin or causal path.

Thus minimum distance against coordinate faults and rigidity against global
code automorphisms are separate design goals.

## Typed fault metric

Ordinary Hamming distance assumes every port corruption has equal cost and can
occur independently. Real diagnostic packets may require:

- weighted distance for unequal port reliability;
- block distance for shared hardware groups;
- asymmetric distance for one-way faults;
- erasure metrics when missing records are typed;
- and adversarial sets for authorized fault combinations.

For an admitted fault family \(\mathcal E\), exact correction requires disjoint
reachable sets:

\[
\mathcal E(c)\cap\mathcal E(c')=\varnothing
\]

for all distinct \(c,c'\). This is the general invariant behind the Hamming
bound.

## Candidate completeness and anomaly detection

A received word outside \(\mathcal C_F\) falsifies the conjunction of the
candidate model and the declared observation-fault budget. It does not by
itself say whether the mechanism family was incomplete or a port failed.

An unknown mechanism whose signature happens to equal a valid codeword is not
detected. Therefore code membership supplies a residual test, not an open-world
completeness theorem.

The programme must distinguish:

- decoding among admitted mechanisms;
- detecting corrupted diagnostic records;
- detecting violation of the admitted model family;
- and identifying a previously unmodelled mechanism.

Only the first two follow directly from code distance.

## Constructor-sensitive code design

Candidate mechanisms should be quotiented by predictive equivalence before
forming codewords. If two microscopic mechanisms require the same recovery and
have identical future behavior under every admitted constructor, separating
them adds no control value.

Conversely, two mechanisms requiring different recovery actions must have
distinct codewords. If diagnostic faults are admitted, their codewords must be
separated by the distance required by the recovery risk.

The design target is therefore not maximal code size. It is sufficient distance
between action-inequivalent mechanism classes using source-authorized ports.

## Toric-code instance

The ideal syndrome map assigns a binary signature to each Pauli error. Errors
with the same syndrome may differ by stabilizers or logical operators. Syndrome
codewords therefore classify local repair information, not the full logical
state.

Repeated syndrome extraction adds temporal or spatial record coordinates. Its
distance can detect measurement faults only under a typed circuit-level fault
model. A common extraction or calibration fault may map one valid syndrome
history to another and remain invisible.

Logical loop probes add coordinates that separate homology classes. They solve
a different kernel problem from repetition of syndrome bits.

## Optical instance

Several detector channels can encode source alternatives as click patterns.
Minimum distance determines which detector-record faults can be detected or
corrected. A shared threshold or calibration shift may permute valid patterns
and evade membership checks.

Adding another detector in the same common frame can raise coordinate distance
without breaking the common-mode symmetry. An independently calibrated optical
reference serves a different role from another replica.

## Software instance

A distributed event may carry replicated values, checksums, sequence numbers,
and provenance fields. Together they form a typed diagnostic codeword.

Checksums raise distance against some transport corruptions. They do not detect
a producer that consistently emits the wrong value and recomputes the checksum.
Breaking that common-mode action requires an independent source assertion,
recomputation, or authority path.

## DPC: diagnostic distance before confidence

The conjecture is:

> Every fault-tolerant diagnostic claim should state the code of valid joint
> signatures, the admitted fault action, and the minimum separation between
> control-inequivalent mechanisms. Replica count and sample confidence are not
> substitutes for distance, and distance against local corruption is not a
> substitute for an independent reference against common-mode code
> automorphisms.

This explains why some redundancy corrects faults while other redundancy only
repeats a shared mistake.

## Critics

### Diagnostic outputs are continuous

Then replace Hamming balls with neighborhoods under the declared metric or
divergence. Robust identification still requires disjoint reachable sets around
action-inequivalent signatures.

### Observation faults are probabilistic rather than adversarial

Distance gives a worst-case certificate. A probabilistic decoder may perform
better on average, but its guarantee depends on the frozen channel model and
prior.

### Nonlinear codes complicate syndrome decoding

Correct. Linearity is not required for the separation theorem. It is additional
structure that may make encoding and decoding efficient.

### More ports always increase distance

No. A duplicate coordinate can increase some pairwise distances, while a
constant or redundant coordinate may leave the minimum distance unchanged.

### A codeword outside the model proves a new mechanism

No. It proves incompatibility with the joint candidate-and-fault packet. Port
corruption, model error, and a new mechanism remain rival explanations.

## Exact falsifiers

- Clean injectivity used to claim correction of one port error when
  \(d_{\min}<3\).
- Two-copy disagreement detection called one-error correction.
- A common-mode code automorphism claimed detectable by code membership.
- Additional replicas in the same reference frame presented as an independent
  origin.
- A received invalid signature used to identify one new mechanism uniquely.
- Distance computed between microscopic candidates while action-inequivalent
  candidates still collide.
- Hamming distance used when the admitted fault family contains correlated
  block errors that violate the coordinate model.

## Machine-readable distance certificate

```json
{
  "code": "diagnostic_signature_distance",
  "candidate_codewords": ["000", "111"],
  "minimum_distance": 3,
  "clean_faithfulness": true,
  "detectable_coordinate_errors": 2,
  "correctable_coordinate_errors": 1,
  "common_mode_flip_detected": false,
  "independent_reference_required": true,
  "candidate_completeness_proved": false
}
```

## Deutschian explanation

A diagnostic system is reliable when rival mechanisms leave records far enough
apart that admitted damage cannot make one look like another. Distance measures
that margin. Repetition works because it separates valid patterns under local
faults.

But a shared transformation can move the entire valid-pattern system onto
itself. That failure is not overcome by making more copies in the same frame.
It is overcome only by a reference whose history is not carried by the same
transformation.

## Claim boundary

This packet proves the finite code-distance hierarchy for deterministic
diagnostic signatures and arbitrary finite error reachable sets. It does not
derive a physical fault model, validate independence, or prove candidate
completeness.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was a robust extension of joint diagnostic
faithfulness.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Diagnostic signatures form a code; distance governs
local record faults, while an independent source reference is required against
common-mode code automorphisms.
