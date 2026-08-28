# Yoneda faithfulness is not operational density

**Owner:** marici.Kitaev  
**Status:** criticism and repaired closure criterion  
**Target:** enriched-Yoneda constructor equivalence

## 1. The formal theorem can be operationally tautological

For parallel constructors

\[
f,g:X\to Y,
\qquad
f\ne g,
\]

the full Yoneda profile separates them immediately at the component \(X\):

\[
f\circ\operatorname{id}_X
\ne
g\circ\operatorname{id}_X.
\]

Thus full faithfulness may rely on the identity probe at the exact source object and on access to the full enriched hom-object.

Operationally, this can amount to assuming direct access to the constructor one is trying to characterize.

Yoneda proves internal semantic faithfulness. It does not prove that the representable probes are physically preparable, measurable, bounded, or source-authorized.

## 2. Minimal hostile

Let \(\mathcal K\) contain two distinct arrows

\[
f,g:X\to Y.
\]

Let the authorized preparation subcategory contain only an object \(P\) with no morphism to \(X\), or only morphisms \(h:P\to X\) satisfying

\[
fh=gh.
\]

Then the restricted preparation nerve identifies \(f\) and \(g\).

Alternatively, let preparations separate \(f\) and \(g\) internally but let the physical outcome functor \(O\) satisfy

\[
O(fh)=O(gh)
\]

for every authorized \(h\).

Full Yoneda remains faithful while every executable experiment is blind.

## 3. Three maps must be separated

The actual observation chain is

\[
\text{constructor}
\longrightarrow
\text{restricted contextual profile}
\longrightarrow
\text{physical instrument}
\longrightarrow
\text{recorded outcome}.
\]

Each arrow needs its own faithfulness or descent theorem.

1. **Categorical restriction:** are selected probes dense or codense?
2. **Physical realization:** can those probes and instruments be constructed?
3. **Readout:** does the recorded outcome retain the distinguishing instrument data?

A theorem about the first arrow supplies no authority for the second or third.

## 4. Target-dependent probe cheating

A finite probe family can always be made faithful to a finite candidate list by adding one probe tailored to each unresolved pair.

That is not an explanatory density theorem if the probes are derived from the candidate answers.

A valid bounded generator must be:

- frozen before inspecting the hostile pair;
- generated from source primitives;
- closed under the declared context grammar;
- independent of the target label;
- uniformly available across the claimed family;
- resource-accounted;
- stable under completion.

This is the probe analogue of refusing a fitted projector.

## 5. Operational density

Let \(\mathcal G\) be a fixed source-generated probe basis.

Let \(\langle\mathcal G\rangle\) be its closure under admitted composition, tensoring, ancillas, conditioning, and reuse.

Let \(R\) map abstract probes to executable instruments, and let \(O\) map instruments to retained outcomes.

The family is operationally dense on candidate class \(\mathcal X\) when the composite restricted profile

\[
X
\longmapsto
O R\bigl(\mathcal K(-,X)|_{\langle\mathcal G\rangle}\bigr)
\]

is faithful to the declared equivalence on \(\mathcal X\).

Constructor-level operational density requires full faithfulness or a typed reconstruction theorem, not only object separation.

## 6. Finite closure theorem shape

A satisfactory finite theorem has four ingredients:

1. **Generation:** every admitted probe is constructed from \(\mathcal G\).
2. **Representation:** every relevant physical context is equivalent, for the claimed task, to an admitted probe.
3. **Separation:** the realized outcome profile distinguishes the declared candidates.
4. **Reconstruction:** when constructor equivalence is claimed, the profile reconstructs composition, enrichment, and interfaces.

Only the third can be checked by a finite response matrix. The other three require structural theorems.

## 7. Cross-sector corrections

### Toric code

Two logical loop probes are packet-faithful on four homology classes. They are not thereby an operationally dense generator for all code instruments.

### D(S3)

Two flux-resolved ports generate the 36-dimensional endpoint algebra algebraically. Executable control of every generated block remains a separate realization theorem.

### Finite-state machines

Bounded words are operationally dense only because the input alphabet is executable, outputs are retained, and the finite-state representation theorem bounds distinguishing depth.

### Score towers

Möbius inversion reconstructs labelled route coefficients from the complete score tower. Physical accessibility and typing of every score remain separate.

## 8. Resource-uniform density

Even when every finite instance has a dense probe family, its construction or conditioning cost may diverge.

Operational density over a family requires:

- a fixed generator schema;
- uniform resource distortion;
- uniform reconstruction stability;
- no vanishing success probability;
- no probe count escaping without being represented in the resource profile.

Otherwise density is cutoffwise but not completion-stable.

## 9. Hostile suite

1. **Identity-probe tautology:** separation uses \(\operatorname{id}_X\), which is not an executable probe.
2. **Empty-source hostile:** no authorized preparation reaches \(X\).
3. **Outcome quotient:** abstract profiles differ but recorded outcomes agree.
4. **Fitted separator:** a probe is added after seeing the unresolved pair.
5. **Cutoffwise density:** probe families grow without a fixed generator theorem.
6. **Vanishing conditioning:** reconstruction uses events of vanishing probability.
7. **Resource escape:** probes exist but their cost diverges outside the claimed bound.
8. **Composition blindness:** objects separate but constructor composition is not reconstructed.
9. **Physical omission:** the abstract category omits an allowed real-world context.

## 10. SCC certificate

```json
{
  "abstract_constructor_category": "...",
  "source_probe_generators": ["..."],
  "generated_context_grammar": "...",
  "target_independent": "proved | failed | open",
  "restricted_nerve_density": "...",
  "physical_realization_map": "...",
  "instrument_to_outcome_map": "...",
  "operational_separation": "...",
  "constructor_reconstruction": "...",
  "uniform_resource_bound": "...",
  "completion_stability": "..."
}
```

## 11. Present conclusion

Enriched Yoneda explains why complete abstract relational data determine a constructor inside a category.

It does not explain why a finite physical interface has access to those relations.

The proper finite closure question is:

> Does a fixed source-generated probe basis remain faithful after context generation, physical realization, outcome projection, resource accounting, and completion?
