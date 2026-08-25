# WP147 — topology congruence-selector audit

## Bounded question

Can a source-geometric admissibility constraint select an accessible topology
without encoding that topology as the minimum of an adjustable potential?

## Frozen conditional operation

Let \(k=\chi/24\in\mathbb N_{>0}\). Introduce the exact admissibility
projector

\[
\Pi_m(k)=
\begin{cases}
1,&k\equiv0\pmod m,\\
0,&\text{otherwise}.
\end{cases}
\]

This models the type of divisibility condition that an independently derived
anomaly, index, or tadpole constraint could impose. No such microscopic
derivation is claimed here. The target case \(m=4\) is frozen before the
calculation, and \(m=1\) is the hostile alternative.

Condition the WP145 linear weight \(q^k\), with \(q=1/2\), on the allowed
domain \(k=mj\). Then

\[
P_m(j)=(1-q^m)(q^m)^{j-1}.
\]

## Exact target result

For \(m=4\), the admissible domain is
\(\{4,8,12,\ldots\}\). Every admitted topology is accessible under the WP140
threshold because \(M_{\rm KK}(k)^2=1/k<9/16\). Moreover,

\[
P_4(k=4)=\frac{15}{16},
\qquad
\mathbb E_4[k]=\frac{64}{15}.
\]

At finite source temperature this remains an ensemble, not a point. In the
zero-temperature limit it selects \(k=4\) uniquely. Unlike WP143, the
selection is performed by a domain projector rather than by centering a
potential at four.

## Authority obstruction

The congruence *form* does not derive its modulus. The equally valid-looking
projector \(\Pi_1\) leaves the full positive lattice and selects inaccessible
\(k=1\) in the zero-temperature limit. Thus

\[
\text{projector architecture}\neq\text{authority for }m=4.
\]

If a source anomaly or index theorem independently forces \(m=4\), the
operation is a genuine selector of a proper topology subspace and makes the
threshold response uniformly accessible. Until that theorem exists, it is a
conditional selector whose numerical content resides in an unauthorized
discrete datum.

## Typing

- **Admitted state domain:** positive topology classes, restricted
  conditionally to \(4\mathbb N\).
- **Faithful flavor quotient:** `physical16`, downstream of the WP144 matching.
- **Source-authorized probe family:** the conditional projector, normalized
  topology weights, and WP140 threshold predicate.
- **Contextual partition:** rejected \(k\notin4\mathbb N\) versus admitted
  \(k\in4\mathbb N\); threshold accessibility is constant on the admitted
  domain and therefore does not separate its members.
- **Separation:** no separation of admitted physical points by the threshold
  record.
- **Selection:** proper-subspace selection conditional on a derived modulus;
  point selection only in the zero-temperature limit.
- **Rigidification:** none; the condition is topology invariant rather than
  presentation data.
- **Descent:** \(\chi\), divisibility, and the induced `physical16` packet are
  invariant under geometric presentation and full weak-basis equivalence.
- **Reference port:** not required for mathematical descent.
- **Physical instrument:** absent; uniform formal accessibility is not an
  implemented detector.

## Smallest exact falsifier

Replace \(m=4\) by \(m=1\) without changing the projector grammar. The
zero-temperature minimum becomes \(k=1\), and

\[
M_{\rm KK}(1)=1>\frac34.
\]

Therefore projector structure alone does not explain the accessible numerical
sector.

## Reopening condition

Derive the modulus from a declared UV geometry—for example an independently
specified anomaly polynomial, index integrality condition, or tadpole law—and
show that it is exactly four on the admitted source domain. The derivation must
precede flavor matching and remain stable under allowed source deformations.
An instrument must then distinguish any residual admitted source stories, not
merely confirm threshold accessibility.

## Verification

```text
python research/flavor/checkers/wp147_topology_congruence_selector.py
```

The dependency-free exact checker writes the result JSON and requires 12/12
checks.

## Process calibration

Pre-objective: excitement 8/10, confidence 9/10, expected information gain
8/10. The attraction was a selector acting on admissibility rather than a
fitted energy. The confound was the absence of a microscopic derivation of the
modulus.

Frozen optionality snapshot: target projector \(m=4\), hostile projector
\(m=1\), one finite-temperature ensemble branch, one zero-temperature limit,
12 checks, and no physical instrument.

Post-objective: excitement 8/10, confidence 10/10 in the conditional result,
realized information gain 8/10. One new canonical map—the congruence
projector—was constructed and shown to select a proper uniformly accessible
subspace. Unconditional numerical selection was not promoted: the hostile
modulus transfers the ambiguity to discrete source data. No contradiction was
introduced and no instrument gate was closed.

