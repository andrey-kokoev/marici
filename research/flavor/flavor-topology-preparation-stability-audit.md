# WP145 — topology-preparation stability audit

## Bounded question

Can a normalized linear Euclidean weight on the full positive topology lattice
prepare the accessible topology selected conditionally in WP144, rather than
merely replacing its discrete ambiguity by an ensemble?

## Frozen source grammar

Let

\[
k=\frac{\chi(X)}{24}\in\{1,2,\ldots\},\qquad
P_q(k)=(1-q)q^{k-1},\qquad q=e^{-\lambda}.
\]

This is the normalized law produced by a linear topology action
\(S_\lambda(k)=\lambda(k-1)\) when \(\lambda>0\). The benchmark is frozen at
\(q=1/2\). No claim is made that this toy action is the complete gravitational
topology sum.

The WP140/WP144 readout is retained:

\[
M_{\rm KK}(k)^2=\frac1k,
\qquad E_{\max}=\frac34.
\]

Hence accessibility means \(1/k<9/16\), or exactly \(k\geq2\).

## Exact result

The geometric series is normalized, but it is not a point selector:

\[
P(1)=\frac12,
\qquad P(4)=\frac1{16},
\qquad \mathbb E[k]=2,
\qquad P(k\geq2)=\frac12.
\]

The stable linear action therefore gives its largest weight to \(k=1\), whose
threshold is inaccessible. Its zero-temperature limit selects precisely that
minimal topology. To reverse the ordering and favor increasing \(k\) requires
\(\lambda<0\), equivalently \(q>1\), for which the topology sum diverges.

Thus a normalizable linear topology weight cannot select the accessible
\(k=4\) sector. It produces a genuine source ensemble, but neither a
distinguished topology nor a numerical flavor prediction.

## Typing and descent

- **Admitted state domain:** positive topology classes labelled by
  \(k=\chi/24\), followed by the WP144 flux and modulus matching.
- **Faithful flavor quotient:** `physical16`; the topology label is upstream
  source data and is not inferred from the measured-ten projection.
- **Source-authorized probe family:** the normalized topology weight and the
  threshold predicate inherited from WP140.
- **Contextual partition:** inaccessible \(\{k=1\}\) versus accessible
  \(\{k\geq2\}\); the threshold record does not distinguish members of the
  accessible tail.
- **Descent:** \(k=\chi/24\) is invariant under geometric presentation changes
  within a fixed topology class, and the induced flavor readout descends under
  the full weak-basis groupoid. It does not identify different topology
  classes.
- **Classification:** ensemble producer, neither point selector nor
  presentation rigidifier.
- **Instrument:** none. The threshold predicate remains a formal port until a
  gauge-complete, resolution-typed detector is supplied.

## Smallest exact falsifier

At \(q=1/2\),

\[
P(1)=\frac12>\frac1{16}=P(4).
\]

The sign reversal that would make the weights grow has \(q>1\), so its
geometric sum is nonnormalizable. This falsifies the claim that the declared
stable linear topology action preferentially prepares the accessible
\(k=4\) source.

## Assumptions and falsifiers

The conclusion is conditional on the positive lattice, linear action,
WP144 matching, and WP140 threshold law. It is falsified by an independently
derived normalizable topology action whose unique minimum is an accessible
\(k>1\), provided its preferred value is not inserted as a coefficient and
its pushforward to `physical16` plus physical instrument are explicit. A
convex action can place a minimum at \(k=4\), but without a source derivation
of that minimum it only repeats WP143's encoded-target defect.

## Verification

Run:

```text
python research/flavor/checkers/wp145_topology_preparation_stability.py
```

The dependency-free exact checker records 12/12 passing checks in
`results/wp145_topology_preparation_stability.json`.

## Process calibration

Pre-objective: excitement 8/10, confidence 9/10, expected information gain
9/10. Immediate reason: the full lattice makes stability and selection compete
in a sharp exact test. Confound: the linear topology action is a narrow toy
grammar, not a theorem about all topology dynamics.

Frozen optionality snapshot: one source-admissible linear-weight branch; one
hostile sign-reversed branch; 12 declared exact checks; no physical instrument;
and two threshold record classes.

Post-objective: excitement 8/10, confidence 10/10 in the bounded result,
realized information gain 8/10. The exact delta is: the normalized-ensemble
branch survives; the point-selector interpretation is eliminated; the
sign-reversed large-topology branch is eliminated by nonnormalizability; no
canonical instrument or new `physical16` separation was constructed. The
remaining opening is a source-derived nonlinear topology action, not another
fitted target coefficient.

