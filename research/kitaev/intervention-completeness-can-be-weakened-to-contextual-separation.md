# Intervention completeness can be weakened to contextual separation

**Owner:** marici.Kitaev  
**Status:** bounded research packet  
**Question:** How can a source theory justify that no omitted context reveals another next-rung filler?

## 1. The earlier demand was too strong

A source theory need not enumerate every physically possible intervention.

For termination, it is enough to possess a family of contexts that separates every pair of physically inequivalent candidate fillers. Call this **contextual separation completeness**.

Let \(L_x\) be the groupoid of candidate fillers over lower boundary \(x\), let \(\mathcal C\) be the admitted context category, and let \(O\) be the observation functor. Each filler \(f\) determines its contextual profile

\[
N_{\mathcal C}(f): C \longmapsto O(C[f]).
\]

The admitted contexts are separation-complete on \(L_x\) when

\[
N_{\mathcal C}(f) \cong N_{\mathcal C}(g)
\quad\Longrightarrow\quad
f \simeq g.
\]

Categorically, the contextual nerve must be conservative on equivalence classes; where transformations and higher identifications matter, full faithfulness is the stronger certificate.

This is weaker than saying every physical context belongs to \(\mathcal C\). It says every omitted context is redundant for the particular task of distinguishing fillers.

## 2. Three completeness notions

These must not be conflated.

1. **Generative completeness:** every admitted context is composed from the declared generators.
2. **Realization completeness:** every physically possible context is represented by an admitted context.
3. **Separation completeness:** the admitted contexts distinguish every physically inequivalent filler.

Generative completeness alone is syntactic. Realization completeness is usually too ambitious. Separation completeness is the minimal property needed by a termination theorem.

## 3. The finite-dimensional quantum model

For linear maps on a finite-dimensional input space, equality can be tested using a bounded ancillary system.

The Choi map sends a channel \(\Phi\) to

\[
J(\Phi)=(\Phi\otimes \operatorname{id})(|\Omega\rangle\langle\Omega|),
\]

where the ancilla dimension need not exceed the input dimension. Injectivity of \(J\) implies

\[
J(\Phi)=J(\Psi)
\quad\Longrightarrow\quad
\Phi=\Psi.
\]

Thus one canonical entangled probe, followed by an informationally complete output readout, is separation-complete for channel equality. It does not enumerate every laboratory context. It proves that every other channel-distinguishing experiment factors through information already contained in the Choi operator.

This is a proper explanatory pattern:

- the linear operator representation fixes the candidate class;
- tensoring with a bounded identity exposes every matrix component;
- informational completeness separates the resulting operator;
- the input dimension supplies the finite ancilla bound.

The experimental authority to prepare the probe and measure the output remains a separate executable question.

## 4. Why ordinary observation can fail

Without ancillary contexts, distinct transformations can agree on the declared state set. With an ancilla they may separate. Likewise:

- real and complex quantum theories differ in local tomography;
- processes with memory require process-tensor or comb testers;
- repeated-use devices can differ despite identical one-shot channels;
- indefinite causal structures may evade a fixed-order comb language.

Therefore the context family must be typed by the claimed object:

- states require state tomography;
- channels require ancilla-assisted process tomography;
- finite-memory processes require comb testers of adequate depth;
- reusable constructors require behavioral or coalgebraic tests;
- completed objects require limit-stable separators.

No universal context certificate works across all strata.

## 5. Dense-probe formulation

Let \(\mathcal P\subseteq\mathcal C\) be a bounded probe subcategory. The desired theorem is that \(\mathcal P\) is dense or separating for the declared fillers:

\[
L_x
\longrightarrow
[\mathcal P^{\mathrm{op}},\mathcal O]
\]

is conservative, or fully faithful when the higher equivalences themselves matter.

Then a contractible contextual profile implies a contractible filler space, provided the physical candidate class is covered by the representation theorem.

This is the Yoneda-shaped core of the explanation: an object is determined by its action on a sufficiently rich family of probes.

## 6. What still requires a physical theorem

A compiler cannot establish separation completeness merely by testing its own generated examples. It needs a representation theorem specifying the entire candidate class.

For finite quantum channels, complete positivity and linearity provide that class, and Choi injectivity supplies the separator.

For a new sector, the certificate must state:

1. the physical or mathematical candidate class;
2. the allowed equivalence relation;
3. the bounded probe family;
4. the comparison or nerve map;
5. the theorem that this map is conservative;
6. stability under composition, ancillas, repeated use, and completion relevant to the claim.

Without item 1, the proof is circular: the source language defines both the candidates and the tests, then declares itself complete.

## 7. Strengthened DPC

**DPC.** A tower terminates at rung \(r\), relative to a represented candidate class, when:

1. every compatible boundary has a contractible source lift space;
2. a bounded source-authorized probe family is contextually separation-complete for the represented physical lift space;
3. contractibility and separation survive every context extension admitted by the claimed process type;
4. the representation theorem covers every candidate capable of changing the declared operational predictions.

Absolute enumeration of all interventions is unnecessary. A universal separating family suffices.

## 8. Hostile models

1. **Generator-only hostile:** all generated contexts agree, but an allowed ungenerated context separates two fillers.
2. **State-tomography hostile:** two channels agree on the tested states but differ on an entangled input.
3. **One-shot hostile:** two memory devices induce the same channel once but different two-use combs.
4. **Fixed-depth hostile:** process tensors agree through depth \(r\) and differ at \(r+1\).
5. **Finite-cutoff hostile:** every finite separator is injective while its lower bound collapses in completion.
6. **Scalar hostile:** a scalar readout agrees while operator-valued Choi data differ.
7. **Authority hostile:** the universal mathematical probe exists but cannot be prepared or read by source-authorized constructors.

## 9. SCC consequence

A termination certificate should add:

```json
{
  "candidate_class": "...",
  "candidate_representation_theorem": "...",
  "context_completeness": "generative | realization | separation",
  "probe_family": ["..."],
  "comparison_map": "...",
  "separation_status": "proved | refuted | open",
  "required_ancilla_or_memory_bound": "...",
  "process_type": "state | channel | comb | reusable | completed",
  "executable_probe_authority": "proved | open | absent"
}
```

SCC should reject any inference from generative completeness to separation completeness.

## 10. Present conclusion

The deepest explanatory question is no longer:

> Have we listed every possible context?

It is:

> Why is this bounded family of contexts guaranteed to distinguish every inequivalent filler in the represented candidate class?

The Choi theorem is the simplest pinned example of a satisfactory answer. It suggests that the main programme should search for universal separators and representation theorems, rather than ever longer lists of probes.
