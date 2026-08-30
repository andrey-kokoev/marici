# Termination is a contractible, context-stable lift space

**Owner:** marici.Kitaev  
**Status:** bounded research packet  
**Question:** What explains why a coherence tower has no independent next rung?

## 1. Replace the mechanism list by a fiber question

Fix a lower object \(x_{\le r}\). Let

\[
\operatorname{Lift}_{r+1}(x_{\le r})
\]

be the groupoid or space of source-admissible next-rung fillers, including their authorized equivalences.

There are three primary cases:

1. **Empty lift space:** the boundary is obstructed. No filler exists.
2. **Contractible lift space:** a filler exists and is unique up to the authorized equivalence. The next rung carries no independent information.
3. **Noncontractible lift space:** distinct fillers, automorphisms, or higher paths remain. The next rung is independent.

Thus termination is not mere nonexistence of a new operation. It is unique extension.

A hollow boundary has an empty lift space. It is not a self-closing tower.

## 2. The four known mechanisms are proof families

Coskeletality, flag closure, functional saturation, and controlled invariance are not plausibly exhaustive ontological kinds. They are four ways already encountered for proving that an appropriate lift space is contractible.

- Coskeletality proves unique fillers through matching objects.
- Flag closure proves higher admissibility is forced by pairwise admissibility.
- Functional saturation proves higher observations are reconstructed faithfully.
- Controlled invariance proves indefinite behavior is fixed by an invariant or greatest fixed point.

A conservation or resource law is not automatically a fifth mechanism. Usually it proves that a proposed lift is impossible, hence that a lift space is empty. It proves termination only if an authorized trivial or canonical lift remains and every alternative is forbidden.

## 3. Context stability is essential

Contractibility in one isolated presentation is insufficient. A hidden distinction may become accessible after adjoining:

- an ancilla;
- a reference frame;
- a catalyst;
- a second copy;
- a measurement context;
- repeated use and reset;
- a completion or asymptotic limit.

Therefore the lift space must remain contractible under every admitted context extension \(C\):

\[
\operatorname{Lift}_{r+1}(x_{\le r})
\longrightarrow
\operatorname{Lift}_{r+1}(C[x_{\le r}]).
\]

The required property is universal or base-change-stable unique lifting, not pointwise uniqueness.

This is the categorical form of the three-polarizer warning: a distinction invisible in the two-element context can become operationally visible after inserting a third constructor.

## 4. Relative and ontological termination

SCC can establish only relative termination unless its source semantics are intervention-complete.

Relative termination says:

> In source language \(L\), under assumptions \(A\), every admitted boundary has a context-stable contractible lift space.

Ontological termination additionally requires:

> Every physically possible intervention relevant to this claim is represented by an admitted context of \(L\).

The second statement cannot normally be proved by the same compiler that freezes \(L\). It requires an external completeness or realization theorem.

Let

\[
\mathcal S \longrightarrow \mathcal P
\]

map source constructors to possible physical transformations. Ontological closure requires enough fullness and essential surjectivity on the transformations and contexts capable of distinguishing fillers. Faithfulness of scalar observations is not enough.

## 5. Deutsch–Popperian conjecture

**DPC.** A tower genuinely terminates at rung \(r\), relative to an intervention-complete source theory, exactly when every compatible lower boundary has a nonempty contractible \((r+1)\)-lift space and this contractibility is preserved by every admitted context extension, composition, repeated-use construction, and completion.

The explanation is that no possible intervention can select between alternative fillers because there are no alternative fillers, even after contextual amplification.

## 6. Hard falsifiers

The conjecture or a claimed instance fails if any of the following occurs:

1. **Ancilla splitting:** a unique isolated filler becomes two inequivalent fillers after tensoring with an ancilla.
2. **Reference-frame activation:** a superselection-hidden phase becomes selectable after adjoining a reference frame.
3. **Catalytic activation:** a forbidden constructor becomes possible with a catalyst returned unchanged.
4. **Copy activation:** one-copy equivalence separates at two or more copies.
5. **Sequential activation:** equal bounded traces differ under reset or repeated execution.
6. **Completion escape:** every finite cutoff has a unique filler, but the limit develops a kernel or additional extension.
7. **Observation blindness:** scalar outputs agree while ordered constructors differ.
8. **Authority incompleteness:** the source language omits a physically allowed distinguishing intervention.

## 7. Consequence for SCC

SCC should make `lift_space_status` the semantic core of its termination certificate:

```json
{
  "lift_space_status": "empty | contractible | noncontractible | unknown",
  "equivalence_not_used_as_identity": "...",
  "context_family": ["authorized contexts"],
  "context_stability": "proved | refuted | open",
  "completion_stability": "proved | refuted | open",
  "intervention_completeness": "proved | assumed | open",
  "classification": "obstruction | relative_termination | independent_rung | inconclusive"
}
```

The earlier four mechanisms remain useful as values of `proof_method`, not as a claim of exhaustiveness.

## 8. Present conclusion

The stronger structural line is:

\[
\text{coherent lower boundary}
\;\not\Rightarrow\;
\text{filler exists}
\;\not\Rightarrow\;
\text{filler is unique}
\;\not\Rightarrow\;
\text{uniqueness survives contexts}
\;\not\Rightarrow\;
\text{source contexts exhaust reality}.
\]

Each implication needs its own theorem. This is the hard-to-vary explanatory structure missing from a bare closure flag.