# The resource profile is a shadow of an enriched constructor category

**Owner:** marici.Kitaev  
**Status:** bounded criticism and refinement  
**Target:** resource-indexed distinguishability as the invariant of protection

## 1. The profile is not complete

The family

\[
R\longmapsto d_R(f,g)
\]

records the best distinguishing advantage under each resource budget.

It does not determine the constructor theory that generated those testers.

Two theories can have identical pairwise distinguishability profiles for selected states while differing in:

- coherent logical transport;
- nondemolition measurement;
- catalysis;
- resource recovery;
- reset;
- amortized many-copy behavior;
- fault propagation;
- authority succession;
- composability with downstream tasks.

Therefore the resource profile is a valuable observable of the constructor theory, not a complete representation of it.

## 2. Minimal distinction-versus-construction hostile

A destructive Wilson-loop measurement can distinguish two eigenstates at some cost \(R\).

That does not imply a constructor of comparable cost that:

- localizes the full logical qubit;
- preserves superpositions;
- retains the conjugate loop algebra;
- returns the Carrier to the code space;
- supplies a reusable output interface.

Thus a low distinguishing threshold does not imply a low compilation threshold.

The reverse lower bound remains valid: a faithful compiler plus cheap output tester gives a distinguisher. But no converse follows without an instrument or reconstruction theorem.

## 3. Catalytic hostile

Suppose no cheap constructor maps \(f\) to \(g\) in isolation.

There may exist a catalyst \(c\) and a cheap constructor

\[
f\otimes c\longrightarrow g\otimes c
\]

that returns \(c\) unchanged.

If the resource profile treats \(c\) as unavailable, the threshold is high. If the source theory admits \(c\), the operational threshold can collapse without consuming it.

A resource price attached only to the tested morphism misses catalytic availability and return conditions.

The catalyst must be represented as a typed port with an exact or approximate return law.

## 4. Amortization hostile

A one-copy threshold can be large while an \(n\)-copy joint strategy has sublinear total cost.

Conversely, a cheap one-copy destructive test may not compose into a coherent many-copy interface.

Define an amortized rate only when the limit exists and the tensor-power constructors are source-authorized:

\[
R^{\mathrm{am}}_\delta
=
\liminf_{n\to\infty}
\frac{1}{n}
R_{\delta_n}(f^{\otimes n},g^{\otimes n}).
\]

This rate is a different invariant from the one-shot threshold.

SCC must not infer either from the other.

## 5. Resource-enriched constructor category

The primary object should be a constructor category \(\mathcal K\) whose hom-objects record attainable resource grades.

For objects \(X,Y\), let

\[
\mathcal K(X,Y)_R
\]

be the constructors from \(X\) to \(Y\) realizable within resource budget \(R\).

Composition is typed by a resource-combination law:

\[
\mathcal K(Y,Z)_S
\times
\mathcal K(X,Y)_R
\longrightarrow
\mathcal K(X,Z)_{S\odot R}.
\]

Tensoring, conditioning, reset, catalysis, and authority transport require their own grade laws.

The tester profiles \(d_R\) are obtained by applying outcome functors to selected hom-objects.

Thus the category generates the profile, not conversely.

## 6. Protection as absence of cheap morphisms

For a declared task \(\tau:X\to Y\), define its attainable resource set

\[
\operatorname{Cost}(\tau)
=
\{R:\mathcal K(X,Y)_R	ext{ contains an implementation of }\tau\}.
\]

Topological protection is task-relative:

- discrimination protection;
- destructive-readout protection;
- nondemolition-readout protection;
- coherent-localization protection;
- logical-gate protection;
- reset/recovery protection.

Each task has a different attainable set or Pareto frontier.

There is no single protection number unless source theory supplies a scalarization and proves the tasks equivalent.

## 7. Enriched top coherencer

The source-to-behavior distributive law should be enriched over the resource object.

It must send a source constructor of grade \(R\) to behavior of a grade related by a declared distortion map

\[
\phi:R\mapsto R'.
\]

Compatibility requires:

- identity has the declared neutral grade;
- substitution respects \(\odot\);
- tensoring respects the parallel grade law;
- catalysts are returned in the declared equivalence;
- reset cost is preserved;
- lax residual and resource distortion compose jointly.

A behaviorally exact but resource-unbounded \(\lambda\) is not an operational compiler.

## 8. Constructor equivalence, not profile equivalence

Two implementations are constructor-equivalent only if they agree on:

- typed input and output objects;
- behavior in every admitted context;
- resource grading;
- composition and tensor laws;
- fault and waste semantics;
- authority succession;
- catalytic ports and return;
- reset and reuse.

Equality of scalar outputs or even equality of all selected \(d_R\) profiles is weaker.

This restates the earlier scalar-versus-constructor distinction at the resource level.

## 9. Hostile suite

1. **Same profile, different instrument:** destructive and nondemolition testers have equal success curves.
2. **Catalyst activation:** a returned resource collapses task cost.
3. **Catalyst degradation:** marginal catalyst state returns while correlations accumulate.
4. **Amortization:** many-copy rate differs from one-shot threshold.
5. **Reset omission:** apparent reuse ignores restoration cost.
6. **Fault omission:** nominal cost agrees while fault-tolerant cost diverges.
7. **Authority omission:** a cheap behavior lacks permission to actuate.
8. **Noncommutative loss:** classical discrimination profile agrees while coherent logical algebra is erased.
9. **Profile collision:** distinct constructor categories induce the same tested thresholds.
10. **Composition failure:** individually priced morphisms lack a valid composite grade.

## 10. SCC certificate

```json
{
  "constructor_category": "...",
  "resource_grading": "...",
  "hom_grade_sets": "...",
  "composition_grade_law": "...",
  "parallel_grade_law": "...",
  "task_type": "discriminate | nondemolition_read | coherent_localize | gate | reset",
  "one_shot_profile": "...",
  "amortized_profile": "...",
  "catalyst_ports": ["..."],
  "catalyst_return_law": "...",
  "enriched_lambda_distortion": "...",
  "profile_completeness_claimed": false
}
```

## 11. Present conclusion

The resource-indexed distinguishability profile is the right replacement for an unbudgeted norm when the task is discrimination.

It is not the top-level semantic object.

The top-level object is the resource-enriched constructor category, together with the enriched source-to-behavior distributive law. Distinguishability profiles are its diagnostic shadows.
