# WP165 — finite decoupling-probe uniform no-go

## Bounded question

Can any finite family of fixed-resolution decoupling probes identify the
continuous protector uniformly over an unbounded source-scale domain?

## Theorem

Let a finite physical probe family satisfy

\[
|\chi_j(M)|\leq\frac{C_j}{M^{p_j}},
\qquad C_j>0,
\qquad p_j>0,
\]

and let every detector have fixed positive resolution \(\delta_j>0\). Then
there exists a finite mass \(M_*\) such that for all \(M>M_*\),

\[
|\chi_j(M)|<\delta_j
\]

for every probe \(j\).

Proof: because the family is finite, choose

\[
M_*>
\max_j\left(\frac{C_j}{\delta_j}\right)^{1/p_j}.
\]

Every response then lies below its detector threshold. The detector record is
identical to the zero tangent record of the corresponding discrete protector.
Thus no such finite family is uniformly faithful on an unbounded mass domain.

## Exact bounded witness

Freeze three probes

\[
\chi_1=\frac1{M^2},
\qquad
\chi_2=\frac3{M^4},
\qquad
\chi_3=\frac5{M^6},
\]

all with \(\delta=1/100\). At \(M=10\), the first probe is exactly at
threshold. At \(M=11\), every response is strictly positive but all three are
below threshold. Eleven is the smallest blind integer mass for this packet,
and every larger tested mass remains blind.

## Relation to the protector programme

WP160's return records are nondecoupling but WP161 proves they factor through
holonomy order and cannot distinguish discrete from rational continuous
sources. WP162's tangent complement distinguishes those sources, while
WP163--WP164 show its physical responses decouple. The two probe types
therefore leave complementary but nonclosing gates:

\[
\begin{array}{c|c}
\text{return order}&\text{nondecoupling but source-nonfaithful}\\
\text{tangent susceptibility}&\text{source-separating but nonuniformly detectable}
\end{array}
\]

## Typing

- **Admitted state domain:** unbounded positive continuous-protector mass with
  bounded response coefficients.
- **Faithful flavor quotient:** `physical16`; mass dilation leaves the flavor
  selector unchanged.
- **Source-authorized probe family:** any declared finite family obeying the
  decoupling bounds.
- **Contextual partition:** beyond the blind mass, continuous and corresponding
  discrete protectors share the detector-zero class.
- **Separation:** algebraic at every finite mass; not uniform after detector
  thresholding.
- **Selection:** none.
- **Rigidification:** none.
- **Descent:** the bound is expressed in physical mass and response data;
  flavor descent remains full weak-basis invariant.
- **Reference port:** every tangent probe remains a new relational experiment.
- **Physical instrument:** any fixed finite positive-threshold family is
  insufficient uniformly on this domain.

## Claim boundary

The theorem does not cover a genuinely nondecoupling complementary observable,
an infinite adaptive measurement with unbounded resources, or a source domain
with an independently established upper mass bound. Each would change an
assumption and requires its own instrument typing.

## Smallest exact falsifier

For the frozen packet, \(M=11\) yields three nonzero formal responses, all
below \(1/100\). This is the smallest integer witness against uniform detector
faithfulness.

## Reopening condition

Any progressive successor must supply at least one of:

1. an independently source-selected compact mass domain;
2. a complementary nondecoupling observable that does not factor through one
   holonomy order;
3. a physically finite instrument with a proven uniform response margin;
4. an adaptive resource law whose cost and stopping condition are physically
   authorized.

Absent one of these, further finite decoupling ports cannot close the source
kernel.

## Verification

```text
python research/flavor/checkers/wp165_finite_decoupling_probe_no_go.py
```

The dependency-free exact checker writes the JSON result and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 8/10, confidence 10/10, expected information gain
9/10. The aim was to replace repeated examples with a theorem. The confound
was exclusion of nondecoupling complementary observables and bounded domains.

Frozen optionality snapshot: one finite three-probe witness, one unbounded mass
domain, one exact blind threshold, 12 checks, and three explicit reopening
classes plus adaptive measurement.

Post-objective: excitement 8/10, confidence 10/10, realized information gain
9/10. The scale obstruction was promoted from benchmark behavior to a finite-
family no-go theorem. All finite decoupling branches on the unbounded domain
were eliminated uniformly. Nondecoupling complements, compact domains, and
authorized adaptive resources remain open; no sufficient instrument was
constructed.

